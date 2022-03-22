from app import app
from tasks import update


if __name__ == "__main__":
    update.delay()
