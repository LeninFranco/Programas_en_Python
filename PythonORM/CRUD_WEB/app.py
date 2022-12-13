from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    artist = db.Column(db.String(30))

app.secret_key = 'mykey'

@app.route('/')
def home():
    return render_template('index.html', songs = Song.query.all())

@app.route('/addSong', methods=['POST'])
def add():
    id = int(request.form['idSong'])
    name = request.form['name']
    artist = request.form['artist']
    s = Song()
    s.id = id
    s.name = name
    s.artist = artist
    db.session.add(s)
    db.session.commit()
    flash('success')
    flash('Song Added Successfully')
    return redirect(url_for("home"))

@app.route('/deleteSong/<string:idSong>')
def delete(idSong):
    song_id = int(idSong)
    s = Song.query.filter_by(id=song_id).first()
    db.session.delete(s)
    db.session.commit()
    flash('danger')
    flash('Song Deleted Successfully')
    return redirect(url_for("home"))

@app.route('/editSong/<string:idSong>')
def edit(idSong):
    song_id = int(idSong)
    s = Song.query.filter_by(id=song_id).first()
    return render_template('edit.html', song = s)

@app.route('/updateSong', methods=['POST'])
def update():
    ID = int(request.form['idSong'])
    name = request.form['name']
    artist = request.form['artist']
    s = Song.query.filter_by(id=ID).first()
    s.name = name
    s.artist = artist
    db.session.commit()
    flash('success')
    flash('Song Updated Successfully')
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=3000, debug=True)