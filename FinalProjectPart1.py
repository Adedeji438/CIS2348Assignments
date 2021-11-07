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


def generate_full_inventory_report(items):
    """
    Write all inventory to the file sorted by manufacturer
    """
    # Put all items as a list (from a dictionary)
    items_list = list()

    for item_id in items.keys():
        items_list.append(items[item_id])

    # Sort the items by manufacturer name, if equal then by type
    for i in range(len(items_list) - 1):
        for j in range(i, len(items_list)):
            if items_list[i].get_manufacturer() > items_list[j].get_manufacturer():
                items_list[i], items_list[j] = items_list[j], items_list[i]
            elif items_list[i].get_manufacturer() == items_list[j].get_manufacturer() and items_list[i].get_type() > \
                    items_list[j].get_type():
                items_list[i], items_list[j] = items_list[j], items_list[i]

    # Write the results to a file
    file = open("FullInventory.csv", "w")

    for item in items_list:
        file.write(str(item.get_id()) + ",")
        file.write(item.get_manufacturer() + ",")
        file.write(item.get_type() + ",")
        file.write(str(item.get_price()) + ",")
        file.write(datetime.strftime(item.get_service_date(), "%m/%d/%Y") + ",")

        if item.is_damaged():
            file.write("damaged")

        file.write("\n")

    file.close()


def generate_item_type_report(item_type, items):
    """
    Filter and generate a report for the specific item type only
    """
    # Get the items of the given type
    filtered_items = list()

    for item_id in items.keys():
        if items[item_id].get_type() == item_type:
            filtered_items.append(items[item_id])

    # Sort the items by ID
    for i in range(len(filtered_items) - 1):
        for j in range(i, len(filtered_items)):
            if filtered_items[i].get_id() > filtered_items[j].get_id():
                filtered_items[i], filtered_items[j] = filtered_items[j], filtered_items[i]

    # Write report to file
    file = open(item_type.capitalize() + "Inventory.csv", "w")

    for item in filtered_items:
        file.write(str(item.get_id()) + ",")
        file.write(item.get_manufacturer() + ",")
        file.write(item.get_type() + ",")
        file.write(str(item.get_price()) + ",")
        file.write(datetime.strftime(item.get_service_date(), "%m/%d/%Y") + ",")

        if item.is_damaged():
            file.write("damaged")

        file.write("\n")

    file.close()


def generate_item_types_report(items):
    """
    Generate a report for each item type
    """
    # Extract all unique item types
    item_types = list()

    for item_id in items.keys():
        if items[item_id].get_type() not in item_types:
            item_types.append(items[item_id].get_type())

    # Generate report for each item type
    for item_type in item_types:
        generate_item_type_report(item_type, items)


def generate_past_service_date_report(items):
    """
    Generate a report of items that is past the service date based on the current date
    """

    # Get the current date as string ignoring the time
    # then convert it to an actual date object
    current_date_str = date.today().strftime("%m/%d/%Y")
    current_date = datetime.strptime(current_date_str, "%m/%d/%Y")

    # For each item get those past service date
    filtered_items = list()

    for item_id in items.keys():
        if items[item_id].get_service_date() < current_date:
            filtered_items.append(items[item_id])

    # Sort by date
    for i in range(len(filtered_items) - 1):
        for j in range(i, len(filtered_items)):
            if filtered_items[i].get_service_date() > filtered_items[j].get_service_date():
                filtered_items[i], filtered_items[j] = filtered_items[j], filtered_items[i]

    # Write to file
    file = open("PastServiceDateInventory.csv", "w")

    for item in filtered_items:
        file.write(str(item.get_id()) + ",")
        file.write(item.get_manufacturer() + ",")
        file.write(item.get_type() + ",")
        file.write(str(item.get_price()) + ",")
        file.write(datetime.strftime(item.get_service_date(), "%m/%d/%Y") + ",")

        if item.is_damaged():
            file.write("damaged")

        file.write("\n")

    file.close()


def generate_damaged_inventory_report(items):
    """
    Generate all damaged items sorted by price
    """
    # Filter all damaged items
    filtered_items = list()

    for item_id in items.keys():
        if items[item_id].is_damaged():
            filtered_items.append(items[item_id])

    # Sort by price descending
    for i in range(len(filtered_items) - 1):
        for j in range(i, len(filtered_items)):
            if filtered_items[i].get_price() < filtered_items[j].get_price():
                filtered_items[i], filtered_items[j] = filtered_items[j], filtered_items[i]

    # Write to file
    file = open("DamagedInventory.csv", "w")

    for item in filtered_items:
        file.write(str(item.get_id()) + ",")
        file.write(item.get_manufacturer() + ",")
        file.write(item.get_type() + ",")
        file.write(str(item.get_price()) + ",")
        file.write(datetime.strftime(item.get_service_date(), "%m/%d/%Y"))
        file.write("\n")

    file.close()


def main():
    """
    Entry point of the program
    """
    # Initialize the items from file
    items = load_items()
    initialize_item_prices(items)
    initialize_item_service_dates(items)

    # Generate the reports
    generate_full_inventory_report(items)
    generate_item_types_report(items)
    generate_past_service_date_report(items)
    generate_damaged_inventory_report(items)


main()
