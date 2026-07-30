from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {
        "id": 101,
        "name": "John",
        "department": "HR",
        "email": "john@example.com"
    },
    {
        "id": 102,
        "name": "David",
        "department": "IT",
        "email": "david@example.com"
    },
    {
        "id": 103,
        "name": "Sarah",
        "department": "Finance",
        "email": "sarah@example.com"
    }
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# Webhook test