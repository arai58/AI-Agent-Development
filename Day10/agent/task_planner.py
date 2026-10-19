from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm_client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def decompose_task(user_request):

    prompt=f"""
        You are an AI task planner. Break the user's request into smaller tasks.
        Rules:
        1. Create only the tasks necessary to complete request.
        2. Put the tasks in the correct execution order.
        3. Each tasks should be a short action.
        4. Return one task per line.
        5. Do not number the tasks.
        6. Do not explain anything.
        User Request :
        {user_request}
    """

    response=llm_client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {
                "role":"system",
                "content":"You are AI Planner"
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    result=""
    tasks=[]
    if response.choices[0]:
        result=response.choices[0].message.content.strip()
        print(f"result returned \n{result}")
        print("------------------")
        for line in result.splitlines():
            line=line.strip()
            if line:
                tasks.append(line)
    
    return tasks