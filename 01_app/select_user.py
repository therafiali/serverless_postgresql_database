from sqlalchemy import select
from connect import engine
from sqlalchemy.orm import Session
from models import User

session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)
    
    
    
# Output: User(id=1, name='spongebob', fullname='Spongebob Squarepants')
#         User(id=2, name='sandy', fullname='Sandy Cheeks')    