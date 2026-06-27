import os
import shutil
import random

TRAIN_IMG = "road_damage_yolo/images/train"
TRAIN_LABEL = "road_damage_yolo/labels/train"

VAL_IMG = "road_damage_yolo/images/val"
VAL_LABEL = "road_damage_yolo/labels/val"

os.makedirs(VAL_IMG, exist_ok=True)
os.makedirs(VAL_LABEL, exist_ok=True)

images = [f for f in os.listdir(TRAIN_IMG) if f.endswith(".jpg")]

print("Total train images:", len(images))

# Move 20% to validation
val_count = int(len(images) * 0.2)

random.shuffle(images)

val_images = images[:val_count]

for img in val_images:

    src_img = os.path.join(TRAIN_IMG, img)
    dst_img = os.path.join(VAL_IMG, img)

    shutil.move(src_img, dst_img)

    label = img.replace(".jpg", ".txt")

    src_label = os.path.join(TRAIN_LABEL, label)
    dst_label = os.path.join(VAL_LABEL, label)

    if os.path.exists(src_label):
        shutil.move(src_label, dst_label)

print("Validation images:", len(os.listdir(VAL_IMG)))
print("Validation labels:", len(os.listdir(VAL_LABEL)))
print("Done")
