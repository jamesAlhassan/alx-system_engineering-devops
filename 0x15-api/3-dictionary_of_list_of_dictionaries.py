#!/usr/bin/python3
'''GET request for employee's  TODO list progress
  2 export results to json'''

import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"

    emps = requests.get(url).json()

    dictionary = {}
    for emp in emps:
        emp_id = emp['id']
        username = emp['username']

        todos = requests.get("{}/{}/todos".format(url, emp_id))
        todos_res = todos.json()

        dictionary[emp_id] = []
        tasks = []
        for todo in todos:
            tasks.append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            })
            dictionary[emp_id] = tasks

    with open("todo_all_employees.json".format(emp_id), "w") as f:

        json.dump(dictionary, f)
