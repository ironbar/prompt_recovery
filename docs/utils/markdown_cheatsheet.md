# Markdown cheatsheet

## Examples of attaching images

First an image with markdown syntax

![alt text](https://www.kaggle.com/static/images/site-logo.png "Metric used in the challenge")

Next an image with html syntax that allows to control the size

<img src="https://www.kaggle.com/static/images/site-logo.png" alt="drawing" width="100"/>

## Examples of equations

Equation on a different line:

$$\epsilon = \sqrt{\frac{1}{n}\sum_{i=1}^n(log(\frac{p_i}{a_i}))^2} $$

Examples of inline equations. Let's consider $e^{q_i} = p_i + 1$ and $e^{b_i} = a_i + 1$.

## Easy way to create tables

[http://www.tablesgenerator.com/markdown_tables#](http://www.tablesgenerator.com/markdown_tables#)

| representation_size | fmeasure | val_fmeasure |
|---------------------|----------|--------------|
| 1024                | 0.893    | 0.573        |
| 512                 | 0.819    | 0.476        |
| 256                 | 0.676    | 0.365        |
| 128                 | 0.45     | 0.33         |
| 64                  | 0.31     | 0.29         |
| 32                  | 0.26     | 0.26         |
| 16                  | 0.214    | 0.216        |