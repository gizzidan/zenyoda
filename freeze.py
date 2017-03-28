from flask_frozen import Freezer
from zenyoda import hello

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
