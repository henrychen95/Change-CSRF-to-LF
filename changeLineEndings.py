# Change files line endings to unix line endings

import os
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

def change_files(path):
     for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.php'):
                with open(os.path.join(root, file), 'rb') as open_file:
                    content = open_file.read()

                content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

                with open(os.path.join(root, file), 'wb') as open_file:
                    open_file.write(content)
                    print('File name: ' + file + ' has been changed\n')


change_files(os.getcwd())
