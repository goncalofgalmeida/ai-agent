import os

def get_files_info(working_directory, directory='.'):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    working_dir_abs_path = os.path.abspath(working_directory)

    if not(full_path == working_dir_abs_path or full_path.startswith(working_dir_abs_path + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not(os.path.isdir(full_path)):
        return f'Error: "{directory}" is not a directory'
    

    try:
        entries = os.listdir(full_path)
        directory_files_infos = []
        for entry in entries:
            entry_path = os.path.join(full_path, entry)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            directory_files_infos.append(f'- {entry}: file_size={size} bytes, is_dir={is_dir}')
        
        return '\n'.join(directory_files_infos)
    except Exception as e:
            return f'Error: {e}'
        



# Build and return a string representing the contents of the directory. It should use this format:

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False