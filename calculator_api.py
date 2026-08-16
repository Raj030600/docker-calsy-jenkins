from flask import Flask, request, jsonify

app = Flask(__name__)


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    elif operator == "%":
        if b == 0:
            raise ValueError("Cannot use modulo with zero")
        return a % b
    elif operator == "**":
        return a ** b
    else:
        raise ValueError("Unsupported operator")


@app.route("/")
def home():
    return jsonify({
        "message": "Docker Calculator API is running",
        "usage": "/calculate?a=10&b=2&op=+"
    })


@app.route("/calculate")
def calculate_api():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        operator = request.args.get("op")

        result = calculate(a, b, operator)

        return jsonify({
            "a": a,
            "b": b,
            "operator": operator,
            "result": result
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except Exception:
        return jsonify({
            "error": "Invalid request"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)