# Business Understanding

<!--- --->

## Challenge description

<!--- Look at the challenge description, understand the goal of the challenge
and write it here with your own words. Use images if they improve the explanation--->

The challenge is to guess the prompt that was used to transform a text, given the original and the
transformed text.

The texts were rewritten using [Gemma 7b-it-quant](https://www.kaggle.com/models/google/gemma/frameworks/pyTorch/variations/7b-it-quant) LLM, so we can use it to create training data.

The test dataset has around 1300 samples and it is hidden, we have to submit code that runs in [less than 9 hours](www.kaggle.com/competitions/llm-prompt-recovery/overview/code-requirements).

## Evaluation

<!--- Understand the metric used on the challenge, write it here and study
the characteristics of the metric --->

> For each row in the submission and corresponding ground truth, sentence-t5-base is used to calculate corresponding embedding vectors. The score for each predicted / expected pair is calculated using the [Sharpened Cosine Similarity](https://github.com/brohrer/sharpened-cosine-similarity/blob/main/README.md?plain=1#L32), using an exponent of 3. The SCS is used to attenuate the generous score given by embedding vectors for incorrect answers. Do not leave any rewrite_prompt blank as null answers will throw an error.

So they compute the cosine similarity of the embedding of the ground truth and the prediction, and that
value is elevated to 3. We have to maximize the similarity between the predictions and the ground truth.

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

This competition is a good opportunity to gain hands-on experience with LLMs.

## Terminology

<!--- Sometimes the field of the challenge has specific terms, if that is the
case write them here, otherwise delete this section.--->

- EOS token: End of sentence token

## Questions

<!--- Write here any question that arises when reading about the challenge --->

### Does the prompt include the original text?

It does not seem to be the case according to this [experiment](https://www.kaggle.com/code/ironbar/submit-original-text). Making a submission with the original text only received a LB score of 0.38, while
submitting a simple prompt such as `Improve the text to this.` received a score of 0.6.

https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/480466

## Project Plan

<!--- Write initial ideas for the project. This is just initial thoughts,
during the challenge I will have a better understanding of the project and
with better information I could decide other actions not considered here.--->

### Prompt engineering

On a first step I should try using prompt engineering. We should get a good baseline just by
asking an LLM to look at the original text, the rewritten text and ask what the prompt could have been.

Also giving some examples could boost the scores even further.

### Model fine-tuning

Being able to fine-tune the model using new tokens could teach the model to learn a new task. This
has the potential to achieve even better results.

### Model inversion

We already know which model was used to generate the text, can't we reverse the process to [fill in the middle](https://arxiv.org/abs/2207.14255)?
