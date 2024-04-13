# Iteration 14. More high quality data

_12-04-2024_

## Goal

Can I get a score higher than 0.62 by fine-tuning Mistral 7B on my own data?

## Motivation

Fine-tuning Mistral 7B has shown that:

- My own data gives better results than public data
- Small datasets can give good results

Thus I should focus on improving my datasets.

## Development

### Multi instruction theory

Let's think which elements can be required to be changed on a rewritten text:

- length: extend, shorten, summarize, less than n words...
- tone: formal, informal, humorous, professional, persuasive, optimistic, sarcastic, inspirational...
- style: academic, fiction, in the style of some famous author, poem, rhyme, blog, journal, news
- remove: remove some parts of the text
- additions: add new elements to the text, f.e. questions, calls to action
- transformations: translate to other language, format as markdown, encode
- perspective: first person, third, change the main character
- audience: Adjusting the text to cater to a specific demographic, professional group, age range, cultural background, etc.
- Grammar and Syntax: Adjusting sentence structure for better readability or to fit stylistic preferences; correcting grammatical errors.
- Clarity and Precision: Enhancing the text to be clearer or more precise, which may involve rephrasing technical jargon, simplifying complex concepts, or providing additional explanations where needed.
- Legal and Ethical Compliance: Modifying text to comply with legal or ethical standards, particularly in marketing, health-related content, and public communications.
- Emphasis and Highlighting: Altering the text to emphasize key points or ideas, which might involve using bold or italic formatting, or restructuring sections to highlight critical information.

### Creating more data from the leaked examples with GPT4

```
I want to create a dataset of original and rewritten texts. The first step is to gather a diverse set of text prompts that would be used later to transform the original text into the rewritten text. Given the following examples, can you create 20 new prompts?

## Examples

- Update this email to make it more typical and incorporate the topic of "incentive". The new version should be shorter than 53 words long
- Rephrase this memo to evoke a sense of concern and incorporate the topic "acre", ensuring that the tone reflects worry and apprehension. The new version should be shorter than 53 words long.
- Rework this text message to infuse it with a playful and humorous complaint, adding a touch of whimsy and lightness to the conversation
```

ChatGPT is an amazing tool for this task. I'm able to generate realistic new data very easily.

### Creating multi-instruction prompts with GPT4

Let's try to do the same, but giving simple prompts and asking GPT4 to create new multi instruction prompts.

```
I want to create a dataset of original and rewritten texts.

The first step is to gather a diverse set of text prompts that would be used later to transform the original text into the rewritten text.

Your task is to generate 20 realistic prompts. Below you can find a list with all the posible changes that can be required to be changed on a text. For each prompt pick randomly 2 or 3 types of changes from the list.

I have listed also some sample prompts for reference

Take in mind that the original texts will have less than 200 words.

## Theory

This are the possible changes that can be done to a text. After each change some examples or explanations will follow. Do not limit yourself to this examples.

- length: extend, shorten, summarize, less than n words...
- tone: formal, informal, humorous, professional...
- style: academic, fiction, in the style of some author, poem, rhyme
- remove: remove some parts of the text
- additions: add new elements to the text, f.e. questions, calls to action
- transformations: translate to other language, format as markdown, encode
- perspective: first person, third, change the main character
- audience: Adjusting the text to cater to a specific demographic, professional group, age range, cultural background, etc.
- Grammar and Syntax: Adjusting sentence structure for better readability or to fit stylistic preferences; correcting grammatical errors.
- Clarity and Precision: Enhancing the text to be clearer or more precise, which may involve rephrasing technical jargon, simplifying complex concepts, or providing additional explanations where needed.
- Legal and Ethical Compliance: Modifying text to comply with legal or ethical standards, particularly in marketing, health-related content, and public communications.
- Emphasis and Highlighting: Altering the text to emphasize key points or ideas, which might involve using bold or italic formatting, or restructuring sections to highlight critical information.

## Sample prompts


```

### Create prompts for consistency, legal, DEI, SEO...

```
I want to create a dataset of original and rewritten texts.

The first step is to gather a diverse set of text prompts that would be used later to transform the original text into the rewritten text.

Your task is to generate 20 realistic prompts.

Can you create them with the following topic?

Consistency: Ensuring that the text maintains consistent use of terminology, voice, and narrative points of view, which can be particularly important in longer texts or texts that have been edited by multiple people.
```


### Train parameters

- I believe I should use `r=1` on LoRA because that gave very good LB results.
- I'm going to simplify the prompt because the previous prompt constrained the solution to be
  a single sentence and now that won't be always the case. The new prompt is minimalistic.
- I will be using `high_quality_dataset_v1` for validation as in the previous data-centric iteration.
- On inference I should increase the max tokens to around 50.

### Create dataset with hints

The leaked data showed many rewritten texts starting by words that hinted the prompt. I'm going to
manually modify some of my data to include those hints.

## Results

### Experiments

- Does adding prompts imitating the leaked ones improves LB score?
- Does adding prompts with hints improves the LB score?
- Does creating new multi-instruction prompts improves the LB score?

## Conclusion

## Next steps

- I know that model does not seem to be relevant, but Mistral-22B is out! https://huggingface.co/Vezora/Mistral-22B-v0.2 I should try it.

## TODO

- [x] Reread my prompts
- [x] Read prompts from other relevant dataset: mooney leaked, supp_rewrite. I don't see anything special.
- [x] Use ChatGPT to come up with more prompts -> autobrainstorm
- [x] Multi-instruction prompts (inspired on leaked data)
