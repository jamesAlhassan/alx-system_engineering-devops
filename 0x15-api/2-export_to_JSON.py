#!/usr/bin/python3
'''GET request for employee's  TODO list progress
export results to json'''

import requests
import sys
import json


if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    empUrl = baseUrl + "/" + empId

    response = requests.get(empUrl)
    userName = response.json()['username']

    todoUrl = empUrl + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dict = {empId: []}
    for task in tasks:
        dict[empId].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": userName
        })
    with open('{}.json'.format(empId), 'w') as f:
        json.dump(dict, f)
