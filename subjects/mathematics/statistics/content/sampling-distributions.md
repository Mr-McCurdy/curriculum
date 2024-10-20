# 4. Understanding Sampling Distributions

---

## Introduction

In statistics, understanding how sample data behaves in relation to the population it comes from is essential. A key tool to achieve this is the concept of a sampling distribution. A sampling distribution is the probability distribution of a given statistic based on a random sample. When we calculate statistics like the sample mean or sample proportion, they vary from sample to sample. The distribution of these statistics forms what we call a *sampling distribution*.

To fully grasp this concept, we also need to understand the distinction between **parameters** and **statistics**. A parameter refers to a number that describes the entire population (for example, population mean $\mu$ or population proportion $p$). A statistic, on the other hand, refers to a number calculated from a sample, such as the sample mean $\bar{x}$ or sample proportion $\hat{p}$. Statistics are used to estimate parameters.

Sampling distributions form the foundation for statistical inference, allowing us to make probabilistic statements about how close our sample statistics are to the true population parameters. By understanding the variability and distribution of these statistics, we can construct confidence intervals and perform hypothesis tests.

---

## What is a Sampling Distribution?

Suppose you wanted to estimate the average height of students at your school. Measuring every student's height might be impractical, so you decide to take a random sample of 30 students and calculate the sample mean height $\bar{x}$. If another student were to take a different random sample of 30 students, their calculated sample mean $\bar{x}$ would likely be different from yours. In fact, if many students each took their own random samples of 30 students and calculated the sample means, we would have a collection of sample means.

This collection of sample means forms a distribution, known as the **sampling distribution of the sample mean**. Similarly, for proportions, if you were estimating the proportion of students who prefer online classes over in-person classes, each sample would yield a different sample proportion $\hat{p}$, and the collection of these proportions forms the **sampling distribution of the sample proportion**.

A sampling distribution describes how a statistic (like $\bar{x}$ or $\hat{p}$) varies from sample to sample. It is a probability distribution of a statistic obtained through a large number of samples drawn from the same population. Understanding the sampling distribution is crucial because it allows us to make inferences about the population parameter based on our sample statistic.

Key points about sampling distributions:

- **Variability:** Different samples yield different statistics due to random sampling variability.
- **Center:** The mean of the sampling distribution is centered at the population parameter (e.g., $\mu$ or $p$) if the statistic is an unbiased estimator (more on this later).
- **Spread:** The spread (standard deviation) of the sampling distribution decreases as the sample size increases.
- **Shape:** The shape of the sampling distribution depends on the sample size and the population distribution. The Central Limit Theorem helps us understand the shape for large samples.

---

## The Importance of Sampling Distributions

Sampling distributions are crucial because they allow us to:

- Assess the reliability of sample statistics as estimates of population parameters.
- Determine probabilities associated with sample statistics.
- Construct confidence intervals for parameters.
- Perform hypothesis testing to make decisions about population parameters.

Without sampling distributions, we wouldn't be able to quantify the uncertainty inherent in using sample data to make inferences about populations.

## Sampling Distributions for Proportions and Means

We deal with sampling distributions for both proportions and means in AP Statistics, and understanding both is vital for making inferences about populations from sample data. Below, we'll explore each type.

### 1. Sampling Distribution for Sample Proportions

For a categorical variable, we often calculate the sample proportion $\hat{p}$. The sampling distribution of $\hat{p}$ provides the distribution of the sample proportions for all possible random samples of a given size from a population with proportion $p$. The sampling distribution of $\hat{p}$ has the following characteristics:

- Mean of the sampling distribution of $\hat{p}$ is $\mu_{\hat{p}} = p$.
- Standard deviation of the sampling distribution of $\hat{p}$ is $\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}}$, where $n$ is the sample size.
- The shape of the distribution is approximately normal if the sample size is large enough. Specifically, if $np \geq 10$ and $n(1 - p) \geq 10$, the sampling distribution of $\hat{p}$ can be modeled by a normal distribution.

**Conditions for Approximate Normality of $\hat{p}$:**

- **Randomness:** The data should come from a random sample or randomized experiment.
- **Independence:** The observations must be independent. When sampling without replacement, the sample size should be less than 10% of the population (the 10% condition).
- **Large Sample Size:** Both $np \geq 10$ and $n(1 - p) \geq 10$ to ensure normal approximation is appropriate.

### 2. Sampling Distribution for Sample Means

For numerical data, the sample mean $\bar{x} $ is of interest. The sampling distribution of $\bar{x}$ gives the distribution of the sample means for all possible random samples of a given size from a population with mean $\mu$ and standard deviation $\sigma$. The characteristics of the sampling distribution for the sample mean are as follows:

- Mean of the sampling distribution of $\bar{x}$ is $\mu_{\bar{x}} = \mu$.
- Standard deviation of the sampling distribution of $\bar{x}$ is $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$, where $n$ is the sample size.
- According to the Central Limit Theorem (CLT), if the population distribution is not normal, the sampling distribution of $\bar{x}$ will be approximately normal if the sample size is sufficiently large (usually $n \geq 30$).

**Conditions for Approximate Normality of $\bar{x}$:**

- **Randomness:** The data should come from a random sample or randomized experiment.
- **Independence:** Observations must be independent; when sampling without replacement, the sample size should be less than 10% of the population.
- **Normality:** If the population distribution is normal, the sampling distribution of $\bar{x}$ is normal regardless of sample size. If the population distribution is not normal, a large sample size (usually $n \geq 30$) is needed for the CLT to apply.

## The Central Limit Theorem (CLT)

The Central Limit Theorem is one of the most important concepts in statistics. It states that, regardless of the shape of the population distribution, the sampling distribution of the sample mean $\bar{x}$ will become approximately normal as the sample size increases.

Mathematically, for a population with mean $\mu$ and finite standard deviation $\sigma$, the sampling distribution of $\bar{x}$ approaches a normal distribution with mean $\mu$ and standard deviation $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ as $n$ becomes large.

## Law of Large Numbers

The Law of Large Numbers states that as the size of a sample increases, the sample mean $\bar{x}$ gets closer to the population mean $\mu$. This law explains why larger samples tend to give more accurate estimates of population parameters.

## Bias and Variability

When working with sampling distributions, it's important to distinguish between bias and variability:

- **Bias:** Bias refers to systematic errors that cause the sample statistic to deviate from the population parameter. An unbiased estimator has a sampling distribution centered at the true parameter.
- **Variability:** Variability refers to how spread out the sampling distribution is. Larger samples tend to have less variability because they average out more of the random fluctuations.

An ideal estimator is both unbiased and has low variability.

## Sample Size Considerations

Choosing an appropriate sample size is critical. Larger samples reduce the standard deviation of the sampling distribution, leading to more precise estimates. However, larger samples can be more costly or time-consuming to collect.

## Worked Examples

### Example 1: Sampling Distribution for Proportions

Suppose a population has a proportion $p = 0.4$ who prefer a particular brand. If we take a random sample of size 100, what is the mean and standard deviation of the sampling distribution of $\hat{p}$? Is the normal approximation appropriate?

**Solution:**

**Mean:** $\mu_{\hat{p}} = p = 0.4$.

**Standard Deviation:**

$$\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}} = \sqrt{\frac{0.4 \times 0.6}{100}} = \sqrt{\frac{0.24}{100}} = 0.049$$

**Check for Normality:**

$$np = 100 \times 0.4 = 40 \geq 10 \quad \text{and} \quad n(1 - p) = 100 \times 0.6 = 60 \geq 10$$

Since both conditions are met, the normal approximation is appropriate.

### Example 2: Sampling Distribution for Means

Suppose the mean height of all adult women is $\mu = 64$ inches with a standard deviation $\sigma = 3$ inches. If we take a random sample of 50 women, what is the mean and standard deviation of the sampling distribution of the sample mean height $\bar{x}$? Is the sampling distribution approximately normal?

**Solution:**

**Mean:** $\mu_{\bar{x}} = \mu = 64$.

**Standard Deviation:**

$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{50}} \approx 0.424$$

**Check for Normality:**

If the population distribution is normal, then $\bar{x}$ is normal. If not, since $n = 50 \geq 30$, by the Central Limit Theorem, the sampling distribution of $\bar{x}$ is approximately normal.

### Example 3: Effect of Sample Size on Variability

Consider the same population as in Example 2. If instead we take a sample of size 200, what is the standard deviation of the sampling distribution of $\bar{x}$?

**Solution:**

$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{3}{\sqrt{200}} \approx 0.212$$

The standard deviation decreases as the sample size increases, indicating less variability in the sample mean.

### Example 4: Non-Normal Population Distribution

Suppose we have a skewed population distribution with mean $\mu = 100$ and standard deviation $\sigma = 20$. If we take a sample of size $n = 5$, can we assume the sampling distribution of $\bar{x}$ is approximately normal?

**Solution:**

Since the sample size is small ($n = 5$), and the population distribution is not normal, we cannot assume the sampling distribution of $\bar{x}$ is approximately normal. The Central Limit Theorem does not apply here because the sample size is not large enough.

## Exercises

1. Given a population proportion $p = 0.7$, calculate the mean and standard deviation of the sampling distribution for a sample size of 150. Is the normal approximation appropriate?
2. A population has a mean $\mu = 50$ and a standard deviation $\sigma = 12$. For a sample of size 40, find the mean and standard deviation of the sampling distribution of the sample mean.
3. If a population proportion is $p = 0.3$, what is the minimum sample size required for the sampling distribution of $\hat{p}$ to be approximately normal?
4. In a population, $p = 0.55$. For a sample of size 200, find the standard deviation of the sampling distribution of $\hat{p}$. Is the normal approximation justified?
5. What does the Central Limit Theorem tell us about the shape of the sampling distribution of $\bar{x}$ for a sample of size 50 from a population with a mean $\mu = 20$ and a standard deviation $\sigma = 5$?
6. For a sample size of 60 and a population standard deviation $\sigma = 8$, calculate the standard deviation of the sampling distribution of $\bar{x}$. If the population is normally distributed, what is the shape of the sampling distribution?
7. Suppose the sample size is doubled. How does this affect the standard deviation of the sampling distribution of $\bar{x}$? Provide a mathematical explanation.
8. A population has a proportion $p = 0.65$. For a sample size of 120, calculate the mean and standard deviation of the sampling distribution of $\hat{p}$. Verify if the normal approximation is appropriate.
9. A survey finds that 40% of people prefer tea over coffee. If we take a sample of 80 people, what is the probability that more than half prefer tea? Assume the normal approximation is appropriate.
10. A factory produces bolts with a mean length of 5 cm and a standard deviation of 0.2 cm. If a quality control engineer measures a random sample of 25 bolts, what is the probability that the sample mean length is between 4.95 cm and 5.05 cm? Assume the bolt lengths are normally distributed.
11. The weights of apples from an orchard are skewed right with a mean of 150 grams and a standard deviation of 30 grams. If a random sample of 36 apples is selected, what is the probability that the sample mean weight is more than 155 grams?
12. Explain why increasing the sample size decreases the standard deviation of the sampling distribution. Use the formula for the standard deviation of $\bar{x}$ in your explanation.
13. A sample of size 100 is taken from a population with proportion $p = 0.2$. What is the probability that the sample proportion $\hat{p}$ is less than 0.15?
14. For a normally distributed population with $\mu = 100$ and $\sigma = 15$, what is the probability that a random sample of size 50 has a sample mean greater than 105?
15. If $n = 25$ and $\sigma = 10$, what sample size would be needed to reduce the standard deviation of the sampling distribution of $\bar{x}$ by half?
16. A population is skewed left with a mean of 80 and a standard deviation of 16. If a sample of size 64 is taken, what is the probability that the sample mean is less than 78?
17. Explain the difference between the standard deviation of a population and the standard deviation of the sampling distribution (also known as the standard error).
18. Given a sample size of 49 and a population standard deviation of 21, calculate the standard error of the sample mean.
19. A population has a mean of 500 and a standard deviation of 100. If we take all possible samples of size 25, what will be the mean and standard deviation of the sampling distribution of $\bar{x}$?
20. In a large population, 30% of individuals have a certain characteristic. If we take a sample of size 200, what is the probability that at least 35% of the sample has the characteristic?
21. The time it takes to assemble a product is uniformly distributed between 20 and 40 minutes. If a sample of size 36 is taken, what is the probability that the sample mean assembly time is more than 31 minutes?
22. A population is bimodal with an unknown distribution. If we take a sample of size 100, can we assume the sampling distribution of $\bar{x}$ is approximately normal? Explain.
23. Discuss how the shape of the population distribution affects the shape of the sampling distribution of the sample mean, particularly for small sample sizes.
24. A sample of 64 observations is taken from a population with a standard deviation of 32. What is the probability that the sample mean differs from the population mean by more than 5 units?

---

## Solutions

1. **Mean:** $\mu_{\hat{p}} = p = 0.7$.

   **Standard Deviation:**

   $$\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}} = \sqrt{\frac{0.7 \times 0.3}{150}} = \sqrt{\frac{0.21}{150}} \approx 0.037$$

   **Normal Approximation:**

   $$np = 150 \times 0.7 = 105 \geq 10, \quad n(1 - p) = 150 \times 0.3 = 45 \geq 10$$

   Therefore, the normal approximation is appropriate.

2. **Mean:** $\mu_{\bar{x}} = \mu = 50$.

   **Standard Deviation:**

   $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{12}{\sqrt{40}} \approx 1.897$$

3. For the normal approximation to be appropriate:

   $$np \geq 10 \quad \text{and} \quad n(1 - p) \geq 10$$

   Solving for $n$:

   $$n \geq \frac{10}{p} = \frac{10}{0.3} \approx 33.33$$

   $$n \geq \frac{10}{1 - p} = \frac{10}{0.7} \approx 14.29$$

   Therefore, $n \geq 34$ to satisfy both conditions.

4. **Standard Deviation:**

   $$\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}} = \sqrt{\frac{0.55 \times 0.45}{200}} = \sqrt{\frac{0.2475}{200}} \approx 0.035$$

   **Normal Approximation:**

   $$np = 200 \times 0.55 = 110 \geq 10, \quad n(1 - p) = 200 \times 0.45 = 90 \geq 10$$

   The normal approximation is justified.

5. The Central Limit Theorem tells us that the sampling distribution of $\bar{x}$ will be approximately normal because the sample size $n = 50$ is greater than 30, regardless of the population distribution.

6. **Standard Deviation:**

   $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{60}} \approx 1.033$$

   Since the population is normally distributed, the sampling distribution of $\bar{x}$ is also normally distributed.

7. When the sample size is doubled from $n$ to $2n$:

   $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \quad \text{becomes} \quad \sigma_{\bar{x}}' = \frac{\sigma}{\sqrt{2n}} = \frac{\sigma}{\sqrt{2} \sqrt{n}} = \frac{\sigma_{\bar{x}}}{\sqrt{2}}$$

   Therefore, the standard deviation decreases by a factor of $\frac{1}{\sqrt{2}}$ (approximately 0.7071).

8. **Mean:** $\mu_{\hat{p}} = p = 0.65$.

   **Standard Deviation:**

   $$\sigma_{\hat{p}} = \sqrt{\frac{p(1 - p)}{n}} = \sqrt{\frac{0.65 \times 0.35}{120}} = \sqrt{\frac{0.2275}{120}} \approx 0.043$$

   **Normal Approximation:**

   $$np = 120 \times 0.65 = 78 \geq 10, \quad n(1 - p) = 120 \times 0.35 = 42 \geq 10$$

   The normal approximation is appropriate.

9. **Solution:**

   **Mean:** $\mu_{\hat{p}} = 0.40$.

   **Standard Deviation:**

   $$\sigma_{\hat{p}} = \sqrt{\frac{0.4 \times 0.6}{80}} = \sqrt{\frac{0.24}{80}} \approx 0.055$$

   Calculate the Z-score:

   $$Z = \frac{0.5 - 0.4}{0.055} \approx \frac{0.1}{0.055} \approx 1.818$$

   Using the standard normal table:

   $$P(\hat{p} > 0.5) = 1 - P(Z \leq 1.818) \approx 1 - 0.9656 = 0.0344$$

   So, there is approximately a 3.44% chance that more than half prefer tea.

10. **Solution:**

    **Mean:** $\mu_{\bar{x}} = 5$ cm.

    **Standard Deviation:**

    $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{0.2}{\sqrt{25}} = \frac{0.2}{5} = 0.04 \text{ cm}$$

    We are asked for $P(4.95 < \bar{x} < 5.05)$. Calculate the Z-scores:

    $$Z_1 = \frac{4.95 - 5}{0.04} = \frac{-0.05}{0.04} = -1.25$$

    $$Z_2 = \frac{5.05 - 5}{0.04} = \frac{0.05}{0.04} = 1.25$$

    Using standard normal table:

    $$P(-1.25 < Z < 1.25) = P(Z < 1.25) - P(Z < -1.25) \approx 0.8944 - 0.1056 = 0.7888$$

    So, there is approximately a 78.88% chance that the sample mean is between 4.95 cm and 5.05 cm.

11. **Solution:**

    Since the population is skewed right, but $n = 36 \geq 30$, we can use the CLT.

    **Mean:** $\mu_{\bar{x}} = 150$ grams.

    **Standard Deviation:**

    $$\sigma_{\bar{x}} = \frac{30}{\sqrt{36}} = \frac{30}{6} = 5 \text{ grams}$$

    Calculate the Z-score:

    $$Z = \frac{155 - 150}{5} = 1$$

    Probability:

    $$P(\bar{x} > 155) = 1 - P(Z \leq 1) = 1 - 0.8413 = 0.1587$$

    There is approximately a 15.87% chance that the sample mean weight is more than 155 grams.

12. Increasing the sample size $n$ increases the denominator in the formula for the standard deviation of the sampling distribution:

    $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

    As $n$ increases, $\sqrt{n}$ increases, so $\sigma_{\bar{x}}$ decreases. This means the variability of the sample mean decreases, making it a more precise estimate of the population mean.

13. **Solution:**

    **Mean:** $\mu_{\hat{p}} = 0.2$.

    **Standard Deviation:**

    $$\sigma_{\hat{p}} = \sqrt{\frac{0.2 \times 0.8}{100}} = \sqrt{\frac{0.16}{100}} = 0.04$$

    Calculate the Z-score:

    $$Z = \frac{0.15 - 0.2}{0.04} = \frac{-0.05}{0.04} = -1.25$$

    Probability:

    $$P(\hat{p} < 0.15) = P(Z < -1.25) \approx 0.1056$$

    So, there's approximately a 10.56% chance that $\hat{p} < 0.15$.

14. **Solution:**

    **Mean:** $\mu_{\bar{x}} = 100$.

    **Standard Deviation:**

    $$\sigma_{\bar{x}} = \frac{15}{\sqrt{50}} \approx 2.121$$

    Calculate the Z-score:

    $$Z = \frac{105 - 100}{2.121} \approx 2.357$$

    Probability:

    $$P(\bar{x} > 105) = 1 - P(Z \leq 2.357) \approx 1 - 0.9906 = 0.0094$$

    So, there is approximately a 0.94% chance that $\bar{x} > 105$.

15. To reduce the standard deviation by half:

    $$\sigma_{\bar{x}}' = \frac{\sigma}{\sqrt{n'}} = \frac{\sigma_{\bar{x}}}{2}$$

    Solving for $n'$:

    $$\frac{\sigma}{\sqrt{n'}} = \frac{1}{2} \left( \frac{\sigma}{\sqrt{n}} \right )$$

    $$\sqrt{n'} = 2 \sqrt{n}$$

    $$n' = 4n = 4 \times 25 = 100$$

    So, a sample size of 100 is needed.

16. **Solution:**

    **Mean:** $\mu_{\bar{x}} = 80$.

    **Standard Deviation:**

    $$\sigma_{\bar{x}} = \frac{16}{\sqrt{64}} = \frac{16}{8} = 2$$

    Calculate the Z-score:

    $$Z = \frac{78 - 80}{2} = \frac{-2}{2} = -1$$

    Probability:

    $$P(\bar{x} < 78) = P(Z < -1) \approx 0.1587$$

    So, there is approximately a 15.87% chance that the sample mean is less than 78.

17. The standard deviation of a population $\sigma$ measures the variability of individual observations in the population. The standard deviation of the sampling distribution (standard error $\sigma_{\bar{x}}$) measures the variability of the sample mean $\bar{x}$ from sample to sample. The standard error is smaller than $\sigma$ and decreases with increasing sample size $n$.

18. **Solution:**

    $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{21}{\sqrt{49}} = \frac{21}{7} = 3$$

19. **Mean of Sampling Distribution:** $\mu_{\bar{x}} = \mu = 500$.

    **Standard Deviation (Standard Error):**

    $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{100}{\sqrt{25}} = \frac{100}{5} = 20$$

20. **Solution:**

    **Mean:** $\mu_{\hat{p}} = 0.30$.

    **Standard Deviation:**

    $$\sigma_{\hat{p}} = \sqrt{\frac{0.3 \times 0.7}{200}} = \sqrt{\frac{0.21}{200}} \approx 0.0324$$

    Calculate the Z-score:

    $$Z = \frac{0.35 - 0.30}{0.0324} \approx \frac{0.05}{0.0324} \approx 1.543$$

    Probability:

    $$P(\hat{p} \geq 0.35) = 1 - P(Z \leq 1.543) \approx 1 - 0.9382 = 0.0618$$

    So, there is approximately a 6.18% chance that at least 35% of the sample has the characteristic.

21. **Solution:**

    The mean of the uniform distribution is:

    $$\mu = \frac{a + b}{2} = \frac{20 + 40}{2} = 30 \text{ minutes}$$

    The standard deviation is:

    $$\sigma = \frac{b - a}{\sqrt{12}} = \frac{40 - 20}{\sqrt{12}} \approx 5.7735 \text{ minutes}$$

    Standard error:

    $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{5.7735}{\sqrt{36}} = \frac{5.7735}{6} \approx 0.9623$$

    Z-score:

    $$Z = \frac{31 - 30}{0.9623} \approx 1.038$$

    Probability:

    $$P(\bar{x} > 31) = 1 - P(Z \leq 1.038) \approx 1 - 0.8508 = 0.1492$$

    So, there's approximately a 14.92% chance that the sample mean assembly time is more than 31 minutes.

22. Yes, according to the Central Limit Theorem, for large sample sizes (usually $n \geq 30$), the sampling distribution of $ \bar{x} $ will be approximately normal regardless of the shape of the population distribution. So with $n = 100$, we can assume the sampling distribution is approximately normal.

23. The shape of the population distribution affects the sampling distribution of $\bar{x}$ especially when the sample size is small. If the population is normal, the sampling distribution of $\bar{x}$ is normal regardless of sample size. If the population is skewed or has heavy tails, the sampling distribution will reflect that skewness or kurtosis unless the sample size is large enough for the Central Limit Theorem to apply. With small sample sizes, the sampling distribution will more closely resemble the population distribution.

24. **Solution:**

    Standard error:

    $$\sigma_{\bar{x}} = \frac{32}{\sqrt{64}} = \frac{32}{8} = 4$$

    We need $P(|\bar{x} - \mu| > 5)$.

    Calculate the Z-scores:

    $$Z = \frac{5}{4} = 1.25$$

    Probability:

    $$P(|\bar{x} - \mu| > 5) = 2 \times P(Z > 1.25) = 2 \times (1 - P(Z \leq 1.25)) = 2 \times (1 - 0.8944) = 2 \times 0.1056 = 0.2112$$

    So, there is approximately a 21.12% chance that the sample mean differs from the population mean by more than 5 units.