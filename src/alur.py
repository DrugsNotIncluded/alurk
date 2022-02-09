from os import path, chdir, getcwd
import abuild
import requests
import subprocess
import json

INDEX_REPO = "INDEX"
DEFAULT_PATH = "/tmp/alur"
INDEX_DIR = path.join(DEFAULT_PATH, "index")
PACKAGES_CACHE = path.join(DEFAULT_PATH, "pcache")

def github_get_raw_file_from_repo(git_user, project, file_path):
    raw_url = "https://raw.githubusercontent.com"
    full_raw_file_url = path.join(raw_url, git_user, project, file_path)
    r = requests.get(full_raw_file_url)
    data = r.text
    data = data.strip()
    return(data)

git_get_raw_file_data = github_get_raw_file_from_repo
    
def git(*args):
    out = subprocess.Popen(f"git {' '.join(args)}", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    out.wait()
    return(out)

def update_index(git_user_url):
    full_url = path.join(git_user_url, INDEX_REPO)
    if not path.exists(INDEX_DIR):
        git("clone", full_url, INDEX_DIR)
    else:
        prev_dir = getcwd()
        chdir(INDEX_DIR)
        git("pull")
        chdir(prev_dir)

def get_available_packages():
    with open(path.join(INDEX_DIR,"index"),"r") as INDEX:
        INDEX_DATA = INDEX.read()
    packages_list = json.loads(INDEX_DATA)
    return(packages_list)

def fetch_package_recipe(package, git_user_url, dest):
    package_dir = path.join(dest, package)
    package_repo = path.join(git_user_url, package)
    git("clone", package_repo, package_dir)

def construct_builddeps_tree(package, git_user_url):    

def build_builddeps_tree(builddeps_tree):
    
def resolve_circular_dependencies(builddeps_tree):
