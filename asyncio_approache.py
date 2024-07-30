import asyncio
from pathlib import Path
from typing import Iterable

import aiofiles
import aiohttp

from interfaces import ImageDownloader


class AsyncImageDownLoader(ImageDownloader):
    """Asynchronous image downloader implementing ImageDownloader.

    Methods:
        download_image(url: str, file_name: str): Download a single image asynchronously.
        download_bunch_images(urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int): Download multiple images concurrently using asyncio.
    """
    def __init__(self, user_agent: str, save_dir: Path) -> None:
        headers = {"User-Agent": user_agent}
        self.headers = headers
        self.save_dir = save_dir

    async def download_image(self, url: str, file_name: str) -> None:
        """
        Download a single image asynchronously.

        Args:
            url (str): URL of the image to download.
            file_name (str): File name to save the downloaded image.
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    full_path = self.save_dir / file_name
                    async with aiofiles.open(full_path, mode="wb") as file:
                        async for chunk in response.content.iter_chunked(64 * 1024):
                            await file.write(chunk)
                    print(f"Image downloaded and saved to {full_path}")
                else:
                    print(f"Failed to download image from {url}")

    async def _bound_download(self, sem, url, file_name):
        """
        Helper method to limit the number of concurrent downloads.

        Args:
            sem (asyncio.Semaphore): Semaphore to limit concurrent downloads.
            url (str): URL of the image to download.
            file_name (str): File name to save the downloaded image.
        """
        async with sem:
            await self.download_image(url, file_name)

    async def download_bunch_images(self, urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int) -> None:
        """
        Download multiple images concurrently using asyncio.

        Args:
            urls (Iterable[str]): List of image URLs to download.
            file_names (Iterable[str]): List of file names for saving the images.
            max_concurrent_downloads (int): Maximum number of concurrent downloads.
        """
        sem = asyncio.Semaphore(max_concurrent_downloads)
        tasks = [
            asyncio.create_task(self._bound_download(sem, url, file_name))
            for url, file_name in zip(urls, file_names)
        ]
        await asyncio.gather(*tasks)



