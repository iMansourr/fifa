import random
from random import shuffle
import requests
import pandas as pd

my_csv = pd.read_csv('players_database.csv', names = ['first', 'last','rating', 'resourceid'])


players_db = []
for i, row in my_csv.iterrows():

    player_entry = {'first':row['first'] , 'last':row['last'], 'resourceid': row['resourceid']}

    players_db.append(player_entry)

x = players_db['last'].count("Messi")
print(x)
# print(players_db[5]['first'] + " " + players_db[5]['last'] + " " + players_db[5]['resourceid'])

# print all resourceid
# for x in players_db:
#     if x.get("resourceid") == 1:
#         continue
#     print(x["resourceid"])


def futbin():
    player_name = ["RAHEEM STERLING", 190790]
    #resource_id = input("enter reasource id ")

    futbin_api = requests.get(f'https://www.futbin.org/futbin/api/fetchPriceInformation?playerresource={player_name[1]}&platform=PS')

    data = futbin_api.json()

    last_price = data['LCPrice']

    price_updated = int(data['updatedon'] / 60)

    print("Player Name: " + player_name[0])

    print("\nLast price is " + str(last_price) + ". Price updated " + str(price_updated) + " minutes ago.")

    buy_percentage = 0.90
    sell_percentage = 0.98

    search_price = int(last_price * buy_percentage)
    sell_price = int(last_price * sell_percentage)

    print("\nrecommended to purchase the player for " + str(search_price) + ".")
    print("\nrecommended to sell the player for " + str(sell_price) + ".")








