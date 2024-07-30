## Description
The solution for the test task from the company neuro-core.ru

   Какими средствами распараллелить загрузку X картинок на сервер, чтобы в каждый момент времени загружалось не более N картинок?

   Одна реализация - coroutine \
   Вторая реализация - multithreading


## Installation

1. Clone the repo, switch to **dev** branch, pull changes:

    ```bash
    https://github.com/ur-org/team_tracker_back.git
    cd team_tracker_back
    git switch dev
    git pull
    ```

2. Make sure you have **Poetry** installed:

    ```bash
    pip install -U pip
    poetry config virtualenvs.in-project true
    pip install poetry
    ```

3. Install the project dependencies:

    ```bash
    poetry install
    poetry shell
    ```

:exclamation: if you encounter any problems such as **"poetry is unable to read poetry.lock file"** - delete the existing **poetry.lock** file from your project directory and run the command again.

## Run
1. To run the asynchronous approach use: 

   ```bash
   python main.py download-asynchronously
   ```

2. To run by using threads:
   
   ```bash
   python main.py download-by-threads
   ```