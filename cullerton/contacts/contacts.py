stored_contacts = [
    {'name': 'stella',
     'realname': 'Stella McShwella',
     'company': 'Big Company',
     'phone': '3216540987',
     'email': 'mcshwella@bigcompany.com',
     'notes': 'something nice to say'},
    {'name': 'rigor', 'realname': 'Rigor Mortis', 'company': 'Resting Place', 'phone': '5467895243', 'email': 'rigor.mortis@restingplace.com', 'notes': 'Kind of quiet'},
    {'name': 'boop', 'realname': 'Betty Boop', 'company': 'Girls R Us', 'phone': '1812398537', 'email': 'bboop@girlsrus.com', 'notes': 'Rubber Bands'},
    {'name': 'captain', 'realname': 'Captain Picard', 'company': 'Starfleet', 'phone': '8765432190', 'email': 'captain.picard@starfleet.com', 'notes': 'Rubber Bands'},
    {'name': 'amazing', 'realname': 'Grace Hopper', 'company': 'Girls R Us', 'phone': '1812398537', 'email': 'ghopper@girlsrus.com', 'notes': 'Paper Clips'},
    {'name': 'godfather', 'realname': 'James Brown', 'company': 'Nunya Business', 'phone': '7834621389', 'email': 'jb@nunya.com', 'notes': 'Paper Clips'}]


def get_contacts():
    contacts = []
    for contact in stored_contacts:
        contacts.append(contact)
    return contacts


def get_contact(name):
    for contact in stored_contacts:
        if contact['name'] == name:
            return(contact)


def add_contact(name=None, realname='', company='', phone='', email='', notes=''):
    if name and not get_contact(name):
        stored_contacts.append(
            {'name': name,
             'realname': realname,
             'company': company,
             'phone': phone,
             'email': email,
             'notes': notes})


def edit_contact(name, realname=None, company=None, email=None, phone=None, notes=None):
    for contact in stored_contacts:
        if contact['name'] == name:
            if realname:
                contact['realname'] = realname
            if company:
                contact['company'] = company
            if email:
                contact['email'] = email
            if phone:
                contact['phone'] = phone
            if notes:
                contact['notes'] = notes


def delete_contact(name):
    for count, contact in enumerate(stored_contacts):
        if contact['name'] == name:
            del(stored_contacts[count])


def display_contacts():
    display_strings = []
    contacts = get_contacts()
    for contact in contacts:
        display_strings.append("%s, %s" % (contact['name'], contact['realname']))
    print("\n".join(display_strings) + "\n")


def display_contact(name):
    contact = get_contact(name)
    if contact:
        print("%s, %s\n%s\n%s\n%s" % (contact['realname'], contact['company'],
              contact['phone'], contact['email'], contact['notes']))
    else:
        print("No contact found")


def display_add_contact():
    name = realname = company = phone = email = notes = ''
    while not name and not get_contact(name):
        name = input(
            "Please enter a name for the new contact. It must be unique.: ")
    realname = input("Enter realname (or <return> if None): ")
    company = input("Enter company (or <return> if None): ")
    phone = input("Enter phone (or <return> if None): ")
    email = input("Enter email address (or <return> if None): ")
    notes = input("Enter notes (or <return> if None): ")
    add_contact(name, realname=realname, company=company,
                phone=phone, email=email, notes=notes)


def display_edit_contact():
    name = ''
    while not name:
        name = input("Please enter the name of a contact to edit: ")
    contact = get_contact(name)
    if not contact:
        return "No Contact Found"
    print(contact)
    realname = input("Enter realname (or <return> to keep): ")
    company = input("Enter company (or <return> to keep): ")
    phone = input("Enter phone (or <return> to keep): ")
    email = input("Enter email (or <return> to keep): ")
    notes = input("Enter notes (or <return> to keep): ")

    edit_contact(name, realname=realname, company=company, phone=phone,
                 email=email, notes=notes)


def display_delete_contact():
    name = ''
    while not name:
        name = input("Please enter the name of a contact to delete: ")
    confirm = input("Delete contact %s? [y/N]" % name)
    if confirm.lower() == 'y':
        delete_contact(name)


def contacts():
    """""Simple Contacts Application"""

    name = None
    while name != 'exit':
        if name == 'new':
            display_add_contact()
        elif name == 'edit':
            display_edit_contact()
        elif name == 'delete':
            display_delete_contact()
        elif name:
            display_contact(name)
        else:
            display_contacts()
        name = input("Enter contact name, 'new', 'edit', 'delete' or 'exit': ")


# if __name__ == '__main__':
#     contacts()

__all__ = ['get_contacts', 'get_contact', 'add_contact', 'edit_contact', 'delete_contact']
