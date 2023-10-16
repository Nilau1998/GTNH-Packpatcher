import os

from script_helpers import *

if __name__ == "__main__":
    # Backup to data
    for file in dirs_to_copy:
        copy_directory(
            os.path.join(paths['backup'], file),
            os.path.join(paths['server_data'], file)
        )
    for file in files_to_copy:
        copy_file(
            os.path.join(paths['backup'], file),
            os.path.join(paths['server_data'])
        )

    # Move extra mods
    for file in os.listdir(paths['extra_mods']):
        copy_file(
            os.path.join(paths['extra_mods'], file),
            os.path.join(paths['server_mods'])
        )

    # Patch configs
    find_and_replace_in_file(
        config_paths['gregtech'],
        'B:EnablePollution=true',
        '    B:EnablePollution=false'
    )
    print("Pack has been patched!")
