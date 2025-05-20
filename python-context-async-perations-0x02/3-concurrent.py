#!/usr/bin/python3

import asyncio
import aiosqlite

async def setup_database():
    async with aiosqlite.connect("users.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email VARCHAR(50),
                age INTEGER
            )
        """)

        await db.executemany(
            "INSERT OR IGNORE INTO users (id, name, email, age) VALUES (?, ?, ?, ?)",
            [(3, 'Charlie', 'charlie@yahoo.com', 45), (4, 'Diana', 'diana@yahoo.com', 50)]
        )

        await db.commit()

async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users: ")
            for user in users:
                print(user)

async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            users = await cursor.fetchall()
            print("User with age greater than 40: ")
            for user in users:
                print(user)

async def fetch_concurrently():
    await setup_database()
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())