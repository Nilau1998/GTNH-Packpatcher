import os
import shutil
from time import gmtime, strftime

from script_helpers import *


def backup_pack():
    backup_path = os.path.join(paths['backup'])

    # Check if data dir has data
    with os.scandir(paths['server_data']) as it:
        if not any(it):
            print("Data folder is empty, hopefully you already have a backup!")
            exit()

    # Check if backup dir exists
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    # Data to backup
    for file in dirs_to_copy:
        copy_directory(
            os.path.join(paths['server_data'], file),
            os.path.join(paths['backup'], file)
        )
    for file in files_to_copy:
        copy_file(
            os.path.join(paths['server_data'], file),
            os.path.join(paths['backup'])
        )

    # Pack backup
    print("Packing your backup to a zip...")
    now = strftime('%Y-%m-%d_%H-%M-%S', gmtime())
    shutil.make_archive('backup_' + now, 'zip', paths['backup'])
    print("Done!")


if __name__ == "__main__":
    backup_pack()
