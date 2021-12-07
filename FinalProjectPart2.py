"""
Your name
Your student ID
"""

from FinalProjectItem import *
from datetime import *


def load_items():
    """
    Load the items the manufacturer's CSV file
    """
    items = dict()
    file = open("ManufacturerList.csv", "r")

    for line in file:
        # For each line parse and extract item data
        tokens = line.strip().split(",")
        id = int(tokens[0])
        manufacturer = tokens[1]
        type = tokens[2]
        status = tokens[3]

        # Create an object to encapsulate the data and put it into
        # a dictionary using the ID as the key
        item = Item(id, manufacturer, type, status == "damaged")
        items[id] = item

    file.close()
    return items


def initialize_item_prices(items):
    """
    Load the price of each item from the prices list CSV file
    """
    file = open("PriceList.csv", "r")

    for line in file:
        # For each line extract the price
        tokens = line.strip().split(",")
        item_id = int(tokens[0])
        price = int(tokens[1])

        # Put the price on the appropriate item
        if item_id in items.keys():
            items[item_id].set_price(price)

    file.close()


def initialize_item_service_dates(items):
    """
    Load the service dates of each item from the services dates list CSV file
    """
    file = open("ServiceDatesList.csv", "r")

    for line in file:
        # For each line extract the service date
        tokens = line.strip().split(",")
        item_id = int(tokens[0])
        service_date = datetime.strptime(tokens[1], "%m/%d/%Y")

        # Put the service date on the appropriate item
        if item_id in items.keys():
            items[item_id].set_service_date(service_date)

    file.close()


def search_items_by_manufacturer_and_type(items, manufacturer, item_type):
    """
    Return a list of items targeted on the given manufacturer and item type
    and only retrieves those that aren't damaged and have exceeded the service date
    """
    filtered_items = list()

    # Convert the search keywords to lowercase to make case insensitive comparison
    manufacturer = manufacturer.lower()
    item_type = item_type.lower()

    # Initialize the current date to filter out only those that have not exceeded the service date
    current_date_str = date.today().strftime("%m/%d/%Y")
    current_date = datetime.strptime(current_date_str, "%m/%d/%Y")

    for item_id in items.keys():
        item = items[item_id]

        # Filter by manufacturer
        if item.get_manufacturer().strip().lower() in manufacturer:
            # Filter by item type
            if item.get_type().strip().lower() in item_type:
                # Filter damage status
                if not item.is_damaged():
                    # Filter service date
                    if item.get_service_date() > current_date:
                        filtered_items.append(item)

    # Sort the filtered items by price descending
    for i in range(len(filtered_items) - 1):
        for j in range(i, len(filtered_items)):
            if filtered_items[i].get_price() < filtered_items[j].get_price():
                filtered_items[i], filtered_items[j] = filtered_items[j], filtered_items[i]

    return filtered_items


def search_items_by_type(items, item_type, exclude_manufacturer):
    """
    Return a list of items targeted on an item type
    """
    filtered_items = list()
    item_type = item_type.lower()
    exclude_manufacturer = exclude_manufacturer.strip().lower()

    # Initialize the current date to filter out only those that have not exceeded the service date
    current_date_str = date.today().strftime("%m/%d/%Y")
    current_date = datetime.strptime(current_date_str, "%m/%d/%Y")

    for item_id in items.keys():
        item = items[item_id]

        # Filter by item type
        if item.get_manufacturer().strip().lower() not in exclude_manufacturer:
            if item.get_type().strip().lower() in item_type:
                # Filter damage status
                if not item.is_damaged():
                    # Filter service date
                    if item.get_service_date() > current_date:
                        filtered_items.append(item)

    return filtered_items


def main():
    """
    Entry point of the program
    """

    # Initialize the items from a CSV file
    items = load_items()
    initialize_item_prices(items)
    initialize_item_service_dates(items)

    # Perform a query until user decides to quit
    while True:
        manufacturer = input("Enter a manufacturer (enter 'q' to quit): ").strip()

        if manufacturer.lower() == "q":
            break

        item_type = input("Enter item type: ").strip()
        filtered_items = search_items_by_manufacturer_and_type(items, manufacturer, item_type)

        # Display search results
        if len(filtered_items) == 0:
            print("No such item in inventory")
        else:
            item = filtered_items[0]
            print("Your item is:\n\t" + str(item.get_id()) + ", " + item.get_manufacturer().strip() + ", " + item.get_type() + ", " + str(item.get_price()))

            related_items = search_items_by_type(items, item_type, manufacturer)

            if len(related_items) > 0:
                print("You may, also consider:")

                for item in related_items:
                    print("\t" + str(item.get_id()) + ", " + item.get_manufacturer().strip() + ", " + item.get_type() + ", " + str(item.get_price()))

        print()


main()
