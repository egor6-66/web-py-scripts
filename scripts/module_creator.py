import os
from pathlib import Path
from bin.dir_workers import create_dir
from distutils.dir_util import copy_tree


def start():
    menu_options = {
        1: 'entitie',
        2: 'feature',
        3: 'widget',
        5: 'Exit',
    }

    work_dir = Path.cwd()

    def print_menu():
        for key in menu_options.keys():
            print(key, ')', menu_options[key])

    print('📂🤖creator🤖📂')
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            try:
                name = str(input('Name: '))
                res = create_dir('entities' + '/' + name)
                # template_path = Path('templates/entitie').resolve()
                # copy_tree(template_path, work_dir)
            except:
                print('Wrong input. Please enter a string ...')

        elif option == 2:
            os.chdir(Path('py-scripts/scripts/git_mirroring.py').resolve())
        elif option == 5:
            print('exit from web-py-scripts')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
