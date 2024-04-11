# Iteration 13. Data centric approach around Mistral 7B

_11-04-2024_

## Goal

What is the highest LB score I can get with Mistral 7B?

## Motivation

Training with Mistral is much faster than training with Mixtral. And the leaderboard results are the same.

On this iteration I'm going to change the training data and try to get the best possible LB score.

This is a continuation of iterations 8 and 10, but focusing on Mistral and the data.

## Development

### Explore public datasets

| dataset                                             | n     | n_prompts | ratio | median_tokens |
|-----------------------------------------------------|-------|-----------|-------|---------------|
| dipamc77_prompts_0_500_wiki_first_para_3000_curated | 2872  | 494       | 0.17  | 215           |
| gemma_suppl_rewrite_curated                         | 298   | 189       | 0.63  | 171           |
| nbroad-v1_curated                                   | 2162  | 109       | 0.05  | 1120          |
| nbroad-v2_curated                                   | 2400  | 2400      | 1.00  | 1135          |
| winddude_70k_gemma_template_built_curated           | 69487 | 61947     | 0.89  | 666           |
| aishaalmahmoud/llm_dataset_1_curated                | 9842  | 839       | 0.09  | 197           |
| aishaalmahmoud/llm_dataset_20k_curated              | 16620 | 860       | 0.05  | 198           |
| alexxxsem/data_gemma_0_1000_curated                 | 994   | 41        | 0.04  | 174           |
| galileo/gemma_v1_7b-it_curated                      | 26160 | 1469      | 0.06  | 427           |
| newtonbaba/gemini_data_set_prompt_recover_3_curated | 1802  | 1778      | 0.99  | 198           |
| newtonbaba/gemma_data_set_prompt_recover_1_curated  | 994   | 766       | 0.77  | 418           |
| newtonbaba/gemma_data_set_prompt_recover_2_curated  | 1530  | 1530      | 1.00  | 604           |

- Except for `nbroad` the rest of the datasets have a reasonable number of tokens
- I'm going to train in all the datasets and see what is the leaderboard and validation score. If I group
  the datasets by creator that would be 8 experiments.

### Wandb

```python
os.environ['WANDB_PROJECT'] = 'datacentric_mistral'
os.environ['WANDB_NAME'] = experiment_name
```

I have learned that by setting [those environment variables](https://docs.wandb.ai/guides/track/environment-variables) I can control the project and name of the
training, thus making much easier to inspect data in [Weights and Bias](https://wandb.ai/guillermobarbadillo/datacentric_mistral?nw=nwuserguillermobarbadillo). It's a useful tool.

## Results

## Conclusion

## Next steps

## TODO

- [x] Is there any useful public dataset that I can use directly? Measure text length and prompt diversity.
- [ ] Collect useful prompts from other datasets
- [ ] Generate samples with multi-instruction prompts (similar to leaked data)
- [x] New notebook for sequential training
  - [x] Gain more control over wandb for easier inspection
  - [x] Increase batch size and maybe context length
