def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone  
        return f"Phone number for {name} has been updated to {new_phone}."
    else:
        return f"Contact with name {name} not found."


def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return f"Contact with name {name} not found."


def get_all(contacts):
    if not contacts:
        return "Not one contacts added yet."
    all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return all_contacts
