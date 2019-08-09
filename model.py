from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    #In case this fcn is ran more than once 
    Game.query.delete()

    #Adding sample data to testdb Database 
    sample1 = Game(game_id=10, name="Grace Game", description="YAY")
    sample2 = Game(game_id=13, name="Kaz Game", description="Easiest game ever")
    db.session.add_all([sample1,sample2])
    db.session.commit()



if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
