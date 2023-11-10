import openai

assistant = openai.beta.assistants.create(
    model="gpt-3.5-turbo-1106",
    name="Riddlebot",
    instructions="You answer all questions in riddles",
)

print(f"Assistant ID: {assistant.id}")

thread = openai.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How do I get started with Python?",
        }
    ]
)

print(f"Thread ID: {thread.id}")

run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

print(f"Run ID: {run.id}")
