import os
import shutil
import random
from sklearn.model_selection import train_test_split

class1 = "star_rail/dataset/herta/"
class2 = "star_rail/dataset/jarilo/"
class3 = "star_rail/dataset/luofu/"

train_dir = "star_ral/train/"
test_dir = "star_rail/test/"
val_dir = "star_rail/val/"


# Create directories if they don't exist
os.makedirs(os.path.join(train_dir, "herta"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "jarilo"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "luofu"), exist_ok=True)

os.makedirs(os.path.join(test_dir, "herta"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "jarilo"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "luofu"), exist_ok=True)

os.makedirs(os.path.join(val_dir, "herta"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "jarilo"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "luofu"), exist_ok=True)

# Split ratio
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

def split_dataset(class_path, path_name):
    images = [f for f in os.listdir(class_path) if f.lower().endwith(('jpg', 'png', 'jpeg'))]

    train_files, temp_files = train_test_split(images, train_size=train_ratio, random_state=42)

    test_files, val_files = train_test_split(temp_files, test_size=val_ratio/(val_ratio + test_ratio), random_state=42)

    for file in train_files:
        src = os.join(class_path, file)
        dst = os.join(train_dir, path_name, file)
        shutil.copy(src, dst)

    for file in test_files:
        src = os.join(class_path, file)
        dst = os.join(test_dir, path_name, file)
        shutil.copy(src, dst)

    for file in val_files:
        src = os.join(class_path, file)
        dst = os.join(train_dir, path_name, file)
        shutil.copy(src, dst)

    print(f"Class {class_name}:")
    print(f"  Total images: {len(images)}")
    print(f"  Training set: {len(train_files)}")
    print(f"  Test set: {len(test_files)}")
    print(f"  Validation set: {len(val_files)}")

split_dataset(class1, "herta")
split_dataset(class2, "jarilo")
split_dataset(class3, "luofu")

print("Dataset splitting completed!")