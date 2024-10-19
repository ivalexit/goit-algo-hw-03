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

            
