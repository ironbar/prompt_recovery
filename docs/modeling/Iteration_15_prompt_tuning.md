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

It seems that load adapter does not work. I have to use the `PEFTModel` and created a [new notebook](https://www.kaggle.com/code/ironbar/autobots-prompt-tuning?scriptVersionId=172066440) to make this submissions.

## Results

### Shuffle the train dataset

When running multiple experiments with different learning rates and number of virtual tokens I have noticed
that the train loss of the different runs had a very similar pattern.

Thus I have realized that the training was not shuffling the data. So maybe I have to revisit previous
fine-tuning adding data shuffling.

The model trained with shuffled data consistently outperforms the other model.

### No improvement on leaderboard

I have made a few submissions and the results did not improve over fine-tuning. Moreover one of the
submissions seemed very brittle and a tiny change of adding one space to the submission resulted in very different predictions.

| base_model | virtual tokens | train steps | train loss | val loss | LB score |
|------------|----------------|-------------|------------|----------|----------|
| mistral    | 8              | 250         | 0.97       | 1        | 0.61     |
| mistral    | 64             | 250         | 1.1        | 1.15     | 0.61     |
| mistral    | 8              | 1000        | 0.61       | 0.78     | 0.56     |
| mixtral    | 8              | 1000        | 0.96       | 1        | 0.6      |

## Conclusion

Prompt-tuning is not the solution we are looking for.
