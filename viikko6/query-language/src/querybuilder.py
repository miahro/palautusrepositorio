from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.item.pop()

    def empty(self):
        return len(self.items)


class QueryBuilder:
    def __init__(self):
        self._stack = []

    def playsIn(self, team):
        self._stack.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._stack.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._stack.append(Not(HasFewerThan(value, attr)))
        return self

    def notPlaysIn(self, team):
        self._stack.append(Not(PlaysIn(team)))
        return self

    def notHasAtLeast(self, value, attr):
        self._stack.append(Not(HasAtLeast(value, attr)))
        return self

    def notHasFewerThan(self, value, attr):
        self._stack.append(Not(HasFewerThan(value, attr)))
        return self

    def build(self):
        if not self._stack:
            print("not self._stack")
            return All
        else:
            return And(*self._stack)
