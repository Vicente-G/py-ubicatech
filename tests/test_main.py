from flask import Flask


def test_app_is_created(test_app):
    assert isinstance(test_app, Flask), "app should be a Flask instance"


def test_blueprints_registered(test_app):
    assert "cpu" in test_app.blueprints, "cpu blueprint should be registered"
