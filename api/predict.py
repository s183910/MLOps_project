import torch
from model import SignModel
import numpy as np
from PIL import Image

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
            image.save('api/test_images/postimage.png')

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

        alphabet = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y"}
        
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
                characters = [alphabet[output] for output in outputs]

        return characters


if __name__ == "__main__":

    model = APIModelHandler()
    classes = model.classify(["api/test_images/sign_test_a.png"], from_path = True)
    print(classes)