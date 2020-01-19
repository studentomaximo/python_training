# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Maximum", middle_name="ab", last_name="Kane", nick="Strabo", title="SQA",
        company="Faceboof", address="234 Hacker Dr", home_phone="321", mobile_phone="312",
        work_phone="999", fax="006", email="e1@gmai.com", email2="e2@gmail.com", email3="e3@gmail.com",
        home_page="NA", address2="12345 Wed Dr", notes="NA"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nick="", title="",
        company="", address="", home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="",
        home_page="", address2="", notes=""))
    app.logout()