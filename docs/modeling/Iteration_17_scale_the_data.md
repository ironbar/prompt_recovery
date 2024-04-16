# Iteration 17. Scale the data

_15-04-2024_

## Goal

Can I improve the LB score simply by scaling the data?

## Motivation

This is the last idea I have: to take GPT4 and use to to scale the training data.

## Development

I'm going to divide the generation process into two steps:

1. Given prompt samples create new prompts
2. With those prompts create new training samples

I have generated 2k new training samples, with a cost of around 20$.

## Results

I get a LB score of `0.60`, worse than the best one which is `0.62`

## Conclusion

No improvement when scaling the data.
