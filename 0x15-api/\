#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from command-line argument
    employee_id = sys.argv[1]

    # API URL
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    username = user.get("username")

    # Fetch TODO list for the employee
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Export TODO list to CSV
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
