import time
import subprocess
import os
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

watch_path = 'd:\Downloads\\'
txt_path = watch_path + 'txt\\'

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        file = str(event.src_path)
        extension = event.src_path.split('.')[-1]
        if extension == 'txt':
            print(f'event type: {event.event_type} path: "{file}"')
            os.system(f'mv {file} {txt_path}')
            # subprocess.run(('cmd',  '/C mv', 'start', '', f'{file} {txt_path}'))
        elif extension == 'jpg':
            print('its a jpg')


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, watch_path, recursive=False)
observer.start()


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
