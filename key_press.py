import keyboard
import brain

# Define the function to be called when '0' is pressed
def on_zero_pressed():
    brain.test()

# Hook the event listener to the '0' key
keyboard.add_hotkey('0', on_zero_pressed)

# Keep the script running to listen for key events
print("Press '0' to trigger the function. Press 'Esc' to exit.")
keyboard.wait()