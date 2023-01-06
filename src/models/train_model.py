import torch
from torch import nn
import logging
import data
from model import Initial

def train(lr, output_file):
    logger = logging.getLogger(__name__)
    logger.info(f'Training with learning rate ${lr}')

    model = Initial()
    model.train()
    criterion = nn.NLLLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    training_set = data.load_train_set()

    running_loss = 0

    for images, labels in training_set:
        optimizer.zero_grad()
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    else:
        logger.info(f"Training finished with loss: ${running_loss/len(training_set)}")

    # output trained model state
    torch.save(model.state_dict(), output_file)


if __name__ == "__main__":
    train(0.001, 'models/initial.pth')