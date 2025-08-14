#!/usr/bin/env python3
import csv
import subprocess
import requests
import os

# URL of your CSV (direct link)
CSV_URL = "https://raw.githubusercontent.com/cokeryeena/bulk-user-creation/refs/heads/main/users.csv" 

def download_csv(url, filename):
    """Download CSV from the internet."""
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded latest CSV to {filename}")

def create_user(username, password):
    """Create system user and set password."""
    try:
        subprocess.run(["useradd", "-m", username], check=True)
        subprocess.run(["chpasswd"], input=f"{username}:{password}".encode(), check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

def main():
    csv_file = "users.csv"
    
    # Step 1: Get latest CSV
    download_csv(CSV_URL, csv_file)

    # Step 2: Read CSV and create users
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row['username']
            password = row['password']
            # Check if user already exists
            if subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                print(f"User '{username}' already exists. Skipping.")
            else:
                create_user(username, password)

if __name__ == "__main__":
    main()
