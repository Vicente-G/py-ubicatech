from sqlmodel import Session, SQLModel, create_engine

from src.config import PG_URL

engine = create_engine(PG_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def db_exec(operation, *args):
    with Session(engine) as session:
        return operation(session, *args)
