import pytest

from python_uv.calc import add


@pytest.mark.unit_test
@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-1, -1, -2),
    ],
)
def test_add_correct(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


@pytest.mark.unit_test
@pytest.mark.parametrize(
    ("a", "b"),
    [
        (1, "2"),
        ("1", 2),
        ("1", "2"),
        (1, 2.1),
        (1.1, 2),
        (1.1, 2.1),
    ],
)
def test_add_incorrect(a: int, b: int) -> None:
    with pytest.raises(TypeError):
        add(a, b)
