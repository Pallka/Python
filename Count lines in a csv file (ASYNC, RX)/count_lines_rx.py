import aiofiles
import asyncio
import time
from rx import from_iterable
from rx import operators as ops

async def count_ukraine_rx():
    start_time = time.time()
    
    async with aiofiles.open("updated_data.csv", mode="r", encoding="utf-8") as infile:
        lines = await infile.readlines()

    count = (
        from_iterable(lines[1:])
        .pipe(
            ops.map(lambda line: line.strip().split(",")),
            ops.filter(lambda row: row[1] == "Ukraine"), 
            ops.to_list()
        )
    ).run()

    end_time = time.time()
    print(f"'country = Ukraine': {len(count)}")
    print(f"Час виконання (reactive): {end_time - start_time:.6f} с.")

asyncio.run(count_ukraine_rx())