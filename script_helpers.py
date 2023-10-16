import os
import shutil

dirs_to_copy = [
    'local',
    'resourcepacks',
    'TCNodeTracker',
    'visualprospecting',
    'World'
]

files_to_copy = [
    'banned-ips.json',
    'banned-players.json',
    'ops.json',
    'server.properties',
    'usernamecache.json',
    'whitelist.json',
    'run.sh'
]

paths = {
    'server_data': os.path.join('data'),
    'server_mods': os.path.join('data', 'mods'),
    'backup': os.path.join('backup'),
    'extra_mods': os.path.join('extra_mods'),
}

config_paths = {
    'gregtech': os.path.join('data', 'config', 'GregTech', 'GregTech.cfg')
}


def copy_directory(src_dir, des_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(des_dir):
            os.makedirs(des_dir)

        for item in os.listdir(src_dir):
            source_item = os.path.join(src_dir, item)
            destination_item = os.path.join(des_dir, item)

            if os.path.isdir(source_item):
                # Recursively copy subdirectories
                copy_directory(source_item, destination_item)
            else:
                # Copy individual files
                shutil.copy2(source_item, destination_item)

        print(f"Directory '{src_dir}' copied to '{des_dir}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def find_and_replace_in_file(file_path, target_string, replacement_string):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        found = False
        with open(file_path, 'w') as file:
            for line in lines:
                if target_string in line:
                    file.write(replacement_string + '\n')
                    found = True
                else:
                    file.write(line)

        if found:
            print(f"Target string '{target_string}' found and replaced in '{file_path}'.")
        else:
            print(f"Target string '{target_string}' not found in '{file_path}'. No replacements made.")

    except Exception as e:
        print(f"Error: {e}")


def copy_file(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except shutil.Error as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
