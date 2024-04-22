#!/usr/bin/python3
"""
Export all employees' TODO list data in JSON format.

This script fetches the TODO list data of all
employees from the JSONPlaceholder API,
constructs JSON data with the required format,
and writes it to a JSON file.

Requirements:
- Records all tasks from all employees.
- Format: {
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS},
            ...
            ],
            ...
        }
- File name: todo_all_employees.json

Usage:
python script.py
"""

import requests
import json


def export_all_todo_json():
    """
    Export all employees' TODO list data in JSON format.

    This function fetches the TODO list data of all
    employees from the JSONPlaceholder API,
    constructs JSON data with the required format,
    and writes it to a JSON file.

    Args:
        None

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    # Fetching user data
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Constructing JSON data
    json_data = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        todo_url = f"{base_url}/todos?userId={user_id}"
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()
        json_data[str(user_id)] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            } for task in todo_data]

    # Writing to JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"JSON file '{filename}' has been generated successfully.")


if __name__ == "__main__":
    export_all_todo_json()
