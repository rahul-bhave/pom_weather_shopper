"""
This class models the redirect page of the cart page
URL: cart
The page consists of Item and price details
"""
from .Base_Page import Base_Page
from .payment_object import Payment_Object
from .product_object import Product_Object
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Cart_Redirect_Page(Base_Page,Payment_Object,Product_Object):
    

    #locators
    checkout_heading = locators.checkout_heading

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'cart'
        self.open(url)

    
