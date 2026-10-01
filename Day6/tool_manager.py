from tools import(get_current_time,roll_dice,generate_password)

def execute_tool(user_intent):

    user_intent_lower = user_intent.lower()
    output=""
    if "time" in user_intent_lower or "clock" in user_intent_lower:
        output="current time is " + get_current_time()
    elif "password" in user_intent_lower or "passcode" in user_intent_lower:
        output="Your generated password of length 12 is " + generate_password(12)
    elif "dice" in user_intent_lower or "die" in user_intent_lower:
        output=f"You rolled {roll_dice()}"
    else:
        output="AI_RUN"

    return output