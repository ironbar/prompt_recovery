# Business Understanding

<!--- --->

## Challenge description

<!--- Look at the challenge description, understand the goal of the challenge
and write it here with your own words. Use images if they improve the explanation--->

The challenge is to guess the prompt that was used to transform a text, given the original and the
transformed text.

The texts were rewritten using [Gemma 7b-it-quant](https://www.kaggle.com/models/google/gemma/frameworks/pyTorch/variations/7b-it-quant) LLM, so we can use it to create training data.

The test dataset has around 1300 samples and it is hidden, we have to submit code that runs in [less than 9 hours](www.kaggle.com/competitions/llm-prompt-recovery/overview/code-requirements). That gives less than 25s to make
each inference.

## Evaluation

<!--- Understand the metric used on the challenge, write it here and study
the characteristics of the metric --->

> For each row in the submission and corresponding ground truth, sentence-t5-base is used to calculate corresponding embedding vectors. The score for each predicted / expected pair is calculated using the [Sharpened Cosine Similarity](https://github.com/brohrer/sharpened-cosine-similarity/blob/main/README.md?plain=1#L32), using an exponent of 3. The SCS is used to attenuate the generous score given by embedding vectors for incorrect answers. Do not leave any rewrite_prompt blank as null answers will throw an error.

So they compute the cosine similarity of the embedding of the ground truth and the prediction, and that
value is elevated to 3. We have to maximize the similarity between the predictions and the ground truth.

In the forum it has been said that T5 is not a good model.

## Assess situation

<!---This task involves more detailed fact-finding about all of the resources,
constraints, assumptions, and other factors that should be considered in determining
the data analysis goal and project plan

* timeline. Is there any week where I could not work on the challenge?
* resources. Is there any other project competing for resources?
* other projects. May I have other more interesting projects in the horizon?
 --->

The timeline is tight, just a month for this challenge. It does not give too much time to try things.

I'm also participating on [Drivendata's Pose bowl competition](https://www.drivendata.org/competitions/group/competition-nasa-spacecraft/). That competition ends on May 14 so there is an extra month and I should
apply most of my focus to Kaggle.

This competition is a good opportunity to gain hands-on experience with LLMs. I'm going to devote
a week to the challenge to learn and if my score is promising I would consider devoting more time.
The week of Monday 18 March.

## Terminology

<!--- Sometimes the field of the challenge has specific terms, if that is the
case write them here, otherwise delete this section.--->

- **EOS token**: End of sentence token
- **GGUF format**: GGUF is a file format for storing models for inference with GGML and executors based on GGML. GGUF is a binary format that is designed for fast loading and saving of models, and for ease of reading.
- [GPTQ](https://arxiv.org/abs/2210.17323): Accurate Post-Training Quantization for Generative Pre-trained Transformers. It is a a new one-shot weight quantization method based on approximate second-order information, that is both highly-accurate and highly-efficient. It is implemented on [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) and it seems to be used by [TheBloke](https://huggingface.co/TheBloke)
- [QLoRA](https://github.com/artidoro/qlora): Efficient Finetuning of Quantized LLMs. It quantizes the
  original model to 4bits and trains a LoRA. The paper claims that achieves state of the art results
  while requiring much less memory.
- [Nous-Hermes-Llama2-13b](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGUF): is a state-of-the-art language model fine-tuned on over 300,000 instructions. I have read that it is the state of the art for that
size of model.
- [DPO](https://arxiv.org/abs/2305.18290) Direct Preference Optimization is a method to fine-tune a model
  to learn preferences of some output over other output.
- [Goal-conditioned imitation learning](https://sites.google.com/view/goalconditioned-il/)

## Questions

<!--- Write here any question that arises when reading about the challenge --->

### Does the prompt include the original text?

It does not seem to be the case according to this [experiment](https://www.kaggle.com/code/ironbar/submit-original-text). Making a submission with the original text only received a LB score of 0.38, while
submitting a simple prompt such as `Improve the text to this.` received a score of 0.6.

[Does rewrite_prompt contain original_text? Forum](https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/480466)

### What is the advantage of using custom tokens for retraining?

I know they are used for converting LLM to assistants. If I'm fine-tuning an assistant does it have
sense to add new tokens? My intuition says that if I use an specific prompt when fine-tuning the model
it should be comparable to adding new tokens but simpler.

## Project Plan

<!--- Write initial ideas for the project. This is just initial thoughts,
during the challenge I will have a better understanding of the project and
with better information I could decide other actions not considered here.--->

### Premises

- I have to use the biggest model possible. As a rule of thumb larger LLM models give better results.
  Thus I have to use the biggest model possible that allows to make a successful submission.
- Fine-tuning is likely to give better results over just prompt engineering.
- Given the model information about the evaluation metrics is likely to be helpful. It could be as simple
  as conditioning the generation on the score by giving the desired score in the prompt. Or could it
  be something more advanced like DPO, reinforcement learning or weighted loss.

### Plan

1. Find the biggest model that could be used for the submission. Make a few submissions using prompt engineering.
2. Basic fine-tuning of the model on public data
3. Evaluate on public data
4. Submission

At this point the next steps could involve:

- Generate more training data with Gemma
- Try more advanced training methods that use information from the evaluation metrics
