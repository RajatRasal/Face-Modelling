from os.path import isfile, join
import pathlib
import cv2
from tqdm import tqdm

mypath = "data/"
data = pathlib.Path(mypath)
files = [path for path in data.rglob("*") if isfile(path)]

print("Total files found:", len(files))

model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = []

for f in tqdm(files):
    f = join("/Users/work/Face-Modelling", f)
    img = cv2.imread(f)
    if img is None:
        continue
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_rects = model.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
    if len(faces_rects) != 0:
        faces.append(f)

print("Total faces found:", len(faces))

with open("data/valid_faces.txt", "w") as f:
    for face in faces:
        f.write(f"{face}\n")