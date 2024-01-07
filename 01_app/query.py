from models import Base
from connect import engine

Base.metadata.create_all(engine)