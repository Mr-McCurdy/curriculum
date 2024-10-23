# I. Probability and Random Variables

## 1. Random Variables

Show all your work. Indicate clearly the methods you use, because you will be scored on the correctness of your methods as well as on the accuracy and completeness of your results and explanations.

A farm produces olive oil that is put into bottles that are sealed with a cork. The diameter of the bottle opening is 1.03 inches. To provide an acceptable fit, the cork diameter should be from 0.99 inch to 1.03 inches. The corks are purchased in bulk from a supplier, and the distribution of cork diameters is approximately normal with mean 1.00 inch and standard deviation 0.05 inch.

#### 1.a
If one cork is selected at random, what is the probability that the cork selected will provide an acceptable fit for the bottle? Show your work.

#### 1.b
A farm manager decides to purchase the corks from a new supplier. Seventy percent of corks produced by the new supplier have a diameter with an acceptable fit. The farm manager is investigating how many corks in a box of 20 randomly selected corks will provide an acceptable fit. Consider the probability that **at least 19** of the corks will provide an acceptable fit for the bottle.

##### 1.b.i
Define the random variable of interest and state how the random variable is distributed.

##### 1.b.ii 
What is the probability that **at least 19** of the corks will provide an acceptable fit for the bottle? Show your work.

#### 1.c
Suppose corks are inspected one at a time until an acceptable fit is found. Let the random variable $W$ represent the number of corks inspected. What is the probability that $W$ is less than or equal to 2? Show your work.

### Solution

#### 1.a

To determine the probability that a randomly selected cork has a diameter between **0.99 inch** and **1.03 inches**, we can use the properties of the normal distribution.

1. **Define the Random Variable:**
   - Let **X** be the diameter of a randomly selected cork.
   - **X** is normally distributed: $$X \sim N(\mu = 1.00, \sigma = 0.05)$$.

2. **Standardize the Values:**
   We convert the raw scores to **z-scores** using the formula:
$$
z = \frac{X - \mu}{\sigma}
$$
   
   - For **X = 0.99 inches**:
$$
z_1 = \frac{0.99 - 1.00}{0.05} = \frac{-0.01}{0.05} = -0.2
$$
   
   - For **X = 1.03 inches**:

$$
z_2 = \frac{1.03 - 1.00}{0.05} = \frac{0.03}{0.05} = 0.6
$$

3. **Find the Probabilities Using the Standard Normal Distribution Table:**
   
   - **P(Z < 0.6):**
     From the z-table, $$P(Z < 0.6) \approx 0.7257$$.
   
   - **P(Z < -0.2):**
     From the z-table, $$P(Z < -0.2) \approx 0.4207$$.
   
   - **Probability Between Z = -0.2 and Z = 0.6:**
    
$$
P(-0.2 < Z < 0.6) = P(Z < 0.6) - P(Z < -0.2) = 0.7257 - 0.4207 = 0.3050
$$
   
4. **Interpret the Result:**
   
   The probability that a randomly selected cork has an acceptable diameter is **30.50%**.

**Answer:**  
The probability of selecting an acceptable cork is **0.3050** or **30.50%**.

---

#### **(b) Probability with a New Supplier**

A new supplier produces corks where **70%** have an acceptable fit.

##### **(i) Define the Random Variable and Its Distribution**

**Question:**  
Define the random variable of interest and state how the random variable is distributed.

**Solution:**

1. **Define the Random Variable:**
   
   - Let **X** represent the number of corks with an acceptable fit in a box of **20** randomly selected corks.

2. **Determine the Distribution:**
   
   - Each cork has two outcomes: acceptable fit (success) with probability **p = 0.70**, and unacceptable fit (failure) with probability **q = 1 - p = 0.30**.
   
   - The selection of corks is independent.
   
   - **X** follows a **Binomial Distribution**: $$X \sim \text{Binomial}(n = 20, p = 0.70)$$.

**Answer:**  
Let **X** be the number of corks with an acceptable fit in a box of 20. **X** is binomially distributed with parameters **n = 20** and **p = 0.70**, denoted as $$X \sim \text{Binomial}(20, 0.70)$$.

##### **(ii) Probability of At Least 19 Acceptable Corks**

**Question:**  
What is the probability that **at least 19** of the corks will provide an acceptable fit for the bottle? Show your work.

**Solution:**

1. **Identify the Desired Probability:**
   
   We need to find $$P(X \geq 19)$$, which includes:
  $$
   P(X = 19) + P(X = 20)
  $$

2. **Use the Binomial Probability Formula:**
   
   The probability of exactly **k** successes in **n** trials is:
  $$
   P(X = k) = \binom{n}{k} p^k q^{n-k}
  $$
   
   - **For X = 19:**
    $$
     P(X = 19) = \binom{20}{19} (0.70)^{19} (0.30)^{1}
    $$
    $$
     = 20 \times (0.70)^{19} \times 0.30
    $$
   
   - **For X = 20:**
    $$
     P(X = 20) = \binom{20}{20} (0.70)^{20} (0.30)^{0}
    $$
    $$
     = 1 \times (0.70)^{20} \times 1 = (0.70)^{20}
    $$

3. **Calculate the Probabilities:**
   
   - **Calculate $$(0.70)^{19}$$:**
    $$
     (0.70)^{19} \approx 0.0007979226629761201
    $$
   
   - **Calculate $$P(X = 19)$$:**
    $$
     P(X = 19) = 20 \times 0.0007979226629761201 \times 0.30 \approx 0.004787536
    $$
   
   - **Calculate $$(0.70)^{20}$$:**
    $$
     (0.70)^{20} \approx 0.0005585458640832844
    $$
   
   - **Calculate $$P(X = 20)$$:**
    $$
     P(X = 20) = 0.0005585458640832844
    $$
   
   - **Sum the Probabilities:**
    $$
     P(X \geq 19) = P(X = 19) + P(X = 20) \approx 0.004787536 + 0.000558546 = 0.005346082
    $$

4. **Interpret the Result:**
   
   The probability that at least **19** corks out of **20** have an acceptable fit is approximately **0.5346%**.

**Answer:**  
The probability that at least 19 corks provide an acceptable fit is approximately **0.5346%**.

---

#### **(c) Probability in Sequential Inspections**

**Question:**  
Suppose corks are inspected one at a time until an acceptable fit is found. Let the random variable $$W$$ represent the number of corks inspected. What is the probability that $$W$$ is less than or equal to 2? Show your work.

**Solution:**

1. **Define the Random Variable:**
   
   - Let $$W$$ be the number of inspections needed to find the first acceptable cork.
   
   - Since each inspection is independent and has a probability of success $$p = 0.70$$, $$W$$ follows a **Geometric Distribution**: $$W \sim \text{Geometric}(p = 0.70)$$.

2. **Understand the Probability Asked:**
   
   - $$P(W \leq 2)$$ is the probability that the first acceptable cork is found on the **first** or **second** inspection.

3. **Calculate $$P(W \leq 2)$$:**
   
   - **Case 1:** First inspection is acceptable.
    $$
     P(W = 1) = p = 0.70
    $$
   
   - **Case 2:** First inspection is unacceptable, and the second is acceptable.
    $$
     P(W = 2) = q \times p = 0.30 \times 0.70 = 0.21
    $$
   
   - **Sum the Probabilities:**
    $$
     P(W \leq 2) = P(W = 1) + P(W = 2) = 0.70 + 0.21 = 0.91
    $$

4. **Interpret the Result:**
   
   There is a **91%** probability that an acceptable cork will be found within the first two inspections.

**Answer:**  
The probability that $$W$$ is less than or equal to 2 is **0.91** or **91%**.

---

### **Summary of Answers**

- **(a)** Probability = **0.3050** or **30.50%**
- **(b)(i)** $$X \sim \text{Binomial}(20, 0.70)$$
- **(b)(ii)** Probability = **0.005346** or **0.5346%**
- **(c)** Probability = **0.91** or **91%**

---

**Note:**  
All calculations were performed using standard normal distribution properties for part (a), binomial probability formulas for part (b), and geometric distribution formulas for part (c). Each step was carefully executed to ensure accuracy and adherence to AP Statistics guidelines.