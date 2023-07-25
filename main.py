import openai
openai.api_key = "API_KEY"

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages = [{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message["content"]

while True:
    print("Enter -exit- to exit")
    text = input("Enter your prompt:\n")
    if text == "exit":
        break
    response = get_completion(text)
    print(response)
    
