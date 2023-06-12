import csv


def read_csv_file(file_path):
    """
    Imports shares data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: Shares data as a list of tuples (action, cost, profit).
    """
    shares_list = []

    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            action = row[0].strip()
            cost = float(row[1])
            profit = float(row[2])
            shares_list.append((action, cost, profit))
    return shares_list
