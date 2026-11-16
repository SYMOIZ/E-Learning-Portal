# ML Inference Service

[← Project catalog](./README.md) · [Machine Learning](../Advanced/23-machine-learning.md)

**Level:** Advanced  
**Lessons:** NumPy or a small model, API serving, monitoring, versioning

## Problem

A product team wants a local inference endpoint that scores a fixed feature vector and reports which model version produced the score.

## Non-goals

- No training on private personal data.
- No claim of production accuracy without an evaluation set.

## Requirements

- Pin the model artifact or a deterministic baseline function to a version string.
- Reject the wrong number of features before scoring.
- Return the score, the version, and the elapsed time in milliseconds.
- Keep a tiny offline evaluation that prints accuracy or error on a fixture.

## Starter

```python
MODEL_VERSION = "baseline-1"


def score(features):
    if len(features) != 2:
        raise ValueError("expected 2 features")
    weight_sum = features[0] * 0.2 + features[1] * 0.8
    return {"score": weight_sum, "model_version": MODEL_VERSION}


def main():
    print(score([1.0, 2.0]))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- Two calls with the same features and version return the same score.
- A short feature list raises `ValueError`.
- The response includes `model_version`.
- The README states what the baseline does and does not predict.

## Extension

Log latency without logging raw feature payloads that could be sensitive.
