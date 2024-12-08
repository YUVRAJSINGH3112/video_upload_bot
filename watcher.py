import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VideoHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if event.src_path.endswith(".mp4"):
            asyncio.run(self.callback(event.src_path))

async def monitor_directory():
    path = "./videos"
    event_handler = VideoHandler(callback=upload_videos)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
