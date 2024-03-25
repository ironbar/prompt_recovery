# Iteration 4. Create new data

_25-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Create new data that could be used for evaluation or training.

## Motivation

When studying the leaked data I found difficult to guess the prompt that was used to rewrite the text. GPT4 is much better than me at that task (at least in english).

I'm going to use GPT4 to guess the prompts and that will enable me to:

1. Learn what it is the space of tasks that the hosts had in mind
2. Create a new dataset that hopefully is closer to the private test set

## Development

### Creation process

1. Play with ChatGPT to find the best prompt for the task.
2. Automatize the task using GPT4 API
3. Evaluate the quality of the recovered prompts on the `Supplementary-Rewritten-texts` dataset
4. Create a new set of rewritten texts using the recovered prompts

### Prompts for GPT4

I have found that GPT4 is more helpful than Mixtral, it follows the instructions much better.

```
Analyze the original and rewritten text and answer with the most likely text prompt that was given to rewrite or make stylistic changes to the original text.

- The text prompt should be a single sentence. Reply just with a short sentence and do not add any notes or comments.
- Sometimes the rewritten text will have hints about the text prompt. For example if it starts by
  Reworded, Rephrased, Translated, etc. you should include that word in the text prompt.
- Unless necessary do not make reference to details in the original text and keep the text prompt abstract and generic.

## Original text

{original_text}

## Rewritten text

{rewritten_text}

## Output format

Let's do the task step by step:

1. On a first step analyze the differences of the texts in less than 30 words.
2. On a second step write the most likely prompt using json format
```

The response of the prompt could be used later to fine-tune Mixtral to do some "chain of thought" response.

## Results

## Conclusion

## Next steps

## TODO

- [ ]
