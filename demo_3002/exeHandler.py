import os
import webbrowser
import time
import win32process
import win32gui
import win32con
from selenium import webdriver


class ExeHandler:
    def open_exe(self, exe_path):
        os.startfile(exe_path)

    def open_url(self, url):
        webbrowser.open(url)

    # def open_url_in_browser(self, url, browser_path):
    #     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
    #     webbrowser.get('chrome').open(url)

    # def open_url_in_browser_with_selenium(self, url, browser_path):
    #     driver = webdriver.Chrome(browser_path)
    #     driver.get(url)

    def maximum_window(self, window_title):
        hwnd = win32gui.FindWindowEx(None, None, None, window_title)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    
    def resize_window(self, window_title, left=0, top=0, width=1540, height=818):
        hwnd = win32gui.FindWindowEx(None, None, None, window_title)
        win32gui.MoveWindow(hwnd, left, top, width, height, True)
    
    def minimize_window(self, window_title):
        hwnd = win32gui.FindWindowEx(None, None, None, window_title)
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    def enlarge_url(self, url):
        pass

    def get_website_hwnd(self, url):
        # hwnd = win32gui.FindWindowEx(None, None, None, window_title)
        # win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        pass
    
    def get_hwnd(self, window_title):
        hwnd = win32gui.FindWindowEx(None, None, None, window_title)
        return hwnd

    def search_real_window_title_array(self, window_title):
        def enum_callback(hwnd, windows):
            title = win32gui.GetWindowText(hwnd)
            windows.append(title)
            return True

        windows = [], titles = []
        win32gui.EnumWindows(enum_callback, windows)
        for title in windows:
            # print(title)
            if window_title in title:
                titles.append(title)                    #Bug? only return the first one
        if not titles:
            print(f"No window found with title '{window_title}' on list")
            return False
        return titles
    
    # def resize_window(self, window_title, left=0, top=0, width=1540, height=818):
    #     # window_title is correct
    #     hwnd = win32gui.FindWindowEx(None, None, None, window_title)
    #     if hwnd != 0:
    #         win32gui.MoveWindow(hwnd, left, top, width, height, True)
    #     else:
    #         print(f"No window found with title '{window_title}'")

    # def minimize_window(self, window_title):

    #     # window_title = self.search_real_window_title(window_title)
    #     # if not window_title:
    #     #     print(f"No window found with title '{window_title}' on list")
    #     #     return

    #     # window_title is correct
    #     hwnd = win32gui.FindWindowEx(None, None, None, window_title)
    #     if hwnd != 0:
    #         win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    #     else:
    #         print(f"No window found with title '{window_title}'")

    def open_path(self, path, left=0, top=0, width=1540, height=818, is_web=False, need_new=True):
        if need_new:
            if is_web:
                self.open_url(path)
            else:
                try:
                    handle, _, _, _ = win32process.CreateProcess(
                        None,
                        path,
                        None,
                        None,
                        False,
                        0,
                        None,
                        os.path.dirname(path),
                        win32process.STARTUPINFO(),
                    )

                    hwnd = None
                    while not hwnd:
                        hwnd = win32gui.FindWindow(None, os.path.basename(path))

                    win32gui.MoveWindow(hwnd, left, top, width, height, True)

                    return handle

                except Exception as e:
                    os.startfile(path)
                    hwnd = win32gui.FindWindow(None, os.path.basename(path))
                    if hwnd != 0:
                        _, _, w, h = win32gui.GetWindowRect(hwnd)
                        win32gui.MoveWindow(hwnd, 0, 0, width, height, True)
        else:
            self.unminimize_app(path, left, top, width, height, is_web)

    def unminimize_app(self, path, left=0, top=0, width=1540, height=818, is_web=False):
        #max width:1540
        #max height:818
        if is_web:
            if not self.url_ok(window_title):
                webbrowser.open(window_title)
                handle = win32gui.FindWindow(None, window_title)
                window_title = self.search_real_name_window('Google Chrome')
                handle = win32gui.FindWindow(None, window_title)
                adjust_Size(handle,left,top,width,height)
                return
        else:
            window_title = self.search_real_name_window(window_title)
            if not window_title:
                print(f"No window found with title '{window_title}' on list")
                return

            hwnd = win32gui.FindWindowEx(None, None, None, window_title)
            if hwnd != 0:
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            else:
                print(f"No window found with title '{window_title}'")


        def adjust_Size(handle, left, top, width, height):
            win32gui.ShowWindow(handle, win32con.SW_RESTORE)
            win32gui.SetWindowPos(handle, win32con.HWND_TOP, left, top, width, height, win32con.SWP_SHOWWINDOW)
            #win32gui.ShowWindow(handle, win32con.SW_RESTORE)

        app_name = ""
        app_path = path

        while True:
            hwnd = win32gui.GetForegroundWindow()
            if win32gui.GetWindowText(hwnd) == "Untitled - Notepad":
                break
            time.sleep(0.1)

        win32gui.ShowWindow(hwnd, 3)  # 3 corresponds to SW_MAXIMIZE
    


    def reopenOpen_Application(self,window_title, left, top, width, height, IsWeb=False):
        #max width:1540
        #max height:818
        if IsWeb:
            if not self.url_ok(window_title):
                webbrowser.open(window_title)
                handle = win32gui.FindWindow(None, window_title)
                window_title = self.search_real_window_title('Google Chrome')
                handle = win32gui.FindWindow(None, window_title)
                adjust_Size(handle,left,top,width,height)
                return

        window_title = self.search_real_window_title(window_title)
        #print(window_title)
        # if not window_title:
        #     if IsWeb:
        #         webbrowser.open('https://miro.com/app/dashboard/')
        #         print('Web opening: ', window_title,"...")
        #     else:
        #         print('app opening: ', window_title,"...")
        #     return
        # print('app reopening: ', window_title,"...")
        handle = win32gui.FindWindow(None, window_title)
        adjust_Size(handle,left,top,width,height)

        def adjust_Size(handle, left, top, width, height):
            win32gui.ShowWindow(handle, win32con.SW_RESTORE)
            win32gui.SetWindowPos(handle, win32con.HWND_TOP, left, top, width, height, win32con.SWP_SHOWWINDOW)
            #win32gui.ShowWindow(handle, win32con.SW_RESTORE)

    def url_ok(self, url):            #problem!!! Not working!!!!!
        from selenium import webdriver

        driver = webdriver.Chrome()

        driver.get(url)
        tabs = driver.window_handles
        print("tabs", tabs)
        print("url in tabs: ",url in tabs)
        return (url in tabs)


# exe_name = os.path.splitext(os.path.basename(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"))[0]
# print(exe_name)
# eh = ExeHandler()
# eh.open_path(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE", 0, 0, 1540, 818)
# os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
# os.startfile(r"C:\Users\carll\AppData\Roaming\Zoom\bin\Zoom.exe")
# webbrowser.open('https://miro.com/app/dashboard/')