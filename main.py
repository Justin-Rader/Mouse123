import pynput.mouse
import getpass
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import schedule
import time

# Replace 'YOUR_SERVICE_ACCOUNT_JSON_KEY_FILE.json' with the actual JSON key file path
json_keyfile = 'googleAuth.json'

# Authenticate using the service account JSON key file
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gc = gspread.authorize(credentials)

# Replace 'YOUR_SPREADSHEET_ID' with the actual Google Sheet ID
spreadsheet_id = '12rcp-kvO9FP5kkWCDy7fy-j8xcH_P4Vyxe-MLDpPE_w'

# Open the Google Sheet by its ID
sheet = gc.open_by_key(spreadsheet_id)

# Access the specific worksheet
worksheet = sheet.get_worksheet(0)

# Get the current user's name
user_name = getpass.getuser()

# Variable to keep track of the click count
click_count = 0

# Function to count mouse clicks and print the running count with the user's name
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        print(f"User: {user_name}, Mouse click count: {click_count}")

# Function to send data to Google Sheets
def send_data_to_sheets():
    global click_count
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write data to the worksheet with timestamp
    data = [str(current_time), str(user_name), str(click_count)]  # Convert all values to strings
    worksheet.insert_rows([data], 2)  # Insert data as a list containing a list (2D array)

    # Reset counter
    click_count = 0

# Create a mouse listener
mouse_listener = pynput.mouse.Listener(on_click=on_click)

# Start the mouse listener
mouse_listener.start()

# Schedule the data upload task to run every 5 minutes
schedule.every(1).minutes.do(send_data_to_sheets)
# Schedule the data upload task to run at the top of every hour
#schedule.every().hour.at(":00").do(send_data_to_sheets)

# Continuously check the schedule and run the task
while True:
    schedule.run_pending()
    time.sleep(1)  # Check every second

