"""
This class models the redirect page of the cart page
URL: cart
The page consists of Item and price details
"""
from .Base_Page import Base_Page
from .product_object import Product_Object
from utils.Wrapit import Wrapit


class Cart_Redirect_Page(Base_Page,Product_Object):
    "Page object for cart redirect"
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'cart'
        self.open(url)
