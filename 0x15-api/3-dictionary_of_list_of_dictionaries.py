#!/usr/bin/python3
'''GET request for employee's  TODO list progress
  2 export results to json'''

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()

        dict[user_id] = []

        for task in tasks:
            dict[user_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict, f)
