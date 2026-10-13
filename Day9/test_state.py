from agent.agent import *

state=create_state("Generate Password and tell me current time")

print(state)

add_action(state,"generate_password")
record_observation(
    state,
    "generate_password",
    "Password: X#L8adhaih"
)
next_step(state)
finish(state)

print(state)