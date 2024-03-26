# Iteration 2. Prompt engineering

_21-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Can we improve the baseline leaderboard score of 0.52 of Mixtral using prompt engineering?

We will have to implement some validation and test evaluations to be able to do prompt engineering.

## Motivation

We already know that Mixtral is going to be our workhorse for the challenge and that the input to the model should be below 7200 tokens. Now is the time to see how much we can improve simply with prompt engineering and few shot prompting.

## Development

### Cleaning the datasets

I have downloaded 6 datasets and iteratively created code to clean the datasets. Most of the cleaning
was done to remove Gemma starts that give hints of the prompt used. For example very frequently
answers start by `Sure, here is your rewritten text:`.

I also removed some of the samples where Gemma refused to answer.

The process of finding the patterns to clean the data was done iteratively. I evaluated the datasets
using a model and then looked at the worse and best predictions.

### Slow evaluation

Evaluating the 6 datasets can take around 90 minutes. Thus prompt engineering is slow because
if we want to measure small improvements we need that evaluation time.

I could use [Mistral API](https://docs.mistral.ai/platform/pricing/) to accelerate evaluation. Assuming
that each request would use around 2500 input tokens, each dataset evaluation (around 300 samples) would
cost 0.7\$, so the total evaluation in 6 datasets would be likely less than 4\$. If I make 5 requests per
second that would be around 6 minutes.

## Results

### First prompt engineering optimizations

These results are previous to data cleaning.

| prompt                                  | gemma_suppl_rewrite | leaderboard |
|-----------------------------------------|---------------------|-------------|
| baseline                                | 0.628               | 0.52        |
| few shot markdown                       | 0.691               | 0.58        |
| few shot conversation                   | 0.715               | 0.61        |
| conversation + Improve the text to this | -                   | 0.63        |
| Improve the text to this                | 0.617               | 0.6         |

- Adding 9 examples and changing the prompt slightly was enough to boost the score ~0.09
- Merging the prediction with the simple text of `Improve the text to this` improves the LB even further.
- With a template prompt of around 2k tokens the submission takes less than 6 hours.

#### Number of output tokens

| number of tokens | mean score |
|------------------|------------|
| 10               | 0.588      |
| 25               | 0.637      |
| 50               | 0.639      |
| 75               | 0.639      |

A small number of tokens is hurtful, but once a point is reached there is no point on allowing more
output tokens.

#### Second steps

After data cleaning I have carried more thorough optimization:

| prompt variations                                | gemma_suppl_rewrite | nbroad_v2 | newtonbaba | dipamc77 | alexxxsem | galileo | mean  |
|--------------------------------------------------|---------------------|-----------|------------|----------|-----------|---------|-------|
| few shot conversation                            | 0.698               | 0.609     | 0.672      | 0.634    | 0.574     | 0.647   | 0.639 |
| add user and assistant names                     | 0.694               | 0.606     | 0.656      | 0.61     | 0.572     | 0.632   | 0.628 |
| more detailed intro                              | 0.705               | 0.62      | 0.672      | 0.632    | 0.569     | 0.664   | 0.644 |
| prompt instead of instruction                    | 0.721               | 0.621     | 0.672      | 0.633    | 0.572     | 0.662   | 0.647 |
| order instead of instruction                     | 0.642               | 0.551     | 0.615      | 0.635    | 0.555     | 0.597   | 0.599 |
| order instead of instruction v2                  | 0.627               | 0.544     | 0.59       | 0.612    | 0.545     | 0.584   | 0.584 |
| prompt and more detailed intro                   | 0.717               | 0.623     | 0.679      | 0.65     | 0.581     | 0.674   | 0.654 |
| Improve response start                           | 0.724               | 0.623     | 0.68       | 0.647    | 0.577     | 0.665   | 0.653 |
| Original and rewrritten text in a single message | 0.711               | 0.622     | 0.675      | 0.615    | 0.572     | 0.651   | 0.641 |
| chatgpt intro                                    | 0.713               | 0.627     | 0.671      | 0.635    | 0.579     | 0.67    | 0.649 |
| reorder the introduction                         | 0.719               | 0.627     | 0.68       | 0.65     | 0.587     | 0.676   | 0.657 |

By adding a more detailed intro (better definition of the task) and replacing the word "instruction" by
"text prompt" I was able to improve the mean scs score from `0.639` to `0.657`.

TODO: add submission results

## Conclusion

## Next steps

- Is fine-tuning necessary for this problem? Which data should I use to finetune?
- Analyze the supplementary material
- Make a list of real rewrite scenarios, not made up ones
- Prepare more examples for few shot prompting, some of them must exploit the hints leave by Gemma.

## TODO

- [x] Update the submission notebook to avoid loading the model when the test set is small and save GPU credits
- [x] Which dataset I could use for validation?
- [x] Set up a validation pipeline
- [ ] ~~Batch size speedup on inference~~
- [x] Does the order of the prompt has an effect on inference time? YES
