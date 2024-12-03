# **Understanding Secant Lines and Average Rates of Change**

---

## Introduction

In calculus, the concepts of **secant lines** and **average rates of change** are fundamental tools for analyzing the behavior of functions over specific intervals. These concepts are not only essential in mathematics but also have practical applications in various fields such as economics and physics. This tutorial explores these ideas using function notation, providing a comprehensive understanding through definitions, examples, and exercises.

---

## What Are Secant Lines and Average Rates of Change?

### **Secant Lines**

Imagine you're watching a plant grow. You measure its height today and then again a week later. Drawing a straight line between these two measurements gives you an overall idea of how quickly the plant is growing. This straight line is called a **secant line**.

In mathematics, a secant line is a straight line that connects two points on a curve (a curved line). It helps us understand the general trend between those two points.

### **Average Rate of Change**

The **average rate of change** tells us how much something changes, on average, over a certain interval. It's like calculating the average speed of a car on a trip. If you drove 150 miles in 3 hours, your average speed was 50 miles per hour.

Mathematically, for a function $f(x)$, the average rate of change between two points $x = a$ and $x = b$ is calculated as:

$$
\text{Average Rate of Change} = \frac{f(b) - f(a)}{b - a}
$$

This formula gives us the slope of the secant line connecting the two points on the graph of the function.

---

## Secant Lines and their Applications

### Physics

#### **Example 1: Velocity of a Falling Object**

Suppose you drop a ball from a tall building. The height $h$ (in meters) of the ball after $t$ seconds is given by:

$$
h(t) = -4.9t^2 + 100
$$

This equation models the ball's downward motion due to gravity.

##### **Calculating the Average Velocity**

Let's find the average velocity of the ball between $t = 2$ seconds and $t = 4$ seconds.

1. **Identify the Interval**:

   - Starting time ($a$): 2 seconds
   - Ending time ($b$): 4 seconds

2. **Compute $h(a)$ and $h(b)$**:

   - $h(2) = -4.9(2)^2 + 100 = -19.6 + 100 = 80.4$ meters
   - $h(4) = -4.9(4)^2 + 100 = -78.4 + 100 = 21.6$ meters

3. **Calculate the Average Rate of Change (Velocity)**:

$$
\text{Average Velocity} = \frac{h(4) - h(2)}{4 - 2} = \frac{21.6 - 80.4}{2} = \frac{-58.8}{2} = -29.4 \text{ m/s}
$$

##### **Understanding the Result**

The negative average velocity indicates the ball is moving downward. On average, the ball's height decreases by 29.4 meters every second between 2 and 4 seconds.

---

#### **Example 2: Position Function**

An object moves along a straight line, and its position $s$ (in meters) at time $t$ (in seconds) is given by the quadratic function:

$$
s(t) = 5t^2 - 2t + 1
$$

##### **Calculating the Average Velocity**

Find the average velocity of the object between $t = 2$ seconds and $t = 5$ seconds.

1. **Identify the Interval:**
   - $a = 2$
   - $b = 5$

2. **Compute $s(a)$ and $s(b)$:**
   $$
   \begin{align*}
   s(2) &= 5(2)^2 - 2(2) + 1 = 20 - 4 + 1 = 17 \\
   s(5) &= 5(5)^2 - 2(5) + 1 = 125 - 10 + 1 = 116 \\
   \end{align*}
   $$

3. **Calculate the Average Velocity:**
   $$
   \text{Average Velocity} = \frac{s(5) - s(2)}{5 - 2} = \frac{116 - 17}{3} = \frac{99}{3} = 33 \text{ m/s}
   $$

##### **Understanding the Result**

The average velocity of 33 m/s indicates that, on average, the object's position increases by 33 meters every second over the interval from 2 to 5 seconds.

---

### Economics

#### **Example 3: Revenue Function**

Consider a company whose revenue $R$ (in thousands of dollars) from selling $x$ units of a product is modeled by a quadratic function:

$$
R(x) = -0.5x^2 + 20x
$$

##### **Calculating the Average Rate of Change**

Let's find the average rate of change of revenue as sales increase from 10 to 30 units.

1. **Identify the Interval:**
   - $a = 10$
   - $b = 30$

2. **Compute $R(a)$ and $R(b)$:**
   $$
   \begin{align*}
   R(10) &= -0.5(10)^2 + 20(10) = -50 + 200 = 150 \\
   R(30) &= -0.5(30)^2 + 20(30) = -450 + 600 = 150 \\
   \end{align*}
   $$

3. **Calculate the Average Rate of Change:**
   $$
   \text{Average Rate of Change} = \frac{R(30) - R(10)}{30 - 10} = \frac{150 - 150}{20} = \frac{0}{20} = 0
   $$

##### **Understanding the Result**

An average rate of change of zero indicates that, over the interval from 10 to 30 units, the revenue remains constant. This suggests the company has reached its maximum revenue at some point within this interval.

---

#### **Example 4: Cost of Producing Goods**

A company's cost $C$ (in dollars) to produce $x$ units of a product is modeled by:

$$
C(x) = 0.5x^2 - 10x + 150
$$

##### **Calculating the Average Rate of Change of Cost**

Let's find how the cost changes on average when production increases from 10 to 20 units.

1. **Identify the Interval**:

   - Starting units ($a$): 10
   - Ending units ($b$): 20

2. **Compute $C(a)$ and $C(b)$**:

   - $C(10) = 0.5(10)^2 - 10(10) + 150 = 50 - 100 + 150 = 100$ dollars
   - $C(20) = 0.5(20)^2 - 10(20) + 150 = 200 - 200 + 150 = 150$ dollars

3. **Calculate the Average Rate of Change**:

   $$
   \text{Average Rate of Change} = \frac{150 - 100}{20 - 10} = \frac{50}{10} = 5 \text{ dollars per unit}
   $$

##### **Understanding the Result**

On average, the cost increases by $5 for each additional unit produced between 10 and 20 units.

---

### Computer Science

#### **Example 5: Understanding Model Performance**

Suppose we're training a machine learning model, and we want to understand how its **accuracy** improves over time.

Let's say the accuracy $A$ (in percentage) of our model after $t$ hours of training is given by a function:

$$
A(t) = -2t^2 + 20t + 50
$$

This function is a simple way to model how accuracy might change over time. The curve of this function is a parabola.

##### **Calculating the Average Rate of Change**

Let's find out how the accuracy changes on average between 2 hours and 5 hours of training.

1. **Identify the Interval**:

   - Starting time ($a$): 2 hours
   - Ending time ($b$): 5 hours

2. **Compute $A(a)$ and $A(b)$**:

   - $A(2) = -2(2)^2 + 20(2) + 50 = -8 + 40 + 50 = 82\%$
   - $A(5) = -2(5)^2 + 20(5) + 50 = -50 + 100 + 50 = 100\%$

3. **Calculate the Average Rate of Change**:

   $$
   \text{Average Rate of Change} = \frac{A(5) - A(2)}{5 - 2} = \frac{100 - 82}{3} = \frac{18}{3} = 6\% \text{ per hour}
   $$

##### **Understanding the Result**

The average rate of change is 6% per hour. This means that, on average, the model's accuracy increases by 6 percentage points each hour between the 2nd and 5th hour of training.

---

#### **Example 6: Loss Function in Machine Learning**

In machine learning, a **loss function** measures how well a model makes predictions. We want to minimize this loss to improve the model.

Suppose the loss $L$ depends on the number of training iterations $n$ and is given by:

$$
L(n) = \frac{100}{n + 1}
$$

##### **Calculating the Average Rate of Change**

Let's find out how the loss decreases on average from iteration 0 to iteration 9.

1. **Identify the Interval**:

   - Starting iteration ($a$): 0
   - Ending iteration ($b$): 9

2. **Compute $L(a)$ and $L(b)$**:

   - $L(0) = \frac{100}{0 + 1} = 100$
   - $L(9) = \frac{100}{9 + 1} = \frac{100}{10} = 10$

3. **Calculate the Average Rate of Change**:

   $$
   \text{Average Rate of Change} = \frac{L(9) - L(0)}{9 - 0} = \frac{10 - 100}{9} = \frac{-90}{9} = -10 \text{ per iteration}
   $$

##### **Understanding the Result**

The average rate of change is -10 per iteration. This means that, on average, the loss decreases by 10 units with each training iteration between iterations 0 and 9.

---

## Exercises

#### Exercise 1

A firm's profit $P$ (in thousands of dollars) based on the number of units sold $x$ is given by:

$$
P(x) = -x^2 + 20x - 50
$$

##### i. Calculate the average rate of change of profit as sales increase from 5 to 15 units.
##### ii. Interpret the result in the context of the firm's profit.

---

2. An object's height $h$ (in meters) at time $t$ (in seconds) is described by:

$$
h(t) = -4.9t^2 + 30t + 2
$$

i. Find the average velocity between $t = 2$ seconds and $t = 4$ seconds.
ii. Explain the physical meaning of your result.

---

3. The demand $D$ for a product at price $p$ (in dollars) is modeled by:

$$
D(p) = \frac{500}{p^2}
$$

i. Determine the average rate of change of demand as price increases from $5 to $10.
ii. Discuss how demand changes with price based on your calculation.

---

4. The acceleration $a$ (in m/s\(^2\)) of a particle at time $t$ (in seconds) is given by:

$$
a(t) = 6t - 4
$$

i. Compute the average acceleration between $t = 1$ second and $t = 5$ seconds.
ii. Interpret the result in terms of the particle's motion.

---

5. A machine learning model's accuracy $A$ (in %) after $t$ hours is:

$$
A(t) = 4t + 60
$$

i. Calculate the average rate of change of accuracy from $t = 3$ to $t = 7$.
ii. What does this rate tell you about the model's performance?


---

6. The loss $L$ after $n$ iterations is:

$$
L(n) = n^2 - 10n + 50
$$


i. Find the average rate of change of the loss from $n = 5$ to $n = 10$.
ii. Interpret the result.


7. Suppose the time $T$ (in seconds) it takes to process $n$ data points is:

$$
T(n) = 0.5n^2 + 2n + 1
$$


i. Calculate the average rate of change of time from $n = 10$ to $n = 20$.
ii. Explain what this means for processing larger datasets.

---

## Solutions

1. 

i. Calculate $P(5)$ and $P(15)$:
   
   $$
   \begin{align*}
   P(5) &= -(5)^2 + 20(5) - 50 = -25 + 100 - 50 = 25 \\
   P(15) &= -(15)^2 + 20(15) - 50 = -225 + 300 - 50 = 25 \\
   \end{align*}
   $$

**Average Rate of Change:**
   $$
   \text{Average Rate of Change} = \frac{25 - 25}{15 - 5} = \frac{0}{10} = 0
   $$

ii. The profit remains constant over this interval, indicating the firm has maximized its profit at some point between 5 and 15 units.

2. 

1. **Compute $h(2)$ and $h(4)$:**
   $$
   \begin{align*}
   h(2) &= -4.9(2)^2 + 30(2) + 2 = -19.6 + 60 + 2 = 42.4 \\
   h(4) &= -4.9(4)^2 + 30(4) + 2 = -78.4 + 120 + 2 = 43.6 \\
   \end{align*}
   $$

2. **Average Velocity:**
   $$
   \text{Average Velocity} = \frac{43.6 - 42.4}{4 - 2} = \frac{1.2}{2} = 0.6 \text{ m/s}
   $$

**Interpretation:** The object ascends slowly between 2 and 4 seconds, with an average upward velocity of 0.6 m/s.

### **Exercise 3 Answer**

1. **Calculate $D(5)$ and $D(10)$:**
   $$
   \begin{align*}
   D(5) &= \frac{500}{5^2} = \frac{500}{25} = 20 \\
   D(10) &= \frac{500}{10^2} = \frac{500}{100} = 5 \\
   \end{align*}
   $$

2. **Average Rate of Change:**
   $$
   \text{Average Rate of Change} = \frac{5 - 20}{10 - 5} = \frac{-15}{5} = -3 \text{ units per dollar}
   $$

**Discussion:** Demand decreases by 3 units for each dollar increase in price between $5 and $10.

### **Exercise 4 Answer**

1. **Compute $a(1)$ and $a(5)$:**
   $$
   \begin{align*}
   a(1) &= 6(1) - 4 = 2 \text{ m/s}^2 \\
   a(5) &= 6(5) - 4 = 26 \text{ m/s}^2 \\
   \end{align*}
   $$

2. **Average Acceleration:**
   $$
   \text{Average Acceleration} = \frac{26 - 2}{5 - 1} = \frac{24}{4} = 6 \text{ m/s}^2
   $$

**Interpretation:** The particle's acceleration increases by an average of 6 m/s\(^2\) each second over the interval.

---

### **Exercise 5 Answer**

**Solution**:

1. $A(3) = 4(3) + 60 = 72\%$

   $A(7) = 4(7) + 60 = 88\%$

   Average rate of change:

   $$
   \frac{88 - 72}{7 - 3} = \frac{16}{4} = 4\% \text{ per hour}
   $$

2. The model's accuracy increases by 4% each hour between the 3rd and 7th hour.

### **Exercise 6 Answer**

**Solution**:

1. $L(5) = (5)^2 - 10(5) + 50 = 25 - 50 + 50 = 25$

   $L(10) = (10)^2 - 10(10) + 50 = 100 - 100 + 50 = 50$

   Average rate of change:

   $$
   \frac{50 - 25}{10 - 5} = \frac{25}{5} = 5 \text{ per iteration}
   $$

2. The loss increases by 5 units with each iteration between iterations 5 and 10, indicating that the model might be overfitting or not learning effectively in this range.

---

### **Exercise 7 Answer**

**Solution**:

1. $T(10) = 0.5(10)^2 + 2(10) + 1 = 50 + 20 + 1 = 71$

   $T(20) = 0.5(20)^2 + 2(20) + 1 = 200 + 40 + 1 = 241$

   Average rate of change:

   $$
   \frac{241 - 71}{20 - 10} = \frac{170}{10} = 17 \text{ seconds per data point}
   $$