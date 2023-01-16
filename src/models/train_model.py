from model import SignModel
from torch import nn, optim, save, utils, jit
from torchvision import transforms
import hydra
from omegaconf import DictConfig
import logging
from src.data import SignMNISTDataset

import wandb


@hydra.main(version_base="1.3", config_path="conf/", config_name="config.yaml")
def train(cfg: DictConfig):

    logger = logging.getLogger(__name__)
    logger.info("Loading training set")

    wandb.init(
        project="Very awesome sign project",
        entity="mlops_14",
        config=cfg,
    )

    trainset = SignMNISTDataset(
        csv_file=cfg.data_folder.mnist_train,
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
    torch_script = jit.script(model)
    torch_script.save("models/initial_jit.pt")

    save(model.state_dict(), "models/initial.pth")


if __name__ == "__main__":
    train()
    # log.configure("train.log")
    # with log.log_errors:
    #     train(0.001, "models/initial.pth")
