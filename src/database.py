from sqlmodel import Session, SQLModel, create_engine

from src.config import PG_URL

engine = None
if PG_URL is not None:
    engine = create_engine(PG_URL)


def init_db():
    if engine is not None:
        SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def db_exec(operation, *args):
    with Session(engine) as session:
        return operation(session, *args)
