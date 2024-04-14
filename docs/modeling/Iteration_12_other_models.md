# Iteration 12. Fine-tuning Phi-2 and Gemma

_11-04-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Try fine-tuning and making predictions with [Phi-2](https://www.kaggle.com/models/Microsoft/phi/Transformers/2) and [Gemma-7b-it](https://www.kaggle.com/models/google/gemma/transformers/1.1-7b-it).

## Motivation

My experiments with Mistral, Mixtral and LLama 13b show tiny differences between the models. Maybe
I can get the same results using Phi-2 and Gemma-7b-it. If that is the case it is likely that an
ensemble using all the models would score better than making multiple submissions with the same model.

Also a new Mistral-22B model is out that it is worth trying.

## Development

The idea is to use the models in transformer format so I can reuse the code for fine-tuning previous models.
I would have to look at the different prompt format of the new models.

### Prompt format

#### Phi-2

<https://www.kaggle.com/models/Microsoft/phi/Transformers/2>

```
Instruct: Write a detailed analogy between mathematics and a lighthouse.
Output: Mathematics is like a lighthouse. Just as a lighthouse guides ships safely to shore, mathematics provides a guiding light in the world of numbers and logic. It helps us navigate through complex problems and find solutions. Just as a lighthouse emits a steady beam of light, mathematics provides a consistent framework for reasoning and problem-solving. It illuminates the path to understanding and helps us make sense of the world around us.
<|endoftext|>
```

#### Gemma

<https://www.promptingguide.ai/models/gemma>

```
<start_of_turn>user
knock knock<end_of_turn>
<start_of_turn>model
who is there<end_of_turn>
<start_of_turn>user
Gemma<end_of_turn>
<start_of_turn>model
Gemma who?<end_of_turn><eos>
```

#### Mistral-22B

https://huggingface.co/Vezora/Mistral-22B-v0.2

```
<s>### System: You are a helpful assistant.
### Human: Give me the best chili recipe you can
### Assistant: Here is the best chili recipe...</s>
```

## Results

| model        | LB score |
|--------------|----------|
| Mistral 7B   | 0.62     |
| Llama 2 13B  | 0.61     |
| Mistral 22B  | 0.62     |
| Mixtral 8x7B | 0.61     |

I haven't made a submission with Gemma or Phi because considering that all other models score almost the
same it is not promising and I have few submissions left.

## Conclusion

## Next steps

## TODO

- [ ]
