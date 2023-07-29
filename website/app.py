import os

from flask import Flask, render_template

app = Flask(__name__)


#Main and categories
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/articles")
def articles():
    return render_template('articles.html')

@app.route("/apps")
def apps():
    return render_template('apps.html')

@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/about")
def about():
    return render_template('about.html')


#Standalones
@app.route("/animelist")
def animelist():
    return render_template('animelist.html')

@app.route("/careerplanner")
def careerplanner():
    return render_template('careerplanner.html')

@app.route("/game-design")
def game_design():
    return render_template('game_design.html')

@app.route("/game-list")
def game_list():
    return render_template('game_list.html')


#Reviews
@app.route("/reviews")
def reviews():
    return render_template('reviews.html')

@app.route("/reviews/book-list")
def book_list():
    return render_template('reviews/book_list.html')

@app.route("/reviews/carl-jung")
def carl_jung():
    return render_template('reviews/carl_jung.html')

@app.route("/reviews/music")
def music():
    return render_template('reviews/music.html')


#Apps
@app.route("/apps/journal")
def journal():
    return render_template('journal.html')


#Games
@app.route("/games/frankia")
def frankia():
    return render_template('frankia.html')

@app.route("/games/hero-wars")
def hero_wars():
    return render_template('hero_wars.html')
    

#Articles
@app.route("/articles/anime")
def anime():
    return render_template('articles/anime.html')

@app.route("/articles/game-development")
def game_development():
    return render_template('articles/game_development.html')

@app.route("/articles/jordan-peterson-carl-jung")
def jbp_cgjung():
    return render_template('articles/jbp_cgjung.html')

@app.route("/articles/psychological-types")
def psychological_types():
    return render_template('articles/psychological_types.html')

@app.route("/articles/write-your-own-rules")
def rules():
    return render_template('articles/rules.html')
    
@app.route("/articles/seneca")
def seneca():
    return render_template('articles/seneca.html')

@app.route("/articles/fishing-in-stardew-valley")
def sdv_fishing():
    return render_template('articles/sdv_fishing.html')

@app.route("/articles/vinland-saga")
def vinland_saga():
    return render_template('articles/vinland_saga.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))