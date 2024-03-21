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

## Results

## Conclusion

## Next steps

## TODO

- [ ] Update the submission notebook to avoid loading the model when the test set is small and save GPU credits
- [ ] Which dataset I could use for validation?
- [ ] Set up a validation pipeline
- [ ] ~~Batch size speedup on inference~~
- [x] Does the order of the prompt has an effect on inference time? YES
