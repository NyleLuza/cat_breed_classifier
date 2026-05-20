import torch
import torch.nn as nn
import torch.nn.functional as F
# defining network

class Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(1,20,5)
        self.conv2 - nn.Conv2d(20,20,5)