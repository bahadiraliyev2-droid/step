print("HELLO, and welcome to nebula.st!")

import sqlite3

connection = sqlite3.connect("user_online.db")
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (password TEXT, name TEXT, mail TEXT, username TEXT)")

cur.execute("INSERT INTO users (password, name, mail, username) VALUES ('123348354544', 'Malik Beybutov', 'Malik.Beybutov@example.com', 'Malik.Beybutov')")
cur.execute("INSERT INTO users (password, name, mail, username) VALUES ('1232813183184', 'Baxtiyar Aliyev', 'BAXA.ALI@example.com', 'BAXA.ALI')")
cur.execute("INSERT INTO users (password, name, mail, username) VALUES ('1110033203030234', 'Ceasar Johnson', 'Ceasar.Johnson@example.com', 'Ceasar.Johnson')")

user_name = input("Enter your name: ")
user_mail = input("Enter your email: ")
user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

cur.execute(
    "INSERT INTO users (password, name, mail, username) VALUES (?, ?, ?, ?)",
    (user_password, user_name, user_mail, user_username)
)

connection.commit()
connection.close()

print("Your information was saved to user_online.db.")
