"""
This Moisturizer_Redirect_Page
"""
from .Base_Page import Base_Page
from .product_object import Product_Object
from utils.Wrapit import Wrapit


class Moisturizer_Redirect_Page(Base_Page,Product_Object):
    "Page Object for the redirect page"
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'moisturizer'
        self.open(url)