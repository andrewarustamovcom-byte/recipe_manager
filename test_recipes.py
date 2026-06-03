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




def test_recipe_creation():
    ingredients = [Ingredient("Спагетти", 300, "г"), Ingredient("Гуанчале", 150, "г")]
    recipe = Recipe("Карбонара", ingredients)

    assert recipe.title == "Карбонара"
    assert recipe.ingredients == ingredients


def test_recipe_add_ingredient_new():
    recipe = Recipe("Карбонара")
    recipe.add_ingredient(Ingredient("Пекорино Романо", 80, "г"))

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "Пекорино Романо"


def test_recipe_add_ingredient_merge():
    recipe = Recipe("Карбонара")
    recipe.add_ingredient(Ingredient("Желток", 4, "шт"))
    recipe.add_ingredient(Ingredient("Желток", 2, "шт"))

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 6.0


def test_recipe_scale():
    recipe = Recipe("Том-ям", [Ingredient("Кокосовое молоко", 400, "мл"), Ingredient("Креветки", 300, "г")])

    scaled = recipe.scale(2)

    assert isinstance(scaled, Recipe)
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity == 800.0
    assert scaled.ingredients[1].quantity == 600.0

    assert recipe.ingredients[0].quantity == 400.0
    assert recipe.ingredients[1].quantity == 300.0