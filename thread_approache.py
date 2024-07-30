import concurrent
from pathlib import Path
from typing import Iterable

import requests

from interfaces import ImageDownloader


class ThreadImageLoader(ImageDownloader):
    """
    Multithreaded image downloader implementing ImageDownloader.

    Methods:
       download_image(url: str, file_name: str):
           Download a single image synchronously.
       download_bunch_images(urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int):
           Download multiple images concurrently using threads.
    """
    def __init__(self, user_agent: str, save_dir: Path) -> None:
        headers = {"User-Agent": user_agent}
        self.headers = headers
        self.save_dir = save_dir

    def download_image(self, url: str, file_name: str) -> None:
        """
        Download a single image synchronously.

        Args:
            url (str): URL of the image to download.
            file_name (str): File name to save the downloaded image.
        """
        response = requests.get(url)
        if response.status_code == 200:
            full_path = self.save_dir / file_name
            with open(full_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved to {full_path}")
        else:
            print(f"Failed to download image from {url}")

    def download_bunch_images(self, urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int) -> None:
        """
        Download multiple images concurrently using threads.

        Args:
            urls (Iterable[str]): List of image URLs to download.
            file_names (Iterable[str]): List of file names for saving the images.
            max_concurrent_downloads (int): Maximum number of concurrent downloads.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent_downloads) as executor:
            futures = [
                executor.submit(self.download_image, url, file_name)
                for url, file_name in zip(urls, file_names)
            ]
            concurrent.futures.wait(futures)
