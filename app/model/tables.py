from app import db


#criação da tabela de usuarios
class User(db.Model):
    #atribuição do nome da tabela no banco
    __tablename__ = "users"

    # colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # construtor da tabela
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

#criação da tabela de usuarios
class Post(db.Model):
    #atribuição do nome da tabela no banco
    __tablename__ = "posts"

    # colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))

    owner = db.relationship('User', foreign_keys=user_id)

    # construtor da tabela
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id

class Followers(db.Model):
    __tablename__ = "followers"


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.foreignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)

    def __init__(self, user_id, follwer_id):
        self.user_id = user_id
        self.follower_id = follwer_id

