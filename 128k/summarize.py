import openai

with open("ultimate-guide-to-digital-marketing.txt") as f:
    book_text = f.read()

response = openai.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "user",
            "content": book_text + "\n\n####\n\n What delivery rate does the book recommend?"
        }
    ]
)

print(response.choices[0].message.content)

print(f"\nTotal tokens: {response.usage.total_tokens}")
