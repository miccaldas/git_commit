import os
import subprocess
from datetime import datetime
from time import sleep

import snoop

fullpaths = []
py = os.listdir("/home/mic/python/")
site = os.listdir("/usr/share/nginx/html/")
clean_site = [i for i in site if i != "setup.cfg"]
print(f"second py is {py}")
print(clean_site)

for i in py:
    fpath = os.path.join("/home/mic/python", i)
    fullpaths.append(fpath)
for f in clean_site:
    fpath = os.path.join("/usr/share/nginx/html/", f)
    fullpaths.append(fpath)
print(fullpaths)

for path in fullpaths:
    os.chdir(path)
    date = datetime.today().strftime("%d-%m-%Y")
    add = "git add ."
    commit = f"git commit -m '{date} commit'"
    push_github = "git push -u origin_github master"
    push_notabug = "git push -u origin master"
    with open(f"{path}/.git/config", "r") as f:
        git_remotes = f.readlines()
        gr = str(git_remotes)
        if '[remote "origin"]' in gr:
            subprocess.run(add, cwd=path, shell=True)
            sleep(1)
            subprocess.run(commit, cwd=path, shell=True)
            sleep(1)
            subprocess.run(push_notabug, cwd=path, shell=True)
            sleep(1)
        else:
            print(f"There's no repo notabug in {path}")
        if '[remote "origin_github"]' in gr:
            subprocess.run(add, cwd=path, shell=True)
            sleep(1)
            subprocess.run(commit, cwd=path, shell=True)
            sleep(1)
            subprocess.run(push_github, cwd=path, shell=True)
        else:
            print(f"There's no repo github in {path}")
