import pytest
import model_User


def test_user():
    x = model_User.User(123456, "Vasiliy", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)
    name = x.name
    email = x.email
    user_id = x.id
    used_book_id = x.used_books_id

    assert name == "Vasiliy"
    assert email == "parazit@gmail.com"
    assert user_id == 123456
    assert used_book_id == [1234, 5678, 9101112, 7889]

# If delivered empty.


def test_passes_id():
    with pytest.raises(Exception):
        model_User.User(" ", "dsds", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_name():
    with pytest.raises(Exception):
        model_User.User(123456, " ", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_email():
    with pytest.raises(Exception):
        model_User.User(123456, "dsds", " ",
                        1234, 5678, 9101112, 7889)


def test_passes_user_book_id():
    with pytest.raises(Exception):
        model_User.User(123456, "dsds", "parazit@gmail.com", " ")


# If delivered short.

def test_passes_id_short():
    with pytest.raises(Exception):
        model_User.User(123, "Vasiliy", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_name_short():
    with pytest.raises(Exception):
        model_User.User(123456, "Vas", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_email_short():
    with pytest.raises(Exception):
        model_User.User(123456, "Vasiliy", "par",
                        1234, 5678, 9101112, 7889)


def test_passes_user_book_id_short():
    with pytest.raises(Exception):
        model_User.User(123456, "Vasiliy", "parazit@gmail.com",
                        1234, 567, 9101112, 7889)

# If delivered long.


def test_passes_id_long():
    with pytest.raises(Exception):
        model_User.User(1234567891, "Vasiliy", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_name_long():
    with pytest.raises(Exception):
        model_User.User(123456, "Vasiliygrtdefrt", "parazit@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_email_long():
    with pytest.raises(Exception):
        model_User.User(123456, "Vasiliy",
                        "parazitxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@gmail.com",
                        1234, 5678, 9101112, 7889)


def test_passes_user_book_id_long():
    with pytest.raises(Exception):
        model_User.User(123456, "Vasiliy", "parazit@gmail.com",
                        1234567891, 5678, 9101112, 7889)
