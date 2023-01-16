import logging
from pathlib import Path

import click
import torch
from dotenv import find_dotenv, load_dotenv
from model import SignModel
from torchvision import transforms

from src.data import SignMNISTDataset


@click.command()
@click.argument("input_filepath")
@click.argument("checkpoint")
def evaluate(input_filepath: str, checkpoint: str) -> None:
    """
    Loads model state from checkpoint and validates it. Prints the model accuracy.

    Parameters:
        checkpoint (string): saved model state (trained)

    Returns:
        :rtype: None
    """
    checkpoint = "models/trained_model.pth"
    logger = logging.getLogger(__name__)
    logger.info("Loading test set")
    testset = SignMNISTDataset(
        csv_file=input_filepath,
        transform=transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize(0, 255)]
        ),
    )
    testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)
    images, _ = next(iter(testloader))

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
            print(f"Accuracy: {accuracy.item()*100} %")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    evaluate()
