from main import isbn13
import pytest


@pytest.mark.parametrize(
    "isbn, expected",
    [
        ("9780316066525", "Valid"),
        ("0330301824", "Invalid"),
        ("0316066524", "9780316066525"),
        ("9780140449112", "Valid"),
        ("9780306406157", "Valid"),
        ("1234567890", "Invalid"),
        ("9780316066521", "Invalid"),
        ("031606652X", "Invalid"),
        ("877195869X", "9788771958690"),
    ],
)
def test_isbn13(isbn, expected):
    assert isbn13(isbn) == expected




