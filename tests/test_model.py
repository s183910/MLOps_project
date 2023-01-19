import pytest
import torch

from src.models.model import SignModel


@torch.no_grad()
def test_model_input_output():
    model = SignModel(25)
    n = 10
    x = torch.randn(n, 3, 28, 28)
    y = model(x)
    assert y.shape[0] == n and y.shape[1] == 25


@torch.no_grad()
def test_error_wrong_dimensions():
    model = SignModel(25)
    x = torch.randn(1)
    match_string = r"Expected 3D .*"
    with pytest.raises(RuntimeError, match=match_string):
        model(x)


@torch.no_grad()
def test_error_wrong_shape():
    model = SignModel(25)
    batch_size = 10
    x = torch.randn(batch_size, 10)
    match_string = r"Expected 3D .*"
    with pytest.raises(RuntimeError, match=match_string):
        model(x)
