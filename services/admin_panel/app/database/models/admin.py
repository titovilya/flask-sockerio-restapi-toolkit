from app.database import db


class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(120))
    login = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return "<Admin(id = '{0}', name = '{1}', role = '{2}')>".format(self.id, self.name, self.role)
