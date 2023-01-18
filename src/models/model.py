from __future__ import annotations

import torch
import torch.nn as nn
# from torchvision.models import resnet18, ResNet18_Weights


class SignModel(nn.Module):

    _hidden_layer_sizes = (256, 64)

    def __init__(self, input_size: int, output_size: int):
        super().__init__()
        # self._resnet = resnet18(ResNet18_Weights.DEFAULT)
        self._mobilenet = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
        # self._module = nn.Sequential(*self._build_layers(1000, output_size))
        self._module = nn.Linear(1000, output_size)

    def forward(self, x: torch.FloatTensor) -> torch.FloatTensor:
        x = self._mobilenet(x)
        return self._module(x)
