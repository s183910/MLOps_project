from model import SignModel
from torch import nn, optim, save, utils
from torchvision import transforms
import hydra
from omegaconf import DictConfig
import logging
from src.data import SignMNISTDataset

# TODO: eval if this is how we integrate wandb or not??
import wandb

wandb.init(
    project="test-project",
    entity="mlops_14",
    config={"learning_rate": 0.01, "epochs": 5, "batch_size": 64, "dropout": 0.5},
)


@hydra.main(version_base="1.3", config_path="configs_kat/", config_name="defaults")
def train(cfg: DictConfig):

    logger = logging.getLogger(__name__)
    logger.info("Loading training set")

    trainset = SignMNISTDataset(
        csv_file=cfg.data.csv_file,
        transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize(0, 255)]),
    )
    trainloader = utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    images, _ = next(iter(trainloader))
    model = SignModel(images.shape[1], 25)

    wandb.watch(model, log_freq=100)

    model.train()
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=cfg.hyperparameters.lr)

    for e in range(cfg.hyperparameters.epochs):
        running_loss = 0
        for images, labels in trainloader:
            optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            wandb.log({"loss": loss})
        else:
            logger.info(
                f"Training finished for epoch no. {e} with loss: {running_loss/len(trainloader)}"
            )

    # output trained model state
    save(model.state_dict(), cfg.logger.output_file)


if __name__ == "__main__":
    train()
    # log.configure("train.log")
    # with log.log_errors:
    #     train(0.001, "models/initial.pth")
