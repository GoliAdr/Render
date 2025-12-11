from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>Hello</title>
<h1>What's your name?</h1>

<form method="post">
  <input name="name" placeholder="Your name" required>
  <button type="submit">Say hello</button>
</form>

{% if name %}
  <p>Hello, {{ name }}!</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

    return render_template_string(PAGE, name=name)


if __name__ == "__main__":
    app.run(debug=True)