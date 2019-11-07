"""
This class models the form on the weather shopper application main page
"""

from page_objects.Base_Page import Base_Page
from page_objects.weathershopper_object import Weathershopper_Object
from utils.Wrapit import Wrapit


class Weathershopper_Main_Page(Base_Page,Weathershopper_Object):
    "Page Object for the weathershopper main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)