from typing import Callable, Tuple, Union

import numpy as np
import pandas as pd
import torch


class SignMNISTDataset(torch.utils.data.Dataset):
    """
    A class to represent the Sign MNIST Dataset.
    To be used with torch.utils.data.DataLoader

    Attributes:
        raw_signs (pandas.DataFrame): Raw data from csv loaded into a dataframe
        transform (Callable | nn.Module): callable transform to execute on raw data
    """

    def __init__(
        self, csv_file: str, transform: Union[Callable, torch.nn.Module] = None
    ) -> None:
        """
        Get data record at specified location.

        Parameters:
            index (int): location of record
            csv_file (string):

        Args:
            transform (Callable | nn.Module) = None : transforms to apply to the data on access

        Returns:
            :rtype:  None
        """
        self.raw_signs = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self) -> int:
        """
        Get length of dataset.

        Returns:
            :rtype:  int: number of records in dataset
        """
        return len(self.raw_signs)

    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Get data record at specified location.

        Parameters:
            index (int): location of record

        Returns:
            :rtype:  (Tensor, Tensor): images, labels as tuple
        """
        if torch.is_tensor(index):
            index = index.tolist()
        labels = self.raw_signs.iloc[index, 0]
        images = self.raw_signs.iloc[index, 1:]
        images = np.array([images])
        images = images.astype(np.float32)
        if self.transform:
            images = self.transform(images).reshape(-1)
        images = images.reshape(28, 28)
        images = torch.stack([images, images, images])
        return images, labels
