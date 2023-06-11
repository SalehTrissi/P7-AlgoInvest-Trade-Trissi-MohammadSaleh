import csv
from itertools import combinations
import time


def read_csv_file(file_path):
    """
    Imports shares data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: Shares data as a list of tuples (action, cost, profit).
    """
    shares_list = []

    # Open the CSV file
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)

        # Read each row in the CSV file
        for row in reader:
            # Extract the values from each row and convert them to the appropriate data type

            # Remove leading/trailing spaces from the action name
            action = row[0].strip()
            cost = float(row[1])
            profit = float(row[2])

            # Append the values as a tuple to the shares list
            shares_list.append((action, cost, profit))

    return shares_list


def calculate_total_cost(combination):
    """
    Calculates the total cost of a combination of shares.

    Args:
        combination (tuple): A combination of shares as a tuple (action, cost, profit).

    Returns:
        float: Total cost of the combination.
    """
    return sum(action[1] for action in combination)


def calculate_total_profit(combination):
    """
    Calculates the total profit of a combination of shares.

    Args:
        combination (tuple): A combination of shares as a tuple (action, cost, profit).

    Returns:
        float: Total profit of the combination.
    """
    return sum(action[1] * action[2] / 100 for action in combination)


def maximize_profit(shares_list, max_budget):
    """
    Maximizes the profit for a given list of shares and maximum budget.

    Args:
        shares_list (list): List of shares as tuples (action, cost, profit).
        max_budget (float): Maximum budget for the investment.

    Returns:
        tuple: Best investment options as a tuple (combination, profit).
    """
    max_profit = 0
    best_investment = ()

    # Generate combinations of shares
    for i in range(len(shares_list)):
        for combination in combinations(shares_list, i):
            total_cost = calculate_total_cost(combination)
            if total_cost <= max_budget:
                total_profit = calculate_total_profit(combination)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_investment = combination
    return best_investment, max_profit
