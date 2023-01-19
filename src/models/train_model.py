import logging

import hydra
import torch.profiler as profiler
from model import SignModel
from omegaconf import DictConfig
from torch import jit, nn, optim, save, utils
from torchvision import transforms

import wandb
from src.data import SignMNISTDataset


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
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize(0, 255)]
        ),
    )
    trainloader = utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    images, _ = next(iter(trainloader))
    model = SignModel(images.shape[1], 25)

    wandb.watch(model, log_freq=100)

    model.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=cfg.hyperparameters.lr)

    with profiler.profile(
        activities=[profiler.ProfilerActivity.CPU],
        record_shapes=True,
        on_trace_ready=profiler.tensorboard_trace_handler(
            "./outputs/tensorprofilebrrr"
        ),
    ) as prof:
        for e in range(cfg.hyperparameters.epochs):
            logging.info("Epooch %i / %i" % (e + 1, cfg.hyperparameters.epochs))
            running_loss = 0
            for i, (images, labels) in enumerate(trainloader):
                logging.debug("Batch %i / %i" % (i + 1, len(trainloader)))
                optimizer.zero_grad()
                logits = model(images)
                loss = criterion(logits, labels)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()
                wandb.log({"loss": loss})
                prof.step()
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
