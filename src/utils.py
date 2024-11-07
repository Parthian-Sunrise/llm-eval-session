import os
from local_variables import ROOT_DIR


def get_root_dir():
    return ROOT_DIR


def test_root_dir(rel_root):
    cwd = os.getcwd()
    if cwd.replace(str(ROOT_DIR), "").count("/") == rel_root.count("/"):
        print("Root directory set up correctly!")
    else:
        print("Root directory may be incorrect, check local variables")
