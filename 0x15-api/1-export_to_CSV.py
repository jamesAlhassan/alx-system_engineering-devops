#!/usr/bin/python3
'''GET request for employee's  TODO list progress
export results to csv'''

import requests
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    empUrl = baseUrl + "/" + empId

    response = requests.get(empUrl)
    userName = response.json()['username']

    todoUrl = empUrl + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(empId), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(empId, userName, task['completed'],
                            task['title']))
