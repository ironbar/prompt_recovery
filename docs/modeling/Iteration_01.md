# Iteration 1. Prompt engineering

_07-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Explore how far we can go using prompt engineering

## Development

### Prompt engineering

I have been playing with `Gemma 2b-it` because it is fast enough to be able to make predictions with it.

The problem is that the model is pretty dumb. Very frequently ignores the given instructions, so doing prompt engineering with the model is challenging.

One option could be to divide the task in two:

1. Create a list with the differences between the two texts
2. Given the list of the differences summarize the differences into a prompt

This is probably the chain of thought that a person will likely do to solve the problem.

## Results

### Which LLMs are fast enough to be used for inference?

The inference needs to run in less than 9 hours and there are around 1300 samples. Thus predictions should be faster than 24 seconds.

| model             | inference time (s) |
|-------------------|--------------------|
| Gemma 2b-it       | 2.6                |
| Gemma 7b-it-quant | 40                 |

### How the input and output length affects to the inference time?

The inference time is directly proportional to the output length. Pytorch implementation is not good
and does not stop after receiving and EOS token.

The input length has a much smaller effect on inference time. The input has to be very big to have
a noticeable effect on the inference time.

![input_length_vs_inference_time](res/input_length_vs_inference_time.png)

### Inference speed on local PC with 2X3090 GPU

Using [lmstudio](https://lmstudio.ai/) it's possible to try LLM models very easily.

```raw numbers
openhermes 2 5 mistral q8
75.5 token/s

phi 2 3B q8
131 token/s on GPU

Llama 2 7B q8
76 token/s
```

The predictions use the 2 gpus at the same time but at 50% or less. There are different levels of quantization
provided by theBloke

¿GGUF models? Search about the format

## Next steps

## TODO

- [ ] Which LLMs are fast enough can be used for inference?
  - [ ] LLama 2
  - [ ] Mistral 7B
  - [ ] Phi-2
  - [ ] Gemma
  - [ ] DeciLM-7B
- [ ] Which dataset I could use for validation?
- [ ] Set up a validation pipeline
- [ ] How much could I improve the evaluation speed if using a more powerful GPU?
- [ ] Which LLMs I can finetune and use for inference?
- [ ] Which speed can I get on my computer using lmstudio?
