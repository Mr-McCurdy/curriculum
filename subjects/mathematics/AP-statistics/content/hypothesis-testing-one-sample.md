# **Hypothesis Testing: 1-Sample t-Test for Population Mean and 1-Sample z-Test for Population Proportion**

---

## Introduction

In the realm of statistics, **hypothesis testing** is an essential tool for making inferences about population parameters based on sample data. By systematically evaluating evidence, hypothesis tests enable researchers and analysts to make informed decisions and draw meaningful conclusions. This tutorial focuses on two fundamental hypothesis tests:

1. **1-Sample t-Test for Population Mean**
2. **1-Sample z-Test for Population Proportion**

Furthermore, we will explore how these tests interrelate with **confidence intervals**, enhancing your ability to interpret and apply statistical findings effectively. This guide provides a step-by-step approach to conducting these tests manually, utilizing z-score and t-score tables, without the aid of calculators or statistical software.

---

## What is Hypothesis Testing?

**Hypothesis testing** is a statistical method that allows us to make decisions or inferences about population parameters based on sample data. It involves formulating two competing hypotheses:

- **Null Hypothesis ($H_0$)**: A statement of no effect or no difference, serving as the default or starting assumption.
- **Alternative Hypothesis ($H_a$ or $H_1$)**: A statement that contradicts the null hypothesis, indicating the presence of an effect or difference.

The objective is to determine whether there is sufficient evidence in the sample data to reject the null hypothesis in favor of the alternative hypothesis.

### **Key Components:**

1. **Significance Level ($\alpha$)**: The probability threshold for rejecting the null hypothesis, commonly set at 0.05 (5%).
2. **Test Statistic**: A standardized value calculated from sample data, used to decide whether to reject $H_0$.
3. **Critical Value(s)**: The cutoff point(s) on the test statistic distribution, beyond which we reject $H_0$.
4. **P-Value**: The probability of observing a test statistic as extreme as, or more extreme than, the one calculated from the sample, assuming $H_0$ is true.

---

## 1-Sample t-Test for Population Mean

The **1-sample t-test** is used to determine whether the mean of a single population differs significantly from a known or hypothesized population mean. This test is particularly useful when the population standard deviation ($\sigma$) is unknown and the sample size is small ($n < 30$).

### **When to Use:**

- Estimating the population mean when $\sigma$ is unknown.
- Comparing a sample mean to a known value.
- Assessing the effectiveness of a treatment or intervention.

### **Assumptions and Preconditions:**

Before conducting a 1-sample t-test, certain assumptions must be met to ensure the validity of the test. These assumptions are based on the population parameters ($\mu$) and the sample data:

1. **Random Sampling**: The sample must be randomly selected from the population, ensuring that each member has an equal chance of being included.
2. **Normality**: The population from which the sample is drawn should be approximately normally distributed. For smaller samples ($n < 30$), the normality assumption is critical. For larger samples, the Central Limit Theorem allows for some deviation from normality.
3. **Independence**: Observations should be independent of one another.

**Note:** The assumption of normality is verified using the population parameter $\mu$. If the population distribution is known to be normal or the sample size is sufficiently large, the normality condition is satisfied.

### **Steps to Perform a 1-Sample t-Test by Hand:**

1. **State the Hypotheses:**
   
   - **Null Hypothesis ($H_0$)**: $\mu = \mu_0$
   - **Alternative Hypothesis ($H_a$)**: $\mu \neq \mu_0$ (two-tailed), $\mu > \mu_0$ (right-tailed), or $\mu < \mu_0$ (left-tailed)

2. **Choose the Significance Level ($\alpha$):**
   
   Common choices are 0.05, 0.01, or 0.10.

3. **Calculate the Test Statistic (t):**
   
$$
t = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}}
$$
   
   Where:
   - $\bar{x}$ = Sample mean
   - $\mu_0$ = Hypothesized population mean
   - $s$ = Sample standard deviation
   - $n$ = Sample size

4. **Determine the Degrees of Freedom (df):**
   
$$
df = n - 1
$$

5. **Find the Critical t-Value ($t^*$) from the t-Distribution Table:**
   
   Use the degrees of freedom and the chosen $\alpha$ to locate the critical value for a two-tailed or one-tailed test.

6. **Make a Decision:**
   
   - **Two-Tailed Test:** Reject $H_0$ if $|t| > t^*$.
   - **One-Tailed Test:** Reject $H_0$ if $t > t^* \text{(right-tailed) or }t < -t^* \text{left-tailed}$.

7. **Conclusion:**
   
   Interpret the results in the context of the problem.

### **Example:**

**Problem:**
A teacher believes that the average score of her class on a standardized test is 75. After administering the test, she finds that a sample of 25 students has an average score of 78 with a sample standard deviation of 10. Test the teacher's belief at the 5% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $\mu = 75$
   - $H_a$: $\mu \neq 75$ (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.05$

3. **Calculate the Test Statistic:**
   
$$
t = \frac{78 - 75}{10 / \sqrt{25}} = \frac{3}{2} = 1.5
$$

4. **Degrees of Freedom:**
   
$$
df = 25 - 1 = 24
$$

5. **Critical t-Value:**
   
   From the t-distribution table, for $df = 24$ and $\alpha = 0.05$ (two-tailed), $t^* \approx 2.064$

6. **Decision:**
   
   $|1.5| < 2.064$ → Do not reject $H_0$

7. **Conclusion:**
   
   There is not enough evidence at the 5% significance level to conclude that the average score differs from 75.

---

## 1-Sample z-Test for Population Proportion

The **1-sample z-test** is employed to determine whether the proportion of successes in a single population differs significantly from a known or hypothesized population proportion. This test is suitable when the sample size is large enough to justify the normal approximation.

### **When to Use:**

- Comparing a sample proportion to a known population proportion.
- Evaluating the effectiveness of a marketing campaign, voting behavior, etc.

### **Assumptions and Preconditions:**

Before conducting a 1-sample z-test, certain assumptions must be met to ensure the validity of the test. These assumptions are based on the population parameter ($p$) and the sample data:

1. **Random Sampling**: The sample must be randomly selected from the population, ensuring that each member has an equal chance of being included.
2. **Normality**: The sampling distribution of the proportion is approximately normal. This is ensured if both:
   
   $$
   np \geq 10 \quad \text{and} \quad n(1 - p) \geq 10
   $$
   
   Where:
   - $n$ = Sample size
   - $p$ = Population proportion
   
3. **Independence**: Observations should be independent of one another.

**Note:** The assumptions regarding the population proportion $p$ are critical for validating the normality condition. Ensuring that $np \geq 10$ and $n(1 - p) \geq 10$ guarantees that the sampling distribution of $\hat{p}$ is sufficiently normal to apply the z-test.

### **Steps to Perform a 1-Sample z-Test by Hand:**

1. **State the Hypotheses:**
   
   - **Null Hypothesis ($H_0$)**: $p = p_0$
   - **Alternative Hypothesis ($H_a$)**: $p \neq p_0$ (two-tailed), $p > p_0$ (right-tailed), or $p < p_0$ (left-tailed)

2. **Choose the Significance Level ($\alpha$):**
   
   Common choices are 0.05, 0.01, or 0.10.

3. **Calculate the Test Statistic (z):**
   
   $$
   z = \frac{\hat{p} - p_0}{\sqrt{ \frac{p_0(1 - p_0)}{n} }}
   $$
   
   Where:
   - $\hat{p}$ = Sample proportion
   - $p_0$ = Hypothesized population proportion
   - $n$ = Sample size

4. **Find the Critical z-Value ($z^*$) from the Standard Normal Distribution Table:**
   
   Use the chosen $\alpha$ to locate the critical value for a two-tailed or one-tailed test.

5. **Make a Decision:**
   
   - **Two-Tailed Test:** Reject $H_0$ if $|z| > z^*$.
   - **One-Tailed Test:** Reject $H_0$ if $z > z^*$ (right-tailed) or $z < -z^*$ (left-tailed).

6. **Conclusion:**
   
   Interpret the results in the context of the problem.

### **Example:**

**Problem:**
A company claims that 40% of its customers are satisfied with their service. In a sample of 200 customers, 90 report being satisfied. Test the company's claim at the 1% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $p = 0.40$
   - $H_a$: $p \neq 0.40$ (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.01$

3. **Check Conditions:**
   
   $np_0 = 200 \times 0.40 = 80 \geq 10$
   
   $n(1 - p_0) = 200 \times 0.60 = 120 \geq 10$
   
   Conditions met; normal approximation is appropriate.

4. **Calculate the Test Statistic:**
   
   $\hat{p} = \frac{90}{200} = 0.45$
   
   $$
   z = \frac{0.45 - 0.40}{\sqrt{ \frac{0.40 \times 0.60}{200} }} = \frac{0.05}{\sqrt{ \frac{0.24}{200} }} = \frac{0.05}{0.0346} \approx 1.447
   $$

5. **Critical z-Value:**
   
   From the standard normal table, for $\alpha = 0.01$ (two-tailed), $z^* \approx 2.576$

6. **Decision:**
   
   $|1.447| < 2.576$ → Do not reject $H_0$

7. **Conclusion:**
   
   There is not enough evidence at the 1% significance level to reject the company's claim that 40% of its customers are satisfied.

---

## Relationship Between Hypothesis Tests and Confidence Intervals

**Confidence intervals** and **hypothesis tests** are intrinsically linked, both serving as methods for making inferences about population parameters based on sample data. Understanding their relationship enhances the interpretation and application of statistical analyses.

### **Connection Points:**

1. **Complementary Concepts:**
   
   - **Confidence Interval:** Provides a range of plausible values for a population parameter with a specified confidence level.
   - **Hypothesis Test:** Assesses whether there is enough evidence to reject a null hypothesis about a population parameter.

2. **Duality:**
   
   For any two-tailed hypothesis test, if the hypothesized parameter value lies outside the corresponding confidence interval, the null hypothesis is rejected at the complementary significance level.
   
   - **Example:** A 95% confidence interval corresponds to a hypothesis test with $\alpha = 0.05$.

3. **Decision Making:**
   
   - If the null hypothesis value is **not** contained within the confidence interval, reject $H_0$.
   - If the null hypothesis value **is** contained within the confidence interval, do not reject $H_0$.

4. **Interpretation:**
   
   Confidence intervals offer more information by providing a range of plausible values, while hypothesis tests offer a binary decision regarding the null hypothesis.

### **Example of Duality:**

Consider the 1-sample z-test for a population proportion:

- **Hypothesis Test:**
  
  - $H_0$: $p = 0.40$
  - $H_a$: $p \neq 0.40$
  - $\alpha = 0.05$

- **Confidence Interval:**
  
  - 95% confidence interval for $p$: $(0.4109, 0.6891)$

**Decision:**

- Since $0.40$ (the null hypothesis value) is **not** within the confidence interval, we reject $H_0$.
- Conversely, if $0.40$ were within the interval, we would not reject $H_0$.

This demonstrates how confidence intervals and hypothesis tests are two sides of the same coin, providing complementary insights into the population parameter based on sample data.

---

## Properties of Hypothesis Tests and Confidence Intervals

1. **Interval Width and Significance Level:**
   
   - **Higher Confidence Level ($1 - \alpha$)**: Results in a wider confidence interval and a higher critical value, making it harder to reject $H_0$.
   - **Lower Confidence Level ($1 - \alpha$)**: Results in a narrower confidence interval and a lower critical value, making it easier to reject $H_0$.

2. **Sample Size:**
   
   - **Larger Sample Size ($n$)**: Leads to a narrower confidence interval and a smaller standard error, increasing the precision of estimates.
   - **Smaller Sample Size ($n$)**: Leads to a wider confidence interval and a larger standard error, decreasing the precision of estimates.

3. **Standard Error (SE):**
   
   - **For Means:** $SE = \frac{s}{\sqrt{n}}$ or $SE = \frac{\sigma}{\sqrt{n}}$
   - **For Proportions:** $SE = \sqrt{ \frac{\hat{p}(1 - \hat{p})}{n} }$

4. **Interpretation:**
   
   - **Confidence Interval:** Provides a range where the true parameter is likely to lie.
   - **Hypothesis Test:** Provides a decision on whether to reject $H_0$ based on sample evidence.

---

## Worked Examples

### Example 1: 1-Sample t-Test for Population Mean

**Problem:**
A manufacturer claims that the average lifetime of its batteries is 500 hours with an unknown standard deviation. A random sample of 25 batteries has an average lifetime of 480 hours with a sample standard deviation of 50 hours. Test the manufacturer's claim at the 5% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $\mu = 500$ hours
   - $H_a$: $\mu \neq 500$ hours (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.05$

3. **Check Preconditions:**
   
   - **Random Sampling:** Assumed to be satisfied.
   - **Normality:** Population is assumed to be normally distributed (critical for small sample sizes).
   - **Independence:** Assumed to be satisfied.

4. **Calculate the Test Statistic:**
   
   $$
   t = \frac{480 - 500}{50 / \sqrt{25}} = \frac{-20}{10} = -2.0
   $$

5. **Degrees of Freedom:**
   
   $df = 25 - 1 = 24$

6. **Find the Critical t-Value ($t^*$):**
   
   From the t-distribution table, for $df = 24$ and $\alpha = 0.05$ (two-tailed), $t^* \approx 2.064$

7. **Make a Decision:**
   
   $|-2.0| < 2.064$ → Do not reject $H_0$

8. **Conclusion:**
   
   There is not enough evidence at the 5% significance level to reject the manufacturer's claim that the average lifetime of the batteries is 500 hours.

---

### Example 2: 1-Sample z-Test for Population Proportion

**Problem:**
In a survey of 200 voters, 120 reported supporting a particular candidate. The candidate claims that 60% of voters support them. Test the candidate's claim at the 1% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $p = 0.60$
   - $H_a$: $p \neq 0.60$ (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.01$

3. **Check Preconditions:**
   
   - $np_0 = 200 \times 0.60 = 120 \geq 10$
   - $n(1 - p_0) = 200 \times 0.40 = 80 \geq 10$
   
   Conditions met; normal approximation is appropriate.

4. **Calculate the Test Statistic:**
   
   $\hat{p} = \frac{120}{200} = 0.60$
   
   $$
   z = \frac{0.60 - 0.60}{\sqrt{ \frac{0.60 \times 0.40}{200} }} = \frac{0}{\sqrt{ \frac{0.24}{200} }} = 0
   $$

5. **Find the Critical z-Value ($z^*$):**
   
   From the standard normal table, for $\alpha = 0.01$ (two-tailed), $z^* \approx 2.576$

6. **Make a Decision:**
   
   $|0| < 2.576$ → Do not reject $H_0$

7. **Conclusion:**
   
   There is not enough evidence at the 1% significance level to reject the candidate's claim that 60% of voters support them.

---

## Relationship Between Hypothesis Tests and Confidence Intervals

**Confidence intervals** and **hypothesis tests** are two sides of the same statistical coin, both providing insights into population parameters based on sample data. Understanding their relationship is crucial for comprehensive statistical analysis.

### **Complementary Nature:**

- **Confidence Interval:** Provides a range of plausible values for a population parameter with a specified confidence level.
- **Hypothesis Test:** Assesses whether there is enough evidence to reject a null hypothesis about a population parameter.

### **Duality Principle:**

For any two-tailed hypothesis test at significance level $\alpha$, the corresponding confidence interval will have a confidence level of $1 - \alpha$. Specifically:

- If the hypothesized parameter value ($\mu_0$ or $p_0$) lies **outside** the confidence interval, we **reject** $H_0$.
- If the hypothesized parameter value lies **inside** the confidence interval, we **do not reject** $H_0$.

**Example of Duality:**

Consider a 95% confidence interval for a population mean $\mu$:

- **Confidence Interval:** $\bar{x} \pm t^* \times \frac{s}{\sqrt{n}}$
- **Hypothesis Test:** Testing $H_0: \mu = \mu_0$ vs. $H_a: \mu \neq \mu_0$ at $\alpha = 0.05$

If $\mu_0$ is **not** within the 95% confidence interval, we reject $H_0$ at the 5% significance level.

### **Practical Implications:**

1. **Interpretation:**
   
   - **Confidence Interval:** Offers a range of plausible values for the parameter, providing more information than a simple acceptance or rejection of $H_0$.
   - **Hypothesis Test:** Provides a clear decision about the validity of $H_0$.

2. **Decision Making:**
   
   - Confidence intervals can be used to inform or corroborate the results of hypothesis tests, ensuring consistency in statistical conclusions.

3. **Comprehensive Analysis:**
   
   - Utilizing both confidence intervals and hypothesis tests offers a more nuanced understanding of the data, facilitating better decision-making processes.

---

## Properties and Best Practices

1. **Interval Width and Confidence Level:**
   
   - **Higher Confidence Level ($1 - \alpha$)**: Results in a wider interval and a higher critical value, making it harder to reject $H_0$.
   - **Lower Confidence Level ($1 - \alpha$)**: Results in a narrower interval and a lower critical value, making it easier to reject $H_0$.

2. **Sample Size:**
   
   - **Larger Sample Size ($n$)**: Leads to a narrower confidence interval and a smaller standard error, increasing the precision of estimates.
   - **Smaller Sample Size ($n$)**: Leads to a wider confidence interval and a larger standard error, decreasing the precision of estimates.

3. **Standard Error (SE):**
   
   - **For Means:** $SE = \frac{s}{\sqrt{n}}$ or $SE = \frac{\sigma}{\sqrt{n}}$
   - **For Proportions:** $SE = \sqrt{ \frac{\hat{p}(1 - \hat{p})}{n} }$

4. **Interpretation:**
   
   - **Confidence Interval:** Provides a range where the true parameter is likely to lie.
   - **Hypothesis Test:** Provides a decision on whether to reject $H_0$ based on sample evidence.

---

## Worked Examples

### Example 3: 1-Sample t-Test with Small Sample Size

**Problem:**
A researcher claims that the average time employees spend on social media during work hours is 30 minutes per day. A random sample of 16 employees reports an average of 35 minutes with a sample standard deviation of 5 minutes. Test the researcher's claim at the 10% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $\mu = 30$ minutes
   - $H_a$: $\mu \neq 30$ minutes (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.10$

3. **Check Preconditions:**
   
   - **Random Sampling:** Assumed to be satisfied.
   - **Normality:** Population is assumed to be normally distributed (critical for small sample sizes).
   - **Independence:** Assumed to be satisfied.

4. **Calculate the Test Statistic:**
   
   $$
   t = \frac{35 - 30}{5 / \sqrt{16}} = \frac{5}{1.25} = 4.0
   $$

5. **Degrees of Freedom:**
   
   $df = 16 - 1 = 15$

6. **Find the Critical t-Value ($t^*$):**
   
   From the t-distribution table, for $df = 15$ and $\alpha = 0.10$ (two-tailed), $t^* \approx 1.753$

7. **Make a Decision:**
   
   $|4.0| > 1.753$ → Reject $H_0$

8. **Conclusion:**
   
   There is enough evidence at the 10% significance level to reject the researcher's claim that the average time employees spend on social media during work hours is 30 minutes per day.

---

### Example 4: 1-Sample z-Test for Population Proportion

**Problem:**
A marketing team claims that 25% of consumers prefer their new product over the competitor's. In a sample of 400 consumers, 120 prefer the new product. Test the marketing team's claim at the 5% significance level.

**Solution:**

1. **State the Hypotheses:**
   
   - $H_0$: $p = 0.25$
   - $H_a$: $p \neq 0.25$ (two-tailed)

2. **Significance Level:**
   
   $\alpha = 0.05$

3. **Check Preconditions:**
   
   - $np_0 = 400 \times 0.25 = 100 \geq 10$
   - $n(1 - p_0) = 400 \times 0.75 = 300 \geq 10$
   
   Conditions met; normal approximation is appropriate.

4. **Calculate the Test Statistic:**
   
   $\hat{p} = \frac{120}{400} = 0.30$
   
   $$
   z = \frac{0.30 - 0.25}{\sqrt{ \frac{0.25 \times 0.75}{400} }} = \frac{0.05}{\sqrt{ \frac{0.1875}{400} }} = \frac{0.05}{0.0217} \approx 2.303
   $$

5. **Critical z-Value:**
   
   From the standard normal table, for $\alpha = 0.05$ (two-tailed), $z^* \approx 1.96$

6. **Decision:**
   
   $|2.303| > 1.96$ → Reject $H_0$

7. **Conclusion:**
   
   There is enough evidence at the 5% significance level to reject the marketing team's claim that 25% of consumers prefer their new product over the competitor's.

---

## Best Practices for Performing Hypothesis Tests by Hand

1. **Understand the Problem Context:**
   
   Clearly define what you are testing and ensure that the appropriate test (t-test or z-test) is selected based on the known parameters and sample size.

2. **Organize Your Data:**
   
   Gather all necessary information such as sample mean ($\bar{x}$), sample standard deviation ($s$), sample size ($n$), and hypothesized population parameter ($\mu_0$ or $p_0$).

3. **Follow the Steps Methodically:**
   
   Adhere to the structured steps outlined for each test to avoid calculation errors and ensure accurate results.

4. **Use Tables Effectively:**
   
   Familiarize yourself with z-score and t-score tables to quickly locate critical values based on your significance level and degrees of freedom.

5. **Double-Check Calculations:**
   
   Manual calculations are prone to errors. Revisit each step to verify accuracy, especially when dealing with square roots and division.

6. **Interpret Results in Context:**
   
   Beyond the numerical outcome, provide meaningful interpretations that relate back to the original problem or research question.

7. **Practice Regularly:**
   
   Enhance proficiency by working through various examples and scenarios, solidifying your understanding of when and how to apply each test.

8. **Verify Assumptions:**
   
   Always check that the preconditions and assumptions for the test are met. This includes verifying the normality conditions based on the population parameters ($\mu$ or $p$) and sample size.

---

## Additional Resources

- **Statistical Tables:**
  
  - [Standard Normal (Z) Table](https://www.mathsisfun.com/data/standard-normal-distribution-table.html)
  - [t-Distribution Table](https://www.mathsisfun.com/data/t-distribution-table.html)

- **Tutorials and Guides:**
  
  - [Khan Academy: Hypothesis Testing](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals)
  - [Statistics How To: t-Test](https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/t-test/)
  - [Statistics How To: z-Test](https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/z-test/)

- **Software Tools:**
  
  - **Excel:** Useful for large datasets and automated calculations.
  - **R and Python:** Powerful programming languages for statistical analysis and visualization.

---

## Conclusion

Hypothesis testing and confidence intervals are foundational tools in statistical inference, each offering unique perspectives on population parameters. The **1-sample t-test** and **1-sample z-test** allow for rigorous assessments of population means and proportions, respectively, facilitating informed decision-making across various fields such as medicine, business, and social sciences.

By mastering the manual calculation of these tests using z-score and t-score tables, you gain a deeper understanding of the underlying statistical principles, enhancing your ability to interpret and apply statistical findings effectively.

---

# **Exercises**

1. **1-Sample t-Test for Population Mean:**
   
   A researcher claims that the average number of hours spent on homework per week by high school students is 15 hours. A random sample of 20 students has an average of 17 hours with a sample standard deviation of 4 hours. Test the researcher's claim at the 5% significance level.

2. **1-Sample z-Test for Population Proportion:**
   
   In a sample of 500 voters, 275 support a new policy. The government claims that 50% of voters support the policy. Test the government's claim at the 1% significance level.

3. **Confidence Interval and Hypothesis Test Relationship:**
   
   A 95% confidence interval for the population mean is (48, 52). Conduct a hypothesis test to determine if the population mean is equal to 50 at the 5% significance level. State your conclusion.

4. **Determining Appropriate Test:**
   
   You want to test if the proportion of defective items in a production line is less than 2%. You collect a sample of 300 items and find that 4 are defective. Decide whether to use a z-test or t-test and justify your choice.

5. **Calculating Critical Value:**
   
   For a two-tailed 99% confidence interval, what are the critical z-values? Use these values to explain when to reject the null hypothesis in a z-test.

6. **Effect of Sample Size on Test Statistic:**
   
   Explain how increasing the sample size affects the standard error and the test statistic in both the t-test and z-test. What implications does this have for hypothesis testing?

7. **Interpreting Test Results:**
   
   After performing a 1-sample t-test, you obtain a p-value of 0.03. If your significance level is 0.05, what decision do you make regarding the null hypothesis? What if your significance level was 0.01?

8. **Calculating Test Statistic Manually:**
   
   A sample of 30 students has a mean score of 85 with a sample standard deviation of 5. The national average score is 80. Perform a 1-sample t-test at the 5% significance level to determine if the sample mean is significantly different from the national average.

9. **Relating Confidence Interval to Hypothesis Test:**
   
   Construct a 90% confidence interval for a population proportion based on a sample proportion of 0.45 from a sample size of 100. Using this interval, determine whether to reject $H_0: p = 0.40$ at the 5% significance level.

10. **Understanding Assumptions:**
    
    Discuss why it is important to verify the normality conditions based on population parameters ($\mu$ and $p$) before conducting hypothesis tests. What could be the consequences of violating these assumptions?

---

**Happy Testing!**  
Mastering hypothesis testing empowers you to make data-driven decisions with confidence and precision. By understanding and applying the 1-sample t-test and z-test, you are well-equipped to tackle a wide range of statistical challenges.

---