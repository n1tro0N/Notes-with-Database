from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm.session import Session
from .db_postgre import session
from .models import User, Note



def get_user(login: str, password: str) -> User:
    stmt = select(User).where(User.login == login and User.password == password)
    result = session.execute(stmt)
    return result.scalars().one_or_none()


def get_user_by_id(id: int) -> User:
    stat = select(User).where(User.user_id == id)
    result = session.execute(stat)
    return result.scalars().one_or_none()


def add_user(login: str, password: str):
    stmt = insert(User).values(login = login, password = password)
    result = session.execute(stmt)
    session.commit()
    return result.scalars().one_or_none()


def add_note(user_id: int, title: str, content: str):
    stmt = insert(Note).values(user_id = user_id, title = title, content = content)
    result = session.execute(stmt)
    session.commit()
    return result.scalars().one_or_none()


def get_note_by_id(note_id: int) -> Note|None:
    stmt = select(Note).where(Note.note_id == note_id)
    result = session.execute(stmt)
    return result.scalars().one_or_none()


def get_all_notes_by_user(user_id):
    stmt = select(Note).where(Note.user_id == user_id)
    result = session.execute(stmt)
    return result.scalars().fetchall()


def update_note(note_id: int, title: str, content: str):
    stmt = (
        update(Note).where(Note.note_id == note_id).values(title=title, content=content)
    )
    session.execute(stmt)
    session.commit()


def delete_note(note_id: int):
    stmt = delete(Note).where(Note.note_id == note_id)
    session.execute(stmt)
    session.commit()
