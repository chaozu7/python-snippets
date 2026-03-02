fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

fruit_name = input("Item: ")
fruit_name = fruit_name.title()
calories = 0

match fruit_name:
    case "Apple":
        print("Calories: 130")
    case "Avocado" | "Cantaloupe" | "Honeydew Melon" | "Pineapple" | "Strawberries" | "Tangerine":
        print("Calories: 50")
    case "Banana":
        print("Calories: 110")
    case "Grapefruit" | "Nectarine" | "Peach":
        print("Calories: 60")
    case "Grapes" | "Kiwifruit":
        print("Calories: 90")
    case "Lemon":
        print("Calories: 15")
    case "Lime":
        print("Calories: 20")
    case "Orange" | "Watermelon":
        print("Calories: 80")
    case "Pear" | "Sweet Cherries":
        print("Calories: 100")
    case "Plums":
        print("Calories: 70")
   

