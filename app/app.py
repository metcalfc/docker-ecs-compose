
from flask import Flask
from redis import StrictRedis
from datetime import datetime

app = Flask(__name__)
redis = StrictRedis(host='redis', port=6379)

@app.route('/')
def home():
    redis.lpush('times', datetime.now().strftime('%H:%M:%S'))
    return 'This page was requested at: {}\n'.format(
        [t.decode('utf-8') for t in redis.lrange('times', 0, -1)])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
