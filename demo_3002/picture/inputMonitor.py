from pynput import keyboard, mouse
import time
import threading

class InputListener:
    def __init__(self):
        # Set the starting time to 0
        self.start_time = 0
        self.last_mouse_move_time = 0

    def start(self):
        # Empty the buffers to store the pressed keys and mouse events with their timestamps
        self.keyboard_buffer = []
        self.mouse_buffer = []
        # Set the starting time to the current time
        self.start_time = time.time()
        # Create listener objects for keyboard and mouse
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move, on_click=self.on_mouse_click, on_scroll=self.on_mouse_scroll)
        # Start listening for keyboard and mouse events in separate threads
        self.keyboard_listener_thread = threading.Thread(target=self.keyboard_listener.start())
        self.mouse_listener_thread = threading.Thread(target=self.mouse_listener.start)
        self.keyboard_listener_thread.start()
        self.mouse_listener_thread.start()


    def on_keyboard_press(self, key):
        try:
           # Try to get the key name, otherwise get the key code
            name = key.name if hasattr(key, 'name') else key
            # Get the timestamp in seconds since the epoch and round to 3 decimal places
            self.keyboard_buffer.append((round(time.time() - self.start_time, 3), 'key_pressed', name))
            # print('press  Key:', name, 'Timestamp:', timestamp)
        except AttributeError:
            # Ignore special keys that don't have a name or a code
            pass

    def on_keyboard_release(self, key):
        try:
            # Try to get the key name, otherwise get the key code
            name = key.name if hasattr(key, 'name') else key
            # Get the timestamp in seconds since the epoch and round to 3 decimal places
            # timestamp = round(time.time() - self.start_time, 3)
            self.keyboard_buffer.append((round(time.time() - self.start_time, 3), 'key_released', name))
            # print('release  Key:', name, 'Timestamp:', timestamp)


            if key == keyboard.Key.space:
            # Pause or resume listening for keyboard events if the 'Space' key is pressed
                if self.keyboard_listener.running:
                    self.keyboard_listener.stop() 
                    print('Listener paused')


        except AttributeError:
            # Ignore special keys that don't have a name or a code
            pass

    # def on_mouse_move(self, x, y):
    #     self.mouse_buffer.append(('move', x, y, round(time.time() - self.start_time, 3)))
    #     print('move', x, y, round(time.time() - self.start_time, 3))
    #     # time.sleep(1)
 
    def on_mouse_move(self, x , y):
        current_time = time.time()
        if current_time - self.last_mouse_move_time >= 0.01:
            self.mouse_buffer.append((round(time.time() - self.start_time, 3), 'move', x, y))
            # print('move', x, y, round(current_time - self.start_time, 3))
            self.last_mouse_move_time = current_time


    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            event = 'mouse_pressed'
        else: 
            event = 'mouse_released'

        if button == mouse.Button.left:
            button_str = 'left'
        elif button == mouse.Button.right:
            button_str = 'right' 
        elif button == mouse.Button.middle:
            button_str = 'middle'
        else:
            button_str = 'unknown'

        self.mouse_buffer.append((round(time.time() - self.start_time, 3), event, x, y, button_str))
        # print(event, x, y, button, round(time.time() - self.start_time, 3))
 

    def on_mouse_scroll(self, x, y, dx, dy):
        self.mouse_buffer.append((round(time.time() - self.start_time, 3), 'scroll', x, y, dy))
        # print('scroll', x, y, dx, dy, round(time.time() - self.start_time, 3))

    def stop(self):
        # Stop listening for keyboard and mouse events and join the threads
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        self.keyboard_listener_thread.join()
        self.mouse_listener_thread.join()

    def get_events(self):
        # Combine the keyboard and mouse buffers and sort them by timestamp
        events = self.keyboard_buffer + self.mouse_buffer
        events.sort(key=lambda x: x[0])
        return events

# to use !!!!!
# Define a function to start the input listener
    def start_Input_listener(self):
        # Create a input listener object
        listener = InputListener()
        # Start the input   
        listener.start()
        # Wait for the listener to stop
        while listener.keyboard_listener.running:
            time.sleep(1)
        
        # Stop the listener
        listener.stop() 

        # Print the keys and their timestamp
        # for item in listener.get_events():
        #     print(item)
            # press,name, timestamp = item 
            # print(press, 'Key:', name, 'Timestamp:', timestamp)
        return listener.get_events()

# Call the function to start the input listener
# start_Input_listener()