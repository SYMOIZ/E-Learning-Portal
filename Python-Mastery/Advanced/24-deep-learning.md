> **Level 3: Advanced** · Topic 24 of 40

[← Machine Learning](./23-machine-learning.md) · [↑ Level index](../README.md) · [NLP →](./25-nlp.md)

# Deep Learning

## Overview
- **What is it?** Deep learning trains layered differentiable functions with gradient-based optimization to learn representations from high-dimensional data.
- **Why is it important?** PyTorch makes tensors, modules, automatic differentiation, optimizers, devices, and data loaders explicit.
- **Where is it used?** It is used for vision, language, audio, recommendation, scientific modeling, and representation learning.

## Learning Objectives
- Construct PyTorch tensors and `nn.Module` models with correct shapes and devices.
- Implement training and evaluation loops with gradients enabled only where needed.
- Track validation metrics, checkpoints, numerical stability, and reproducibility.

## Real World Applications
- Image and text classification, sequence modeling, and embedding generation.
- Fine-tuning pretrained models on domain-specific labeled data.
- Learning nonlinear representations for ranking and forecasting.

## Core Concepts

### Tensors and Autograd
- **Definition:** A tensor carries multidimensional values and optional gradient history; backpropagation applies the chain rule through recorded operations.
- **Visual explanation:** `parameters → forward graph → scalar loss → backward gradients`
- **Practical example:**

```python
import torch

weight = torch.tensor(2.0, requires_grad=True)
loss = (weight * 3 - 10) ** 2
loss.backward()
print(weight.grad)
```

### Modules and Optimization
- **Definition:** `nn.Module` registers parameters and composes layers; an optimizer updates those parameters from gradients after each batch.
- **Visual explanation:** `batch → module forward → loss → zero_grad/backward/step`
- **Practical example:**

```python
import torch
from torch import nn

model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
inputs = torch.randn(16, 4)
targets = torch.randint(0, 2, (16,))
```

### Training and Evaluation Modes
- **Definition:** `train()` enables training behavior such as dropout, while `eval()` freezes that behavior; `torch.inference_mode()` disables autograd bookkeeping for inference.
- **Visual explanation:** `train batches → update parameters; validation batches → inference-only metrics`
- **Practical example:**

```python
model.eval()
with torch.inference_mode():
    logits = model(inputs)
    predictions = logits.argmax(dim=1)
model.train()
```

## Infographic Summary

| Infographic Block | Topic-specific takeaway |
| --- | --- |
| 📌 Concept | Deep learning trains layered differentiable functions with gradient-based optimization to learn representations from high-dimensional data. |
| ⚡ Purpose | PyTorch makes tensors, modules, automatic differentiation, optimizers, devices, and data loaders explicit. |
| 🔥 Benefits | Builds the ability to construct PyTorch tensors and `nn.Module` models with correct shapes and devices; it also helps practitioners implement training and evaluation loops with gradients enabled only where needed. |
| 🎯 Use Cases | Image and text classification, sequence modeling, and embedding generation. Fine-tuning pretrained models on domain-specific labeled data. |
| 🚀 Best Practices | Checkpoint model, optimizer, epoch, and metric state. |
| ❌ Common Mistakes | Ignoring the guardrail “Validate against a baseline before increasing model size”. |

## Syntax Guide

### Basic Syntax

```python
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor = torch.randn(32, 4, device=device)
```

### Standard Structure

```python
from torch import nn

class Classifier(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.network = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))

    def forward(self, inputs):
        return self.network(inputs)
```

### Code Pattern

```python
def train_step(model, optimizer, criterion, inputs, targets) -> float:
    model.train()
    optimizer.zero_grad(set_to_none=True)
    loss = criterion(model(inputs), targets)
    loss.backward()
    optimizer.step()
    return loss.item()
```

## Examples

### Beginner Example

```python
import torch

values = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
normalized = values / values.norm(dim=1, keepdim=True)
print(normalized)
```

### Intermediate Example

```python
import torch
from torch import nn

model = Classifier()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
inputs = torch.randn(8, 4)
targets = torch.randint(0, 2, (8,))
print(train_step(model, optimizer, criterion, inputs, targets))
```

### Advanced Example

```python
import torch

checkpoint = {
    "model": model.state_dict(),
    "optimizer": optimizer.state_dict(),
    "epoch": 4,
    "validation_loss": 0.31,
}
torch.save(checkpoint, "checkpoint.pt")
restored = torch.load("checkpoint.pt", map_location="cpu", weights_only=True)
model.load_state_dict(restored["model"])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Prepare batched tensors] --> B[Run forward pass]
    B --> C[Compute stable loss]
    C --> D[Backpropagate and update]
    D --> E[Evaluate and checkpoint]
    E -. feedback .-> A
```

---

[← Machine Learning](./23-machine-learning.md) · [↑ Level index](../README.md) · [NLP →](./25-nlp.md)
