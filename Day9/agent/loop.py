from state import *

async def run_agent_loop(user_request, planner, 
execute_action,
format_answer, tools, client):

    #Step 1:
    state=create_state(user_request)

    #loop
    while can_continue(state):

        #Call planner to get next step tool
        action=planner(state,tools)
        print("Planner selected:", action)
        if action.upper()=="FINISH":
            answer=format_answer(state)
            finish(state,answer)
            break
        
        #Weexcute the action
        observation=await execute_action(action,state, client)

        #update state
        add_action(state,action)
        record_observations(state, action, observation)
        next_step(state)

    return state