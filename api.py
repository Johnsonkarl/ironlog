
from flask import Flask, jsonify, request, render_template
from app import calculate_one_rep_max

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/calculate")
def calculate():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    weight = data.get("weight")
    reps = data.get("reps")

    if (isinstance(weight, bool)
            or not isinstance(weight, (int, float))
            or not 0 < weight < float("inf")
            or type(reps) is not int
            or not 1 <= reps <= 30):
        return jsonify({"error": "Enter a positive weight and 1-30 reps"}), 400

    estimated_max = calculate_one_rep_max(weight, reps)

    return jsonify({
        "weight": weight,
        "reps": reps,
        "estimated_1rm": estimated_max
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
