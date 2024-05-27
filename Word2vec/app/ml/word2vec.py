import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

word2vec_model = Word2Vec.load("app/ml/word2vec.model")


def preprocess_text(record: str) -> list[str]:
    # 1. tokenize all
    tokens = word_tokenize(record.lower())
    # 2. remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

    # 3. stemming /lemmatizing
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    return stemmed_tokens


def update_model(model: Word2Vec, pre_processed_text: list[str]) -> None:
    # re-train word2vec model
    model.build_vocab(pre_processed_text, min_count=1, vector_size=5)
    model.train(pre_processed_text, total_examples=model.corpus_count, epochs=model.epochs)
    model.save("app/ml/word2vec.model")


def generate_embeddings(record: str) -> np.ndarray:
    pre_processed_text = preprocess_text(record)
    model = Word2Vec.load("app/ml/word2vec.model")
    embedding_vector = np.array(
        [model.wv[word] for word in pre_processed_text if word in model.wv.vocab]
    )
    return embedding_vector


def find_similar_records(record: str, records: list[schemes.Record], db: Session) -> list[schemes.Record]:
    embedding_vector = generate_embeddings(record)
    embeddings_by_record_id = {record.id: generate_embeddings(record.content) for record in records}
    similarities = {
        record_id: cosine_similarity(embedding_vector.reshape(1, -1), embeddings_by_record_id[record_id].reshape(1, -1))
        for record_id in embeddings_by_record_id
    }
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    most_similar_record_ids = [record_id for record_id, similarity in sorted_similarities[:3]]
    similar_records = [db.query(models.Record).filter(models.Record.id == record_id).first() for record_id in most_similar_record_ids]

    # Add the counter for the number of similar records found
    num_similar_records = len(most_similar_record_ids)
    return similar_records, num_similar_records