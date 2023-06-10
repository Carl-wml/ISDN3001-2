import threading
import pyautogui
import time


class InputPlayer:
    def __init__(self):
        self.data_sets = []
        self.thread = None
        self.stop_event = threading.Event()

    def load(self, data_set):
        self.data_sets.append(data_set)

    def play(self, data_set_index=0):
        if self.thread is not None and self.thread.is_alive():
            raise RuntimeError("Playback is already in progress")

        self.thread = threading.Thread(target=self._play_thread, args=(data_set_index,))
        self.stop_event.clear()
        self.thread.start()

    def stop(self):
        self.stop_event.set()

    def _play_thread(self, data_set_index):
        passTime = 0
        self.start_time = time.time()
        for action in self.data_sets[data_set_index]:
            if self.stop_event.is_set():
                break

            if action[1] == 'move':
                pyautogui.moveTo(action[2], action[3])

            elif action[1] == 'mouse_pressed':
                pyautogui.mouseDown(button=action[4], x=action[2], y=action[3])

            elif action[1] == 'mouse_released':
                pyautogui.mouseUp(button=action[4], x=action[2], y=action[3])

            elif action[1] == 'scroll':
                try:
                    pyautogui.scroll(action[4]*80, x=action[2], y=action[3])
                except:
                    pyautogui.hscroll(action[4]*80, x=action[2], y=action[3])

            elif action[1] == 'key_pressed':
                if str(action[2]).__len__() == 3:
                    pyautogui.keyDown(str(action[2])[1:-1])
                else:
                    pyautogui.keyDown(str(action[2]))

            elif action[1] == 'key_released':
                pyautogui.keyUp(str(action[2]))

            time.sleep(action[0]-passTime)
            passTime = action[0]

##to-use!!!

# data_set = [[1.456, 'move', 1277, 369],
# [1.48, 'move', 1277, 374],
# [1.505, 'move', 1277, 378],
# [1.662, 'move', 1277, 383],
# [1.684, 'move', 1273, 394],
# [2.132, 'scroll', 1273, 398, 1],
# [2.236, 'scroll', 1273, 398, 1],
# [2.416, 'scroll', 1273, 398, 1],
# [2.644, 'scroll', 1273, 398, 1],
# [3.068, 'scroll', 1273, 398, -1],
# [3.17, 'scroll', 1273, 398, -1],
# [3.328, 'scroll', 1273, 398, -1],
# [3.517, 'scroll', 1273, 398, -1],
# [4.412, 'scroll', 1273, 398, -1],
# [5.002, 'mouse_pressed', 1273, 398, 'left'],
# [5.105, 'mouse_released', 1273, 398, 'left'],
# [5.41, 'move', 1273, 403],
# [5.433, 'move', 1269, 409],
# [5.458, 'move', 1267, 413],
# [5.482, 'move', 1265, 419],
# [5.515, 'move', 1263, 421],
# [5.719, 'mouse_pressed', 1263, 421, 'left'],
# [5.813, 'mouse_released', 1263, 421, 'left'],
# [6.056, 'move', 1263, 423],
# [7.131, 'key_pressed', 'a'],
# [7.252, 'key_released', 'a'],
# [7.3, 'key_pressed', 'b'],
# [7.422, 'key_released', 'b'],
# [8.135, 'key_pressed', 'c'],
# [8.266, 'key_released', 'c'],
# [9.355, 'key_pressed', 'backspace'],
# [9.428, 'key_released', 'backspace'],
# [9.523, 'key_pressed', 'backspace'],
# [9.598, 'key_released', 'backspace'],
# [9.698, 'key_pressed', 'backspace'],
# [9.774, 'key_released', 'backspace'], 
# [11.276, 'move', 1273, 431],
# [11.298, 'move', 1295, 437],
# [11.331, 'move', 1301, 441],
# [11.55, 'move', 1300, 441],
# [11.573, 'move', 1300, 440],
# [12.346, 'key_pressed', 'space'],
# [12.488, 'key_released', 'space']]


# player = InputPlayer()
# player.load(data_set)

# # Start playing the data set in a new thread
# player.play()

# # Wait for a few seconds
# time.sleep(15)

# # Stop the playback
# player.stop()
