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

I have made a submission adding the original text and the score decreases from 0.63 to 0.51.
It's a mistery why they decided to show a train example like that...

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

#### Where do the original texts come from?

I cannot find them using google. It is likely that they have been generated.

#### How are the original texts?

Many memos
Ladies and gentleman, announcements
Many letters/emails and messages, they start by Dear, Hey, Subject: (Gmail)
News that start by Title:

TODO: are the texts online?

#### Rewritten texts

No text starts by `Sure, here is...:`. I believe this is a clear indication of postprocessing.

#### Which kind of transformations are done?

I cannot know the prompt, but I can study the kind of transformations.

#### Where did the leak happened?

Paul Mooney said:

> This dataset was originally created for testing purposes without the intention of making it public -- but I accidentally made it public for ~15 minutes in mid-January

This is interesting because Gemma [was announced](https://blog.google/technology/developers/gemma-open-models/) on Feb 21.

Info about Paul:

- <https://www.kaggle.com/paultimothymooney>
- <https://www.linkedin.com/in/paultimothymooney/>No activity on LinkedIn
- <https://github.com/paultimothymooney> There are some private contributions in mid-January, which could be related the the message.
- <https://twitter.com/ptimothymooney> He's not very active in twitter.

Searching in google for [paultimothymooney in the range jan5-jan25 2024](https://www.google.com/search?q=%22paultimothymooney%22&sca_esv=451a08b5c56a2f0a&biw=1245&bih=932&sxsrf=ACQVn0-1CrSgjrfI8Dg9RvvD6v4Q6a9SFg%3A1711276857523&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F5%2F2024%2Ccd_max%3A1%2F25%2F2024&tbm=) I don't get anything useful.

He has a lot of Kaggle code, these are some relevant notebooks:

- <https://www.kaggle.com/code/paultimothymooney/generate-text-w-gemini-pro-in-a-kaggle-notebook>
- <https://www.kaggle.com/code/paultimothymooney/few-shot-prompting-w-gemini-pro-on-kaggle>

The few shot prompt is interesting because it shows a way to do it on Gemini, it is likely that Gemma will be similar.

It has a [dataset](https://www.kaggle.com/datasets/databricks/databricks-dolly-15k) of instruction-following records

## Conclusion

The task of guessing the prompt is not easy. For a non-native speaker like me many times is difficult
because some unknown words are used and I'm not able to describe the difference.

## Next steps

## TODO

- [ ]
