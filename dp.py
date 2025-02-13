import torch.nn as nn
import torch

# Definisi arsitektur CNN Siamese Network
class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(64, 128, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.fc = nn.Sequential(
            nn.Linear(128*56*56, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, input1, input2):
        out1 = self.cnn(input1)
        out2 = self.cnn(input2)
        diff = torch.abs(out1 - out2)  # Selisih fitur
        output = self.fc(diff.view(diff.shape[0], -1))
        return output

# Model siap digunakan untuk membandingkan dua gambar
model = SiameseNetwork()
