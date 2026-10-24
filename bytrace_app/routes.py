from flask import render_template, request, jsonify
from bytrace_app import app
from bytrace_app.engine import convert
from bytrace_app.events import save_event


@app.route("/", methods=["GET", "POST"])
def home_page():
    output = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        converter_type = request.form.get("converter_type")

        output = convert(user_input, converter_type)

    return render_template("index.html", output=output)


@app.route("/track-event", methods=["POST"])
def track_event():
    data = request.get_json()
    
    return jsonify({"message": "event tracked"})


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/engine")
def engine_page():
    return render_template("engine.html")