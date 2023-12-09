"""
app.py
2023-12-09, J. Köppern
A Flask application demonstrating both non-session and session-based state
management. The root route ('/') allows users to add items to a shared list,
showing how data persists across different user sessions. The '/session' route
implements Flask sessions, providing each user with their individual list,
demonstrating the isolation of user sessions in a web application.
"""

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a real secret key

# Shared list for non-session demonstration
items = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        items.append(item)
        return redirect(url_for("index"))
    return render_template("index.html", items=items)

@app.route("/session", methods=["GET", "POST"])
def session_index():
    if 'items' not in session:
        session['items'] = []

    if request.method == "POST":
        item = request.form.get("item")
        session['items'].append(item)
        session.modified = True
        return redirect(url_for("session_index"))

    return render_template("index_with_session.html", items=session['items'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
