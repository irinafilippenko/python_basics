from os import getcwd, path, mkdir
import yaml

project = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def dir_start(current_path, project):
    if type(project) == dict:
        for dir, subdirs in project.items():
            if not path.exists(path.join(current_path, dir)):
                mkdir(path.join(current_path, dir))
            dir_start(path.join(current_path, dir), subdirs)
    else:
        if len(project) > 0:
            for subdir in project:
                if not path.exists(path.join(current_path, subdir)):
                    mkdir(path.join(current_path, subdir))

        # if len(project) > 0:
        #     for subdir in project:
        #         if '.' in subdir:
        #             try:
        #                 open(path.join(current_path, subdir), 'a').close()
        #             except OSError:
        #                 print('Не удалось создать файл')
        #         else:
        #             if not path.exists(path.join(current_path, subdir)):
        #                 mkdir(path.join(current_path, subdir))



if __name__ == "__main__":
    # with open('config.yaml') as file_project:
    #     project = yaml.load(file_project, Loader=yaml.FullLoader)
    dir_start(getcwd(), project)
