from pynput import keyboard, mouse
import time

class KeyboardListener:
    def __init__(self):
        # Set the starting time to 0
        self.start_time = 0
        # Create an empty buffer to store the pressed keys and their timestamps
        self.buffer = []
        # Create a listener object, but do not start it yet
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def start(self):
        # Set the starting time to the current time
        self.start_time = time.time()
        # Start listening for keyboard events
        self.listener.start()
        # empty the buffer to store the pressed keys and their timestamps
        self.buffer = []

    def on_press(self, key):
        try:
            # Try to get the key name, otherwise get the key code
            name = key.name if hasattr(key, 'name') else key
            # Get the timestamp in seconds since the epoch and round to 3 decimal places
            timestamp = round(time.time() - self.start_time, 3)
            self.buffer.append(('press', name, timestamp))
            print('press  Key:', name, 'Timestamp:', timestamp)
        except AttributeError:
            # Ignore special keys that don't have a name or a code
            pass

    def on_release(self, key):
        try:
            # Try to get the key name, otherwise get the key code
            name = key.name if hasattr(key, 'name') else key
            # Get the timestamp in seconds since the epoch and round to 3 decimal places
            timestamp = round(time.time() - self.start_time, 3)
            self.buffer.append(('release', name, timestamp))
            print('release  Key:', name, 'Timestamp:', timestamp)
            if key == keyboard.Key.space:
            # Pause or resume listening for keyboard events if the 'Space' key is pressed
                if self.listener.running:
                    self.listener.stop()
                    print('Listener paused')
        except AttributeError:
            # Ignore special keys that don't have a name or a code
            pass

    def on_move(x, y):
        print(f'Mouse moved to ({x}, {y})')

    def on_click(x, y, button, pressed):
        action = 'Pressed' if pressed else 'Released'
        print(f'{action} {button} at ({x}, {y})')

    def on_scroll(x, y, dx, dy):
        print(f'Scrolled {dy} units at ({x}, {y})')

    def stop(self):
        # Stop listening for keyboard events
        self.listener.stop()

    def get_events(self):
        return self.buffer
    

    # to use !!!!!
# Define a function to start the keyboard listener
def start_keyboard_listener():
    # Create a keyboard listener object
    listener = KeyboardListener()
    # Start the keyboard listener
    listener.start()
    # Wait for the listener to stop
    while listener.listener.running:
        time.sleep(1)
    # Print the keys and their timestamp
    for item in listener.get_events():
        press,name, timestamp = item
        print(press, 'Key:', name, 'Timestamp:', timestamp)
    # Stop the listener
    listener.stop()

# Call the function to start the keyboard listener
start_keyboard_listener()