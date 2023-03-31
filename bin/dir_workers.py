import os, stat, shutil
from pathlib import Path

work_dir = Path.cwd()


def remove_readonly(fn, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        fn(path)
    except Exception as exc:
        print("Skipped:", path, "because:\n", exc)


def create_dir(dir_name):
    if os.path.isdir(dir_name):
        return False
    os.mkdir(dir_name)
    return True


def delete_dir(dir_name):
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name, onerror=remove_readonly)
