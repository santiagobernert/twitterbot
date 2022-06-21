from config import client
from favyretweet import interactuar
from twittearfrases import twittear
import schedule, time


def main():
    twittear(client)
    interactuar(client)

schedule.every(15).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)