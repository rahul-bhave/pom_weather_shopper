from .Base_Page import Base_Page
import conf.locators_conf as locators
from .payment_object import Payment_Object
from .product_object import Product_Object
from utils.Wrapit import Wrapit


class Cart_Redirect_Page(Base_Page,Payment_Object,Product_Object):