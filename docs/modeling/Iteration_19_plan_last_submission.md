# Iteration 19. Plan the last submissions

_16-04-2024_

## Goal

Plan the last submissions to be as successful as possible.

## Motivation

Only two days for the end of the challenge, that means I have 10 submissions left. I'm far from the top
position but there might be a shakeup.

## Development

### Number of epochs

```
Mistral_v3 -> 450 steps, batch size 16 -> 7200 train samples, max steps 940 https://wandb.ai/guillermobarbadillo/huggingface/runs/ulrk5o38
Mixtral_v5 -> 114 steps, batch size 16 -> 1824 train samples, max steps 1520 https://wandb.ai/guillermobarbadillo/huggingface/runs/b8rxqez9
Mixtral-22b -> 450 steps, batch size 16 -> 7200 train samples, max steps 1000 https://wandb.ai/guillermobarbadillo/other_models/runs/kh0hr94u?nw=nwuserguillermobarbadillo
public datasets -> 50 steps, batch size 16 -> 800 train samples, max steps 250 https://wandb.ai/guillermobarbadillo/datacentric_mistral/runs/8sc27bj9?nw=nwuserguillermobarbadillo
```

The data above shows the effective batch size, I have found that when using accumulated gradients each step is every time the gradient is updated.

The number of steps is variable, from 50 to 450. I'm going to train for 500 steps. Later I will decide
which is the step used for submission.

### Training data

I believe the best possible training data would be:

- mooney_test_with_gpt4,
- gemma_suppl_rewrite_curated_with_gpt4,
- high_quality_dataset_v2-4 but removing duplicated prompts

This results in around 1k training samples, so the total train will be around 8 epochs.

### LoRA configuration

I'm going to use `r=1` because training and validation loss was almost the same as `r=16` and leaderboard score was successful.

### Models

These are my candidate models for the final ensemble:

- Mistral-7B
- Llama-13B
- Mistral-22B
- Mixtral-8x7B

I will train them all and later try to find the best possible combination.

### Submission planning

- The four models with one prediction each, using sampling. ¿Estimated submission time?
- The above with mean prompt
- The four models with more predictions each, using sampling
- A single model with the maximum predictions possible, mistral_v3 is a candidate for this, f.e. mistral_v3x10
- Same but with mean prompt
- Mistral_v3 with different number of prompts and mean prompt.
- A submission with each of the new models doing as much predictions as possible.

## Results

## Conclusion

## Next steps

## TODO

- [ ] How many predictions is the optimum to combine with the mean prompt? I believe infinite is the best if not using mean prompts. I know that 4 is better than 3 for Mixtral_v5
    - [ ] Submit a model with 
- [ ] Is it better to make a lot of submissions with Mistral, or to combine different models? Intuition says is to use different models.
