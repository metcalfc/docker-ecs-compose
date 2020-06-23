
from flask import Flask
from flask import render_template
from redis import StrictRedis
from datetime import datetime

app = Flask(__name__)
redis = StrictRedis(host='redis', port=6379)

@app.route('/')
def home():
    redis.lpush('times', datetime.now().strftime('%H:%M:%S'))
    return render_template('index.html', title='Home', times=redis.lrange('times', 0, -1))

@app.route('/future')
def future():
    return render_template('future.html', title='Future')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
