from torch import nn


def loadSimpleModel(input_size: int) -> nn.Module:
    """
    Load simple neural network with given input size.

    Parameters:
        input_size (int): input layer size
    """
    return nn.Sequential(
        nn.Linear(input_size, 256),
        nn.ReLU(),
        nn.Linear(256, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, 25),
        nn.LogSoftmax(dim=1),
    )
