from __future__ import annotations

import torch
import torch.nn as nn


class SignModel(nn.Module):

    _hidden_layer_sizes = (256, 128, 64)

    def __init__(self, input_size: int, output_size: int):
        super().__init__()
        self._module = nn.Sequential(*self._build_layers(input_size, output_size))

    def forward(self, x: torch.FloatTensor) -> torch.FloatTensor:
        if x.ndim != 2:
            raise ValueError('Expected input to be a 2D Tensor')
        if x.shape[1] != self._module[0].in_features:
            raise ValueError(f'Expected input to be of size [batch_size, {self._module[0].in_features}]')
        return self._module(x)

    @classmethod
    def _build_layers(cls, input_size: int, output_size: int) -> list[nn.Module]:
        all_layers = (input_size, *cls._hidden_layer_sizes, output_size)
        layers = list()
        for i, (in_size, out_size) in enumerate(zip(all_layers[:-1], all_layers[1:])):
            layers.append(nn.Linear(in_size, out_size))
            if i < len(all_layers) - 2:
                layers.append(nn.ReLU())
                layers.append(nn.BatchNorm1d(out_size))
            else:
                layers.append(nn.LogSoftmax(dim=-1))
        return layers
