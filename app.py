from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        if text == text[::-1]:
            result = f'"{text}" is a Palindrome!'
        else:
            result = f'"{text}" is NOT a Palindrome!'

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

        
            

            

   
