def menu(items: dict, title: str = "Menu"):
    """
    Displays a menu and returns the user's choice.
    """
    print(f"--- {title} ---")
    [print(f"{key[0] + 1}. {key[1]}") for key in enumerate(items)]
    print()

    selected_item = choosing(items)
    print()
    print(f"--- {selected_item[0]} ---")
    selected_item[1]()


def choosing(items: dict) -> tuple or callable:
    """
    Prompts the user for a choice and returns the corresponding value.
    """
    try:
        print("Select an option:")
        choice = int(input("> "))
        assert choice in range(1, len(items) + 1)
        return list(items.keys())[choice - 1], list(items.values())[choice - 1]
    except (ValueError, AssertionError):
        print("Invalid choice.")
        return choosing(items)
