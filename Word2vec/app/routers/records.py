from app import schemes, crud
from app.database import get_db
from app.ml import *

from fastapi import APIRouter, Depends, HTTPException
from app.auth_bearer import JWTBearer
from sqlalchemy.orm import Session

records_router = APIRouter(prefix="/records", tags=["records"])


@records_router.post("/", response_model=schemes.Record)
def create_user_record(record: str, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())):
    # 1. Are there new tokens
    pre_processed_text = preprocess_text(record)

    # 2. update_model()
    update_model(word2vec_model, pre_processed_text)

    # 3. gen_embeddings(new_record)
    embeddings = generate_embeddings(record)

    # 4. store record_id -> embedding in a new SQL table
    record_db = RecordTable(embedding=json.dumps(embeddings.tolist()))
    db.add(record_db)
    db.commit()
    db.refresh(record_db)

    return record_db
