import os
import shutil
from pathlib import Path
import sys


def create_random_files(directory, num_files=10):
    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)
    file_extensions = ['txt', 'pdf', 'jpg', 'png', 'docx', 'py']

    for i in range(num_files):
        for ext in file_extensions:
            file_path = target_dir / f'random_file_{i + 1}.{ext}'
            file_path.write_text(f'This is a random test file with extension .{ext}')
            print(f'Created file: {file_path}')


def copy_and_delete_files_recursive(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_and_delete_files_recursive(item_path, dest_dir)

                if not os.listdir(item_path):
                    os.rmdir(item_path) # Delete empty directory 
                    print(f'Deleted empty directory: {item_path}')
                else:
                    file_extension = os.path.splitext(item)[1][1:]
                    if not file_extension:
                        file_extension = "no_extension"
                    target_dir = os.path.join(dest_dir, file_extension)
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    shutil.copy2(item_path, os.path.join(target_dir, item))
                    print(f'Copying file: {item_path} -> {os.path.join(target_dir, item)}')

                    os.remove(item_path)  # Delete file after copying
                    print(f'Deleted original file: {item_path}')

    except OSError as e:
        print(f'Error accessing files or directories: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
           
def main():
    try: #Parse command line args
        if len(sys.argv) < 2:
            print(f'Please specify the path to the source directory.')
            sys.exit(1)

        src_dir = sys.argv[1] #Source directory
        dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist' # Destination directory

        print(f'Creating random files in directory {src_dir}')
        create_random_files(src_dir, num_files=10)

        print(f'Sorting files in directory {dest_dir} and deleting them from {src_dir}')
        copy_and_delete_files_recursive(src_dir, dest_dir)
        print(f'Files have been copied, sorted and deleted from the source directory.')

    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    main()

    