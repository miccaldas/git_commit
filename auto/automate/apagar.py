"""Module Docstring"""
import isort
import snoop
from loguru import logger
from snoop import pp
import typer

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

app = typer.Typer()


@logger.catch
@snoop
@app.command()
def apagar(k1: str = "", k2: str = ""):
    """"""
    print(k1, k2)


if __name__ == "__main__":
    app()
