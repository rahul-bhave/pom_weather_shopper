
from .Base_Page import Base_Page
import conf.locators_conf as locators
from .payment_object import Payment_Object
from .product_object import Product_Object
from utils.Wrapit import Wrapit


class Moisturizer_Redirect_Page(Base_Page,Payment_Object,Product_Object):
    "Page Object for the redirect page"

    #locators
    heading = locators.heading_moisturizer

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'moisturizer'
        self.open(url)

    
