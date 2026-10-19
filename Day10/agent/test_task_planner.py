from task_planner import decompose_task

user_request="Generate a password of length 15 with chars only, tell me current time and explain me Python."

tasks=decompose_task(user_request)

for task in tasks:
    print(f"tasks is : {task}")