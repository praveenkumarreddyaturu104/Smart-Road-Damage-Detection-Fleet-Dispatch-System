import shutil
import random
import os

print("Current Working Directory:")
print(os.getcwd())

SOURCE_ROOT = "train"
OUTPUT_ROOT = "road_damage_yolo"

TRAIN_RATIO = 0.8

countries = ["Czech", "India", "Japan"]

# Create folders
for folder in [
    "images/train",
    "images/val",
    "labels/train",
    "labels/val"
]:
    os.makedirs(os.path.join(OUTPUT_ROOT, folder), exist_ok=True)

all_files = []

# Collect all image-label pairs
for country in countries:

    image_dir = os.path.join(SOURCE_ROOT, country, "images")
    label_dir = os.path.join(SOURCE_ROOT, country, "labels")

    for image_file in os.listdir(image_dir):

        if not image_file.lower().endswith(".jpg"):
            continue

        label_file = image_file.replace(".jpg", ".txt")

        image_path = os.path.join(image_dir, image_file)
        label_path = os.path.join(label_dir, label_file)

        if os.path.exists(label_path):
            all_files.append((image_path, label_path))

print(f"Total Samples Found: {len(all_files)}")

# Shuffle
random.shuffle(all_files)

split_index = int(len(all_files) * TRAIN_RATIO)

train_files = all_files[:split_index]
val_files = all_files[split_index:]

print(f"Train Samples: {len(train_files)}")
print(f"Validation Samples: {len(val_files)}")

# Copy train files
for image_path, label_path in train_files:

    shutil.copy(
        image_path,
        os.path.join(
            OUTPUT_ROOT,
            "images/train",
            os.path.basename(image_path)
        )
    )

    shutil.copy(
        label_path,
        os.path.join(
            OUTPUT_ROOT,
            "labels/train",
            os.path.basename(label_path)
        )
    )

# Copy validation files
for image_path, label_path in val_files:

    shutil.copy(
        image_path,
        os.path.join(
            OUTPUT_ROOT,
            "images/val",
            os.path.basename(image_path)
        )
    )

    shutil.copy(
        label_path,
        os.path.join(
            OUTPUT_ROOT,
            "labels/val",
            os.path.basename(label_path)
        )
    )

print("Dataset Prepared Successfully!")