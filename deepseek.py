
# import argparse
from ollama import chat
from ollama import ChatResponse

# parser = argparse.ArgumentParser(description="User input string")
# parser.add_argument("ask_input", type=str, help="The string to be used as input")

# args = parser.parse_args()
model = "deepseek-r1"

# response: ChatResponse = chat(
#     model=model, messages=[
#         {
#             'role': 'user',
#             'content': args.ask_input,
#         }
#     ],
#     stream=True
# )
# for chunk in response:
#     print(chunk['message']['content'], end='', flush=True)
# print("\n")

# while True:
#     msg=input("enter msg (if you quit enter N): ")
#     if msg.upper()=="N":
#         break
#     else:
#         stream = ollama.chat(model=model,
#                 messages=[{'role': 'user', 'content': msg}],
#                 stream=True,)
#         for chunk in stream:
#             print(chunk['message']['content'], end='', flush=True)

msg=input("enter msg : ")
response: ChatResponse = chat(
     model=model, messages=[
         {
             'role': 'user',
             'content': msg,
         }
     ],
 )

for chunk in response:
    print(chunk['message']['content'], end='', flush=True)
print("\n")
