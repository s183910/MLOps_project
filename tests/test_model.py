import pytest
import torch

from src.models.model import SignModel


@torch.no_grad()
def test_model_input_output():
    model = SignModel(28 * 28, 25)
    n = 10
    x = torch.randn(n, 28 * 28)
    y = model(x)
    assert y.shape[0] == n and y.shape[1] == 25
    assert (y <= 0).all()


@torch.no_grad()
def test_error_wrong_dimensions():
    model = SignModel(28 * 28, 25)
    x = torch.randn(1)
    matchString = "Expected input to be a 2D Tensor"
    with pytest.raises(ValueError, match=matchString):
        model(x)


@torch.no_grad()
def test_error_wrong_shape():
    model = SignModel(28 * 28, 25)
    batch_size = 10
    x = torch.randn(batch_size, 10)
    matchString = r"Expected input to be of size \[batch_size, .*"
    with pytest.raises(ValueError, match=matchString):
        model(x)
