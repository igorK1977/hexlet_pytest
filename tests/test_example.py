from hexlet_pytest.example import reverse
from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""


def test_reverse_for_long_string():
    src_string = read_file("src_string.txt")
    expected = read_file("res_string.txt")
    actual = reverse(src_string)

    assert actual == expected