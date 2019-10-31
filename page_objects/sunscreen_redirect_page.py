
from .Base_Page import Base_Page
from .payment_object import Payment_Object
from .product_object import Product_Object
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Sunscreen_Redirect_Page(Base_Page,Payment_Object,Product_Object):
    "Page Object for the redirect page"

    #locators
    heading = locators.heading_sunscreen

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'sunscreen'
        self.open(url)

    
