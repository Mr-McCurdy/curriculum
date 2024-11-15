# **Review Assignment: Normal and Sampling Distributions**

This review assignment is designed to assess and reinforce your understanding of the **Normal Distribution**, **Sampling Distributions for Sample Means**, and **Sampling Distributions for Sample Proportions**. Additionally, a comprehensive tutorial is provided to ensure you have the foundational knowledge required to tackle these problems effectively.

---

## **Tutorial: Primer on Normal and Sampling Distributions**

### **1. Normal Distribution**

The **Normal Distribution** is a continuous probability distribution characterized by its bell-shaped curve, symmetric about the mean. It is defined by two parameters:
- **Mean ($\mu$)**: The central value around which the data is distributed.
- **Standard Deviation ($\sigma$)**: Measures the spread or dispersion of the distribution.

#### **Key Properties:**
- **Symmetry**: The distribution is symmetric around the mean.
- **Empirical Rule (68-95-99.7 Rule)**:
  - **68%** of the data falls within $\mu \pm \sigma$.
  - **95%** within $\mu \pm 2\sigma$.
  - **99.7%** within $\mu \pm 3\sigma$.
- **Total Area Under the Curve**: Equals 1.

#### **Standard Normal Distribution:**
A special case of the normal distribution with:
- **Mean ($\mu$)**: 0
- **Standard Deviation ($\sigma$)**: 1

To convert any normal distribution to the standard normal distribution, use the **z-score** formula:

$$
z = \frac{X - \mu}{\sigma}
$$

Where:
- $X$ = value from the original distribution
- $\mu$ = mean of the original distribution
- $\sigma$ = standard deviation of the original distribution

#### **Using Z-Tables:**
Z-tables provide the cumulative probability $P(Z \leq z)$ for the standard normal distribution. To find probabilities:
- **Between two values**: $P(a < Z < b) = P(Z < b) - P(Z < a)$
- **Greater than a value**: $P(Z > a) = 1 - P(Z < a)$
- **Less than a value**: $P(Z < a)$ directly from the table

### **2. Sampling Distribution of Sample Means**

When taking repeated samples from a population and calculating their means, the **Sampling Distribution of the Sample Mean ($\bar{x}$)** describes the distribution of these means.

#### **Key Concepts:**
- **Mean of the Sampling Distribution ($\mu_{\bar{x}}$)**:

$$
\mu_{\bar{x}} = \mu
$$

- **Standard Deviation of the Sampling Distribution (Standard Error, $SE_{\bar{x}}$)**:
  
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$
  
  Where $n$ = sample size
- **Central Limit Theorem (CLT)**:
  - Regardless of the population distribution shape, the sampling distribution of the sample mean approaches a normal distribution as the sample size $n$ increases (typically $n \geq 30$).

#### **Implications of CLT:**
- Enables the use of normal probability methods for inference even when the population distribution is not normal, provided $n$ is sufficiently large.

### **3. Sampling Distribution of Sample Proportions**

When taking repeated samples from a population and calculating their proportions, the **Sampling Distribution of the Sample Proportion ($\hat{p}$)** describes the distribution of these proportions.

#### **Key Concepts:**
- **Mean of the Sampling Distribution ($\mu_{\hat{p}}$)**:
  
$$
\mu_{\hat{p}} = p
$$
  
  Where $p$ = population proportion
- **Standard Deviation of the Sampling Distribution (Standard Error, $SE_{\hat{p}}$)**:
  
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} }
$$
  
  Where $n$ = sample size
- **Normal Approximation Conditions**:
  - $np \geq 10$ and $n(1 - p) \geq 10$
  - Ensures the sampling distribution of $\hat{p}$ is approximately normal

#### **Implications:**
- Facilitates the use of z-scores and normal probability methods for proportion-based inference.

---

## **Normal Distribution**

1. The weight of a package is normally distributed with a mean of 55 grams and a standard deviation of 6 grams. What is the probability that a randomly selected package weighs between 49 and 61 grams?

2. A standardized test has scores that are normally distributed with a mean of 520 and a standard deviation of 80. What is the probability that a student scores between 440 and 600?

3. The height of trees in a forest is normally distributed with a mean of 180 cm and a standard deviation of 15 cm. What is the probability that a randomly selected tree is taller than 195 cm?

4. In a normal distribution with a mean of 85 and a standard deviation of 12, what is the probability that a value is less than 70?

5. IQ scores in a population are normally distributed with a mean of 100 and a standard deviation of 15. What is the probability that a randomly selected person has an IQ between 95 and 115?

6. The time to complete a task is normally distributed with a mean of 45 minutes and a standard deviation of 7 minutes. What is the probability that the task takes more than 52 minutes?

7. A test score is normally distributed with a mean of 65 and a standard deviation of 9. What is the probability that a student scores less than 58?

8. The diameter of pipes manufactured by a company is normally distributed with a mean of 5.5 cm and a standard deviation of 0.3 cm. What is the probability that a randomly selected pipe has a diameter greater than 5.8 cm?

9. A machine fills bottles with soda, and the fill amount is normally distributed with a mean of 500 ml and a standard deviation of 20 ml. What is the probability that a bottle contains between 480 ml and 520 ml of soda?

10. The lifespan of a type of light bulb is normally distributed with a mean of 1000 hours and a standard deviation of 100 hours. What is the probability that a randomly selected bulb lasts less than 950 hours?

11. The diameter of screws produced by a machine is normally distributed with a mean of 4.8 mm and a standard deviation of 0.15 mm. What is the probability that a randomly selected screw has a diameter between 4.7 mm and 4.9 mm?

12. A population of fish has lengths normally distributed with a mean of 25 cm and a standard deviation of 2 cm. What is the probability that a randomly selected fish is longer than 28 cm?

---

## **Sampling Distribution of Sample Means**

13. A population has a mean $\mu = 200$ and a standard deviation $\sigma = 25$. For a sample of size 36, find the mean and standard deviation of the sampling distribution of the sample mean $\bar{x}$.

14. If a population has a mean $\mu = 75$ and a standard deviation $\sigma = 15$, what is the standard error of the sample mean for a sample size of 64?

15. The lifetimes of batteries are normally distributed with a mean of 800 hours and a standard deviation of 50 hours. If a sample of 25 batteries is selected, what is the probability that the sample mean lifetime is between 790 and 810 hours?

16. A factory produces widgets with a mean weight of 150 grams and a standard deviation of 10 grams. If a random sample of 49 widgets is selected, what is the probability that the sample mean weight is more than 152 grams?

17. The heights of students in a university are normally distributed with a mean of 170 cm and a standard deviation of 8 cm. What is the probability that the sample mean height of a sample of 25 students is less than 168 cm?

18. A population has a mean $\mu = 500$ and a standard deviation $\sigma = 80$. For a sample of size 100, calculate the mean and standard deviation of the sampling distribution of $\bar{x}$.

19. The amount of time (in minutes) that customers spend in a bank is normally distributed with a mean of 30 minutes and a standard deviation of 5 minutes. What is the probability that the sample mean time for a sample of 25 customers is between 29 and 31 minutes?

20. A population has a mean $\mu = 120$ and a standard deviation $\sigma = 15$. If we take all possible samples of size 64, what will be the mean and standard deviation of the sampling distribution of $\bar{x}$?

21. The diameters of screws produced by a machine are normally distributed with a mean of 4.5 mm and a standard deviation of 0.1 mm. If a sample of 16 screws is selected, what is the probability that the sample mean diameter is greater than 4.55 mm?

22. The weight of apples in an orchard is normally distributed with a mean of 150 grams and a standard deviation of 30 grams. If a random sample of 36 apples is selected, what is the probability that the sample mean weight is more than 155 grams?

23. A sample of 64 observations is taken from a population with a standard deviation of 32. What is the probability that the sample mean differs from the population mean by more than 5 units?

24. A population has a mean of 500 and a standard deviation of 100. If we take all possible samples of size 25, what will be the mean and standard deviation of the sampling distribution of $\bar{x}$?

---

## **Sampling Distribution of Sample Proportions**

25. A population has a proportion $p = 0.40$. For a sample size of 150, calculate the mean and standard deviation of the sampling distribution of the sample proportion $\hat{p}$. Is the normal approximation appropriate?

26. In a population, $p = 0.25$. For a sample of size 200, find the standard deviation of the sampling distribution of $\hat{p}$. Is the normal approximation justified?

27. A survey finds that 38% of people prefer online shopping over in-store shopping. If we take a sample of 180 people, what is the probability that more than 40% of the sample prefers online shopping? Assume the normal approximation is appropriate.

28. A company claims that 30% of its customers are satisfied with their service. In a sample of 250 customers, 80 report being satisfied. Test the company's claim at the 5% significance level. Is the normal approximation appropriate for this test?

29. A population has a proportion $p = 0.35$. For a sample size of 120, calculate the mean and standard deviation of the sampling distribution of $\hat{p}$. Verify if the normal approximation is appropriate.

30. In a population, $p = 0.20$. For a sample of size 150, what is the probability that the sample proportion $\hat{p}$ is less than 0.15?

31. A survey indicates that 55% of customers are satisfied with a service. If a sample of 180 customers is taken, what is the probability that less than 50% are satisfied? Assume the normal approximation is appropriate.

32. A population has a proportion $p = 0.28$. For a sample size of 250, calculate the mean and standard deviation of the sampling distribution of $\hat{p}$. Is the normal approximation appropriate?

33. A survey finds that 42% of people prefer tea over coffee. If we take a sample of 100 people, what is the probability that more than 45% prefer tea? Assume the normal approximation is appropriate.

34. In a population, $p = 0.50$. For a sample size of 300, what is the probability that the sample proportion $\hat{p}$ is between 0.45 and 0.55?

35. A company claims that 25% of its products are defective. In a sample of 400 products, 100 are found defective. Test the company's claim at the 5% significance level. Is the normal approximation appropriate?

36. A population has a proportion $p = 0.60$. For a sample size of 200, what is the probability that the sample proportion $\hat{p}$ is greater than 0.65? Assume the normal approximation is appropriate.

---

## **Solutions**

### **Normal Distribution**

**Problem 1:**  
*The weight of a package is normally distributed with a mean of 55 grams and a standard deviation of 6 grams. What is the probability that a randomly selected package weighs between 49 and 61 grams?*

**Solution:**
1. **Identify Parameters:**
   - Mean ($\mu$) = 55 grams
   - Standard Deviation ($\sigma$) = 6 grams
   - $X$ = 49 grams and 61 grams

2. **Calculate Z-scores:**
   
$$
z_1 = \frac{49 - 55}{6} = \frac{-6}{6} = -1.0 
$$

$$
z_2 = \frac{61 - 55}{6} = \frac{6}{6} = 1.0
$$

3. **Find Probabilities from Z-table:**
   - $P(Z < 1.0) = 0.8413$
   - $P(Z < -1.0) = 0.1587$

4. **Calculate Probability Between 49 and 61 grams:**
   
$$
P(49 < X < 61) = P(Z < 1.0) - P(Z < -1.0) = 0.8413 - 0.1587 = 0.6826
$$

**Conclusion:**  
There is approximately a **68.26%** probability that a randomly selected package weighs between 49 and 61 grams.

---

### **Sampling Distribution of Sample Means**

**Problem 13:**  
*A population has a mean $\mu = 200$ and a standard deviation $\sigma = 25$. For a sample of size 36, find the mean and standard deviation of the sampling distribution of the sample mean $\bar{x}$.*

**Solution:**
1. **Mean of Sampling Distribution ($\mu_{\bar{x}}$):**
   
$$
\mu_{\bar{x}} = \mu = 200
$$

2. **Standard Deviation of Sampling Distribution (Standard Error, $SE_{\bar{x}}$):**
   
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{25}{\sqrt{36}} = \frac{25}{6} \approx 4.1667
$$

**Conclusion:**  
- **Mean ($\mu_{\bar{x}}$)** = 200  
- **Standard Error ($SE_{\bar{x}}$)** ≈ 4.1667

---

### **Sampling Distribution of Sample Proportions**

**Problem 25:**  
*A population has a proportion $p = 0.40$. For a sample size of 150, calculate the mean and standard deviation of the sampling distribution of the sample proportion $\hat{p}$. Is the normal approximation appropriate?*

**Solution:**
1. **Mean of Sampling Distribution ($\mu_{\hat{p}}$):**
   
$$
\mu_{\hat{p}} = p = 0.40
$$

2. **Standard Deviation of Sampling Distribution (Standard Error, $SE_{\hat{p}}$):**
   
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} } = \sqrt{ \frac{0.40 \times 0.60}{150} } = \sqrt{ \frac{0.24}{150} } = \sqrt{0.0016} = 0.04
$$

3. **Check Normal Approximation Conditions:**
   
$$
np = 150 \times 0.40 = 60 \geq 10 
$$

$$
n(1 - p) = 150 \times 0.60 = 90 \geq 10
$$
   
   Both conditions are satisfied.

**Conclusion:**  
- **Mean ($\mu_{\hat{p}}$)** = 0.40  
- **Standard Error ($SE_{\hat{p}}$)** = 0.04  
- **Normal approximation is appropriate** since both $np$ and $n(1 - p)$ are greater than 10.

---

## **Solutions Summary**

Only selected, representative problems from each section are provided here to demonstrate typical solution approaches.

### **Normal Distribution**

**Problem 5:**  
*IQ scores in a population are normally distributed with a mean of 100 and a standard deviation of 15. What is the probability that a randomly selected person has an IQ between 95 and 115?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 100$
   - $\sigma = 15$
   - $X_1 = 95$, $X_2 = 115$

2. **Calculate Z-scores:**
   
$$
z_1 = \frac{95 - 100}{15} = -0.333 
$$

$$
z_2 = \frac{115 - 100}{15} = 1.0
$$

3. **Find Probabilities:**
   - $P(Z < 1.0) = 0.8413$
   - $P(Z < -0.333) \approx 0.3694$

4. **Probability Between 95 and 115:**
   
$$
P(95 < X < 115) = 0.8413 - 0.3694 = 0.4719
$$

**Conclusion:**  
There is approximately a **47.19%** probability that a randomly selected person has an IQ between 95 and 115.

---

### **Sampling Distribution of Sample Means**

**Problem 17:**  
*The amount of time (in minutes) that customers spend in a bank is normally distributed with a mean of 30 minutes and a standard deviation of 5 minutes. What is the probability that the sample mean time for a sample of 25 customers is between 29 and 31 minutes?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 30$ minutes
   - $\sigma = 5$ minutes
   - $n = 25$
   - $\bar{x}_1 = 29$, $\bar{x}_2 = 31$

2. **Calculate Standard Error ($SE_{\bar{x}}$):**
   
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{5}{5} = 1
$$

3. **Calculate Z-scores:**
   
$$
z_1 = \frac{29 - 30}{1} = -1 
$$

$$
z_2 = \frac{31 - 30}{1} = 1
$$

4. **Find Probabilities:**
   - $P(Z < 1) = 0.8413$
   - $P(Z < -1) = 0.1587$

5. **Probability Between 29 and 31 Minutes:**
   
$$
P(29 < \bar{x} < 31) = 0.8413 - 0.1587 = 0.6826
$$

**Conclusion:**  
There is approximately a **68.26%** probability that the sample mean time is between 29 and 31 minutes.

---

### **Sampling Distribution of Sample Proportions**

**Problem 28:**  
*A company claims that 30% of its customers are satisfied with their service. In a sample of 250 customers, 80 report being satisfied. Test the company's claim at the 5% significance level. Is the normal approximation appropriate for this test?*

**Solution:**
1. **State the Hypotheses:**
   - $H_0: p = 0.30$
   - $H_a: p \neq 0.30$ (two-tailed)

2. **Check Normal Approximation Conditions:**
   
$$
np = 250 \times 0.30 = 75 \geq 10 
$$

$$
n(1 - p) = 250 \times 0.70 = 175 \geq 10
$$
   
   Conditions are satisfied.

3. **Calculate Sample Proportion ($\hat{p}$):**
   
$$
\hat{p} = \frac{80}{250} = 0.32
$$

4. **Calculate Standard Error ($SE_{\hat{p}}$):**
   
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} } = \sqrt{ \frac{0.30 \times 0.70}{250} } = \sqrt{ \frac{0.21}{250} } = \sqrt{0.00084} \approx 0.0290
$$

5. **Calculate Z-score:**
   
$$
z = \frac{\hat{p} - p}{SE_{\hat{p}}} = \frac{0.32 - 0.30}{0.0290} \approx 0.6897
$$

6. **Find P-value:**
   - For two-tailed test, multiply the one-tailed probability by 2.
   - $P(Z > 0.6897) \approx 0.245$
   - $p \approx 2 \times 0.245 = 0.490$

7. **Compare P-value with $\alpha$:**
   - $p = 0.490 > 0.05$
   - **Do not reject $H_0$.**

**Conclusion:**  
There is not enough evidence at the 5% significance level to reject the company's claim that 30% of its customers are satisfied with their service.

---

## **Solutions Summary**

Only selected, representative problems from each section are provided here to demonstrate typical solution approaches.

### **Normal Distribution**

**Problem 1:**  
*The weight of a package is normally distributed with a mean of 55 grams and a standard deviation of 6 grams. What is the probability that a randomly selected package weighs between 49 and 61 grams?*

**Solution:**
1. **Identify Parameters:**
   - Mean ($\mu$) = 55 grams
   - Standard Deviation ($\sigma$) = 6 grams
   - $X$ = 49 grams and 61 grams

2. **Calculate Z-scores:**
   
$$
z_1 = \frac{49 - 55}{6} = -1.0 
$$

$$
z_2 = \frac{61 - 55}{6} = 1.0
$$

3. **Find Probabilities from Z-table:**
   - $P(Z < 1.0) = 0.8413$
   - $P(Z < -1.0) = 0.1587$

4. **Calculate Probability Between 49 and 61 grams:**
   
$$
P(49 < X < 61) = 0.8413 - 0.1587 = 0.6826
$$

**Conclusion:**  
There is approximately a **68.26%** probability that a randomly selected package weighs between 49 and 61 grams.

---

### **Sampling Distribution of Sample Means**

**Problem 17:**  
*The amount of time (in minutes) that customers spend in a bank is normally distributed with a mean of 30 minutes and a standard deviation of 5 minutes. What is the probability that the sample mean time for a sample of 25 customers is between 29 and 31 minutes?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 30$ minutes
   - $\sigma = 5$ minutes
   - $n = 25$
   - $\bar{x}_1 = 29$, $\bar{x}_2 = 31$

2. **Calculate Standard Error ($SE_{\bar{x}}$):**
   
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{5}{5} = 1
$$

3. **Calculate Z-scores:**
   
$$
z_1 = \frac{29 - 30}{1} = -1 
$$

$$
z_2 = \frac{31 - 30}{1} = 1
$$

4. **Find Probabilities:**
   - $P(Z < 1) = 0.8413$
   - $P(Z < -1) = 0.1587$

5. **Probability Between 29 and 31 Minutes:**
   
$$
P(29 < \bar{x} < 31) = 0.8413 - 0.1587 = 0.6826
$$

**Conclusion:**  
There is approximately a **68.26%** probability that the sample mean time is between 29 and 31 minutes.

---

### **Sampling Distribution of Sample Proportions**

**Problem 28:**  
*A company claims that 30% of its customers are satisfied with their service. In a sample of 250 customers, 80 report being satisfied. Test the company's claim at the 5% significance level. Is the normal approximation appropriate for this test?*

**Solution:**
1. **State the Hypotheses:**
   - $H_0: p = 0.30$
   - $H_a: p \neq 0.30$ (two-tailed)

2. **Check Normal Approximation Conditions:**

$$
np = 250 \times 0.30 = 75 \geq 10 
$$

$$
n(1 - p) = 250 \times 0.70 = 175 \geq 10
$$
   
   Conditions are satisfied.

3. **Calculate Sample Proportion ($\hat{p}$):**
   
$$
\hat{p} = \frac{80}{250} = 0.32
$$

4. **Calculate Standard Error ($SE_{\hat{p}}$):**
   
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} } = \sqrt{ \frac{0.30 \times 0.70}{250} } = \sqrt{ \frac{0.21}{250} } = \sqrt{0.00084} \approx 0.0290
$$

5. **Calculate Z-score:**
   
$$
z = \frac{\hat{p} - p}{SE_{\hat{p}}} = \frac{0.32 - 0.30}{0.0290} \approx 0.6897
$$

6. **Find P-value:**
   - For two-tailed test, multiply the one-tailed probability by 2.
   - $P(Z > 0.6897) \approx 0.245$
   - $p \approx 2 \times 0.245 = 0.490$

7. **Compare P-value with $\alpha$:**
   - $p = 0.490 > 0.05$
   - **Do not reject $H_0$.**

**Conclusion:**  
There is not enough evidence at the 5% significance level to reject the company's claim that 30% of its customers are satisfied with their service.

---

## **Solutions Summary**

Only selected, representative problems from each section are provided here to demonstrate typical solution approaches.

### **Normal Distribution**

**Problem 5:**  
*IQ scores in a population are normally distributed with a mean of 100 and a standard deviation of 15. What is the probability that a randomly selected person has an IQ between 95 and 115?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 100$
   - $\sigma = 15$
   - $X_1 = 95$, $X_2 = 115$

2. **Calculate Z-scores:**
   
$$
z_1 = \frac{95 - 100}{15} = -0.333 
$$

$$
z_2 = \frac{115 - 100}{15} = 1.0
$$

3. **Find Probabilities:**
   - $P(Z < 1.0) = 0.8413$
   - $P(Z < -0.333) \approx 0.3694$

4. **Probability Between 95 and 115:**
   
$$
P(95 < X < 115) = 0.8413 - 0.3694 = 0.4719
$$

**Conclusion:**  
There is approximately a **47.19%** probability that a randomly selected person has an IQ between 95 and 115.

---

### **Sampling Distribution of Sample Means**

**Problem 15:**  
*The heights of students in a university are normally distributed with a mean of 170 cm and a standard deviation of 8 cm. What is the probability that the sample mean height of a sample of 25 students is less than 168 cm?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 170$ cm
   - $\sigma = 8$ cm
   - $n = 25$
   - $\bar{x} = 168$ cm

2. **Calculate Standard Error ($SE_{\bar{x}}$):**
   
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{8}{5} = 1.6
$$

3. **Calculate Z-score:**
   
$$
z = \frac{168 - 170}{1.6} = \frac{-2}{1.6} = -1.25
$$

4. **Find Probability:**
   - $P(Z < -1.25) \approx 0.1056$

**Conclusion:**  
There is approximately a **10.56%** probability that the sample mean height is less than 168 cm.

---

### **Sampling Distribution of Sample Proportions**

**Problem 30:**  
*In a population, $p = 0.20$. For a sample of size 150, what is the probability that the sample proportion $\hat{p}$ is less than 0.15?*

**Solution:**
1. **Identify Parameters:**
   - $p = 0.20$
   - $n = 150$
   - $\hat{p} = 0.15$

2. **Calculate Standard Error ($SE_{\hat{p}}$):**
   
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} } = \sqrt{ \frac{0.20 \times 0.80}{150} } = \sqrt{ \frac{0.16}{150} } = \sqrt{0.0010667} \approx 0.0327
$$

3. **Calculate Z-score:**
   
$$
z = \frac{\hat{p} - p}{SE_{\hat{p}}} = \frac{0.15 - 0.20}{0.0327} \approx -1.533
$$

4. **Find Probability:**
   - $P(Z < -1.533) \approx 0.0625$

**Conclusion:**  
There is approximately a **6.25%** probability that the sample proportion is less than 0.15.

---

## **Additional Solutions**

### **Normal Distribution**

**Problem 10:**  
*The lifespan of a type of light bulb is normally distributed with a mean of 1000 hours and a standard deviation of 100 hours. What is the probability that a randomly selected bulb lasts less than 950 hours?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 1000$ hours
   - $\sigma = 100$ hours
   - $X = 950$ hours

2. **Calculate Z-score:**
   
$$
z = \frac{950 - 1000}{100} = -0.5
$$

3. **Find Probability:**
   - $P(Z < -0.5) \approx 0.3085$

**Conclusion:**  
There is approximately a **30.85%** probability that a randomly selected bulb lasts less than 950 hours.

---

### **Sampling Distribution of Sample Means**

**Problem 21:**  
*The diameters of screws produced by a machine are normally distributed with a mean of 4.5 mm and a standard deviation of 0.1 mm. If a sample of 16 screws is selected, what is the probability that the sample mean diameter is greater than 4.55 mm?*

**Solution:**
1. **Identify Parameters:**
   - $\mu = 4.5$ mm
   - $\sigma = 0.1$ mm
   - $n = 16$
   - $\bar{x} = 4.55$ mm

2. **Calculate Standard Error ($SE_{\bar{x}}$):**
   
$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{0.1}{4} = 0.025
$$

3. **Calculate Z-score:**
   
$$
z = \frac{4.55 - 4.5}{0.025} = \frac{0.05}{0.025} = 2.0
$$

4. **Find Probability:**
   - $P(Z > 2.0) = 1 - P(Z < 2.0) = 1 - 0.9772 = 0.0228$

**Conclusion:**  
There is approximately a **2.28%** probability that the sample mean diameter is greater than 4.55 mm.

---

### **Sampling Distribution of Sample Proportions**

**Problem 33:**  
*A survey finds that 42% of people prefer tea over coffee. If we take a sample of 100 people, what is the probability that more than 45% prefer tea? Assume the normal approximation is appropriate.*

**Solution:**
1. **Identify Parameters:**
   - $p = 0.42$
   - $n = 100$
   - $\hat{p} = 0.45$

2. **Calculate Standard Error ($SE_{\hat{p}}$):**
   
$$
SE_{\hat{p}} = \sqrt{ \frac{p(1 - p)}{n} } = \sqrt{ \frac{0.42 \times 0.58}{100} } = \sqrt{ \frac{0.2436}{100} } = \sqrt{0.002436} \approx 0.0494
$$

3. **Calculate Z-score:**
   
$$
z = \frac{0.45 - 0.42}{0.0494} \approx 0.607
$$

4. **Find Probability:**
   - $P(Z > 0.607) = 1 - P(Z < 0.607) \approx 1 - 0.7286 = 0.2714$

**Conclusion:**  
There is approximately a **27.14%** probability that more than 45% of the sample prefers tea over coffee.

---

## **Final Remarks**

This review assignment, combined with the provided solutions, aims to enhance your proficiency in understanding and applying Normal Distributions and Sampling Distributions for Means and Proportions. Mastery of these topics is crucial for excelling in statistical analysis and decision-making processes.

---

**Happy Reviewing!**  
Engage with these problems diligently to solidify your understanding and application of key statistical concepts. Consistent practice and thorough comprehension will pave the way for success in your academic and professional endeavors.

---