import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        self.ignorePatterns = [
            "*.py","*.pyc","*.c","*.java","*.php","*.vb","*.cs","*.cpp","*.class","*.cgi","*.pl","*.h" ## common programming Languages
        ]
        self.ignoreDirectories = True
        PatternMatchingEventHandler.__init__(self, ignore_patterns= self.ignorePatterns, ignore_directories=self.ignoreDirectories, case_sensitive=False)

    @staticmethod
    def on_any_event(event):
        try:
            if event.is_directory: 
                return None
            if event.event_type == 'created' or event.event_type == 'modified' or event.event_type == 'moved': 
                srcPath = r"{}".format(event.src_path)
                if os.path.isfile(srcPath) == True:
                    final_srcPath = srcPath.replace("\\","/") ### Here we can get the source path of the file

                    #### Your Business Logic
                    
                else:
                   return None
            else:
                return None
        except:
            print(f"ERROR-MESSAGE")



def monitor(currentActiveDrives):
    event_handler = MyHandler()
    observer = Observer()

    # Empty list of observers
    observers = []
    for line in currentActiveDrives:
        try:
            targetPath = str(line).rstrip()
            observer.schedule(event_handler, r"{}".format(targetPath), recursive=True)
            observers.append(observer)
        except:
            print(f"ERROR-MESSAGE")
            pass

    observer.start()
    try:
        while True:
            # poll every second
            time.sleep(1)

    except KeyboardInterrupt:
        for obs in observers:
            obs.unschedule_all()
            # stop observer if interrupted
            obs.stop()

    for obs in observers:
        # Wait until the thread terminates before exit
        obs.join()


if __name__ == "__main__":
    currentActiveDrives = []  ## Folder path 
    monitor(currentActiveDrives)
