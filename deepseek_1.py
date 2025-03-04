import ollama

model="deepseek-r1"

# msg=input("enter msg : ")
# ollama.generate(model=model, prompt=msg)


while True:
    msg=input("enter msg (if you quit enter N): ")
    if msg.upper()=="N":
        break
    else:
        response = ollama.chat(model=model,
                messages=[{'role': 'user', 'content': msg}],)
        print(response['message']['content'])
