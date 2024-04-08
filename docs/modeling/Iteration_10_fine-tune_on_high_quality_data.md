# Iteration 10. Fine-tune on high quality data

_08-04-2024_

## Goal

Can I improve my leaderboard score using the recently create high quality data?

## Motivation

I believe I have to forget about mean-prompts and bad T5 embeddings and simply focus on building
the best model possible for prompt recovery.

It's time to see if the newly created dataset gives better results than previous fine-tunings.

## Development

## Results

### Train just on completions

On a first step I have done a first experiment using previous data were the model was trained [just on completions](https://huggingface.co/docs/trl/en/sft_trainer#train-on-completions-only).
This means that the model will only be trained on the recovery prompts, not on generating the original and rewritten text.

| ground truth          | base model | v1     | v2     | v3, just on completions |
|-----------------------|------------|--------|--------|-------------------------|
| gemma prompt          | 0.6742     | 0.7095 | 0.7062 | **0.716**               |
| gpt4 recovered prompt | 0.7005     | 0.8108 | 0.8126 | **0.8245**              |
| LB                    | -          | 0.61   | 0.61   | 0.61                    |

We can see an improvement in validation, but do not see improvements on leaderboard.

The training dynamics were changed and the model overfitted earlier. This is very likely due to the
training output being shorter. On previous fine-tunings the best validation epoch was around 15, while on this 
training it was around 6.

Thus we see an improvement on validation score and also the trainings are faster because the best epoch
is achieved faster.

## Conclusion

## Next steps

## TODO

- [ ] What if MoE does not deal correctly with quantization and should I leave some layers as they are?
  - [ ] https://github.com/mobiusml/hqq/issues/2
  - [ ] https://github.com/vllm-project/vllm/issues/2243
  - [ ] I could try this on the forum fork
- [ ] What if I make multiple predictions with the same model and concatenate them? Or with different adapters?
