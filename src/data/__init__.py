import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


class SignMNISTDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.raw_signs = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.raw_signs)

    def __getitem__(self, index):
        if torch.is_tensor(index):
            index = index.tolist()
        labels = self.raw_signs.iloc[index, 0]
        images = self.raw_signs.iloc[index, 1:]
        images = np.array([images])
        images = images.astype(np.float32)
        if self.transform:
            images = self.transform(images).reshape(-1)
        return images, labels
