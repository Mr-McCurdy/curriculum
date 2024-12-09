# **Multi-Stage Probability Problems**

---
## Instructions

Solve the following multi-stage probability problems. Some problems may require constructing a decision tree to determine the probabilities of combined events. Show all your work for full credit.

---

## Problem 1: University Computer Virus

On a university campus, 60%, 30%, and 10% of the computers use Windows, Apple, and Linux operating systems, respectively. A new virus affects 3% of the Windows, 2% of the Apple, and 1% of the Linux operating systems.

a. What is the probability a computer on this campus has the virus?

b. If a randomly chosen computer on this campus has the virus, what is the probability it is a Windows machine? An Apple machine? A Linux machine?

---

## Problem 2: Quality Control in Manufacturing

A factory produces three types of gadgets: Type A, Type B, and Type C. The production distribution is 50% Type A, 30% Type B, and 20% Type C. During quality inspection, it is found that 4% of Type A gadgets are defective, 5% of Type B gadgets are defective, and 2% of Type C gadgets are defective.

a. What is the probability that a randomly selected gadget from the production line is defective?

b. If a randomly selected gadget is defective, what is the probability that it is a Type B gadget?

---

## Problem 3: Medical Testing Accuracy

In a population, 70% of individuals do not have a certain disease, while 30% do. A diagnostic test for the disease has the following accuracy:
- If a person has the disease, the test correctly identifies it 90% of the time (True Positive).
- If a person does not have the disease, the test correctly identifies it 80% of the time (True Negative).

a. What is the probability that a randomly selected individual tests positive for the disease?

b. If a randomly selected individual tests positive, what is the probability that they actually have the disease?

---

## Problem 4: Employee Skill Assessment

A company has three departments: Research, Development, and Marketing. The distribution of employees is 40% in Research, 35% in Development, and 25% in Marketing. The probability that an employee is highly skilled is 25% in Research, 40% in Development, and 30% in Marketing.

a. What is the probability that a randomly selected employee is highly skilled?

b. If a randomly selected employee is found to be highly skilled, what is the probability that they work in the Development department?

---

## Problem 5: Online Platform Usage

An online platform has three types of users: Free, Premium, and Enterprise. The user distribution is 70% Free, 20% Premium, and 10% Enterprise. The platform has implemented new security features, and the probability that a user benefits from these features is 10% for Free users, 50% for Premium users, and 90% for Enterprise users.

a. What is the probability that a randomly selected user benefits from the new security features?

b. If a randomly selected user benefits from the new security features, what is the probability that they are an Enterprise user?

---

# **Solutions**

---
## Problem 1 Solutions

### **a. Probability a Computer Has the Virus**

Use the Law of Total Probability:

$$
P(\text{Virus}) = P(\text{Virus} | \text{Windows}) \times P(\text{Windows}) + P(\text{Virus} | \text{Apple}) \times P(\text{Apple}) + P(\text{Virus} | \text{Linux}) \times P(\text{Linux})
$$

$$
P(\text{Virus}) = 0.03 \times 0.60 + 0.02 \times 0.30 + 0.01 \times 0.10 = 0.018 + 0.006 + 0.001 = 0.025
$$

**Answer:** 2.5%

### **b. Conditional Probabilities Given Virus**

Use Bayes' Theorem:

$$
P(\text{Windows} | \text{Virus}) = \frac{P(\text{Virus} | \text{Windows}) \times P(\text{Windows})}{P(\text{Virus})} = \frac{0.03 \times 0.60}{0.025} = \frac{0.018}{0.025} = 0.72
$$

$$
P(\text{Apple} | \text{Virus}) = \frac{0.02 \times 0.30}{0.025} = \frac{0.006}{0.025} = 0.24
$$

$$
P(\text{Linux} | \text{Virus}) = \frac{0.01 \times 0.10}{0.025} = \frac{0.001}{0.025} = 0.04
$$

**Answers:**
- Windows: 72%
- Apple: 24%
- Linux: 4%

---

## Problem 2 Solutions

### **a. Probability a Gadget is Defective**

$$
P(\text{Defective}) = P(\text{Defective} | A) \times P(A) + P(\text{Defective} | B) \times P(B) + P(\text{Defective} | C) \times P(C)
$$

$$
P(\text{Defective}) = 0.04 \times 0.50 + 0.05 \times 0.30 + 0.02 \times 0.20 = 0.02 + 0.015 + 0.004 = 0.039
$$

**Answer:** 3.9%

### **b. Conditional Probability of Type B Given Defective**

$$
P(B | \text{Defective}) = \frac{P(\text{Defective} | B) \times P(B)}{P(\text{Defective})} = \frac{0.05 \times 0.30}{0.039} = \frac{0.015}{0.039} \approx 0.3846
$$

**Answer:** Approximately 38.46%

---

## Problem 3 Solutions

### **a. Probability an Individual Tests Positive**

Use the Law of Total Probability:

$$
P(\text{Positive}) = P(\text{Positive} | \text{Disease}) \times P(\text{Disease}) + P(\text{Positive} | \text{No Disease}) \times P(\text{No Disease})
$$

$$
P(\text{Positive}) = 0.90 \times 0.30 + 0.20 \times 0.70 = 0.27 + 0.14 = 0.41
$$

**Answer:** 41%

### **b. Conditional Probability of Having Disease Given Positive Test**

Use Bayes' Theorem:

$$
P(\text{Disease} | \text{Positive}) = \frac{P(\text{Positive} | \text{Disease}) \times P(\text{Disease})}{P(\text{Positive})} = \frac{0.90 \times 0.30}{0.41} = \frac{0.27}{0.41} \approx 0.6585
$$

**Answer:** Approximately 65.85%

---

## Problem 4 Solutions

### **a. Probability an Employee is Highly Skilled**

Use the Law of Total Probability:

$$
P(\text{Highly Skilled}) = P(\text{Highly Skilled} | \text{Research}) \times P(\text{Research}) + P(\text{Highly Skilled} | \text{Development}) \times P(\text{Development}) + P(\text{Highly Skilled} | \text{Marketing}) \times P(\text{Marketing})
$$

$$
P(\text{Highly Skilled}) = 0.25 \times 0.40 + 0.40 \times 0.35 + 0.30 \times 0.25 = 0.10 + 0.14 + 0.075 = 0.315
$$

**Answer:** 31.5%

### **b. Conditional Probability of Being in Development Given Highly Skilled**

Use Bayes' Theorem:

$$
P(\text{Development} | \text{Highly Skilled}) = \frac{P(\text{Highly Skilled} | \text{Development}) \times P(\text{Development})}{P(\text{Highly Skilled})} = \frac{0.40 \times 0.35}{0.315} = \frac{0.14}{0.315} \approx 0.4444
$$

**Answer:** Approximately 44.44%

---

## Problem 5 Solutions

### **a. Probability a User Benefits from Security Features**

Use the Law of Total Probability:

$$
P(\text{Benefits}) = P(\text{Benefits} | \text{Free}) \times P(\text{Free}) + P(\text{Benefits} | \text{Premium}) \times P(\text{Premium}) + P(\text{Benefits} | \text{Enterprise}) \times P(\text{Enterprise})
$$

$$
P(\text{Benefits}) = 0.10 \times 0.70 + 0.50 \times 0.20 + 0.90 \times 0.10 = 0.07 + 0.10 + 0.09 = 0.26
$$

**Answer:** 26%

### **b. Conditional Probability of Being Enterprise Given Benefits**

Use Bayes' Theorem:

$$
P(\text{Enterprise} | \text{Benefits}) = \frac{P(\text{Benefits} | \text{Enterprise}) \times P(\text{Enterprise})}{P(\text{Benefits})} = \frac{0.90 \times 0.10}{0.26} = \frac{0.09}{0.26} \approx 0.3462
$$

**Answer:** Approximately 34.62%

---

---
**Practice these problems to enhance your understanding of multi-stage probability and conditional probabilities.**

---