import openai

response = openai.images.generate(
    model="dall-e-3",
    prompt="a puppy drinking a martini on the beach",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)
