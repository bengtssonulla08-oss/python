import pytest
from models import db_table


@pytest.fixture(autouse=True)
def clean_db():
    yield
    db_table.clear_table()


def test_add_subject():
    db_table.add_subject(title="Астрономия")
    result = db_table.get_subject_by_title("Астрономия")

    assert result is not None
    assert result.subject_title == "Астрономия"


def test_update_subject():
    db_table.add_subject(title="Музыка")

    db_table.delete_subject_by_title("Музыка")
    db_table.add_subject(title="Химия")
    old_result = db_table.get_subject_by_title("Музыка")
    new_result = db_table.get_subject_by_title("Химия")
    assert old_result is None
    assert new_result is not None


def test_delete_subject():
    db_table.add_subject(title="Литература")
    db_table.delete_subject_by_title("Литература")
    result = db_table.get_subject_by_title("Литература")
    assert result is None
