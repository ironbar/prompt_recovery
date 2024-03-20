# Iteration 1. Biggest model

_18-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

What is the biggest model that can be used to make a submission?

## Motivation

Scaling laws say that bigger models give better results. To be competitive we have to use the
biggest model available for the challenge.

## Development

### Candidates study

The most popular open-source models are: Mistral, Llama, Phi and Gemma.

Since we want to use the biggest model possible that excludes Phi. Phi-2 model has just
2.7B parameters and the biggest Gemma model is 7B parameters.

Mistral releases claim that the Mistral 7B model is better than Llama 2 13B model (and of course better than Llama 2 7B). If we trust those claims it won't have sense in using Llama 2 models.

![mistral_vs_llama](res/mistral_vs_llama.png)

Mixtral is the best model but it has 56B parameters, that will fit very tightly on 32GB of VRAM memory.
I have to test if I can make reliable predictions using Mixtral and wether I can fine-tune it.

![mixtral_table](res/mixtral_table.png)

Google claims that Gemma is better than Mistral and Llama 2. The differences between Mistral 7B and Gemma 7B
seem to be context dependent. In some contexts like math and code Gemma is better, on reasoning and real life
scenarios Mistral seems to be better.

![mixtral_is_the_best](res/mixtral_is_the_best.png)

If possible I should use Mixtral because it's the most powerful model available. If I'm unable to use
Mixtral then I should go with Mistral 7B or Gemma 7B.

Links:

- <https://mistral.ai/news/announcing-mistral-7b/>
- <https://mistral.ai/news/mixtral-of-experts/>
- <https://blog.google/technology/developers/gemma-open-models/>
- <https://www.ankursnewsletter.com/p/comparative-analysis-gemma-7b-vs>

### Prompt engineering with Gemma 2b

I have been playing with `Gemma 2b-it` because it is fast enough to be able to make predictions with it.

The problem is that **the model is pretty dumb**. Very frequently ignores the given instructions, so doing prompt engineering with the model is challenging.

One option could be to divide the task in two:

1. Create a list with the differences between the two texts
2. Given the list of the differences summarize the differences into a prompt

This is probably the chain of thought that a person will likely do to solve the problem.

## Results

### Which LLMs are fast enough to be used for inference?

The inference needs to run in less than 9 hours and there are around 1300 samples. Thus predictions should be faster than 24 seconds. The table below shows inference speed for one P4 gpu.

| LLM            | Tokens per second |
|----------------|-------------------|
| phi 2 3B q8    | 50                |
| Gemma 3B it    | 38                |
| Llama 2 7B q8  | 25                |
| mistral 7B q8  | 23                |
| Gemma 7B it q8 | 15                |

All the models above could be used for inference, in the worst case we could generate ~350 tokens
in the available time. They pytorch implementation of Gemma 7B is very slow at 2 tokens per second.
I had to search in HuggingFace for an alternative faster implementation.

Llama, Mistral, Gemma and phi are the most popular small LLM models. I don't believe I should make
a broader search.

### How the input and output length affects to the inference time?

The inference time is directly proportional to the output length. Pytorch implementation is not good
and does not stop after receiving and EOS token.

The input length has a much smaller effect on inference time. The input has to be very big to have
a noticeable effect on the inference time.

![input_length_vs_inference_time](res/input_length_vs_inference_time.png)

### Inference speed on local PC with 2X3090 GPU

Using [lmstudio](https://lmstudio.ai/) it's possible to try LLM models very easily.

TODO: add table with speed

The predictions use the 2 gpus at the same time but at 50% or less. There are different levels of quantization
provided by theBloke


## Conclusion

## Next steps

## TODO

- [x] Which LLMs are fast enough can be used for inference?
  - [x] LLama 2
  - [x] Mistral 7B
  - [x] Phi-2
  - [x] Gemma
- [x] Which speed can I get on my computer using lmstudio?
- [ ] Mixtral
  - [ ] Can I make reliable inference with it?
  - [ ] Can I fine-tune it?
  - [ ] https://www.kaggle.com/code/ashishkumarak/mixtral-moe-8x7b-instruct-inference-t4-2-gpu
  - [ ] [Fine-tune Mixtral-8x7B on Your Computer (QLoRA)](https://colab.research.google.com/drive/1VDa0lIfqiwm16hBlIlEaabGVTNB3dN1A?usp=sharing)
  - [ ] https://www.kaggle.com/models/mistral-ai/mixtral/frameworks/PyTorch/variations/8x7b-instruct-v0.1-hf/versions/1
- [ ] Which dataset was used to fine-tune Guanaco? On Qlora paper it is said that it was fine-tuned in less than one day
- [ ] How can I make a submission with a HuggingFace model?
- [ ] Which dataset I could use for validation?
- [ ] Set up a validation pipeline
- [ ] How much could I improve the evaluation speed if using a more powerful GPU?
- [ ] Which LLMs I can finetune and use for inference?
- [x] [Fine-tuning de grandes modelos de lenguaje con Manuel Romero | Hackathon Somos NLP 2023](https://www.youtube.com/watch?v=WYcJb8gYBZU) Está un poco anticuada porque es de hace un año pero la teoría está muy bien explicada.
- [ ] https://github.com/somosnlp/recursos/blob/main/hackathon_2024/entrenamiento_llm_instrucciones.ipynb
