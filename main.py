import ui
# import set_of_ordered_pairs as sp
import operations as op


def main():
    functions = {
        "Properties of Relations": op.properties_of_relations,
        "Composition of Relations": op.composition_of_relations,
        "Powers on Relation": op.powers_on_relation_op,
        "Exit": exit
    }
    ui.menu(functions)
    main()


if __name__ == '__main__':
    main()
