from time import time 
import os

# Import the Python SDK
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

i = 1
for history in ["history_1", "history_2", "history_3"]:
    history = open(f"example_inputs/{history}.txt").read()
    prompt = open("libprompt/gemini_sum.prompt").read()

    print("prompting history %d..." % i)
    start_time = time()
    output = model.generate_content(history + prompt)
    print("finished, %.1f seconds" % (time()- start_time))

    with open("example_outputs/gemini_sum_%d.md" % i , "w") as f:
        f.write(output.text)
        i += 1