from os import walk, path, getcwd
from shutil import copytree


def get_templates():
    path_project = path.join(getcwd(), 'my_project')
    folders = (path.join(root, folder) for root, folders, files in walk(path_project) for folder in folders if
               folder == 'templates')
    for folder in folders:
        copytree(folder, path.join(path_project, 'templates'), dirs_exist_ok=True)


if __name__ == "__main__":
    get_templates()
