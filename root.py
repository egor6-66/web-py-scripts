import os
from pathlib import Path
from scripts import git_pushing
from scripts import module_creator, git_mirroring


if __name__ == '__main__':
    print('🚀🤙web-py-scripts starting🤙🚀')

    menu_options = {
        1: 'creator',
        2: 'git pushing',
        3: 'git mirroring',
        4: 'Exit',
    }


    def print_menu():
        for key in menu_options.keys():
            print(key, ')', menu_options[key])


    work_dir = Path.cwd()

    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            module_creator.start()
        elif option == 2:
            git_pushing.start()
        elif option == 3:
            git_mirroring.start()
        elif option == 4:
            print('exit from web-py-scripts')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')