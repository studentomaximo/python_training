


def test_change_group_info(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group_name()
    app.session.logout()