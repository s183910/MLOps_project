from PIL import Image
import pandas as pd
import requests

# requires transformers package: pip install transformers
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# image from the data/raw/sign_mnist_train.csv
image = pd.read_csv("data/raw/sign_mnist_train.csv")


# set either text=None or images=None when only the other is needed
inputs = processor(text=None, images=image, return_tensors="pt", padding=True)

img_features = model.get_image_features(inputs["pixel_values"])
