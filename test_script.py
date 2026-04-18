print('Python is running from inside the VM')
from flask import Flask
import redis

app = Flask(__name__)
# Connect to our Redis container
cache = redis.Redis(host='db', port=6379)

@app.route('/')
def hello():
    # Increment a counter in Redis every time the page is refreshed
    count = cache.incr('hits')
    return f"<h1>Hello DevOps World!</h1><p>This page has been viewed {count} times.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

