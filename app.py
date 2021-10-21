from flask import Flask

import endpoints
from db import create_tables

app = Flask(__name__)


@app.get("/")
def index():
    return "Hello there!"


app.register_blueprint(endpoints.bp)

if __name__ == "__main__":
    create_tables()

    app.run()
