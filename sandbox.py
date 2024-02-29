import pyautogui
import time
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget
import qtawesome as qta

# Function to find the position of the QTA icon on the screen
def find_qta_icon(icon_name, color):
    screenshot = pyautogui.screenshot()

    # Convert the QTA icon to a QPixmap for comparison
    qta_icon = qta.icon(icon_name, color=color)
    qta_pixmap = qta_icon.pixmap(QSize(16, 16))

    # Try to locate the QTA icon on the screen
    position = pyautogui.locateOnScreen(qta_pixmap)
    return position

# Function to click on the QTA icon
def click_qta_icon(position):
    x, y = pyautogui.center(position)
    pyautogui.click(x, y)

def display_qta_icon(icon_name, color):
    app = QApplication([])

    # Get the screen geometry to calculate the center position
    screen_geometry = QDesktopWidget().screenGeometry()

    qta_icon = qta.icon(icon_name, color=color)
    label = QLabel()
    label.setPixmap(qta_icon.pixmap(QSize(50, 50)))

    # Calculate the center position
    center_x = (screen_geometry.width() - label.width()) // 2
    center_y = (screen_geometry.height() - label.height()) // 2

    label.setGeometry(center_x, center_y, 50, 50)
    label.show()

    app.exec_()

# Example usage
#display_qta_icon('mdi6.duck', color='yellow')

# Function to find and click the QTA icon
def find_and_click_qta_icon(icon_name, color):
    screenshot = pyautogui.screenshot()

    # Convert the QTA icon to a QPixmap for comparison
    qta_icon = qta.icon(icon_name, color=color)
    qta_pixmap = qta_icon.pixmap(QSize(50, 50))

    # Try to locate the QTA icon on the screen
    position = pyautogui.locateOnScreen(qta_pixmap)

    if position:
        # QTA icon found, click on it
        x, y = pyautogui.center(position)
        pyautogui.click(x, y)
        return True
    else:
        print("QTA icon not found.")
        return False

# Main loop
while True:
    # Find and click the QTA icon every 5 seconds
    if find_and_click_qta_icon('mdi6.duck', color='yellow'):
        time.sleep(5)  # Wait for 5 seconds after clicking the QTA icon
    else:
        time.sleep(5)  # If QTA icon is not found, wait for 5 seconds before checking again