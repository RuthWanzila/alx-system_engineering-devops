#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""
import json
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
    todos_resp = requests.get(url + "todos", params={"userId": employee_id})
    todos = todos_resp.json()

    # Export TODO list to JSON
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(
            {
                employee_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username,
                    }
                    for task in todos
                ]
            },
            jsonfile,
        )
