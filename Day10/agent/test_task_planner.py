from task_planner import decompose_task

user_request="Generate a password and tell me current time.."

tasks=decompose_task(user_request)

for task in tasks:
    print(f"tasks is : {task}")