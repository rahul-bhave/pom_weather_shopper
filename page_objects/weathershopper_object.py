"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Weathershopper_Object:
    "Page object for the Form"
    
    #locators
    temp_field=locators.temp_field
    buy_moisturizers = locators.click_moisturizers
    buy_sunscreens = locators.click_sunscreens
    redirect_title_moisturizers= 'moisturizers'
    redirect_title_sunscreens='sunscreens'
    heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"
    heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"
     

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_temprature(self):
        # get temperature
        result_flag= self.get_element(self.temp_field).text
        result_flag=result_flag[:-2]

        return result_flag
        

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_sunscreens(self):
        "click the Buy sunscreens button"
        result_flag = self.click_element(self.buy_sunscreens)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy sunscreens" button',
            negative='Failed to click on "Buy sunscreens" button',
            level='debug')
        
        return result_flag



    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_moisturizers(self):
        "click the Buy moisturizers button"      
        result_flag = self.click_element(self.buy_moisturizers)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy moisturizers" button',
            negative='Failed to click on "Buy moisturizers" button',
            level='debug')
            
        return result_flag


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_moisturizers(self):
        result_flag = False
        heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"
        if self.check_element_present(heading_moisturizer) is not None:
           result_flag = True
           self.switch_page("moisturizers")
        return result_flag   
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_sunscreens(self):
        result_flag = False       
        heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"
        if self.check_element_present(heading_sunscreen) is not None:
            result_flag = True
            self.switch_page("sunscreens")
        
        
        return result_flag


    

