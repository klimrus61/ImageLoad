import asyncio
from pathlib import Path

import typer

from asyncio_approache import AsyncImageDownLoader
from thread_approache import ThreadImageLoader

app = typer.Typer()


@app.command()
def download_asynchronously():
    """Асинхронный подход"""
    async_downloader = AsyncImageDownLoader(user_agent, save_dir)
    asyncio.run(async_downloader.download_bunch_images(urls, file_names, max_concurrent_downloads))


@app.command()
def download_by_threads():
    """Потоковый подход"""
    thread_downloader = ThreadImageLoader(user_agent, save_dir)
    thread_downloader.download_bunch_images(urls, file_names, max_concurrent_downloads)


if __name__ == "__main__":
    # Заранее спарсенные ссылки на фотографии
    urls = ['https://images.dog.ceo/breeds/terrier-sealyham/n02095889_6531.jpg',
            'https://images.dog.ceo/breeds/cotondetulear/IMAG1063.jpg',
            'https://images.dog.ceo/breeds/poodle-standard/n02113799_4458.jpg',
            'https://images.dog.ceo/breeds/poodle-medium/PXL_20210220_100624962.jpg',
            'https://images.dog.ceo/breeds/terrier-dandie/n02096437_4.jpg',
            'https://images.dog.ceo/breeds/schnauzer-miniature/n02097047_6567.jpg',
            'https://images.dog.ceo/breeds/terrier-yorkshire/n02094433_7394.jpg',
            'https://images.dog.ceo/breeds/chow/n02112137_9280.jpg',
            'https://images.dog.ceo/breeds/brabancon/n02112706_2441.jpg',
            'https://images.dog.ceo/breeds/terrier-yorkshire/n02094433_3655.jpg',
            'https://images.dog.ceo/breeds/lhasa/n02098413_18307.jpg',
            'https://images.dog.ceo/breeds/mountain-swiss/n02107574_2086.jpg',
            'https://images.dog.ceo/breeds/segugio-italian/n02090722_001.jpg',
            'https://images.dog.ceo/breeds/australian-shepherd/pepper.jpg',
            'https://images.dog.ceo/breeds/setter-gordon/n02101006_1660.jpg',
            'https://images.dog.ceo/breeds/terrier-tibetan/n02097474_1728.jpg',
            'https://images.dog.ceo/breeds/bulldog-english/bunz.jpg',
            'https://images.dog.ceo/breeds/pembroke/n02113023_6508.jpg',
            'https://images.dog.ceo/breeds/terrier-cairn/n02096177_4768.jpg',
            'https://images.dog.ceo/breeds/terrier-kerryblue/n02093859_1662.jpg']
    # Список имен для скаченных фотографий
    file_names = [
        f"{url.split("/")[-2]}.jpg"
        for url in urls
    ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    max_concurrent_downloads = 5
    save_dir = Path("./dogs/")

    # создание папки для картинок
    if not save_dir.exists():
        save_dir.mkdir()
    # запуск cli приложения
    app()
