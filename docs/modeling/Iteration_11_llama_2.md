# Iteration 11. Llama 2

_10-04-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Can we get better results if we switch from Mistral to Llama 2?

## Motivation

My initial model choice for the challenge was to use Mixtral because it was the
biggest and most capable model that could be used to make a submission for the challenge.

However I haven't found evidences that Mixtral is better than Mistral for this challenge. Two different
experiments gave the same results to Mistral 7B and Mixtral 8x7B. Maybe the

Thus I have decided to try with LLama 2 13b chat because it might give better results.

## Development

### Problem when running quantized Llama

After quantization I get

```
RuntimeError: mat1 and mat2 shapes cannot be multiplied (28x5120 and 1x6912)
```

If I change `"pretraining_tp": 2` to `"pretraining_tp": 1` in the `config.json` it works!
A simpler solution is to do `model.config.pretraining_tp = 1` after loading the model.

Reference: <https://discuss.huggingface.co/t/llama2-finetuning-giving-error-mat1-and-mat2-shapes-cannot-be-multiplied-4096x5120-and-1x2560/47466/7>

### Llama 2 references

The [prompt format](https://huggingface.co/blog/llama2#how-to-prompt-llama-2) is very similar to Mistral, with the addition of the system prompt.

For one way conversations:

```
<s>[INST] <<SYS>>
{{ system_prompt }}
<</SYS>>

{{ user_message }} [/INST]
```

For multi-turn conversations:

```
<s>[INST] <<SYS>>
{{ system_prompt }}
<</SYS>>

{{ user_msg_1 }} [/INST] {{ model_answer_1 }} </s><s>[INST] {{ user_msg_2 }} [/INST]

```

- <https://www.kaggle.com/models/metaresearch/llama-2/PyTorch/13b-chat-hf>
- <https://replicate.com/blog/how-to-prompt-llama>
- <https://huggingface.co/docs/transformers/en/model_doc/llama2>

## Results

### Forum notebook for with Llama

[Notebook](https://www.kaggle.com/code/ironbar/llama-13b-prompt-predict-fork?scriptVersionId=171288400)

I get the same 0.62 score as with Mistral and Mixtral, so it seems that the model is not relevant?

### Fine-tune Llama

Let's fine-tune Llama and compare to Mistral and Mixtral.

I would like to do 2 trainings, one with sys prompt and another without. My guess is that the results will be very similar.

The LB score is 0.61, same as Mixtral but lower than Mistral (0.62) althought the differences are not
likely to be significative.

I have started training with system prompt, but after 200 steps the loss was almost identical to using Mistral prompt
so I have decided to stop the training.

#### Fine-tuning parameters

https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing

This example uses a learning rate of 2e-4, which is 10 times bigger than 2e-5 used for Mixtral.

https://colab.research.google.com/drive/1SYpgFpcmtIUzdE7pxqknrM4ArCASfkFQ?usp=sharing

This other example uses a learning rate of 1e-4.

The validation result is the same with a learning rate of 2e-5 and 4e-5.

## Conclusion

## Next steps

- Other models
    - https://www.databricks.com/blog/mpt-30b
    - Falcon 40b
    - Gemma 7b https://www.kaggle.com/models/google/gemma/transformers/1.1-7b-it
    - Phi-2. https://www.kaggle.com/models/Microsoft/phi/Transformers/2
- I might the tune the lora hyperparameters, but maybe on Mistral 7B to be faster.
- Create a python training script so I can run multiple trainings at night

## TODO

- [ ]
