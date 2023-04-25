#!/usr/bin/python3
'''GET request for employee's  TODO list progress'''

import requests
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    empUrl = baseUrl + "/" + empId

    response = requests.get(empUrl)
    employeeName = response.json()['name']

    todoUrl = empUrl + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    done = 0
    compTasks = []

    for task in tasks:
        if task['completed']:
            compTasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in compTasks:
        print(f"\t {task['title']}")
