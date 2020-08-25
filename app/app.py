import os
from datetime import datetime

from flask import Flask, render_template

from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host="backend", port=6379)
audience = "Just Me"

if os.path.exists("/run/secrets/classified"):
    with open("/run/secrets/classified", "r") as secret:
        audience = secret.readline()


@app.route("/")
def home():
    redis.lpush("times", datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"))
    return render_template(
        "index.html", audience=audience, times=redis.lrange("times", 0, -1),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
