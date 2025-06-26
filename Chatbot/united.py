import openai

openai.api_key = 'your-api-key-here'

def chat():
    print("ChatGPT: Ask me anything! Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            break
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print("ChatGPT:", response['choices'][0]['message']['content'])

chat()