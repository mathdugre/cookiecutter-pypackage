import pytest

from {{cookiecutter.project_slug}} import placeholder_function


def test_placeholder_function():
    result = placeholder_function()
    if result is not True:
        pytest.fail("placeholder_function() did not return True.")
