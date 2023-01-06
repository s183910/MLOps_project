from torch import nn
import torch.functional as F

class Initial(nn.Module):
    def __init__(self):
        super().__init__()
        # Add input feature size
        self.fc1 = nn.Linear(None, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 64)
        self.fc4 = nn.Linear(64, 10)

        self.dropout = nn.Dropout(p=0.02)

    def forward(self, x):
        # make sure input tensor is flattened
        x = self.dropout(F.relu(self.fc1(x)))
        x = self.dropout(F.relu(self.fc2(x)))
        x = self.dropout(F.relu(self.fc3(x)))
        x = F.log_softmax(self.fc4(x), dim=1)

        return x