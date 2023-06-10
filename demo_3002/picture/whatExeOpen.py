import psutil
import threading
import time

def get_running_processes():
    # Get a list of running processes
    processes = []
    for proc in psutil.process_iter():
        try:
            # Get process information as a named tuple
            process_info = proc.as_dict(attrs=['pid', 'name', 'exe'])
            # Append process information to the list
            processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def get_new_processes(initial_processes):
    # Get the current list of running processes
    current_processes = get_running_processes()
    # Find the processes that are in the current list but not in the initial list
    new_processes = [proc for proc in current_processes if proc not in initial_processes]
    return new_processes

class ProcessMonitor:
    def __init__(self):
        self.monitor_stop = threading.Event()
        self.process_list = []
        self.new_processes_list = []
        self.thread = None
    
    def start_monitoring(self):
        self.process_list = get_running_processes()
        self.monitor_stop.clear()
        self.thread = threading.Thread(target=self.update_process_list, daemon=True)
        self.thread.start()
    
    def pause_monitoring(self):
        self.monitor_stop.set()
        self.thread.join()
    
    def get_process_list(self):
        return self.new_processes_list
    
    def update_process_list(self):
        self.process_list = get_running_processes()
        self.new_processes_list = []
        timeZero = time.time()
        while not self.monitor_stop.is_set():
            if new_processes := get_new_processes(self.process_list):
                print("New processes detected:")
                for proc in new_processes:
                    timestamp = time.time()
                    self.new_processes_list.append((round(timestamp-timeZero,2), proc))
                    print(f"{round(timestamp-timeZero,2)} ,{proc['name']} ({proc['exe']})")
                self.process_list = get_running_processes()

#TO-USE !!!
monitor = ProcessMonitor()
monitor.start_monitoring()  # Starts monitoring for new processes
time.sleep(25)  # Wait for 10 seconds
monitor.pause_monitoring()  # Pauses monitoring
process_list = monitor.get_process_list()  # Gets the current list of running processes
print("\n\n\nCurrent processes:")
for process in process_list:
    print(f"{process[0]} ,{process[1]['name']} ({process[1]['exe']})")