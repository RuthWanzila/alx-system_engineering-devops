#!/usr/bin/python3
""" export data in the JSON format """
import json


def export_tasks_to_json(user_id, tasks):
    data = {user_id: []}
    for task in tasks:
        task_data = {
            'task': task['title'],
            'completed': task['completed'],
            'username': task['username']
        }
        data[user_id].append(task_data)

    filename = f'{user_id}.json'
    with open(filename, 'w') as file:
        json.dump(data, file)


# Example usage
user_id = 'USER123'
tasks = [
    {
        'title': 'Task 1',
        'completed': True,
        'username': 'JohnDoe'
    },
    {
        'title': 'Task 2',
        'completed': False,
        'username': 'JohnDoe'
    },
    {
        'title': 'Task 3',
        'completed': True,
        'username': 'JohnDoe'
    }
]

export_tasks_to_json(user_id, tasks)
