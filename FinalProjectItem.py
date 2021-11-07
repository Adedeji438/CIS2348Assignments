"""
Your name
Your student ID
"""


class Item:

    def __init__(self, id, manufacturer, type, damaged):
        """
        Create an item
        """
        self.__id = id
        self.__manufacturer = manufacturer
        self.__type = type
        self.__damaged = damaged
        self.__price = 0
        self.__service_date = None

    def set_price(self, price):
        """
        Initialize the price property
        """
        self.__price = price

    def set_service_date(self, service_date):
        """
        Initialize the service date property
        """
        self.__service_date = service_date

    def get_id(self):
        """
        Access to the ID property
        """
        return self.__id

    def get_manufacturer(self):
        """
        Access to the manufacturer property
        """
        return self.__manufacturer

    def get_type(self):
        """
        Access to the item type property
        """
        return self.__type

    def is_damaged(self):
        """
        Access to check if item is damaged
        """
        return self.__damaged

    def get_price(self):
        """
        Access to the price property
        """
        return self.__price

    def get_service_date(self):
        """
        Access to the service date property
        """
        return self.__service_date
