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

### First trainings on new data

| version | loss        | output type | data                                                                                        | LB score |
|---------|-------------|-------------|---------------------------------------------------------------------------------------------|----------|
| 1       | Full        | CoT         | 1/2 mooney_test_with_gpt4                                                                   | 0.61     |
| 2       | Full        | CoT         | mooney_test_with_gpt4                                                                       | 0.61     |
| 3       | Completions | CoT         | mooney_test_with_gpt4                                                                       | 0.61     |
| 4       | Completions | Prompt      | high_quality_dataset_v1                                                                     | 0.59     |
| 5       | Completions | Prompt      | high_quality_dataset_v1,<br>mooney_test_with_gpt4                                           | **0.62** |
| 6       | Completions | Prompt      | high_quality_dataset_v1,<br>mooney_test_with_gpt4,<br>gemma_suppl_rewrite_curated_with_gpt4 | 0.61     |

- v5 model reaches the best LB score so far for any individual model (without any mean prompt combination)
- This probes that chain of thought (CoT) prompts were not necessary. It seemed like a good idea, but in hindsight
  we were just saying the same in the thoughts and in the prompt.
- It might be possible that we need more that if we train on completions and just prompts, because the number of tokens
  that are used for training is much smaller.

### Submission with multiprompt

Since the model is just predicting a short prompt the submission is much faster. It runs in less than 3 hours.
Thus it is possible to make more than one prediction for each sample and concatenate all together.

| model version | single prompt LB score | multiprompt LB score |
|---------------|------------------------|----------------------|
| 4             | 0.59                   | 0.61                 |
| 5             | 0.62                   | 0.64                 |
| 6             | 0.61                   | 0.62                 |

All the experiments improve when making multiple predictions. 0.64 is the best result so far with a single model.
This could be a way, but I'm far from 0.70.

### Do not quantize Mixtral gates

I have read that quantizing Mixtral gates could be problematic. Thus I have created a notebook to see if I can avoid that quantization.

If we don't quantize the gates and the lm_head of Mixtral the memory usage is almost the same since they are small layers.

Just add `llm_int8_skip_modules=['gate', 'lm_head'],` to the configuration.

References:

- <https://huggingface.co/docs/transformers/main_classes/quantization#transformers.QuantoConfig.modules_to_not_convert>
- <https://github.com/mobiusml/hqq/issues/2>

To see the effect of this change I have launched two experiments:

1. Fine-tune a model without quantizing those layers
2. Resubmit the fork from the forum where I replaced Mistral by Mixtral.

The results on leaderboard do not change. The fine-tuned model gets 0.61 and the fork gets 0.62, exactly as before.

### What if I fine-tune Mistral?

Validation loss during training is slightly higher: 0.7679 vs 0.7456

https://www.kaggle.com/datasets/ahmadsaladin/mistral-7b-it-v02

However in LB score I get exactly the same score as Mixtral: 0.61

This is the second evidence against the use of Mixtral, the first one was the [forum notebook](https://www.kaggle.com/code/ironbar/mixtral-prompt-predict-fork?scriptVersionId=171120108) where I simply replaced Mistral
by Mixtral and got the same score.

## Conclusion

## Next steps

- [ ] Try using LLama 2 13B, https://www.kaggle.com/models/metaresearch/llama-2/pyTorch/13b-chat-hf
- [ ] Why Mixtral is not getting better results than Mistral?

## TODO

- [x] What if MoE does not deal correctly with quantization and should I leave some layers as they are?
- [x] What if I make multiple predictions with the same model and concatenate them?
  - [ ] Or with different adapters?
- [ ] Upload new models to: <https://www.kaggle.com/models/ironbar/mixtral-prompt-recovery>
- [x] Create new data with Newtonbaba? The prompts didn't look right
- [ ] Evaluate new dataset
- [ ] New data with multiple prompt instructions.
- [x] What if I fine-tune Mistral instead of Mixtral?
