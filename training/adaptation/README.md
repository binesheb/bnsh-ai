# ARIV Adaptation and Teacher Learning

ARIV can learn from compatible existing models through explicit adaptation workflows.

## Supported concepts

### 1. Teacher-generated data

An external model can generate responses to a documented prompt set. ARIV can then train on the resulting examples.

```
Prompt set
   ↓
Teacher model
   ↓
Teacher responses
   ↓
Quality / safety filtering
   ↓
ARIV training data
   ↓
ARIV
```

### 2. Knowledge transfer / distillation

A compatible teacher can provide logits or other training signals when the architecture and tokenizer make this technically possible.

### 3. Parameter-efficient adaptation

External models can be used as a development teacher while ARIV is adapted using LoRA/PEFT or related techniques. This does not make the external model an ARIV model.

## Important boundary

"Learn from a model" does not mean automatically copying model weights or proprietary knowledge.

Each teacher must have documented:

- model identity and revision
- license / terms of use
- access method
- dataset generation method
- prompts or task distribution
- filtering and evaluation
- attribution requirements
- known limitations

Only information and outputs that may legally and technically be used for the intended training purpose should enter an ARIV release.

## Planned interfaces

```bash
bnsh teacher list
bnsh teacher register <model>
bnsh adapt generate --teacher <model> --dataset <dataset>
bnsh adapt evaluate --dataset <dataset>
bnsh adapt train --config <config>
```

The first implementation will use teacher-generated datasets because it works across heterogeneous model architectures.
