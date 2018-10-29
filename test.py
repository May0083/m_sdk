from mtgsdk import Card
import pickle
import os

path = "all_card.bin"

with open(path, 'rb') as base_file:
  cards  = pickle.load(base_file)

print(cards[0])

