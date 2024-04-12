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

I believe I should use `r=1` on LoRA because that gave very good LB results.

### Multi instruction theory

Let's think which elements can be required to be changed on a rewritten text:

- length: extend, shorten, summarize, less than n words...
- tone: formal, informal, humorous, professional
- style: academic, fiction, in the style of some author, poem, rhyme
- remove: remove some parts of the text
- additions: add new elements to the text, f.e. questions, calls to action
- transformations: translate to other language, format as markdown, encode
- perspective: first person, third, change the main character
- audience: Adjusting the text to cater to a specific demographic, professional group, age range, cultural background, etc.
- Grammar and Syntax: Adjusting sentence structure for better readability or to fit stylistic preferences; correcting grammatical errors.

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
I have created some simple single instruction prompts, that are shown below as examples.
I would like you to create new multiple instruction prompts that take inspiration in the examples.
They should have 2-3 different instructions in the same prompt and be realistic.
The prompts should describe a single transformation, that could be done in one step (although there are multiple instructions to define that transformation(.

Can you create 20 new multiple instruction prompts?

## Examples


```

This is turning to be more difficult

## Results

## Conclusion

## Next steps

## TODO

- [x] Reread my prompts
- [ ] Read prompts from other relevant dataset: mooney leaked, supp_rewrite
- [ ] Use ChatGPT to come up with more prompts -> autobrainstorm
- [ ] Multi-instruction prompts (inspired on leaked data)
