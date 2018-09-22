import re


class User:

    def __init__(self, user_id,
                 name, email='otsut@stvuet.net', *used_books_id):

        # Check input in initialization. For execute:
        # "user(7777, Ivan, Parazitxxx@mail.ru)".
        # Because across @property it don`t work.

        self._usedBooks_id = []

        # ID.
        if not isinstance(user_id, str) and user_id != "" and \
                3 < len(str(abs(user_id))) < 100:
            self._id = user_id
        else:
            raise Exception("!Delivered empty ID or bad ID")

        # name
        if not isinstance(name, int) and name != "" and \
                3 < len(str(name)) < 15 and not name.isdigit():
            self._name = name
        else:
            raise Exception("!Delivered empty name or not expected quantity \
                            symbols in name or they is digit")

        # EMAIL
        # Mask for email
        reg = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        email = email.lower()
        if email != "" and 3 < len(str(email)) < 64 and\
                re.fullmatch(reg, email):
            self._email = email
        else:
            raise Exception("!Delivered empty  Email or bad Email address")

        # usedBooks_id
        for num in used_books_id:
            if not isinstance(num, str) and num != "" and \
                    3 < len(str(abs(num))) < 10:
                self._usedBooks_id.append(num)
            else:
                raise Exception("!Delivered empty usedBookID or not\
                                expected quantity symbols in usedBookID")

    # Check input. For execute "a.user_id", "a.name".
    # ID
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, str) and value != "" and \
                3 < len(str(abs(value))) < 10:
            self._id = value
        else:
            raise Exception("Delivered empty ID or bad ID")

    # usedBook_ID
    @property
    def used_books_id(self):
        return self._usedBooks_id

    @used_books_id.setter
    def used_books_id(self, value):
        for num in value:
            if not isinstance(value, str) and value != "" and\
                    3 < len(str(abs(value))) < 10:
                self._usedBooks_id.append(num)
            else:
                raise Exception("Delivered empty usedBookID or not\
                                expected quantity symbols in usedBookID")

    # NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, int) and value != "" and \
                3 < len(str(value)) < 15 and not value.isdigit():
            self._name = value
        else:
            raise Exception("Delivered empty name or not expected\
                            quantity symbols in name or they is digit")

    # EMAIL
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        reg = '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
        if value != "" and 3 < len(str(value)) < 64 and\
                re.fullmatch(reg, value):
            self._email = value
        else:
            raise Exception("Передано пустое значение Email \
                            или не соответствует адресу")

    def get_status(self):
        return 'id:', self._id, 'name: ', self._name, 'email :', self.email
