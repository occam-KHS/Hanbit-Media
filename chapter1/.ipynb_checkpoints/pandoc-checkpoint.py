import subprocess
import os
path = r'C:\Users\shinki\PycharmProjects\Hanbit_Media'
os.chdir(path)

my_command=['dir']
subprocess.run(my_command, shell=True)

