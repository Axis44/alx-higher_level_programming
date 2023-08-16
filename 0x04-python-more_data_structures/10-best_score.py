#!/usr/bin/python3
def best_score(my_dict):
    # retturn biggest integer
    return max(my_dict, key=my_dict.get) if my_dict else None
