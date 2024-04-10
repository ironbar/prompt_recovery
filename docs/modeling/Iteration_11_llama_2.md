# Iteration 11. Llama 2

_10-04-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Can we get better results if we switch from Mistral to Llama 2?

## Motivation

My initial model choice for the challenge was to use Mixtral because it was the
biggest and most capable model that could make a submission for the challenge.

However I have no found evidences that Mixtral is better than Mistral for this challenge.

Thus I have decided to try with LLama 2 13b chat because it might give better results.

## Development

### Problem when running quantized Llama

After quantization I get

```
RuntimeError: mat1 and mat2 shapes cannot be multiplied (28x5120 and 1x6912)
```

If I change `"pretraining_tp": 2` to `"pretraining_tp": 1` in the `config.json` it works!
A simpler solution is to do `model.config.pretraining_tp = 1` after loading the model.

Reference: <https://discuss.huggingface.co/t/llama2-finetuning-giving-error-mat1-and-mat2-shapes-cannot-be-multiplied-4096x5120-and-1x2560/47466/7>

## Results

### Forum notebook for with Llama

TODO

### Fine-tune Llama

Let's fine-tune Llama and compare to Mistral and Mixtral.

I would like to do 2 trainings, one with sys prompt and another without. My guess is that the results will be very similar.

## Conclusion

## Next steps

## TODO

- [ ]
