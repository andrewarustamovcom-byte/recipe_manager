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
    