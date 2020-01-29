from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="Test"))
    app.contact.modify_first_contact(Contact(first_name="New Firstname"))


def test_modify_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="Test"))
    app.contact.modify_first_contact(Contact(last_name="New Lastname"))
