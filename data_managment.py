import psycopg2
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()  # підключення до закритого файлу
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db_name = os.getenv('db_name')
def create_table(user_id, name, time):
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:  # курсор ходит по таблице и выполняет ('execute')
			cursor.execute(f'SELECT EXISTS(SELECT user_id FROM feelings WHERE user_id = {user_id})')
			check_user_id = cursor.fetchone()[0]
			if check_user_id == 0:
				cursor.execute(f''' 
				INSERT INTO feelings(user_id, name, time)
				VALUES ('{user_id}', '{name}', '{time}')
				''')
			else:
				update = (time, user_id)  # вопрос! нужно ли после перезахода обновлять все этапы и эмоции, иначе может быть недостоверная инфа
				cursor.execute(f'''UPDATE feelings
								SET time = %s
								WHERE user_id = %s
								''', update)
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()

def update_table(progress, emotion, feedback, time, user_id):
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:  # оновлюємо колонки в залежності від прогресу
			update = (time, user_id)
			cursor.execute(f'''UPDATE feelings
							SET time =%s
							WHERE user_id = %s
							''', update)
			if progress == 0:
				update = (feedback, emotion, user_id)
				cursor.execute(f'''UPDATE feelings
								SET pre_step = %s, emotion = %s
								WHERE user_id = %s
								''', update)
			elif progress == 1:
				update = (feedback, emotion, user_id)
				cursor.execute(f'''UPDATE feelings
								SET step1 = %s, emotion = %s
								WHERE user_id = %s
								''', update)
			else:
				update = (feedback, "done", user_id)
				cursor.execute(f'''UPDATE feelings
								SET step2 = %s, retarget = %s
								WHERE user_id = %s
								''', update)
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()

def update_retarget(user_id, time):
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:
			update = (time, "done", user_id)
			cursor.execute(f'''UPDATE feelings
						SET time =%s, retarget = %s
						WHERE user_id = %s
						''', update)
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()

async def emotion_state_check(step, user_id, message):  # функція котра відповідає за отрмання інформації про попередній стан користувача
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:
			if step == 1:
				cursor.execute(f"SELECT pre_step FROM feelings WHERE user_id = {user_id}")
			elif message == 'Давай сробуємо  👍':
				cursor.execute(f"SELECT step1 FROM feelings WHERE user_id = {user_id}")
			elif step == 2:
				cursor.execute(f"SELECT step1 FROM feelings WHERE user_id = {user_id}")
			else:
				return '10⚫'
			previus_state = cursor.fetchone()
		print(f'previus_state {previus_state}')
		return (previus_state[0]) if (previus_state[0]) is not None else '0❌'
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()

async def emotion_state_road(user_id):  # функція котра відповідає за отрмання інформації про усі стани користувача
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:
			cursor.execute(f"SELECT pre_step, step1, step2 FROM feelings WHERE user_id = {user_id}")
			states_road = cursor.fetchall()
		return states_road
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()

# функція (emotion_proxy) для блоку pre_step, вона необхідна на впипадок якщо proxy_state неможливо буде відкрити
async def emotion_proxy(user_id):
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:
			cursor.execute(f"SELECT emotion FROM feelings WHERE user_id = {user_id}")
			emotion = cursor.fetchone()[0]
		return emotion
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()
def check_retarget():
	conn = None
	try:
		conn = psycopg2.connect(
			host=host,
			database=db_name,
			user=user,
			password=password
		)
		conn.autocommit = True
		with conn.cursor() as cursor:  # курсор ходит по таблице и выполняет ('execute')
			cursor.execute('''CREATE TABLE IF NOT EXISTS feelings(
			user_id BIGINT PRIMARY KEY,
			name TEXT,
			time TIMESTAMP,
			emotion TEXT,
			pre_step TEXT,
			step1 TEXT,
			step2 TEXT,
			retarget TEXT
			)''')
			cursor.execute('SELECT retarget, time FROM feelings')
			retarget_status = cursor.fetchall()
			message_ready_time = set()

			for data in retarget_status:
				now = datetime.now().replace(microsecond=0)
				bd = datetime.strptime(str(data[1]), '%Y-%m-%d %H:%M:%S')

				if data[0] != 'done' and now > bd + timedelta(hours=3):
					cursor.execute(f"SELECT user_id, emotion, retarget FROM feelings WHERE time = '{data[1]}'")
					small_retargert = cursor.fetchone()
					message_ready_time.add(small_retargert)

				elif now > bd + timedelta(days=2):
					cursor.execute(f"SELECT user_id, emotion, retarget FROM feelings WHERE time = '{data[1]}'")
					long_retargert = cursor.fetchone()
					message_ready_time.add(long_retargert)
		print('message_ready>>>', message_ready_time)
		return message_ready_time
	except Exception as er:
		print(f'Error with postgres >>> {er}')
	finally:
		if conn is not None:
			conn.close()