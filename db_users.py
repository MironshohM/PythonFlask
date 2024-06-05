from config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import mysql.connector
from datetime import datetime

db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
db_cursor = db_connection.cursor()


def save_message(user_id, username, message_text, message_url=None):
    timestamp = datetime.now()
    query = "INSERT INTO user_messages (user_id, username, message_text, message_time, message_url) VALUES (%s, %s, %s, %s, %s)"
    values = (user_id, username, message_text, timestamp, message_url)
    db_cursor.execute(query, values)
    db_connection.commit()


def get_last_100_messages():
    query = "SELECT user_id, username, message_text, message_time, message_url " \
            "FROM user_messages ORDER BY message_time DESC LIMIT 1000"
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    html_table = "<table border='1'>"
    html_table += "<tr><th>User ID</th><th>Username</th><th>Message Text</th><th>Message Time</th><th>Message URL</th></tr>"
    for row in results:
        user_id, username, message_text, message_time, message_url = row
        html_table += f"<tr><td>{user_id}</td><td>{username}</td><td>{message_text}</td><td>{message_time}</td><td>{message_url}</td></tr>"
    html_table += "</table>"

    return html_table
