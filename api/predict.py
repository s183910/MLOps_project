import torch
from src.models.model import SignModel
from pelutils import log
from torchvision import transforms
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

class APIModelHandler:
    """ Used for preprocessing and classifying images POSTed to the API. """

    def __init__(self):
        state_dict = torch.load("models/initial.pth")
        self.model = SignModel(784,25)
        self.model.load_state_dict(state_dict)
        self.model.eval()

    def preprocess_image(self, file, from_path = False):
        """ Preprocesses an image to be classified by the model. """
        
        if from_path:
            image = Image.open(file)
        else:
            image = Image.open(file.file)
            image.save('api/sign_png/postimage2.png')

        try:
            image = image.resize((28,28))
            image = image.convert('L')
        except:
            print("Error resizing image and converting to grayscale.")
            return None

        image_np = np.array(image, dtype=np.float32)
        image_np = image_np / 255.0
        image_np = image_np.reshape((784,1))
        image_tensor = torch.from_numpy(image_np).T
        
        return image_tensor

    def classify(self, images, from_path = False):

        tensors = torch.tensor([])

        for image in images:
            tensor = self.preprocess_image(image, from_path=from_path)
            if tensor is None:
                return None
            tensors = torch.cat((tensors, tensor), 0)    
        
        with torch.no_grad():
                outputs = self.model.forward(tensors)
                outputs = torch.exp(outputs)
                outputs = outputs.topk(1, dim=1).indices.flatten().tolist()
                # print(outputs.indices)
                # # outputs = [output[1].item() for output in outputs]
                
        return outputs


if __name__ == "__main__":

    model = APIModelHandler()
    classes = model.classify(["api/sign_png/sign_test_a.png"], from_path = True)
    print(classes)