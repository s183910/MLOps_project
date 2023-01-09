from torch import nn, utils, optim, save
import logging
from src.data import SignMNISTDataset
from model import SignModel
from torchvision import transforms


def train(lr, output_file):
    logger = logging.getLogger(__name__)
    logger.info(f"Training with learning rate ${lr}")

    logger.info("Loading training set")
    trainset = SignMNISTDataset(
        csv_file="data/raw/sign_mnist_train.csv",
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize(0, 255)]
        ),
    )
    trainloader = utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    images, _ = next(iter(trainloader))
    model = SignModel(images.shape[1], 25)
    model.train()
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)

    epochs = 2

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
            logger.info(
                f"Training finished with loss: ${running_loss/len(trainloader)}"
            )

    # output trained model state
    save(model.state_dict(), output_file)


if __name__ == "__main__":
    train(0.001, "models/initial.pth")
