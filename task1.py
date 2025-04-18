import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(100),
  email VARCHAR(100) UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100),
  description TEXT,
  status_id INTEGER,
  user_id INTEGER,
  FOREIGN KEY (status_id) REFERENCES status(id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
""")

conn.commit()
conn.close()

# SELECT * 
# FROM tasks 
# WHERE user_id = 2;


# SELECT * 
# FROM tasks 
# WHERE status_id = (
#   SELECT id FROM status WHERE name = 'new'
# );


# UPDATE tasks
# SET status_id = (
#   SELECT id FROM status WHERE name = 'in progress'
# )
# WHERE id = 5;


# SELECT *
# FROM users
# WHERE id NOT IN (
#   SELECT DISTINCT user_id FROM tasks
# );


# INSERT INTO tasks (title, description, status_id, user_id)
# VALUES (
#   'Нове завдання', 
#   'Опис нового завдання', 
#   (SELECT id FROM status WHERE name = 'new'), 
#   2
# );


# SELECT *
# FROM tasks
# WHERE status_id <> (
#   SELECT id FROM status WHERE name = 'completed'
# );


# DELETE FROM tasks
# WHERE id = 10;


# SELECT *
# FROM users
# WHERE email LIKE '%gmail%';


# UPDATE users
# SET fullname = 'Нове Ім’я Користувача'
# WHERE id = 3;


# SELECT s.name AS status, COUNT(t.id) AS task_count
# FROM status s
# LEFT JOIN tasks t ON s.id = t.status_id
# GROUP BY s.name;


# SELECT t.*
# FROM tasks t
# JOIN users u ON t.user_id = u.id
# WHERE u.email LIKE '%@example.com';


# SELECT *
# FROM tasks
# WHERE description IS NULL OR description = '';


# SELECT u.fullname, t.title, t.description
# FROM users u
# INNER JOIN tasks t ON u.id = t.user_id
# WHERE t.status_id = (
#   SELECT id FROM status WHERE name = 'in progress'
# );


# SELECT u.fullname, COUNT(t.id) AS task_count
# FROM users u
# LEFT JOIN tasks t ON u.id = t.user_id
# GROUP BY u.id;