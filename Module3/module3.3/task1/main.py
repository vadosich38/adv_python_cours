def get_social_status(age: int):
    if not isinstance(age, (int, float)):
        raise ValueError("Введите возраст числом!")

    if age < 0:
        raise ValueError("Возраст может быть только положительным!")
    elif 0 <= age < 13:
        return "ребенок"
    elif 13 <= age < 18:
        return "подросток"
    elif 18 <= age < 50:
        return "взрослый"
    elif 50 <= age < 65:
        return "пожилой"
    else:
        return "пенсионер"
