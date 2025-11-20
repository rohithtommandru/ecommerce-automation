import os
import datetime

def take_screenshot(driver, name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(folder, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path
