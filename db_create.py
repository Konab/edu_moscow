from app import db, create_app
from app.models import Super

db.create_all(app=create_app())

print("DB created.")