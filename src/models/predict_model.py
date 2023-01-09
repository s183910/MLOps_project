import torch
from torchvision import transforms
import logging
from model import SignModel
from src.data import SignMNISTDataset


def evaluate(checkpoint):
    """
    Loads model state from checkpoint and validates it. Prints the model accuracy.

    Parameters:
        checkpoint (string): saved model state (trained)
    """
    logger = logging.getLogger(__name__)
    logger.info('Loading test set')
    testset = SignMNISTDataset(csv_file='data/raw/sign_mnist_test.csv', transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize(0, 255)]))
    testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)
    images, _  = next(iter(testloader))

    state_dict = torch.load(checkpoint)
    model = SignModel(images.shape[1], 25)
    model.load_state_dict(state_dict)

    accuracy = 0
    results = []
    with torch.no_grad():
        model.eval()
        for images, labels in testloader:
            # Get most likely class identifier
            _, p_class = torch.exp(model(images)).topk(1, dim=1)
            # Get where labels and predicitons differ
            equals = p_class == labels.view(*p_class.shape)
            results.append(equals.type(torch.FloatTensor).reshape(-1))
        else:
            accuracy = torch.mean(torch.concat(results))
            print(f"Accuracy: {accuracy.item()*100}%")


if __name__ == "__main__":
    evaluate("models/initial.pth")
