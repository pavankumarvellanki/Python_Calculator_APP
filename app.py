from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    expression = ""
    error = None

    if request.method == "POST":
        expression = request.form.get("expression", "").strip()
        try:
            allowed_chars = "0123456789+-*/(). "
            if not expression:
                raise ValueError("Please enter an expression.")
            if any(ch not in allowed_chars for ch in expression):
                raise ValueError("Only numbers and operators are allowed.")

            result = eval(expression, {"__builtins__": None}, {})
        except Exception:
            error = "Enter a valid expression like 3+4*2 or 12/(3-1)."

    return render_template(
        "index.html",
        result=result,
        expression=expression,
        error=error,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
