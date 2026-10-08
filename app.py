from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        text = request.form["text"]
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

        stack = list(cleaned)
        queue = deque(cleaned)

        stack_output = "".join(stack[::-1])
        queue_output = "".join(queue)

        if cleaned == stack_output:
            result = {
                "result": "PALINDROME",
                "reason": f'"{text}" reads the same forward and backward.',
                "stack": stack_output,
                "queue": queue_output,
                "input": cleaned
            }
        else:
            result = {
                "result": "NOT PALINDROME",
                "reason": f'"{text}" does not read the same forward and backward.',
                "stack": stack_output,
                "queue": queue_output,
                "input": cleaned
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
            

            

   
