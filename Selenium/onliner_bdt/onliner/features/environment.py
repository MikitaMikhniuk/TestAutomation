from framework.utils.driver_factory import DriverFactory
from framework.utils.browser import Browser

def before_all(context):
    context.driver_instance = DriverFactory()
    context.driver = context.driver_instance.set_up()
    context.browser = Browser(context.driver)
    
    
def after_all(context):
    Browser.tear_down(context.driver)