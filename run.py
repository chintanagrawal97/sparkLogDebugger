import os
print(__file__)
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
