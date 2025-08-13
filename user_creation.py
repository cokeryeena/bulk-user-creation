#!/usr/bin/env python3
import csv
from datetime import datetime

def create_user(username, password):
    # Simulate "creating" a user by writing to a log file
    with open("created_users.txt", "a") as f:
        f.write(f"{datetime.now()} - Created user: {username} with password: {password}\n")
    print(f"User '{username}' created (simulated).")

def main():
    csv_file = "users.csv"

    # Open and read CSV file
    with open(csv_file, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 2:
                print(f"Skipping invalid row: {row}")
                continue
            username, password = row
            create_user(username.strip(), password.strip())

if __name__ == "__main__":
    main()
