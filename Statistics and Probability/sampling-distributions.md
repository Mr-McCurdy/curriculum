# Understanding Sampling Distributions

---

## Introduction

In statistics, understanding how sample data behaves in relation to the population it comes from is essential. A key tool to achieve this is the concept of a sampling distribution. A sampling distribution is the probability distribution of a given statistic based on a random sample. When we calculate statistics like the sample mean or sample proportion, they vary from sample to sample. The distribution of these statistics forms what we call a *sampling distribution*.

To fully grasp this concept, we also need to understand the distinction between **parameters** and **statistics**. A parameter refers to a number that describes the entire population (for example, population mean $\mu$ or population proportion $p$). A statistic, on the other hand, refers to a number calculated from a sample, such as the sample mean $\bar{x}$ or sample proportion $\hat{p}$. Statistics are used to estimate parameters.

---

## Sampling Distributions for Proportions and Means

We deal with sampling distributions for both proportions and means in AP Statistics, and understanding both is vital for making inferences about populations from sample data. Below, we'll explore each type.

### 1. Sampling Distribution for Sample Proportions

For a categorical variable, we often calculate the sample proportion $\hat{p}$. The sampling distribution of $\hat{p}$ provides the distribution of the sample proportions for all possible random samples of a given size from a population with proportion $p$. The sampling distribution of $\hat{p}$ has the following characteristics:

- Mean of the sampling distribution of $\hat{p}$ is $\mu_{\hat{p}} = p$.
- Standard deviation of the sampling distribution of $\hat{p}$ is $\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}}$, where $n$ is the sample size.
- The shape of the distribution is approximately normal if the sample size is large enough. Specifically, if $np \geq 10$ and $n(1 - p) \geq 10$, the sampling distribution of $\hat{p}$ can be modeled by a normal distribution.

### 2. Sampling Distribution for Sample Means

For numerical data, the sample mean $\bar{x}$ is of interest. The sampling distribution of $\bar{x}$ gives the distribution of the sample means for all possible random samples of a given size from a population with mean $\mu$ and standard deviation $\sigma$. The characteristics of the sampling distribution for the sample mean are as follows:

- Mean of the sampling distribution of $\bar{x}$ is $\mu_{\bar{x}} = \mu$.
- Standard deviation of the sampling distribution of $\bar{x}$ is $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$, where $n$ is the sample size.
- According to the Central Limit Theorem (CLT), if the population distribution is not normal, the sampling distribution of $\bar{x}$ will be approximately normal if the sample size is sufficiently large (usually $n \geq 30$).

---

## Worked Examples

### Example 1: Sampling Distribution for Proportions

Suppose a population has a proportion $p = 0.4$ who prefer a particular brand. If we take a random sample of size 100, what is the mean and standard deviation of the sampling distribution of $\hat{p}$?

**Solution:**

The mean of the sampling distribution of $\hat{p}$ is $\mu_{\hat{p}} = 0.4$.

The standard deviation of the sampling distribution is:

$$
\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}} = \sqrt{\frac{0.4(1 - 0.4)}{100}} = 0.049
$$

### Example 2: Sampling Distribution for Means

Suppose the mean height of all adult women is $\mu = 64$ inches with a standard deviation $\sigma = 3$ inches. If we take a random sample of 50 women, what is the mean and standard deviation of the sampling distribution of the sample mean height $\bar{x}$?

**Solution:**

The mean of the sampling distribution of $\bar{x}$ is $\mu_{\bar{x}} = 64$.

The [standard deviation](https://github.com/Mr-McCurdy/Curriculum/tree/main/APStatistics) of the sampling distribution is:

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{50}} \approx 0.424
$$

---

## Exercises

1. Given a population proportion $p = 0.7$, calculate the mean and standard deviation of the sampling distribution for a sample size of 150.
2. A population has a mean $\mu = 50$ and a standard deviation $\sigma = 12$. For a sample of size 40, find the mean and standard deviation of the sampling distribution of the sample mean.
3. If a population proportion is $p = 0.3$, what sample size is required for the sampling distribution of $\hat{p}$ to be approximately normal?
4. In a population, $p = 0.55$. For a sample of size 200, find the standard deviation of the sampling distribution of $\hat{p}$.
5. What does the Central Limit Theorem tell us about the shape of the sampling distribution of $\bar{x}$ for a sample of size 50 from a population with a mean $\mu = 20$ and a standard deviation $\sigma = 5$?
6. For a sample size of 60 and a population standard deviation $\sigma = 8$, calculate the standard deviation of the sampling distribution of $\bar{x}$.
7. Suppose the sample size is doubled. How does this affect the standard deviation of the sampling distribution of $\bar{x}$?
8. A population has a proportion $p = 0.65$. For a sample size of 120, calculate the mean and standard deviation of the sampling distribution of $\hat{p}$.

---

## Solutions

1. **Mean** = 0.7, **Standard Deviation** $\sigma_{\hat{p}} \approx 0.037$
2. **Mean** = 50, **Standard Deviation** $\sigma_{\bar{x}} \approx 1.897$
3. Sample size must be large enough for $np \geq 10$ and $n(1 - p) \geq 10$, so $n \geq 34$.
4. **Standard Deviation** $\sigma_{\hat{p}} \approx 0.034$
5. The Central Limit Theorem tells us that the sampling distribution will be approximately normal for a sample of size 50.
6. **Standard Deviation** $\sigma_{\bar{x}} \approx 1.033$
7. If the sample size is doubled, the standard deviation of the sampling distribution will decrease by a factor of $\frac{1}{\sqrt{2}}$.
8. **Mean** = 0.65, **Standard Deviation** $\sigma_{\hat{p}} \approx 0.042$

---