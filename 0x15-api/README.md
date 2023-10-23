## API

#### Task 0
[0-gather_data_from_an_API.py](0-gather_data_from_an_API.py) is a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.
Requirements:
- Uses `urllib` or `requests` module
- The script accepts an integer as a parameter, which is the employee ID
- The script displays on the standard output the employee TODO list progress in this exact format:
	- First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
		- `EMPLOYEE_NAME`: name of the employee
		- `NUMBER_OF_DONE_TASKS`: number of completed tasks
		- `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
	- Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

#### Task 1
[1-export_to_CSV.py](1-export_to_CSV.py) is Python script that extends [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py) to export data in the CSV format.
Requirements:
- Records all tasks that are owned by this employee
- Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- File name: `USER_ID.csv`

#### Task 2
[2-export_to_JSON.py](2-export_to_JSON.py) is Python script that extends [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py) to export data in the JSON format.
Requirements:
- Records all tasks that are owned by this employee
- Format: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name: `USER_ID.json`
