
def create_state(user_request,max_steps=5):
    return {
        "user_request":user_request,
        "tasks":[],
        "current_task":None,
        "current_step":0,
        "max_steps":max_steps,
        "actions":[],
        "observations":[],
        "finished":False,
        "final_answer":""
    }


def add_task(state, task):
    state["task"].append({
        "task":task,
        "status":"pending"
    })

def complete_task(state,task):
    for item in state["tasks"]:
        if item["task"]==task:
            item["status"]="completed"
            return


#def complete_task(state, task):
#    next((item.update(status="completed") for item in state["tasks"] if item["task"] == task), None)

def add_action(state,action):
    state["actions"].append(action)

def record_obersvation(state,action,observation):
    state["observations"].append(
        {
        "step":state["current_step"],
        "action":action,
        "observation":observation
        }
    )

def add_result(state,result):
    state["results"].append(result)

def get_pending(state):
    #pending_tasks=[]
    #for item in state["tasks"]
    return [
        item["task"]
        for item in state["tasks"] item["status"]=="pending"
    ]

def all_tasks_completed(state):
    return all(
        item["status"]=="completed"
        for item in state["tasks"]
    )

def next_step(state):
    state["current_step"]+=1

def can_continue(state):
    return(
        not state["finished"]
        and state["current_step"]==state["max_steps"]
    )

def finish(state, answer):
    state["final_answer"]=answer
    state["finished"]=True