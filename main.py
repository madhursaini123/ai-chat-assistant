from openai import OpenAI

messages = [
    {"role": "system", "content": "You are a helpful AI assistant for students"}
]

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.deepseek.com/v1"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "clear":
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant for students"}
        ]
        print("Memory cleared!")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})