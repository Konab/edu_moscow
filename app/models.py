from app import db


class Super(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), index=True)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Name: {}'.format(self.name)
