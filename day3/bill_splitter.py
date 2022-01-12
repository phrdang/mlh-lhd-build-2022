def calculate_split_cost(num_people, total_cost):
    """
    Calculates the cost for each person assuming the bill is split evenly.
    >>> calculate_split_cost(5, 20)
    4.0
    >>> calculate_split_cost(6, 25)
    4.17
    >>> calculate_split_cost(4, 25)
    6.25
    """
    return round((total_cost / num_people) + 0.005, 2)  # round up at 2nd decimal


if __name__ == "__main__":
    print("Welcome to Bill Splitter!")
    num_people = int(input("How many people are in your party? "))
    total_cost = float(input("What is the total cost of your bill? "))
    split_cost = calculate_split_cost(num_people, total_cost)
    print(f"The cost split evenly among {num_people} people is ${split_cost:.2f}.")
