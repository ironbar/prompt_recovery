# Iteration 15. Prompt tuning

_14-04-2024_

## Goal

Can I improve the LB score by using prompt tuning?

## Motivation

So far I have no seen leaderboard differences when using different models. I'm able to fine-tune them and learn the train data without any problem but it is hard to improve the LB score. One interesting thing is that I'm able to overfit on the train data using LoRA and just `r=1`.

Do I really need fine-tuning for this task? Maybe we can simply learn a good prompt and really on the power of the model to do the task. I believe it is unlikely that with the current scale of data (~1k) the model is going to learn a new task. Thus using the smallest amount possible of parameters could be better.

## Development

### How to do prompt fine-tuning

- [Fine-Tuning Models using Prompt-Tuning with Hugging Face’s PEFT Library](https://pub.towardsai.net/fine-tuning-models-using-prompt-tuning-with-hugging-faces-peft-library-998ae361ee27). This seems very similar to the LoRA fine-tuning.
- [Prompt tuning for causal language modeling, official Hugging Face](https://huggingface.co/docs/peft/main/en/task_guides/clm-prompt-tuning)
- [Prompt tuning official documentation](https://huggingface.co/docs/peft/en/package_reference/prompt_tuning)

### Experiment design

The idea is to take Mistral-7B and do prompt fine-tuning as similar as possible as fine-tuning. I will compare
the results to the previous iteration centered on data.

### Inference

It seems that load adapter does not work.

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[11], line 9
      7 print(f'Running inference for ({inference_conf})')
      8 model, tokenizer = load_model_and_tokenizer(inference_conf.base_model_name)
----> 9 load_adapters(model, inference_conf.adapter_paths)
     10 pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, pad_token_id=tokenizer.eos_token_id)
     11 parse_prompt = get_parse_prompt_func(inference_conf.parse_prompt_func_name)

Cell In[6], line 3, in load_adapters(model, adapter_paths)
      1 def load_adapters(model, adapter_paths):
      2     for path in set(adapter_paths):
----> 3         model.load_adapter(path, path)
      4     model.eval()

File /opt/conda/lib/python3.10/site-packages/transformers/integrations/peft.py:187, in PeftAdapterMixin.load_adapter(self, peft_model_id, adapter_name, revision, token, device_map, max_memory, offload_folder, offload_index, peft_config, adapter_state_dict, adapter_kwargs)
    180     peft_config = PeftConfig.from_pretrained(
    181         peft_model_id,
    182         token=token,
    183         **adapter_kwargs,
    184     )
    186 # Create and add fresh new adapters into the model.
--> 187 inject_adapter_in_model(peft_config, self, adapter_name)
    189 if not self._hf_peft_config_loaded:
    190     self._hf_peft_config_loaded = True

File /opt/conda/lib/python3.10/site-packages/peft/mapping.py:156, in inject_adapter_in_model(peft_config, model, adapter_name)
    142 r"""
    143 A simple API to create and inject adapter in-place into a model. Currently the API does not support prompt learning
    144 methods and adaption prompt. Make sure to have the correct `target_names` set in the `peft_config` object. The API
   (...)
    153         The name of the adapter to be injected, if not provided, the default adapter name is used ("default").
    154 """
    155 if peft_config.is_prompt_learning or peft_config.is_adaption_prompt:
--> 156     raise ValueError("`create_and_replace` does not support prompt learning and adaption prompt yet.")
    158 if peft_config.peft_type not in PEFT_TYPE_TO_TUNER_MAPPING.keys():
    159     raise ValueError(
    160         f"`inject_adapter_in_model` does not support {peft_config.peft_type} yet. Please use `get_peft_model`."
    161     )

ValueError: `create_and_replace` does not support prompt learning and adaption prompt yet.
```

## Results

### Shuffle the train dataset

When running multiple experiments with different learning rates and number of virtual tokens I have noticed
that the train loss of the different runs had a very similar pattern.

Thus I have realized that the training was not shuffling the data. So maybe I have to revisit previous
fine-tuning adding data shuffling.

The model trained with shuffled data consistently outperforms the other model.

## Conclusion

## Next steps

## TODO

- [ ]
