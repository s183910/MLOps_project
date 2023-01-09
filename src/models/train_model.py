from model import SignModel
from torch import nn, optim, save, utils
from torchvision import transforms
from pelutils import log

from src.data import SignMNISTDataset


def train(lr: float, output_file: str, epochs: int = 2) -> None:
    """
    Trains the model using the provided learning rate and saves it.

        Parameters:
            lr (float): The learning rate as a float
            output_file (string): Path to the file where the trained model should be saved

        Args:
            epochs (int): number of epochs to train for (default 2)
    """
    log(f"Training with learning rate {lr}")

    log("Loading training set")
    trainset = SignMNISTDataset(
        csv_file="data/raw/sign_mnist_train.csv",
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
        ),
    )
    trainloader = utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    images, _ = next(iter(trainloader))
    model = SignModel(images.shape[1], 25)
    model.train()
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)

    for e in range(epochs):
        running_loss = 0
        for images, labels in trainloader:
            optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        else:
            log(f"Training finished with loss: {running_loss/len(trainloader)}")

    # output trained model state
    save(model.state_dict(), output_file)


if __name__ == "__main__":
    log.configure("train.log")
    with log.log_errors:
        train(0.001, "models/initial.pth")
