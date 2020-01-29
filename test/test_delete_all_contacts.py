from model.contact import Contact


def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="Test"))
    app.contact.delete_all_contacts()