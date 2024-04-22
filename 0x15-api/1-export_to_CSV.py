#!/usr/bin/python3
'''
This script generaites CSV file
'''

import requests
import csv
import sys


def export_todo_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Writing to CSV
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        for task in todo_data:
            completed = str(task['completed'])
            title_task = task['title']
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                    user_id,
                    username,
                    completed,
                    title_task))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_csv(employee_id)
