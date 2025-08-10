import pytest

from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self, burger, ingredient, sauce):
        burger.add_ingredient(ingredient)
        burger.add_ingredient(sauce)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [sauce, ingredient]

    @pytest.mark.parametrize("ingredient_count,expected_price", [
        (0, 1976.0),  # только булки
        (1, 2276.0),  # булки + 1 ингредиент
        (2, 2576.0),  # булки + 2 ингредиента
    ])
    def test_get_price(self, burger, bun, ingredient, ingredient_count, expected_price):
        burger.set_buns(bun)
        for _ in range(ingredient_count):
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price


    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n' \
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n' \
                           f'(==== {bun.get_name()} ====)\n' \
                           '\n' \
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt


    def test_get_receipt_with_only_bun(self, burger, bun):
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        expected_receipt = f'(==== {bun.get_name()} ====)\n' \
                           f'(==== {bun.get_name()} ====)\n' \
                           '\n' \
                           f'Price: {burger.get_price()}'

        assert receipt == expected_receipt

