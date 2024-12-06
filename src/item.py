class Item:
    short_description: str
    price: str

    def __init__(self, short_description: str, price: str):
        """
        Initialize an Item with description and price.
        
        Args:
            short_description (str): The item's description
            price (str): The item's price in format "XX.XX"
        """
        self.short_description = short_description
        self.price = price
