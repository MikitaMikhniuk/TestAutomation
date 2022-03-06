import time

def highlight(element):
    """
    Highlights a given element.

    Input -> Selenium element
    """

  
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)
    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style")!=None):
        time.sleep(1)
    apply_style(orignal_style)