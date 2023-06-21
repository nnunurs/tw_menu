from functools import lru_cache

menu = {0: {"name": "pizza", "price": 10.99}, 1: {"name": "pasta", "price": 8.99}, 2: {"name": "tea", "price": 2.99}}
orders = {0: [{"name": "pizza", "price": 10.99}, {"name": "tea", "price": 2.99}], 1: [{"name": "pasta", "price": 8.99}]}