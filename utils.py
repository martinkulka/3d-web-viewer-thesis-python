import re


def get_seeds_from_seed_string(seed_string):
    seeds = []
    separate_seeds = seed_string.split("-")

    for seed in separate_seeds:
        seeds.append(tuple(int(coordinate) for coordinate in re.split(r" |,", seed)))

    return seeds
