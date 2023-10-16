import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "** Please Drink Water Now**",
            message = "Water is essential for the kidneys and other bodily functions. When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling. Drinking water instead of soda can help with weight loss.",
            app_icon = "C:/Users/dhana/OneDrive - Riga Technical University/C/Python Practice/icon.ico",
            timeout = 10
        )
        time.sleep(60*60)