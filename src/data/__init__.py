import logging
from torch.utils.data import Dataset
import torch
import pandas as pd
import numpy as np

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
        images = images.astype('float')
        if self.transform:
            images = self.transform(images).reshape(-1)        
        return (images, labels)

