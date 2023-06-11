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
 