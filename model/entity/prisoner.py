class Prisoner:
    def __init__(self, name, age, article, term):
        self._name = name
        self._age = age
        self._term = term
        self._article = article

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term):
        if term > 0:
            self._term = term
        else:
            if not hasattr(self, "_term"):
                self._term = 0
            else:
                raise ValueError("Term was wrong")

    @term.deleter
    def term(self):
        del self._term


    @property
    def article(self):
        return self._article

    @article.setter
    def article(self, article):
        self._article = article

    @article.deleter
    def article(self):
        del self._article


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 18:
            self._age = age


    def __str__(self):
        return (f"{self._name}, age: {self._age}, "
                f"article: {self._article}, term = {self._term}")
