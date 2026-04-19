from flask import Flask
import redis
import time

app = Flask(__name__)

def get_hit_count():
    retries = 5
    cache = redis.Redis(host='db', port=6379)
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            print("Redis not ready, retrying in 2 seconds...")
            time.sleep(2)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1>Hello DevOps World!</h1><p>Viewed {count} times.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

