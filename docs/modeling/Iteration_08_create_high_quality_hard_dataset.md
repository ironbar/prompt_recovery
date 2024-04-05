# Iteration 8. Create a high quality hard dataset

_04-04-2024_

## Goal

Create a high quality hard dataset

## Motivation

My current hypothesis is that the differences between validation and leaderboard score are simply
because the leaderboard samples are more difficult. It doesn't seem to be a problem with the style
of the prompts.

Ideally my best models will score around 0.61 on the new dataset and that could guide new developments
to climb on the leaderboard.

Let's ignore everything about the mean prompts and the issues with T5 embeddings and focus on building
a powerful model.

Current competition leader [said this](https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/481322#2706751):

> I have finally beat the mean prompt and got 0.64 "legit". Wasted 2 weeks and tons of subs, should've tried to build a good model from the start haha.

## Development

### Dataset specification

- **The samples should be realistic and need to have sense.** The test dataset is small so I believe
  it is a high quality dataset an no dumb samples are there.
- **The original and rewritten text should be short.** In the test set and the leaked data the texts
  are short. [Apparently](https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/482228#2685355) less than 350 words on the test set.
  This makes evaluation and training faster.
- **The prompts should be as diverse as possible.** I should try to cover as many different applications as possible.
- **This is likely to be an iterative process.** It is very likely that I will be adding new samples
  to the dataset until the end of the challenge.
- **There might be combinations of prompts.** Two or more changes could be asked in a prompt.

### Search for prompts online

- <https://aihabit.net/category/chatgpt-prompts/prompts-for-writing/>
    - <https://aihabit.net/chatgpt-prompts-for-rewriting-text/>
    - <https://aihabit.net/chatgpt-prompts-for-editing/>
    - <https://aihabit.net/chatgpt-prompts-for-writing-emails/>
- <https://www.linkedin.com/pulse/15-chatgpt-prompts-better-than-rewrite-rajat-jain/>
- <https://www.learnprompt.org/writing-styles-for-chat-gpt-prompts>
- <https://dev.to/mursalfk/50-chatgpt-prompts-for-developers-4bp6>

### Search for prompts in the challenge

The idea is to review the prompts of the public data and take the ones I find useful.

### GPT4 can synthetize the data

I have probed that GPT4 is able to generate an original and rewritten text given a prompt. Thi is ver
convenient because:

- It allows to control the length of the text, forcing them to be short
- GPT4 is a very good model, so the example will be typically good.
- This approach scales, if I want to generate more data I simply have to change the seed or the temperature and create new data.

This approach will reduce my job to simply gather prompts and to review the job done by GPT4.

I have to prepare the prompts with GPT4 in mind. F.e. when making references to text, memo, mail, dialog...
GPT4 will use them to generate the original text.

Since the texts will be short this won't cost too much money to generate a small dataset.

```
Given the following text prompt your task is to:

1. Write a short text that could have sense to be modified with the given text prompt. The number of words should be less than 100.
2. Rewrite the text using the given text prompt. 

## Text prompt

Rewrite the story adding dragons
ChatGPT
Original Short Text
In a distant kingdom, a young knight sets out on a quest to find the legendary golden apple, a treasure believed to bring eternal youth to its possessor. The journey leads through perilous forests, over towering mountains, and across vast deserts. Along the way, the knight faces various challenges, including fierce beasts, treacherous paths, and puzzles left by the guardians of the apple.

Rewritten Text with Dragons
In a distant kingdom, a young knight sets out on a quest to find the legendary golden apple, a treasure believed to bring eternal youth to its possessor. The journey leads through perilous forests, home to wise but wary dragons, over towering mountains guarded by dragonkind, and across vast deserts where dragons soar under the scorching sun. Along the way, the knight faces various challenges, including fierce dragons, treacherous paths, and riddles posed by the dragon guardians of the apple.
```

```
Given the following text prompt your task is to:

1. Write a short text that could have sense to be modified with the given text prompt. The number of words should be less than 100.
2. Rewrite the text using the given text prompt. 

The output should be in json, with the following format:

{"original_text": "...", "rewritten_text": "..."}

## Text prompt

Rewrite the story as if it's being narrated by God
ChatGPT
json
Copy code
{
  "original_text": "The town was small, nestled between two rolling hills. People went about their daily routines, largely unaware of the outside world. A little girl, curious and bright, wandered off into the woods, drawn by the promise of adventure and the mystery of the unknown.",
  "rewritten_text": "Behold the town I have placed between two rolling hills, a testament to the simplicity and beauty of creation. My children there live in harmony, their lives a tapestry of daily rituals, untouched by the chaos of the outside world. Among them, a little girl, a spark of curiosity and brilliance I instilled in her, felt the call of the woods. Guided by My hand, she ventured forth, seeking the adventures and mysteries I laid out before her."
}
```

```
Given the following text prompt your task is to:

1. Write a short text that could have sense to be modified with the given text prompt. The number of words should be less than 100.
2. Rewrite the text using the given text prompt. 

The output should be in json, with the following format:

{"original_text": "...", "rewritten_text": "..."}

## Text prompt

"""Rewrite the python function to be more readable"""

3 / 3

ChatGPT
json
Copy code
{
  "original_text": "def calc(d): return d[0]+d[1] if len(d) > 1 else d[0]*2",
  "rewritten_text": "def calculate_sum_or_double(values):\n    if len(values) > 1:\n        return values[0] + values[1]\n    else:\n        return values[0] * 2"
}





```


## Results

## Conclusion

Does it have sense to have a validation dataset anymore? Or is it better to simply use all the available data
for training?

Once I have created and trained on my own data, I could evaluate the model on public data. Then review the top
scoring samples and if I believe they are good enough add them to the train dataset. 

## Next steps

- Shouldn't I train just on answers when fine-tuning? I have the feeling that the model was trained on the whole text. https://github.com/Lightning-AI/lit-llama/issues/290#issuecomment-1557249666

## TODO

- [ ] Generate more data with Gemini or Gemma
