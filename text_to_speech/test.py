import playsound
import openai
import os

audio = openai.audio.speech.create(
    input="Hello there! Welcome to the Unconventional Coding channel. Please subscribe and hit the like button!",
    model="tts-1",
    voice="alloy",
)

audio.stream_to_file("audio.mp3")

playsound.playsound("audio.mp3")

os.remove("audio.mp3")
