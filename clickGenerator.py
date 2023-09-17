import random
import time
import pyautogui

# Define a function to generate a random mouse click
def generate_random_clicks():
    # Generate a random number of clicks between 1 and 100
    num_clicks = random.randint(1, 100)
    
    # Generate and simulate the mouse clicks
    for _ in range(num_clicks):
        # Generate random coordinates within the screen's dimensions
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        
        # Simulate a mouse click at the random coordinates
        pyautogui.click(x, y)
    
    return num_clicks

# Main loop to generate mouse clicks every minute
while True:
    # Generate random mouse clicks
    clicks = generate_random_clicks()
    
    # Print a message indicating the number of clicks
    print(f"Simulated {clicks} mouse clicks.")
    
    # Sleep for one minute (60 seconds)
    time.sleep(60)
