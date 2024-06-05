from time import time 
import os

# Import the Python SDK
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

history = open("history/all_by_day.json").read()
prompt = open("libprompt/gemini_sum.prompt").read()

print("prompting ...")
start_time = time()
output = model.generate_content(history + prompt)
print("finished, %.1f seconds" % (time()- start_time))

with open("gemini_sum.md", "w") as f:
    f.write(output.text)