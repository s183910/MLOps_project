import torch
from src.models.model import SignModel
from pelutils import log
from torchvision import transforms
import numpy as np
import cv2
from PIL import Image

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (28,28))    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     

    image_np = np.array(image, dtype=np.float32)
    image_np = image_np / 255.0
    image_np = image_np.reshape((784,1))
    image_tensor = torch.from_numpy(image_np).T

    return image_tensor

def predict_img(input_paths):

    tensors = torch.tensor([])

    for input_path in input_paths:        
        img_tensor = preprocess_image(input_path)
        tensors = torch.cat((tensors, img_tensor), 0)

    state_dict = torch.load("models/initial.pth")
    model = SignModel(784,25)
    model.load_state_dict(state_dict)
    model.eval()
    
    with torch.no_grad():
            outputs = model.forward(tensors)
            outputs = torch.exp(outputs)
            outputs = outputs.topk(1, dim=1).indices.flatten().tolist()
            # print(outputs.indices)
            # # outputs = [output[1].item() for output in outputs]
            
    return outputs


if __name__ == "__main__":
    print(predict_img(["api/sign_png/sign_test_i.png", "api/sign_png/sign_test_a.png"]))
