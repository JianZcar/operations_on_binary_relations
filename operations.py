import set_of_ordered_pairs as sp
import ui


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
    if ui.y_n_question("Would you like to see the proof of these properties? (y/n) "):
        print("-Reflexive-")
        for x, y in zip(set_a.proof_of_reflexive()[0], set_a.proof_of_reflexive()[1]):
            print(f"{x} -> {y}")
        print("-Symmetric-")
        for x, y in zip(set_a.proof_of_symmetric()[0], set_a.proof_of_symmetric()[1]):
            print(f"{x} -> {y}")
        print("-Antisymmetric-")
        for x, y in zip(set_a.proof_of_antisymmetric()[0], set_a.proof_of_antisymmetric()[1]):
            print(f"{x} -> {y}")
        print("-Transitive-")
        for x, y, z in zip(set_a.proof_of_transitive()[0], set_a.proof_of_transitive()[1],
                           set_a.proof_of_transitive()[2]):
            print(f"{x} -> {y} -> {z}")
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
