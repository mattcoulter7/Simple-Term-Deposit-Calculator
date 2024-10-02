import pytest


@pytest.mark.parametrize(
    "input_1, input_2, expected_output",
    [
        ("some_string", 12345, None),
    ]
)
def test_template(
    input_1: str,
    input_2: float,
    expected_output: None,
):
    raise NotImplementedError()
