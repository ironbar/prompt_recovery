# Modeling

## Select modeling technique

<!---Document the actual modeling technique that is to be used. If multiple
techniques are applied, perform this task separately for each technique.
Many modeling techniques make specific assumptions about the data—for example,
that all attributes have uniform distributions, no missing values allowed,
class attribute must be symbolic, etc. Record any such assumptions made. --->

### Prompt engineering

On a first step I should try using prompt engineering. We should get a good baseline just by
asking an LLM to look at the original text, the rewritten text and ask what the prompt could have been.

Also giving some examples could boost the scores even further.

### Model fine-tuning

Being able to fine-tune the model using new tokens could teach the model to learn a new task. This
has the potential to achieve even better results.

### Model inversion

We already know which model was used to generate the text, can't we reverse the process to [fill in the middle](https://arxiv.org/abs/2207.14255)?

## Generate experimentation design

<!---Describe the intended plan for training, testing, and evaluating the models.
A primary component of the plan is determining how to divide the available dataset
into training, test, and validation datasets.

Doing a plot of score vs train size could be helpful to decide the validation strategy

Depending on the size of the data we have to decide how we are going to use submissions.
The less the submissions the most confidence we can have on the score. However sometimes
the data distribution is very different, or the size of the data is small and we have
to make a lot of submissions. Sometimes is not easy to have a good correlation between
validation score and LB score
--->

The lack of data makes evaluation very difficult. We don't know if our generated data follows a
similar distribution to the test dataset.

The public leaderboard uses only 15% of the data, so it's just 195 samples.
