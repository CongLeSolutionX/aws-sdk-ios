from datetime import datetime


def log(message):
    print(f'{str(datetime.now())}: {message}')
