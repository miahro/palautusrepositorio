from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, stack=All()):
        self._stack = stack

    def playsIn(self, team):
        return QueryBuilder(And(self._stack, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._stack, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._stack, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self._stack
