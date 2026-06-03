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

def test_recipe_scale_invalid_ratio():
    recipe = Recipe("Тирамису", [Ingredient("Маскарпоне", 250, "г")])
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-2)

def test_recipe_len():
    recipe = Recipe("Рамен")
    recipe.add_ingredient(Ingredient("Мисо", 40, "г"))
    recipe.add_ingredient(Ingredient("Лапша", 200, "г"))
    recipe.add_ingredient(Ingredient("Мисо", 10, "г"))

    assert len(recipe) == 2



def test_shopping_list_add_recipe():
    recipe = Recipe("Карбонара", [Ingredient("Спагетти", 300, "г"), Ingredient("Гуанчале", 150, "г")])
    shopping = ShoppingList()
    shopping.add_recipe(recipe, 2)
    items = shopping.get_list()
    names = [item.name for item in items]
    assert "Спагетти" in names
    assert "Гуанчале" in names


def test_shopping_list_add_recipe_invalid_portions():
    recipe = Recipe("Карбонара", [Ingredient("Спагетти", 300, "г")])
    shopping = ShoppingList()
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        shopping.add_recipe(recipe, 0)


def test_shopping_list_remove_recipe():
    carbonara = Recipe("Карбонара", [Ingredient("Спагетти", 300, "г")])
    tiramisu = Recipe("Тирамису", [Ingredient("Сливки", 200, "г")])
    shopping = ShoppingList()
    shopping.add_recipe(carbonara, 1)
    shopping.add_recipe(tiramisu, 1)
    shopping.remove_recipe("Карбонара")
    items = shopping.get_list()

    assert len(items) == 1
    assert items[0].name == "Сливки"


def test_shopping_list_get_list_sums_same_ingredients():
    carbonara = Recipe("Карбонара", [Ingredient("Пекорино Романо", 80, "г"), Ingredient("Чёрный перец", 5, "г")])
    cacio_e_pepe = Recipe("Качо э пепе", [Ingredient("Пекорино Романо", 50, "г"), Ingredient("Чёрный перец", 3, "г")])
    shopping = ShoppingList()
    shopping.add_recipe(carbonara, 1)
    shopping.add_recipe(cacio_e_pepe, 1)
    items = shopping.get_list()

    assert [item.name for item in items] == ["Пекорино Романо", "Чёрный перец"]
    assert items[0].quantity == 130.0
    assert items[1].quantity == 8.0


def test_shopping_list_add_operator():
    carbonara = Recipe("Карбонара", [Ingredient("Гуанчале", 150, "г")])
    ramen = Recipe("Рамен", [Ingredient("Нори", 2, "шт")])
    shopping1 = ShoppingList()
    shopping1.add_recipe(carbonara, 1)
    shopping2 = ShoppingList()
    shopping2.add_recipe(ramen, 1)
    combo = shopping1 + shopping2

    assert len(shopping1.get_list()) == 1
    assert len(shopping2.get_list()) == 1
    assert len(combo.get_list()) == 2
