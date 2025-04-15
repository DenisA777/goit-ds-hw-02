from faker import Faker
import sqlite3
import random


fake = Faker()


conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()


statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (?)", (status,))


user_ids = []
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))
    user_ids.append(cursor.lastrowid)


for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=200)
    status_id = random.randint(1, len(statuses))
    user_id = random.choice(user_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
        (title, description, status_id, user_id)
    )


conn.commit()
conn.close()
