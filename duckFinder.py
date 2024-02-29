import pyautogui
import time

duckCollection=0

# Function to find and click the PNG image in a specific region
def find_and_click_png_in_region(image_path, region):
    global duckCollection
    try:
        # Try to locate the PNG image on the specified region
        position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.8, grayscale=True)

        if position:
            # Save old Mouse Position
            prev_mouseLocation = pyautogui.position()
            
            
            # PNG image found, click on it
            x, y = pyautogui.center(position)
            pyautogui.click(x, y)
            #myTime = time.localtime()
            print(f'DETECTED DUCK - ITS HUNTING TIME [{x}, {y}]')
            duckCollection+=1
            print(f'Current # of Ducks added to my collection {duckCollection}')
            
            # Lets return mouse back to prev_location
            pyautogui.moveTo(prev_mouseLocation)
            
            return True
        else:
            print("PNG image not found in the specified region.")
            return False

    except pyautogui.ImageNotFoundException:
        print(f"DUCK not found... He will be here eventually...")
        return False

def main():
    # Define the region for a 1080p monitor on display 1 (adjust coordinates as needed)
    monitor_width = 1920
    monitor_height = 1040   #Typically 1080, -40 for the task bar
    region = (0, 30, monitor_width, monitor_height) # Starting point X [Starting from left right], Starting point Y [Starting from top down], Width, Height


    print('----- HUNTING SEASON -----')

    # Main loop
    while True:
        # Find and click the PNG image every 5 seconds
        if find_and_click_png_in_region('DuckTransparent.PNG', region):
            time.sleep(.5)  # Wait for 5 seconds after clicking the PNG image
            
        else:
            time.sleep(.5)  # If PNG image is not found, wait for 5 seconds before checking again
            
main()