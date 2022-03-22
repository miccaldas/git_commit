from celery import Celery
from celery.schedules import crontab


__all__ = ["app"]

app = Celery(
    ".".join(__name__.split(".")[:-1]),
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["man"],
    beat_schedule={
        "git_cron": {"task": "tasks.update", "schedule": crontab(hour="16")},
    },
)


if __name__ == "__main__":
    app.start()
