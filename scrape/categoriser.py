#!.pythonenv/bin/python

from fuzzywuzzy import fuzz
import argparse
import csv
import fileinput
import sys

def import_category_mappers():
    food_map = {}
    categories = set()

    cvsinput = csv.reader(open('./food-composition-ch/data/generic-foods.csv'), delimiter=',')
    next(cvsinput) # skip first
    for vals in cvsinput:
        splitvals = map(lambda x: x.split(';'), vals[11:15])
        cats = set(zip(*splitvals))
        categories.update(cats)

        for v in vals[4:11]:
            if v == "":
                continue
            food_map[v] = cats

    return categories, food_map

def pargs():
    parser = argparse.ArgumentParser("Categorise food")
    parser.add_argument('--list-categories','-l', action='store_true', help='List known categories')

    return parser.parse_args()

if __name__=="__main__":
    categories, food_map = import_category_mappers()

    args = pargs()
    if args.list_categories:
        for c in categories:
            print(';'.join(c))
        sys.exit(0)

    for line in fileinput.input():
        matching_cat = set()
        highest_match = 0

        # Test if a product matches food
        for f,c in food_map.items():
            m = fuzz.ratio(line, f)
            if m > highest_match:
                matching_cat = c
                highest_match = m
            elif m == highest_match:
                matching_cat.update(c)

        # Test if a product matches a categoriy
        for c in categories:
            for clang in c:
                m = fuzz.partial_ratio(line, clang)
                if m > highest_match:
                    matching_cat = set([c])
                    highest_match = m
                elif m == highest_match:
                    matching_cat.update(set([c]))

        print("{}#{}#{}".format(line.strip(),'|'.join(map(lambda c: ';'.join(list(c)), matching_cat)),highest_match))

