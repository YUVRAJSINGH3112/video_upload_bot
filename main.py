import asyncio
from downloader import download_videos
from watcher import monitor_directory
from uploader import upload_videos

async def main():
    # Start video downloading and directory monitoring concurrently
    await asyncio.gather(
        download_videos(),
        monitor_directory()
    )

if __name__ == "__main__":
    asyncio.run(main())
