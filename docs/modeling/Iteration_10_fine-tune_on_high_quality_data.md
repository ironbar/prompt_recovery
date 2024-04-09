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
| 5             | 0.62                   | ?                    |
| 6             | 0.61                   | 0.62                 |

The two experiments run so far show an improvement when making multiple predictions.

## Conclusion

## Next steps

## TODO

- [ ] What if MoE does not deal correctly with quantization and should I leave some layers as they are?
  - [ ] https://github.com/mobiusml/hqq/issues/2
  - [ ] https://github.com/vllm-project/vllm/issues/2243
  - [ ] I could try this on the forum fork
  - [ ] Here we see again the Mixtral gates suggestion, although it is not the bit and bytes config.
  - [ ] https://huggingface.co/docs/transformers/main_classes/quantization#transformers.QuantoConfig.modules_to_not_convert
  - [ ] https://huggingface.co/docs/transformers/main_classes/quantization#transformers.BitsAndBytesConfig
  - [ ] llm_int8_skip_modules might be used
- [x] What if I make multiple predictions with the same model and concatenate them?
- [ ] Or with different adapters?
- <https://www.kaggle.com/models/ironbar/mixtral-prompt-recovery>
- [ ] Create new data with Newtonbaba?
- [ ] Evaluate new dataset
- [ ] New data with multiple prompt instructions.

