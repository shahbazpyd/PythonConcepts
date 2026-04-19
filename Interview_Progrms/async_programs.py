import asyncio
import time

async def fetch_user(user_id):
    await asyncio.sleep(1)          # simulate network call
    return {"id": user_id, "name": f"User_{user_id}"}

async def fetch_all():
    # your code here — fetch user 1, 2, 3 simultaneously
    start = time.time()
    results = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3),
    )
    end = time.time()
    print(results)
    print(f"took {end - start:.2f} seconds")
asyncio.run(fetch_all())

# Expected output (all 3 in ~1 second, not 3):
# [{'id': 1, 'name': 'User_1'}, {'id': 2, ...}, {'id': 3, ...}]