import aiofiles
import asyncio
import time

async def count_ukraine_players_async():
    count = 0
    async with aiofiles.open("updated_data.csv", mode="r", encoding="utf-8") as infile:
        start_time = time.time()
        lines = await infile.readlines()

        headers = lines[0].strip().split(",")
        country_index = headers.index("country")
        
        for line in lines[1:]:
            row = line.strip().split(",")
            if row[country_index] == "Ukraine":
                count += 1

        end_time = time.time()
        print(f"'country = Ukraine': {count}")
        print(f"Час виконання (async): {end_time - start_time:.6f} с.")

asyncio.run(count_ukraine_players_async())