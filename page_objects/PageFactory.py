"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Moisturizer_Redirect_Page
2. Sunscreen_Redirect_Page
3. Weathershopper main page
4. cart redirect page
"""

from page_objects.weathershopper_main_page import Weathershopper_Main_Page
from page_objects.sunscreen_redirect_page  import Sunscreen_Redirect_Page
from page_objects.moisturizer_redirect_page import Moisturizer_Redirect_Page
from page_objects.cart_redirect_page import Cart_Redirect_Page



class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url='https://weathershopper.pythonanywhere.com',trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "main page":
            test_obj = Weathershopper_Main_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "moisturizers":
            test_obj = Moisturizer_Redirect_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "sunscreens":
            test_obj = Sunscreen_Redirect_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)  
        elif page_name == "cart":
            test_obj = Cart_Redirect_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        return test_obj

    get_page_object = staticmethod(get_page_object)