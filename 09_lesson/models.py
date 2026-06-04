from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_URL = "postgresql://postgres:123@localhost:5432/QA"


class SubjectTable:
    __scripts = {
        "insert": text("INSERT INTO subject (subject_title) VALUES (:title);"),
        "select by title": text("SELECT * FROM subject "
                                "WHERE subject_title = :title"),
        "delete by title": text("DELETE FROM subject "
                                "WHERE subject_title = :title_to_delete"),
        "truncate": text("TRUNCATE TABLE subject RESTART IDENTITY CASCADE;")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string, echo=True)

    def clear_table(self):
        self.__db.execute(self.__scripts["truncate"])

    def add_subject(self, title):
        self.__db.execute(self.__scripts["insert"], title=title)

    def get_subject_by_title(self, title):
        return self.__db.execute(self.__scripts["select by title"],
                                 title=title).fetchone()

    def delete_subject_by_title(self, title):
        self.__db.execute(self.__scripts["delete by title"],
                          title_to_delete=title)


db_table = SubjectTable(db_URL)
