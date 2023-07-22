import os

# App Initialization
from . import create_app 

app = create_app(os.getenv("CONFIG_MODE"))

# Hello World!
@app.route('/')
def hello():
    return "Hello World!"

from .task import urls

if __name__ == "__main__":
    app.run()