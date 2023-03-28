contacts = {}


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Enter name and phone number separated by a space"
        except IndexError:
            return "Enter a contact name"
    return wrapper


@input_error
def add_contact(command):
    name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Contact {name} added"


@input_error
def change_contact(command):
    name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Phone number for {name} changed"


@input_error
def get_phone(command):
    name = command.lower()
    return f"Phone number for {name} is {contacts[name]}"


def show_all():
    if not contacts:
        return "No contacts found"
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    while True:
        command = input("Enter command: ")
        command = command.lower()
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(add_contact(command[4:].strip()))
        elif command.startswith("change"):
            print(change_contact(command[7:].strip()))
        elif command.startswith("phone"):
            print(get_phone(command[6:].strip()))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
