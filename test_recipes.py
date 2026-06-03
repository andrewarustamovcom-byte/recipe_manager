import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe


def test_ingredient_creation():
    ing = Ingredient("Гуанчале", 150, "г")
    assert ing.name == "Гуанчале"
    assert ing.quantity == 150.0
    assert ing.unit == "г"


def test_ingredient_str():
    ing = Ingredient("Пекорино Романо", 80, "г")
    assert str(ing) == "Пекорино Романо: 80.0 г"


def test_ingredient_eq():
    ing1 = Ingredient("Желток", 4, "шт")
    ing2 = Ingredient("Желток", 2, "шт")
    ing3 = Ingredient("Белок", 4, "шт")
    ing4 = Ingredient("Желток", 4, "г")

    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4


def test_ingredient_invalid_quantity():
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        Ingredient("Чёрный перец", 0, "г")