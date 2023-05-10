import set_of_ordered_pairs as sp


def properties_of_relations():
    print("Enter a set of ordered pairs: ")
    set_a = sp.OrderedPairSet(sp.str_to_ordered_pairs(input("> ")))
    print(set_a)
    print(f"Reflexive: {set_a.is_reflexive()}")
    print(f"Symmetric: {set_a.is_symmetric()}")
    print(f"Transitive: {set_a.is_transitive()}")
    print(f"Antisymmetric: {set_a.is_antisymmetric()}")
    print(f"Equivalence: {set_a.is_equivalence()}")
    print(f"Partial Order: {set_a.is_partial_order()}")
    print()


def composition_of_relations():
    print("Enter a set of ordered pairs: ")
    set_a = sp.OrderedPairSet(sp.str_to_ordered_pairs(input("> ")))
    print("Enter another set of ordered pairs: ")
    set_b = sp.OrderedPairSet(sp.str_to_ordered_pairs(input("> ")))
    print(set_a.compose(set_b))
    print()


def powers_on_relation_op():
    print("Enter a set of ordered pairs: ")
    set_a = sp.OrderedPairSet(sp.str_to_ordered_pairs(input("> ")))
    print("Enter a number: ")
    num = int(input("> "))
    print(sp.powers_on_relation(set_a, num))
    print()
