from math import ceil
import uuid
from item import Item

class Receipt:
    id: str
    retailer: str
    purchase_date: str
    purchase_time: str
    items: list[Item]
    total: str

    def __init__(self, retailer: str, purchase_date: str, purchase_time: str, items: list[Item], total: str):
        """
        Initialize a Receipt object with the required fields from the API specification.
        
        Args:
            id (str): Unique identifier for the receipt
            retailer (str): Store name
            purchase_date (str): Date in YYYY-MM-DD format
            purchase_time (str): Time in 24-hour format (HH:MM)
            items (list): List of Item objects, minimum 1 item
            total (str): Total amount in format "XX.XX"
        """
        
        self.id = str(uuid.uuid4())
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        
    def get_receipt_id(self) -> str:
        return self.id
    
    def calculate_points(self) -> int:
        alphanumeric = sum(c.isalnum() for c in self.retailer)
        
        rounding = 0
        if self.total.endswith('.00'):
            rounding = 50
        
        quarter_multiple = 0
        if float(self.total) % 0.25 == 0:
            quarter_multiple = 25
        
        pairs = (len(self.items) // 2) * 5
        
        multiples_of_three = 0
        for item in self.items:
            desc_length = len(item.short_description.strip())
            if desc_length % 3 == 0:
                multiples_of_three += ceil(float(item.price) * 0.2)
        
        odd_day = 0
        if int(self.purchase_date.split('-')[2]) % 2 == 1:
            odd_day = 6
        
        time_check = 0
        if 14 <= int(self.purchase_time.split(':')[0]) < 16:
            time_check = 10
        
        points = alphanumeric + rounding + quarter_multiple + pairs + multiples_of_three + odd_day + time_check
        
        return points
