from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def percentage_calculator():
    result = None
    calculator_type = None

    if request.method == "POST":
        calculator_type = request.form.get("calculator_type")

        try:
            if calculator_type == "basic":
                number = float(request.form.get("number"))
                percent = float(request.form.get("percent"))
                result = (number * percent) / 100

            elif calculator_type == "increase_decrease":
                old_value = float(request.form.get("old_value"))
                new_value = float(request.form.get("new_value"))
                result = ((new_value - old_value) / old_value) * 100

            elif calculator_type == "reverse":
                increased_value = float(request.form.get("increased_value"))
                percent = float(request.form.get("percent"))
                result = increased_value / (1 + percent / 100)

            elif calculator_type == "total":
                value = float(request.form.get("value"))
                total = float(request.form.get("total"))
                result = (value / total) * 100

            elif calculator_type == "profit_loss":
                cost = float(request.form.get("cost"))
                selling = float(request.form.get("selling"))
                result = ((selling - cost) / cost) * 100

            elif calculator_type == "discount":
                original_price = float(request.form.get("original_price"))
                discount = float(request.form.get("discount"))
                result = original_price - ((discount / 100) * original_price)

            elif calculator_type == "marks":
                obtained = float(request.form.get("obtained"))
                total_marks = float(request.form.get("total_marks"))
                result = (obtained / total_marks) * 100

            elif calculator_type == "interest":
                principal = float(request.form.get("principal"))
                rate = float(request.form.get("rate"))
                time = float(request.form.get("time"))
                result = (principal * rate * time) / 100

            elif calculator_type == "tax":
                price = float(request.form.get("price"))
                tax = float(request.form.get("tax"))
                result = price + (price * tax / 100)

            elif calculator_type == "weight":
                part_weight = float(request.form.get("part_weight"))
                total_weight = float(request.form.get("total_weight"))
                result = (part_weight / total_weight) * 100

        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, calculator_type=calculator_type)

if __name__ == "__main__":
    app.run(debug=True)
