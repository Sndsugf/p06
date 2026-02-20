def validate_ingredients(ingredients: str) -> str:
    if set(ingredients.split()).issubset({"fire", "water", "earth", "air"}):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
