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
