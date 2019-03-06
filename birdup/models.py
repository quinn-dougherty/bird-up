''' SQLAlchemy models for birdup '''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    ''' twitter users that we pull and analyze tweets for. '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f'<User {self.name}>'


class Tweet(DB.Model):
    ''' tweets '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(500))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(
        DB.BigInteger,
        DB.ForeignKey('user.id'),
        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        try:
            x = self.text
        except BaseException:
            x = self.full_text
        return f'<Tweet {x}>'
