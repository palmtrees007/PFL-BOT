import aiomysql
import asyncio



async def db_connect(host, port, user, password, database):
    try:
        pool = await aiomysql.create_pool(
            host=host,
            port=int(port),
            user=user,
            password=password,
            db=database,
            cursorclass=aiomysql.DictCursor
        )
        print('connected')
        return pool
    except Exception as e:
        print('error connection')


async def check(email, pool: aiomysql.Pool):
    try:
        conn = await pool.acquire()
        cur = await conn.cursor(aiomysql.DictCursor)

        select = f"SELECT EXISTS(SELECT email FROM users WHERE email = '{email}') AS email;"
        await cur.execute(select)
        res = await cur.fetchall()
        res = res[0]['email']
        if res == 1 or res == '1':
            return False
        elif res == 0 or res == '0':
            return True
        else:
                return None
    except Exception as e:
        raise e


async def check_password(psw, email, pool: aiomysql.Pool):
    conn = await pool.acquire()
    cur = await conn.cursor(aiomysql.DictCursor)

    select = f"SELECt pswrd FROM users WHERE email = '{email}'"
    await cur.execute(select)
    res = await cur.fetchall()
    res = res[0]['pswrd']
    if res == psw:
        return True
    else:
        return False


async def add_user(email, nickname, pswrd, pool: aiomysql.Pool):
    try:
        conn = await pool.acquire()
        cur = await conn.cursor(aiomysql.DictCursor)

        insert = f"INSERT INTO users (email, pswrd, nickname) VALUES ('{email}', '{pswrd}', '{nickname}');"
        await cur.execute(insert)
        print('Значение добавлено')
        await conn.commit()
    except Exception as e:
        raise e
    

async def create_lobby(pool: aiomysql.Pool):
    pass