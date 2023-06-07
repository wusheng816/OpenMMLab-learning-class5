import os
import shutil


fruits = "./data/fruits"
train = "./data/train"
val = "./data/val"

labels = os.listdir(fruits)
print(len(labels))

for label in labels:
    dir = os.path.join(fruits, label)
    images = os.listdir(dir)
    num = int(0.85 * len(images))
    images_train = images[:num]
    for image in images:
        img = os.path.join(dir, image)
        if image in images_train:
            save_path = os.path.join(train, label)
        else:
            save_path = os.path.join(val, label)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        shutil.copy(img, os.path.join(save_path, image))
