from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        text = request.form["text"]

        # Remove spaces and special characters
        clean_text = ""

        for ch in text:
            if ch.isalnum():
                clean_text += ch.lower()

        # Create stack and queue
        stack = []
        queue = deque()

        # Insert characters
        for ch in clean_text:
            stack.append(ch)
            queue.append(ch)

        stack_output = ""
        queue_output = ""
        reverse_text = ""

        # Check using stack and queue
        is_palindrome = True

        while stack:

            s = stack.pop()
            q = queue.popleft()

            stack_output += s + " "
            queue_output += q + " "

            reverse_text += s

            if s != q:
                is_palindrome = False

        # Give reason
        if is_palindrome:

            reason = (
                "The characters read the same from "
                "front to back and back to front."
            )

            result_text = "PALINDROME"

        else:

            reason = (
                "The characters are different when "
                "compared from opposite directions."
            )

            result_text = "NOT PALINDROME"

        result = {
            "input": clean_text,
            "result": result_text,
            "reason": reason,
            "stack": stack_output,
            "queue": queue_output
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)