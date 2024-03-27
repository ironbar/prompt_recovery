# Iteration 5. Mixtral fine-tuning

_26-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Learn how to fine-tune Mixtral and make predictions with a fine-tuned model.

## Motivation

Learning to fine-tune LLM was one of the motivations of joining the challenge. On this iteration I just
want to verify that I can fine-tune and make inference with fine-tuned Mixtral. On later iterations I
will try with different data, on this iteration I just want to learn to fine-tune.

As train data I will use the supplementary material labelled with GPT4 that was created on the previous iteration.

## Development

### System prompt

Maybe if we give some information previously to the `[INST]` prompt that would be equivalent
to the system prompt in ChatGPT. Seen on this [dataset](https://huggingface.co/datasets/gathnex/Gath_baize?row=0)

However in this other thread they use multi-turn conversation instead: <https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/discussions/41>

### Generation not ending after fine-tuning

First trainings seemed to learn the format of the output, but did not know how to end. F.e.

```
 1. The rewritten text changes the description of the zither's design and the emotional impact on Amy.
2. {"prompt": "Rewrite the text to emphasize the design of the zither and its emotional impact."} ➔ json prompt format

 1. The rewritten text changes the subject from a peony to a parser and the action from blooming to parsing.
2. {"prompt": "Rewrite the text with a different subject and action."} ➔ [/Note] Note: The prompt is in JSON format to ensure consistency and make it easier to extract the prompt in automated processes.
```

Notice how it generates a json output, but does not stop the generation.

After reading and experiment I have found that the problem was relating to using PAD token equal to EOS token.
It seems that it does not give attention weight to the EOS token and that creates the problem.

I believe the best solution is to create a pad token. Since it will be just used for fine-tuning
and the attention weight will be zero we can use the model for inference without any change (with the original token embeddings).

```python
# initial trains
tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True)
tokenizer.pad_token_id = tokenizer.eos_token_id
tokenizer.pad_token = tokenizer.eos_token

# solution
tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True)
tokenizer.add_special_tokens({'pad_token': '<pad>'})
model.resize_token_embeddings(len(tokenizer))
```

References:

- <https://discuss.huggingface.co/t/how-to-train-the-embedding-of-special-token/10837/2>
- <https://www.reddit.com/r/LocalLLaMA/comments/184g120/mistral_fine_tuning_eos_and_padding/>
- <https://stackoverflow.com/questions/76633368/how-does-one-set-the-pad-token-correctly-not-to-eos-during-fine-tuning-to-avoi>

### Doubts about padding position

What is the default padding position of the tokenizer? **Left**

For generation padding left should be applied, otherwise we will have pad tokens between the input and the generated tokens. However for training padding right might be a better choice since we are not going to generate new text.

```python
# original tokens
[1, 2, 3]
# padding left, the right choice for inference
[0, 0, 1, 2, 3]
# padding right, maybe a better choice for training
[1, 2, 3, 0, 0]
```

When I train with right padding the train and validation loss are slightly smaller, so I believe it
has sense to use that setting for training.

References:

- <https://ai.stackexchange.com/questions/41485/while-fine-tuning-a-decoder-only-llm-like-llama-on-chat-dataset-what-kind-of-pa>
- <https://discuss.pytorch.org/t/right-vs-left-padding/185050/4>
- <https://github.com/huggingface/trl/issues/1217#issuecomment-1889384774>
- <https://github.com/tloen/alpaca-lora/issues/514>

### Creating a new model on Kaggle

I have to upload the lora weights to Kaggle so I can make submissions. Ideally I would create a private
model with different versions and I could release it once the competition is over.

What are the minimal files required? There are many files saved in the checkpoint folder.

<https://www.kaggle.com/models/ironbar/mixtral-prompt-recovery>

It is enough with two files:

```
v1
├── adapter_config.json
└── adapter_model.safetensors
```

## Results

I have learned to fine-tune Mixtral, but what data should I train on?

## Conclusion

## Next steps

- Try different combinations of output data and styles

## TODO

- [ ]
