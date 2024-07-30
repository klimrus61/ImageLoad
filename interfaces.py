from abc import abstractmethod, ABC
from pathlib import Path
from typing import Iterable


class ImageDownloader(ABC):
    """
    Abstract base class for downloading images.

    Attributes:
        headers (dict): HTTP headers for the requests.
        save_dir (Path): Directory to save the downloaded images.

    Methods:
        download_image(url: str, save_path: str):
            Abstract method to download a single image.
        download_bunch_images(urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int):
            Abstract method to download multiple images concurrently.
    """
    headers: dict
    save_dir: Path

    @abstractmethod
    async def download_image(self, url: str, save_path: str):
        """
        Download a single image.

        Args:
            url (str): URL of the image to download.
            save_path (str): Path to save the downloaded image.
        """
        pass

    @abstractmethod
    async def download_bunch_images(self, urls: Iterable[str], file_names: Iterable[str], max_concurrent_downloads: int):
        """
        Download multiple images concurrently.

        Args:
            urls (Iterable[str]): List of image URLs to download.
            file_names (Iterable[str]): List of file names for saving the images.
            max_concurrent_downloads (int): Maximum number of concurrent downloads.
        """
        pass
