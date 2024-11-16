from src.utils import get_n_elements


def test_get_n_elements():
    assert get_n_elements(3) == "122"
    assert get_n_elements(0) == ""
