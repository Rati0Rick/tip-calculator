from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_tip():
    total = None
    if request.method == "POST":
        bill = float(request.form["bill"])
        tip_pct = float(request.form["tip"])
        total = bill * tip_pct / 100 + bill
    return render_template("tip.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)