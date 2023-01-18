import torch
from app.model import SignModel
import numpy as np
from PIL import Image

class APIModelHandler:
    """ Used for preprocessing and classifying images POSTed to the API. """

    def __init__(self):
        state_dict = torch.load("app/initial.pth")
        self.model = SignModel(784,25)
        self.model.load_state_dict(state_dict)
        self.model.eval()

    def preprocess_image(self, file):
        """ Preprocesses an image to be classified by the model. """
        
        image = Image.open(file.file)

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

    def classify(self, images):

        alphabet = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y"}
        
        tensors = torch.tensor([])

        for image in images:
            tensor = self.preprocess_image(image)
            if tensor is None:
                return None
            tensors = torch.cat((tensors, tensor), 0)    
        
        with torch.no_grad():
                outputs = self.model.forward(tensors)
                outputs = torch.exp(outputs)
                outputs = outputs.topk(1, dim=1).indices.flatten().tolist()
                characters = [alphabet[output] for output in outputs]

        return characters


# if __name__ == "__main__":

#     model = APIModelHandler()
#     classes = model.classify(["test_images/sign_test_a.png"])
#     print(classes)