import pytest
from praktikum.database import Database
from unittest.mock import MagicMock
from praktikum.burger import Burger


@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = "Fluorescent bun R2-D3"
    bun_mock.get_price.return_value = 988.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = MagicMock()
    ingredient_mock.get_name.return_value = "Crispy Mineral Rings"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 300.0
    return ingredient_mock

@pytest.fixture
def sauce():
    sauce_mock = MagicMock()
    sauce_mock.get_name.return_value = "Spicy-X Sauce"
    sauce_mock.get_type.return_value = "SAUCE"
    sauce_mock.get_price.return_value = 90.0
    return sauce_mock