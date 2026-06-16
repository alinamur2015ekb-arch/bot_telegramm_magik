import aiosqlite
from typing import Optional

DB_NAME = "database.db"

async def init_answer():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS answer(
                id INTEGER PRIMARY KEY,
                answer_math1 INTEGER DEFAULT 0,
                answer_math2 INTEGER DEFAULT 0,
                answer_math3 INTEGER DEFAULT 0,
                answer_python1 INTEGER DEFAULT 0,
                answer_python2 INTEGER DEFAULT 0,
                answer_python3 INTEGER DEFAULT 0,
                answer_robotics1 INTEGER DEFAULT 0,
                answer_robotics2 INTEGER DEFAULT 0
            )
        ''')
        await db.commit()

async def create_answer(
    user_id: int,
    answer_math1: Optional[int] = None,
    answer_math2: Optional[int] = None,
    answer_math3: Optional[int] = None,
    answer_python1: Optional[int] = None,
    answer_python2: Optional[int] = None,
    answer_python3: Optional[int] = None,
    answer_robotics1: Optional[int] = None,
    answer_robotics2: Optional[int] = None
):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT id FROM answer WHERE id = ?', (user_id,)) as cursor:
            user_exists = await cursor.fetchone()

        if not user_exists:
            await db.execute('INSERT INTO answer (id) VALUES (?)', (user_id,))
            await db.commit()

        updates = []
        values = []
        for field, value in [
            ("answer_math1", answer_math1), ("answer_math2", answer_math2), ("answer_math3", answer_math3),
            ("answer_python1", answer_python1), ("answer_python2", answer_python2), ("answer_python3", answer_python3),
            ("answer_robotics1", answer_robotics1), ("answer_robotics2", answer_robotics2)
        ]:
            if value is not None:
                updates.append(f"{field} = ?")
                values.append(value)

        if updates:
            values.append(user_id)
            query = f"UPDATE answer SET {', '.join(updates)} WHERE id = ?"
            await db.execute(query, tuple(values))
            await db.commit()


async def get_answer():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM answer') as cursor:
            result = await cursor.fetchall()
            return result


async def init_play():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(''' 
            CREATE TABLE IF NOT EXISTS play_static(
                id INTEGER PRIMARY KEY,
                random INTEGER DEFAULT 0,
                meme INTEGER DEFAULT 0
            )
        ''')
        await db.commit()
        
async def create_play(
    user_id: int, 
    random: Optional[int] = None, 
    meme: Optional[int] = None
):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT id FROM play_static WHERE id = ?', (user_id,)) as cursor:
            user_exists = await cursor.fetchone()

        if not user_exists:

            await db.execute('INSERT INTO play_static (id) VALUES (?)', (user_id,))
            await db.commit()

        updates = []
        values = []
        for field, value in [("random", random), ("meme", meme)]:
            if value is not None:
                updates.append(f"{field} = ?")
                values.append(value)

        if updates:
            values.append(user_id)
            query = f"UPDATE play_static SET {', '.join(updates)} WHERE id = ?"
            await db.execute(query, tuple(values))
            await db.commit()


async def get_answer_by_id(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM answer WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result


async def get_play_by_id(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM play_static WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result