import pytest

from randstr_plus import randstr


@pytest.mark.parametrize(
    "min_length, max_length, min_tokens, max_tokens",
    [
        (4, 4, 2, 2),
        (5, 5, 3, 3),
        (19, 19, 10, 10),
        (20, 20, 10, 10),
        (10, 30, 3, 5),
        (70, 100, 3, 20),
        (2, 9, 2, 6),
    ],
)
def test_create_random_string_with_various_parameters(
    min_length, max_length, min_tokens, max_tokens
):
    string = randstr(
        lowercase_letters=True,
        uppercase_letters=True,
        numbers=True,
        min_length=min_length,
        max_length=max_length,
        min_tokens=min_tokens,
        max_tokens=max_tokens,
    )
    assert min_length <= len(string)
    assert max_length >= len(string)
    assert min_tokens <= len(string.split())
    assert max_tokens >= len(string.split())
    assert all([len(string.strip()) for string in string.split()])  # tokens have chars


def test_create_random_string_with_default_parameters():
    for _ in range(5):
        string = randstr()
        # check that tokens have chars
        assert all([len(string.strip()) for string in string.split()])
