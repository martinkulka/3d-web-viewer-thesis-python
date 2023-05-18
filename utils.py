import re
import os
import shutil


def get_seeds_from_seed_string(seed_string):
    seeds = []
    separate_seeds = seed_string.split("-")

    for seed in separate_seeds:
        seeds.append(tuple(int(coordinate) for coordinate in re.split(r"[ ,]", seed)))

    return seeds


def remove_segmentation_file():
    file_path = os.path.join(os.getcwd(), "segmentation.nii.gz")

    if os.path.exists(file_path):
        os.remove(file_path)



def rename_segmented_file():
    file_path = os.path.join(os.getcwd(), "eval", "input", "input_trans.nii.gz")
    renamed_file_path = os.path.join(os.getcwd(), "eval", "input", "segmentation.nii.gz")

    os.rename(file_path, renamed_file_path)


def replace_segmented_file():
    file_path = os.path.join(os.getcwd(), "eval", "input", "segmentation.nii.gz")
    destination_file_path = os.path.join(os.getcwd(), "segmentation.nii.gz")

    os.replace(file_path, destination_file_path)

def rename_registration_file():
    file_path = os.path.join(os.getcwd(), "dataset", "images", "output.nii.gz")
    renamed_file_path = os.path.join(os.getcwd(), "dataset", "images", "input.nii.gz")

    os.rename(file_path, renamed_file_path)


def replace_input_file_to_segment(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    destination_file_path = os.path.join(os.getcwd(), "dataset", "images", "input.nii.gz")

    if os.path.exists(destination_file_path):
        os.remove(destination_file_path)

    shutil.copy(file_path, destination_file_path)

