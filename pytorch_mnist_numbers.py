# This code defines a simple convolutional neural network for classifying MNIST digits, sets up data loaders, defines
# training and testing loops, and runs the training and testing process for a number of epochs. It uses PyTorch's
# neural network, optimization, and data loading modules.

# Import necessary modules from PyTorch and torchvision
from torch import cuda, device, no_grad, utils, __version__ as torch_version
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, __version__ as torchvision_version


# Define a neural network class inheriting from nn.Module
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Define first convolutional layer
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        # Define second convolutional layer
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        # Define first fully connected layer
        self.fc1 = nn.Linear(320, 50)
        # Define second fully connected layer
        self.fc2 = nn.Linear(50, 10)

    # Define the forward pass of the network
    def forward(self, x):
        # Apply first convolution, ReLU activation, and max pooling
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        # Apply second convolution, ReLU activation, and max pooling
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        # Flatten the output for the fully connected layers
        x = x.view(-1, 320)
        # Apply first fully connected layer with ReLU activation
        x = F.relu(self.fc1(x))
        # Apply second fully connected layer
        x = self.fc2(x)
        # Apply log-softmax to the output
        return F.log_softmax(x, dim=1)


# Set up data loaders for training and testing using the MNIST dataset
train_loader = utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=64, shuffle=True)

test_loader = utils.data.DataLoader(
    datasets.MNIST('../data', train=False, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])),
    batch_size=1000, shuffle=True)

# Initialize the neural network model
model = Net()
# Set up the optimizer, using stochastic gradient descent
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


# Define the training loop
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} '
                  f'({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}')


# Define the testing loop
def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print(f'\nTest set: Average loss: {test_loss:.4f}, '
          f'Accuracy: {correct}/{len(test_loader.dataset)} ({100. * correct / len(test_loader.dataset):.0f}%)\n')

# Basic information
print("This is an experimnental Hello World using ROCm.")

# Print the versions of torch and torchvision
print(f"\tPyTorch Version: {torch_version}")
print(f"\tTorchvision Version: {torchvision_version}")

# Check if CUDA is available and set the device accordingly
device = device("cuda" if cuda.is_available() else "cpu")
print(f"\tUsing [cpu|cuda]: {device}")
model.to(device)

# Check which actual device being utilized
gpu_name = cuda.get_device_name(0)
print(f"\tUsing device: {gpu_name}")

# Check how many devices are available
devices_available = cuda.device_count()
print(f"\tDevices Available {devices_available}")

# Run the training and testing for a number of epochs
for epoch in range(1, 10):
    train(model, device, train_loader, optimizer, epoch)
    test(model, device, test_loader)
