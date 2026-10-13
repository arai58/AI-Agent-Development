
#Initialize variable
def create_state(user_request,max_steps=5):
    """
    Inititalize state variable
    """
    return {
        "user_request":user_request,
        "current_step":0,
        "max_steps":max_steps,
        "actions":[],
        "observations":[],
        "finished":False,
        "final_answer":""
    }

def add_action(state,action):
    """
    Inititalize add latest action taken
    """
    state["actions"].append(action)

def record_observations(state,action,observation):
    """
    add new observation.
    """
    state["observations"].append(
        {
            "step":state["current_step"],
            "action":action,
            "observation":observation
        }
    )

def next_step(state):
    """
    Update state current step with + 1
    """
    state["current_step"]+=1

def can_continue(state):
    """
    validates and suggest if it can continue or not
    """
    return(
        not state["finished"]
        and
        state["current_step"]<state["max_steps"]
    )

def finish(state,answer):
    """
    all steps has been takena nd state to record same.
    """
    state["final_answer"]=answer

    state["finished"]=True