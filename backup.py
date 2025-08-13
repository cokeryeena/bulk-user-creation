#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

# Folders
source_folder = "source"
backup_dir = "backups"

# Ensure both directories exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(backup_dir, exist_ok=True)

# Check if source folder has files
if not os.listdir(source_folder):
    print("No files in source folder. Backup skipped.")
else:
    # Create timestamped backup folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(backup_dir, timestamp)

    # Copy source to backup folder
    shutil.copytree(source_folder, backup_folder)
    print(f"Backup completed: {backup_folder}")

