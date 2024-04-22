#!/usr/bin/python3
"""
Export employee TODO list data in JSON format.

This script fetches the TODO list data of a specific
employee from the JSONPlaceholder API
and exports it to a JSON file with the specified format.

Requirements:
- Records all tasks that are owned by the specified employee.
- Format: { "USER_ID": [
    {
        "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ...
    ]}
- File name: USER_ID.json

Usage:
python script.py <employee_id>
"""

import requests
import json
import sys


def export_todo_json(employee_id):
    """
    Export TODO list data of a specific employee
    in JSON format.

    Args:
        employee_id (int): The ID of the employee
          whose TODO list is to be exported.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetching user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Fetching TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Constructing JSON data
    json_data = {str(user_id): [{"task": task["title"],
                                 "completed": task["completed"],
                                 "username": username} for task in todo_data]}

    # Writing to JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"JSON file '{filename}' has been generated successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_json(employee_id)
