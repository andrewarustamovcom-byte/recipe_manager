class Ingredient:
    def __init__(self, name : str, quantity : float, unit : str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError ("Колчиество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient ({self.name}, {self.quantity}, {self.unit})"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return NotImplemented
        return (self.name == other.name) and (self.unit == other.unit)
    
class Recipe:
    def __init__(self, title : str, ingredients = None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []

    def add_ingredient(self, ingredient : Ingredient):
        for now_ingredient in self.ingredients:
            if now_ingredient == ingredient:
                now_ingredient.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(self, ratio):
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")

        scaled = [Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit) for ingredient in self.ingredients]
        return Recipe(self.title, scaled)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ings = [ing.name for ing in self.ingredients]
        return f"Блюдо:{self.title}. Ингредиенты: {', '.join(ings)}"
    
class ShoppingList:
    def __init__(self, ingredinet : Ingredient, recipe_title : str):
        def __init__(self):
            self._items = []

    def add_recipe(self, recipe: Recipe, portions : float):
        if portions <= 0:
            raise ValueError ("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ingredient in scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title : str):
        self._items = [it for it in self._items if it[1] != title]

    def get_list(self):
        total = {}
        for ingredient, recipe_title in self.items:
            k = (ingredient.name, ingredient.unit)
            if k in total:
                total[k] += ingredient.quantity
            else:
                total[k] = ingredient.quantity

        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in total.items()]
        return sorted(result, key=lambda ingredient: ingredient.name)

    def __add__(self, other):
        if not isinstance(other, ShoppingList):
            return NotImplemented
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list
    