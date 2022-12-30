from models import db,connect_db,Todo
from app import app

db.drop_all()
db.create_all()

todos = [
    Todo(title="Feed the Chickens"),
    Todo(title ="Water Orchids"),
    Todo(title="Wash Dishes", done=True),
    Todo(title = "Workout Today!"),
    Todo(title ="No but really, workout todays", done=True),
    Todo(title = "Collect Eggs From chiekens(steal their unborn babies)")
]

db.session.add(todos)
db.session.commit()