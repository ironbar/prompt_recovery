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

## Results

TODO: make a submission with each model trained on the same data and create a comparison table of LB score

## Conclusion

## Next steps

## TODO

- [ ]
