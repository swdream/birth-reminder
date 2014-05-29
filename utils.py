import os

def fix_path(filename):
    """ return path of filename
    """
    #because this app run with crontab, it must be use abs path
    # return the canonical path of file (__file__)
    filepath = os.path.realpath(__file__)
    # return directory contain filepath
    path = os.path.dirname(filepath)
    fixed = os.path.join(path, filename)
    return fixed
