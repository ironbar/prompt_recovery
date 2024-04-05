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

Asking for less than 200 words creates text of around 100 words, which is 150 tokens. I believe that is
long enough to be expressive and at the same time allow faster train.

With ChatGPT it works really well. The temperature it is said to be 0.7 or 1.

My vision is to create a dataframe with the prompts that will be used to generate the dataset. To enable
for greater flexibility I will allow to use placeholders in the prompts and those will be replaced
with different options when creating the dataset.

```python
prompt_template = """
Given the following text prompt your task is to:

1. Write a short text that could have sense to be modified with the given text prompt. The number of words should be less than 200.
2. Rewrite the text using the given text prompt.

The output should be in json, with the following format:

{"original_text": "...", "rewritten_text": "..."}

## Text prompt

```{prompt}```
"""
```

### OpenAI tokenizer is similar to Mixtral

I have verified that I can use [OpenAI's tokenizer](https://platform.openai.com/tokenizer) as a good estimator of the tokens that will create Mixtral.

<https://www.kaggle.com/code/ironbar/mixtral-tokenizer-analysis?scriptVersionId=170444326>

## Results

## Conclusion

Does it have sense to have a validation dataset anymore? Or is it better to simply use all the available data
for training?

Once I have created and trained on my own data, I could evaluate the model on public data. Then review the top
scoring samples and if I believe they are good enough add them to the train dataset.

## Next steps

- Shouldn't I train just on answers when fine-tuning? I have the feeling that the model was trained on the whole text. https://github.com/Lightning-AI/lit-llama/issues/290#issuecomment-1557249666

## TODO

- [ ] Generate more data with Gemini or Gemma. Once I have the original text and the prompt I can use any model to generate more data.
- [x] Is the Mixtral tokenizer similar to OpenAI's?
- [ ] Combine multiple prompts in one. F.e. rewrite the text adding dragons and with a more humorous tone.
- [ ] Merge model and adapter using public notebook as reference
- [ ] Read about fine-tuning model in question answering datasets and how to adjust the loss just on the answers
