from flask import Flask
from db_users import get_last_100_messages

app = Flask(__name__)

@app.route('/')
def home():
    return get_last_100_messages()

if __name__ == '__main__':
    app.run(port=5000)
