class OrderedPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

    def __hash__(self):
        return hash((self.first, self.second))

    def __repr__(self):
        return f"({self.first}, {self.second})"

    def __str__(self):
        return f"({self.first}, {self.second})"

    def __iter__(self):
        return iter([self.first, self.second])

    def __getitem__(self, index):
        return [self.first, self.second][index]

    def __len__(self):
        return 2

    def compose(self, other):
        return OrderedPair(self.first, other.second)


class OrderedPairSet:
    def __init__(self, iterable):
        self.set = set(iterable)

    def __repr__(self):
        return str(self.set)

    def __str__(self):
        return str(self.set)

    def __iter__(self):
        return iter(self.set)

    def __len__(self):
        return len(self.set)

    def __contains__(self, item):
        return item in self.set

    def add(self, item):
        self.set.add(item)

    def remove(self, item):
        self.set.remove(item)

    def is_reflexive(self):
        return all([OrderedPair(x, x) in self for x in {x.first for x in self}])

    def is_symmetric(self):
        return all([OrderedPair(x.second, x.first) in self for x in self])

    def is_antisymmetric(self):
        return all([x == y for x in self for y in self if can_composition(x, y) and can_composition(y, x)])

    def is_transitive(self):
        return all([OrderedPair(x.first, y.second) in self for x in self for y in self if can_composition(x, y)])

    def is_equivalence(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()

    def is_partial_order(self):
        return self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()

    def compose(self, other):
        return OrderedPairSet(
            {pair.compose(other_pair)
             for pair in self for other_pair
             in other if can_composition(pair, other_pair)})


def num_will_be_int(char: str) -> int or str:
    try:
        return int(char)
    except ValueError:
        return char


def proper_format(str_input: str) -> bool:
    return str_input.count("(") == str_input.count(")") and str_input.count("(") > 0 and str_input.count(")") > 0


def str_to_ordered_pairs(str_input: str) -> OrderedPairSet:
    try:
        assert proper_format(str_input)
        set_of_ordered_pairs = OrderedPairSet({})
        str_input = "!".join(str_input.split("),")).replace("(", "").replace(")", "").replace(" ", "").split("!")

        for pair in str_input:
            pair = pair.split(",")
            set_of_ordered_pairs.add(OrderedPair(num_will_be_int(pair[0]), num_will_be_int(pair[1])))

        return set_of_ordered_pairs
    except AssertionError:
        raise ValueError("Improper format")


def can_composition(element_of_set_a: OrderedPair, element_of_set_b: OrderedPair) -> bool:
    """(a, c)|(a, b) is an element of set A and (b, c) is an element of set B for some element of b"""
    if element_of_set_a[1] == element_of_set_b[0]:
        return True
    else:
        return False


def powers_on_relation(relation: OrderedPairSet, power: int) -> OrderedPairSet:
    if power == 0:
        return OrderedPairSet({OrderedPair(x, x) for x in range(1, 9)})
    elif power == 1:
        return relation
    else:
        return powers_on_relation(relation.compose(relation), power - 1)


if __name__ == '__main__':
    print(str_to_ordered_pairs("(1, 2), (3, 4), (5, 6), (7, 8)"))
    print(powers_on_relation(str_to_ordered_pairs("(1, 1), (2, 1), (3, 2), (4, 3)"), 2))
    print(powers_on_relation(str_to_ordered_pairs("(1, 1), (2, 1), (3, 2), (4, 3)"), 3))
