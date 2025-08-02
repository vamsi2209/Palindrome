from flask import Flask, request, render_template

app = Flask(__name__)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["text"]
        result = "✅ Palindrome!" if is_palindrome(user_input) else "❌ Not a palindrome."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

