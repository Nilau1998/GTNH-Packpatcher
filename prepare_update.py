import os

from script_helpers import *
from backup_pack_dirs import backup_pack


def check_for_backup():
    backup_exists = False
    for fname in os.listdir('.'):
        if fname.endswith('.zip'):
            backup_exists = True
    return backup_exists


if __name__ == "__main__":
    # Make sure backup exists before removing data dir
    backup_pack()
    print("Checking if backup zip exists...")
    backup_exists = check_for_backup()
    if not backup_exists:
        print("No backup found, running the backup script!")
        if not check_for_backup():
            print("Couldn't create a backup, aborting!")
            exit()

    # Remove data dir so docker compose -d up can be ran
    print('Cleaning data dir...')
    shutil.rmtree(paths['server_data'])
    os.mkdir('data')
    print('Done!')
