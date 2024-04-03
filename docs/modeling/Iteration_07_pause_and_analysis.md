# Iteration 7. Pause and analysis

_03-04-2024_

## Goal

I have the tools (fine-tuning and few-shot prompt) but I do not know what is the task to learn. Let's
analyze all the work done and think of ways to advance in the challenge.

## Facts

- A simple prompt like `Improve the text to this` gets `0.60` on leaderboard, while many few-shot prompts
  submissions with a big model like Mixtral score below that.
- Some teams have been able to consistently and  iteratively improve their score on the LB. They have slowly climbed up to `0.70`.
- The uncertainty of the LB score is around `0.02`
- It has not been confirmed that the split of the test set is random.
- By adding `Improve the text to this.` to the predictions of Mixtral I have seen consistent improvements of `0.02` in LB score, from `0.61` to `0.63`.
- On local validation I have been able to reach a score of `0.81` when training and evaluating on prompts recovered by GPT4.
- When trying different datasets for few-shot prompt I have observed great variability on LB scores:
    - Using my hand-made examples I get `0.61`
    - Using `newtonbaba` dataset I get `0.62`
    - Using `alexxxem` dataset I get `0.51`
- The sharpened cosine similarity metric does not penalize greater variance. If two distributions have the same mean, the one with the greater variance will have a greater sharpened score.
- Using a [dataset of mean prompts](https://www.kaggle.com/datasets/kishanvavdara/llm-prompt-recovery-mean-prompts) and LB scores we could measure how similar are local datasets to LB.
- The outputs from Gemma have been likely post-processed because public datasets show that very frequently
  reveals the given prompt in the response.
- When evaluating prompt variations created by GPT4 that preserved the original meaning the score was always above `0.70`
- Many different prompts can lead to the same response. A prompt can be generic or detailed an produce the same result.
- 

## Motivation

## Development

## Results

## Conclusion

## Next steps

- What if I just focus on building the best possible model and praise for the shakeup?
- What if I request Mixtral to only answer when it is very sure and the prompt is evident? (Play safe)
- I could do more experiments on few-shot prompting, f.e. selecting random samples from a dataset
- Analize the few-shot prompt examples with GPT4
- Could I run some mean-prompt optimization using GPT4? I have read that some people have done that but does not transfer well to LB.
- Try again with perplexity/model inversion. But the problem is that the output has likely been postprocessed.

## TODO

- [ ]
