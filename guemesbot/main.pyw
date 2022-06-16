from config import client
from favyretweet import interactuar
from twittearfrases import twittear



def main():
    twittear(client)
    interactuar(client)

if __name__ == "__main__":
    main()