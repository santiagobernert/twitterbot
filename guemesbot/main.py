from config import client
from favyretweet import interactuar
from twittearfrases import twittear
from follow import seguir



def main():
    twittear(client)
    interactuar(client)
    seguir(client)

if __name__ == "__main__":
    main()