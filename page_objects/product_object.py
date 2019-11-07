"""
This is is product category selection page also includes clicking on the cart
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re


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
        result_flag = False
                  
        for num in range(1,2):

            for product in product_category:
                price_product = 100000          
                product_elements = self.get_elements(self.product_price_element%product) 
                #print(product_elements)

                for element in product_elements:                           
                    product_price = element.text                                   
                    product_price = re.findall(r'\b\d+\b', product_price)
                    #print(product_price)

                    if int(product_price[0]) < price_product:                   
                        price_product = int(product_price[0])
                        #print(price_product)

                        result_flag= self.click_element(self.product_add_element%(product,price_product))
                        self.conditional_write(result_flag,
                                positive='Successfully added products',
                                negative='Failed to add products',
                                level='debug')

                    num =+ num
                # print(num)      
        
        return result_flag


    def click_cart(self):
        "Click on the Cart button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "cart" button',
            negative='Failed to click on "cart" button',
            level='debug')

        return result_flag     


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_cart(self):
        "Checking redirecting on cart"
        result_flag = False       
        heading_cart = "xpath,//h2[contains(text(),'Checkout')]"
        if self.check_element_present(heading_cart) is not None:
            result_flag = True
            self.conditional_write(result_flag,
               positive='You are on cart page',
               negative='Failed to go on cart page',
               level='debug')
            self.switch_page("cart")

        return result_flag