import ollama
import subprocess
import re
from rich.console import Console
# from rich.text import Text
# from rich.box import SIMPLE

model="deepseek-r1"

# # msg=input("enter msg : ")
# # # ollama.generate(model=model, prompt=msg)


# # while True:
# #     msg=input("enter msg (if you quit enter N): ")
# #     if msg.upper()=="N":
# #         break
# #     else:
# #         response = ollama.chat(model=model,
# #                 messages=[{'role': 'user', 'content': msg}],)
# #         print(response['message']['content'])


from termcolor import colored
c=Console()

while True:
    msg=input("enter msg (if you quit enter N): ")
    if msg.upper()=="N":
        break
    else:
        r=subprocess.run(['ollama','run',model,msg],capture_output=True,text=True)
        # cleaned_output = re.sub(r'<.*?>','',r.stdout)

        # c.print(cleaned_output,style="bold")
        
        cleaned_output = re.sub(r'<.*?>','',r.stdout)
        cleaned_output=cleaned_output.replace('**', '[bold]').replace('**', '[/bold]')
        c.print(cleaned_output)




