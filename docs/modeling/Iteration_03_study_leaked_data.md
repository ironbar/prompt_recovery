# Iteration 3. Study Leaked data

_24-03-2024_

<!---
The work is done using short iterations. Each iteration needs to have a very
clear goal. This allows to gain greater knowledge of the problem on each iteration.
--->

## Goal

Extract all the possible information from leaked data.

## Motivation

It is very surprising that a basic submission with `Improve the text to this` scores 0.60 on leaderboard while
a naive submission with Mixtral model scores 0.52.

This is likely caused by the ambiguity of the task: many different prompts can lead to the same output.

The space of input texts and prompts is infinite. Thus the more information we can get about the data
that the host team have created we will increase the chance of winning.

## Development

## Results

### Public information

On a first step let's gather all the data available in the challenge.

#### Overview

On the overview of the challenge we can see some sample prompts:

```csv
id,rewrite_prompt
000aaa,"Rewrite this essay but do it using the writing style of Dr. Seuss"
111bbb,"Rewrite this essay but do it using the writing style of William Shakespeare"
222ccc,"Rewrite this essay but do it using the writing style of Tupac Shakur"
```

Is this a hint that in the test set some of the rewritten texts follow the style of some famous english authors?

#### Sample submission

```csv
id,rewrite_prompt
9559194,Improve that text.
```

Very similar to the overview data. Is it a coincidence that the prompt is similar to `Improve the text to this`?

#### Train

```csv
id,original_text,rewrite_prompt,rewritten_text
-1,"The competition dataset comprises text passages that have been rewritten by the Gemma LLM according to some rewrite_prompt instruction. The goal of the competition is to determine what prompt was used to rewrite each original text.  Please note that this is a Code Competition. When your submission is scored, this example test data will be replaced with the full test set. Expect roughly 2,000 original texts in the test set.","Convert this into a sea shanty: """"""The competition dataset comprises text passages that have been rewritten by the Gemma LLM according to some rewrite_prompt instruction. The goal of the competition is to determine what prompt was used to rewrite each original text.  Please note that this is a Code Competition. When your submission is scored, this example test data will be replaced with the full test set. Expect roughly 2,000 original texts in the test set.""""""","Here is your shanty: (Verse 1) The text is rewritten, the LLM has spun, With prompts so clever, they've been outrun. The goal is to find, the prompt so bright, To crack the code, and shine the light. (Chorus) Oh, this is a code competition, my dear, With text and prompts, we'll compete. Two thousand texts, a challenge grand, To guess the prompts, hand over hand.(Verse 2) The original text, a treasure lost, The rewrite prompt, a secret to be"
```

The train data is contradictory. The prompt has the original text inside.

TODO: make a submission with the original text in the answer.

#### Starter notebook

```python
rewrite_prompts = [
    'Explain this to me like I\'m five.',
    'Convert this into a sea shanty.',
    'Make this rhyme.',
]
```

### Leaked dataset

https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/481811

#### How are the original texts?

Many memos
Ladies and gentleman

#### Which kind of transformations are done?

I cannot know the prompt, but I can study the kind of transformations.

## Conclusion

## Next steps

## TODO

- [ ]
