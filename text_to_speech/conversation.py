import playsound
import openai
import json
import os

def play_with_voice(voice, speech):
    audio = openai.audio.speech.create(
        input=speech,
        model="tts-1",
        voice=voice,
    )

    audio.stream_to_file("audio.mp3")
    playsound.playsound("audio.mp3")
    os.remove("audio.mp3")

def mark_speaks(speech):
    play_with_voice("echo", speech)

def lisa_speaks(speech):
    play_with_voice("nova", speech)

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "system",
            "content": "You are a conversation generator. Generate the full conversation using function calls. Call the speech functions 5 times for both Mark and Lisa",
        },
        {
            "role": "user",
            "content": "Create a conversation between Lisa and Mark. They're talking about Rust vs C++"
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "mark_speaks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "speech": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "lisa_speaks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "speech": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    ]
)

for tool_call in response.choices[0].message.tool_calls:
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print(function_name + ": " + arguments["speech"])

    if function_name in ["mark_speaks", "lisa_speaks"]:
        globals()[function_name](**arguments)
