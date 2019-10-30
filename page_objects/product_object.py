
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit



class Product_Object:
    "Page object for the Moisturizer and sunscreens"     
    #locators  
    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element
    cart_button = locators.click_cart  
    checkout_heading = locators.checkout_heading    
    product_category = []    
    product_moisturizers_category = []
    product_sunscreens_category = []
    

    def add_products(self,product_category):
        "Add products to the cart"       
        
        return result_flag

    def click_cart(self):
        "Click on the Cart button"

        return result_flag     

    def check_redirect_cart(self):
        "Check if we have been redirected to the redirect page"

        return result_flag 
