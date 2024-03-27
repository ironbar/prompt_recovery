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

My hypothesis is that I'm using PAD token equal to EOS token. I believe it does not give attention weight
to the EOS token and that results in the problem.

The solution would be to add a new pad token, or to use the unknown token as pad.

## Results

I have learned to fine-tune Mixtral, but what data should I train on?

## Conclusion

## Next steps

- Try different combinations of output data and styles

## TODO

- [ ]
