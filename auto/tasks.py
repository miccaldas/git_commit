"""
Updates git repos in the python and web folders.
"""

import contextlib
import os
import subprocess
from datetime import datetime
from time import sleep

import requests

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# @snoop
def update():
    """
    Adds, commits and pushes changes to
    git repos. Prints a message if source
    is not present.
    """
    fullpaths = []
    ignored = ["reusable_files", "old_alternative_projects"]
    py = [i for i in os.listdir("/home/mic/python/") if i not in ignored]
    site = os.listdir("/usr/share/nginx/html/")
    omit = ["setup.cfg", "50x.html", "index.html"]
    clean_site = [i for i in site if i not in omit]

    for i in py:
        fpath = os.path.join("/home/mic/python", i)
        fullpaths.append(fpath)
    for f in clean_site:
        fpath = os.path.join("/usr/share/nginx/html/", f)
        fullpaths.append(fpath)

    add = "git add ."
    push_github = "git push -f origin_github HEAD"
    for path in fullpaths:
        print(path)
        os.chdir(path)
        date = datetime.now().strftime("%d-%m-%Y")
        commit = f"git commit -m '{date} commit'"
        with contextlib.suppress(FileNotFoundError):
            with open(f"{path}/.git/config", "r") as f:
                git_remotes = f.readlines()
                gr = str(git_remotes)
                if '[remote "origin_github"]' in gr:
                    subprocess.run(add, cwd=path, shell=True)
                    sleep(1)
                    subprocess.run(commit, cwd=path, shell=True)
                    sleep(1)
                    subprocess.run(push_github, cwd=path, shell=True)
                else:
                    print(f"There's no ref origin_github in {path}")


if __name__ == "__main__":
    update()


def notify():
    """
    Sends notifcation to phone that the
    script has been run.
    """
    requests.post(
        "https://ntfy.sh/mic", data="Git update has been run. ".encode(encoding="utf-8")
    )


if __name__ == "__main__":
    notify()
