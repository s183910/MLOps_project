import os

import pytest
from torch import utils
from torchvision import transforms

from src.data import SignMNISTDataset
from tests import PATH_DATA


def load_dataset(path, n):
    dataset = SignMNISTDataset(csv_file=path, transform=transforms.ToTensor())
    dataloader = utils.data.DataLoader(dataset)
    assert (
        len(dataset) == n
    ), f"Dataset did not have the correct number of samples: {len(dataset)} != {n}"
    images, labels = next(iter(dataloader))
    image_shape_error = f"Data feature set: expected shape {(n, 3, 28, 28)}, but got shape {images.shape}"
    label_shape_error = (
        f"Data label set: expected shape {(1,)}, but got shape {labels.shape}"
    )
    assert tuple(images.shape) == (1, 3, 28, 28), image_shape_error
    assert tuple(labels.shape) == (1,), label_shape_error


@pytest.mark.skipif(
    not os.path.exists(os.path.join(PATH_DATA, "raw/sign_mnist_train.csv")),
    reason="Data files not found (training)",
)
def test_load_training_dataset():
    path = os.path.join(PATH_DATA, "raw/sign_mnist_train.csv")
    N_train = 27455
    load_dataset(path, N_train)


@pytest.mark.skipif(
    not os.path.exists(os.path.join(PATH_DATA, "raw/sign_mnist_test.csv")),
    reason="Data files not found (testing)",
)
def test_load_test_dataset():
    path = os.path.join(PATH_DATA, "raw/sign_mnist_test.csv")
    N_test = 7172
    load_dataset(path, N_test)


@pytest.mark.skipif(
    not os.path.exists(os.path.join(PATH_DATA, "raw/sign_mnist_test.csv")),
    reason="Data files not found (testing)",
)
def test_batched_data_loader():
    path = os.path.join(PATH_DATA, "raw/sign_mnist_test.csv")
    dataset = SignMNISTDataset(csv_file=path, transform=transforms.ToTensor())
    batch_size = 64
    dataloader = utils.data.DataLoader(dataset, batch_size=batch_size)
    images, labels = next(iter(dataloader))
    expected_shape = (batch_size, 3, 28, 28)
    image_shape_error = f"Data feature set: expected shape {expected_shape}, but got shape {images.shape}"
    label_shape_error = (
        f"Data feature set: expected shape [{batch_size}], but got shape {labels.shape}"
    )
    assert images.shape == expected_shape, image_shape_error
    assert labels.shape == (batch_size,), label_shape_error
