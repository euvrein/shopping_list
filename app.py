shopping_list = []


def welcome_banner():
    print("*" * 20)
    print("Basic Shopping List")
    print("*" * 20)


def add_to_list(item):
    shopping_list.append(item)
    print("Added {} to the list! List has {} items.".format(item,len(shopping_list)))


def show_list():
    if shopping_list != []:
        print("Here's your list:")
        for item in shopping_list:
            print(item)
    else:
        print("Shopping list is empty")


def delete_from_list():
    if shopping_list != []:
        shopping_list.pop()
    show_list()


def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list.
    Enter 'POP' to delete last item.
    """)


def main():
    while True:
        new_item = input("> ")

        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue  # This shoots you back to while True:
        elif new_item == 'SHOW':
            show_list()
            continue
        elif new_item == 'POP':
            delete_from_list()
            continue

        add_to_list(new_item)


welcome_banner()
show_help()
main()
show_list()