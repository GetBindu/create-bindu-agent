from {{cookiecutter.project_slug}}.main import handler


def test_handler():
    assert handler("foo") == "foo"
