from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to encrypt session data

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get players from the form
        players = []
        for key in request.form:
            if key.startswith("player"):
                name = request.form.get(key)
                if name.strip():
                    players.append(name.strip())

        if players:
            # Save the players in session
            session['players'] = players
            return redirect(url_for('start_game'))

    return render_template("pages.html")  # Change to page.html for your main page

@app.route("/start-game", methods=["GET"])
def start_game():
    if 'players' not in session or len(session['players']) == 0:
        return redirect(url_for('home'))  # If no players are saved, redirect back to the homepage

    # Select a random player
    selected_player = random.choice(session['players'])
    return render_template("game.html", selected_player=selected_player)  # Change to game.html for the game page

@app.route("/reset-game", methods=["GET"])
def reset_game():
    session.pop('players', None)  # Clear players from session
    return redirect(url_for('home'))  # Redirect to the homepage to start fresh

if __name__ == "__main__":
    app.run(debug=True)
