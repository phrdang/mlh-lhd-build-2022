# Build a Recipe tracker
# Find a way to keep track of recipes you’ve made,
# want to make, or even have created yourself!
import json


class RecipeTracker:
    def __init__(self, recipes=None) -> None:
        if recipes is None:
            self.recipes = {}  # key: name string, value: recipe string
        else:
            assert type(recipes) == dict
            self.recipes = recipes

    def add_recipe(self, name, recipe):
        if type(name) != str:
            raise ValueError('Recipe name must be a string')

        if type(recipe) != str:
            raise ValueError('Recipe must be a string')

        if name in self.recipes:
            raise ValueError('Recipe already exists in tracker')

        self.recipes[name] = recipe

    def remove_recipe(self, name):
        if name not in self.recipes:
            raise KeyError("Recipe doesn't exist in tracker, cannot be removed")
        else:
            self.recipes.pop(name)

    def edit_recipe(self, name, recipe):
        if name not in self.recipes:
            raise KeyError("Recipe doesn't exist in tracker, cannot be edited")
        else:
            self.recipes[name] = recipe

    def view_recipe(self, name) -> str:
        if name not in self.recipes:
            raise KeyError("Recipe doesn't exist in tracker, cannot be viewed")
        else:
            return self.recipes[name]

    def write_recipes(self, file_name):
        assert type(file_name) == str, 'File name must be a string'
        assert file_name[-5:] == ".json", 'Must be a .json file'

        with open(file_name, "x") as f:
            json.dump(self.recipes, f)

    def read_recipes(self, file_name):
        assert type(file_name) == str, 'File name must be a string'
        assert file_name[-5:] == ".json", 'Must be a .json file'

        with open(file_name, "r") as f:
            self.recipes = json.load(f)


if __name__ == "__main__":
    print("Welcome to Recipe Tracker!")

    tracker = RecipeTracker()

    # Ask user if they want to load recipes from a previous session
    choice = input("Would you like to load a recipes tracker? Y/N: ").strip().lower()
    if choice == 'y':
        file_name = input("Filename: ")
        tracker.read_recipes(file_name)
        print("Recipes loaded:")
        for recipe in tracker.recipes:
            print(recipe)
    else:
        print("No recipes loaded.")

    finished = False
    while not finished:
        choice = input("""
            What would you like to do?
                (1) Add a new recipe
                (2) Remove an existing recipe
                (3) Edit an existing recipe
                (4) View an existing recipe
                (5) Quit
            Enter 1, 2, 3, 4, or 5: """).strip()
        if choice == '1':
            name = input("Name of recipe to add: ")
            recipe = input("Recipe text: ")
            try:
                tracker.add_recipe(name, recipe)
            except ValueError as err:
                print(f"Error: {err}. Please try again.")
            else:
                print(f"Recipe for {name} added!")
        elif choice == '2':
            name = input("Name of recipe to remove: ")
            try:
                tracker.remove_recipe(name)
            except KeyError as err:
                print(f"Error: {err}. Please try again.")
            else:
                print(f"Recipe for {name} removed!")
        elif choice == '3':
            name = input("Name of recipe to edit: ")
            recipe = input("New recipe text: ")
            try:
                tracker.edit_recipe(name, recipe)
            except KeyError as err:
                print(f"Error: {err}. Please try again.")
            else:
                print(f"Recipe for {name} edited!")
        elif choice == '4':
            name = input("Name of recipe to view: ")
            try:
                text = tracker.view_recipe(name)
            except KeyError as err:
                print(f"Error: {err}. Please try again.")
            else:
                print(f"Recipe text: {text}")
        elif choice == '5':
            finished = True
        else:
            print("Hmm, I didn't understand your choice. Please try again.")

    # Ask user if they want to save tracker data
    choice = input("Would you like to save your recipes tracker to a file? Y/N: ").strip().lower()
    if choice == 'y':
        file_name = input("Filename: ")
        tracker.write_recipes(file_name)
        print(f"Recipes saved to {file_name}!")
    else:
        print("Recipes will not be saved.")

    print("Quitting Recipe Tracker... goodbye!")
