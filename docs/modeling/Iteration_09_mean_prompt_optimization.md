# Iteration 9. Mean prompt optimization

_05-04-2024_

## Goal

Try to find a mean prompt that scores as high as possible on leaderboard.

## Motivation

Yesterday a new mean prompt that scores 0.63 was released. I don't believe that is the way but I consider it is worth exploring it whenever I have unused submissions.

I remember reading news in the past that said that LLMs can be used for optimization.

## Development

### Optimizing with GPT4

The idea is to create a prompt with all the mean prompts and the score so far, and ask GPT4 to create new prompts.

```
I'm trying to find a text prompt that maximizes cosine similarity with a dataset of text prompts. The dataset has text prompts that have been used to rewrite text. Below you can find a table with all the prompts I have tried so far and the mean similarity. Could you use this information and suggest new prompts that could have a higher similarity?

Let's solve the problem step by step.

1. Analyze the higher scoring prompts and try to find insights and patterns that increase and decrease similarity
2. Using the insights suggest a single prompt that would score more than 0.63

| LB   | prompt                                                                                                        |
|------|---------------------------------------------------------------------------------------------------------------|
| 0.63 | Please improve this text using the writing style with maintaining the original meaning but altering the tone. |

```

It could be a conversation where I submit the suggestions and give the scores as feedback.

<https://chat.openai.com/c/83219e8b-db76-4763-9298-1bbee6dc1329>
<https://www.kaggle.com/code/ironbar/mean-prompt-submission>

## Results

<https://docs.google.com/spreadsheets/d/10MUcBnQporulcX5FZGhsQ7uWtT0WmlekX8NTT3fJNSc/edit#gid=1042558503&range=A1>

## Conclusion

## Next steps

## TODO

- [ ]
