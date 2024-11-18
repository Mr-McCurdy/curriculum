# Functions and Their Essential Properties

## Table of Contents

1. [Introduction](#introduction)
2. [Definition of a Function](#definition-of-a-function)
3. [Function Notation](#function-notation)
4. [Domain and Range](#domain-and-range)
5. [Types of Functions](#types-of-functions)
    - [Linear Functions](#linear-functions)
    - [Quadratic Functions](#quadratic-functions)
    - [Polynomial Functions](#polynomial-functions)
    - [Rational Functions](#rational-functions)
    - [Exponential and Logarithmic Functions](#exponential-and-logarithmic-functions)
    - [Trigonometric Functions](#trigonometric-functions)
6. [Properties of Functions](#properties-of-functions)
    - [Injective (One-to-One) Functions](#injective-one-to-one-functions)
    - [Surjective (Onto) Functions](#surjective-onto-functions)
    - [Bijective Functions](#bijective-functions)
    - [Even and Odd Functions](#even-and-odd-functions)
    - [Periodic Functions](#periodic-functions)
7. [Operations on Functions](#operations-on-functions)
    - [Addition, Subtraction, Multiplication, and Division](#addition-subtraction-multiplication-and-division)
    - [Composition of Functions](#composition-of-functions)
    - [Inverse Functions](#inverse-functions)
8. [Graphing Functions](#graphing-functions)
9. [Summary](#summary)
10. [Exercises](#exercises)

---

## Introduction

Functions are foundational concepts in mathematics, serving as the building blocks for various branches such as algebra, calculus, and beyond. Understanding functions, their properties, and how to manipulate them is crucial for solving complex mathematical problems and modeling real-world phenomena.

This article delves into the essential properties of functions, explores different types of functions, and provides clear notation to communicate mathematical ideas effectively. To solidify your understanding, 24 exercises are included at the end of the article.

---

## Definition of a Function

A **function** is a relation between two sets that assigns to every element of the first set exactly one element of the second set. Formally, if $ A $ and $ B $ are sets, a function $ f $ from $ A $ to $ B $ is denoted as:

$$
f: A \rightarrow B
$$

where each $ a \in A $ is associated with exactly one $ b \in B $.

### Example

Consider the function $ f $ defined by:

$$
f(x) = x^2
$$

Here, $ f $ maps every real number $ x $ to its square $ x^2 $.

---

## Function Notation

Functions are typically denoted by letters such as $ f $, $ g $, and $ h $. The notation $ f(x) $ represents the output of the function $ f $ when the input is $ x $.

### Function Evaluation

Given a function $ f(x) = 2x + 3 $, the value of $ f(5) $ is:

$$
f(5) = 2(5) + 3 = 13
$$

---

## Domain and Range

### Domain

The **domain** of a function is the set of all possible input values ($ x $-values) for which the function is defined.

### Range

The **range** of a function is the set of all possible output values ($ f(x) $-values) that the function can produce.

### Example

For the function $ f(x) = \sqrt{x} $:

- **Domain**: $ x \geq 0 $ (since the square root of a negative number is not a real number)
- **Range**: $ f(x) \geq 0 $

---

## Types of Functions

Functions can be categorized based on their expressions and properties. Below are some common types of functions:

### Linear Functions

A **linear function** is of the form:

$$
f(x) = mx + b
$$

where $ m $ is the slope and $ b $ is the y-intercept.

**Example:**

$$
f(x) = 3x - 2
$$

### Quadratic Functions

A **quadratic function** has the form:

$$
f(x) = ax^2 + bx + c
$$

where $ a \neq 0 $.

**Example:**

$$
f(x) = 2x^2 - 4x + 1
$$

### Polynomial Functions

A **polynomial function** is a sum of terms in the form $ ax^n $, where $ n $ is a non-negative integer.

**Example:**

$$
f(x) = x^3 - 6x^2 + 11x - 6
$$

### Rational Functions

A **rational function** is the ratio of two polynomial functions.

**Example:**

$$
f(x) = \frac{2x + 3}{x - 1}
$$

### Exponential and Logarithmic Functions

- **Exponential Function**:

$$
f(x) = a \cdot b^x
$$

where $ b > 0 $ and $ b \neq 1 $.

- **Logarithmic Function**:

$$
f(x) = \log_b(x)
$$

where $ b > 0 $ and $ b \neq 1 $.

**Example:**

$$
f(x) = 2 \cdot 3^x
$$

### Trigonometric Functions

Trigonometric functions relate angles to ratios of side lengths in right triangles.

**Common Trigonometric Functions:**

- Sine: $ \sin(x) $
- Cosine: $ \cos(x) $
- Tangent: $ \tan(x) $

**Example:**

$$
f(x) = \sin(x)
$$

---

## Properties of Functions

Understanding the properties of functions helps in analyzing their behavior and solving equations involving them.

### Injective (One-to-One) Functions

A function $ f: A \rightarrow B $ is **injective** if different inputs produce different outputs. Formally:

$$
\text{If } f(a) = f(b) \text{ then } a = b
$$

### Surjective (Onto) Functions

A function $ f: A \rightarrow B $ is **surjective** if every element in $ B $ is an output of $ f $. Formally:

$$
\forall b \in B, \exists a \in A \text{ such that } f(a) = b
$$

### Bijective Functions

A function is **bijective** if it is both injective and surjective. Bijective functions have inverses.

### Even and Odd Functions

- **Even Function**:

$$
f(-x) = f(x) \quad \forall x \in \text{Domain}
$$

- **Odd Function**:

$$
f(-x) = -f(x) \quad \forall x \in \text{Domain}
$$

### Periodic Functions

A function $ f $ is **periodic** with period $ T $ if:

$$
f(x + T) = f(x) \quad \forall x \in \text{Domain}
$$

---

## Operations on Functions

Functions can be combined and manipulated through various operations to form new functions.

### Addition, Subtraction, Multiplication, and Division

Given two functions $ f $ and $ g $:

- **Addition**: $ (f + g)(x) = f(x) + g(x) $
- **Subtraction**: $ (f - g)(x) = f(x) - g(x) $
- **Multiplication**: $ (f \cdot g)(x) = f(x) \cdot g(x) $
- **Division**: $ \left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)} $, $ g(x) \neq 0 $

### Composition of Functions

The **composition** of functions $ f $ and $ g $ is denoted by $ f \circ g $ and defined as:

$$
(f \circ g)(x) = f(g(x))
$$

### Inverse Functions

A function $ f $ has an **inverse** $ f^{-1} $ if:

$$
f^{-1}(f(x)) = x \quad \text{and} \quad f(f^{-1}(x)) = x
$$

Only bijective functions have inverses.

---

## Graphing Functions

Graphing functions provides a visual representation of their behavior.

### Key Elements to Graph:

- **Intercepts**: Points where the graph crosses the axes.
- **Slope**: For linear functions, indicates the steepness.
- **Asymptotes**: Lines that the graph approaches but never touches (common in rational functions).
- **Symmetry**: Whether the graph is symmetric about the y-axis (even), origin (odd), or neither.
- **Periodicity**: For periodic functions, the interval after which the function repeats.

### Example: Graph of $ f(x) = \sin(x) $

![Graph of sine function](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Sine.svg/320px-Sine.svg.png)

*Graph of the sine function, demonstrating periodicity and symmetry.*

---

## Summary

Functions are integral to understanding and modeling relationships in mathematics and the real world. By understanding their notation, domains, ranges, and properties, you can analyze and manipulate them effectively. Operations such as addition, multiplication, and composition allow for the creation of more complex functions, while properties like injectivity and surjectivity aid in understanding their behavior and inverses.

---

## Exercises

### Definition and Notation

1. **Function Identification**: Determine whether the following relation is a function:
   
   $$
   \{(1, 2), (2, 3), (3, 4), (2, 5)\}
   $$
   
   **Answer**: This relation is **not** a function because the input $2$ maps to two different outputs $3$ and $5$.
   
2. **Function Notation**: Write the function $f$ that maps $x$ to $x^3 - 2x$.

   **Answer**:
   
   $$
   f(x) = x^3 - 2x
   $$

### Domain and Range

3. **Finding Domain**: Find the domain of the function:
   
   $$
   f(x) = \frac{1}{x - 4}
   $$
   
   **Answer**: The denominator cannot be zero:
   
   $$
   x - 4 \neq 0 \implies x \neq 4
   $$
   
   **Domain**: $\mathbb{R} \setminus \{4\}$

4. **Finding Range**: Find the range of the function:
   
   $$
   f(x) = \sqrt{9 - x^2}
   $$
   
   **Answer**: The expression under the square root must be non-negative:
   
   $$
   9 - x^2 \geq 0 \implies x^2 \leq 9 \implies -3 \leq x \leq 3
   $$
   
   The range of $f(x)$ is:
   
   $$
   [0, 3]
   $$
   
### Types of Functions

5. **Linear Function**: Identify the slope and y-intercept of the linear function:
   
   $$
   f(x) = -3x + 7
   $$
   
   **Answer**:
   - **Slope (m)**: $-3$
   - **Y-intercept (b)**: $7$

6. **Quadratic Function**: Determine the vertex of the quadratic function:
   
   $$
   f(x) = 2x^2 - 8x + 6
   $$
   
   **Answer**:
   - The vertex $(h, k)$ is found using:
     
     $$
     h = -\frac{b}{2a} = -\frac{-8}{2 \cdot 2} = 2
     $$
     
     $$
     k = f(2) = 2(2)^2 - 8(2) + 6 = 8 - 16 + 6 = -2
     $$
     
   - **Vertex**: $(2, -2)$

7. **Polynomial Function**: What is the degree of the polynomial function:
   
   $$
   f(x) = 4x^4 - x^3 + 2x - 5
   $$
   
   **Answer**: The degree is **4** (the highest exponent).

8. **Rational Function**: Identify the vertical asymptote of the rational function:
   
   $$
   f(x) = \frac{3x + 2}{x^2 - 1}
   $$
   
   **Answer**: The vertical asymptotes occur where the denominator is zero:
   
   $$
   x^2 - 1 = 0 \implies x = \pm 1
   $$
   
   **Vertical Asymptotes**: $x = 1$ and $x = -1$
   
### 4. Properties of Functions

9. **Injective Function**: Determine if the function $f(x) = 2x + 1$ is injective.

10. **Surjective Function**: Determine if the function $f(x) = x^2$ is surjective when $f: \mathbb{R} \rightarrow \mathbb{R}$.

11. **Bijective Function**: Is the function $f(x) = e^x$ bijective? Justify your answer.

12. **Even or Odd Function**: Determine whether the function $f(x) = x^4 - x^2$ is even, odd, or neither.

13. **Periodic Function**: State whether the function $f(x) = \cos(x)$ is periodic and, if so, find its period.

### 5. Operations on Functions

14. **Addition of Functions**: Given $f(x) = x + 2$ and $g(x) = 3x - 1$, find $(f + g)(x)$.

15. **Multiplication of Functions**: Given $f(x) = 2x$ and $g(x) = x^2$, find $(f \cdot g)(x)$.

16. **Division of Functions**: Given $f(x) = x^2$ and $g(x) = x + 1$, find $\left(\frac{f}{g}\right)(x)$.

17. **Composition of Functions**: Given $f(x) = 2x$ and $g(x) = x + 3$, find $(f \circ g)(x)$.

18. **Inverse Function**: Find the inverse of the function $f(x) = \frac{x - 5}{3}$.

### 6. Graphing Functions

19. **Graphing Linear Function**: Sketch the graph of $f(x) = -x + 4$.

20. **Graphing Quadratic Function**: Sketch the graph of $f(x) = x^2 - 6x + 8$.

21. **Identifying Asymptotes**: For the function $f(x) = \frac{2}{x - 2}$, identify all asymptotes.

### 7. Advanced Properties

22. **Finding Function Inverse**: Given $f(x) = \frac{3x + 2}{x - 1}$, find $f^{-1}(x)$.

23. **Determining Injectivity**: Is the function $f(x) = |x|$ injective? Explain.

24. **Determining Surjectivity**: Is the function $f(x) = \sqrt{x}$ surjective when $f: \mathbb{R} \rightarrow \mathbb{R}$? Explain.

---

# Solutions

*Solutions to the exercises are provided below for self-assessment.*

### 1. Definition and Notation

1. **Function Identification**:
   The relation $\{(1, 2), (2, 3), (3, 4), (2, 5)\}$ is **not** a function because the input $2$ maps to two different outputs $3$ and $5$.

2. **Function Notation**:
   The function $f$ mapping $x$ to $x^3 - 2x$ is written as:

   $$
   f(x) = x^3 - 2x
   $$

### 2. Domain and Range

3. **Finding Domain**:
   For $f(x) = \frac{1}{x - 4}$, the denominator cannot be zero:

   $$
   x - 4 \neq 0 \Rightarrow x \neq 4
   $$

   **Domain**: $\mathbb{R} \setminus \{4\}$

4. **Finding Range**:
   For $f(x) = \sqrt{9 - x^2}$, the expression under the square root must be non-negative:

   $$
   9 - x^2 \geq 0 \Rightarrow x^2 \leq 9 \Rightarrow -3 \leq x \leq 3
   $$

   The range of $f(x)$ is $[0, 3]$.

### 3. Types of Functions

5. **Linear Function**:

   For $f(x) = -3x + 7$:

   - **Slope (m)**: $-3$
   - **Y-intercept (b)**: $7$

6. **Quadratic Function**:

   For $f(x) = 2x^2 - 8x + 6$:

   The vertex $(h, k)$ is found using:

   $$
   h = -\frac{b}{2a} = -\frac{-8}{2 \cdot 2} = 2
   $$

   $$
   k = f(2) = 2(2)^2 - 8(2) + 6 = 8 - 16 + 6 = -2
   $$

   **Vertex**: $(2, -2)$

7. **Polynomial Function**:

   The degree of $f(x) = 4x^4 - x^3 + 2x - 5$ is **4** (the highest exponent).

8. **Rational Function**:

   For $f(x) = \frac{3x + 2}{x^2 - 1}$:

   The vertical asymptotes occur where the denominator is zero:

   $$
   x^2 - 1 = 0 \Rightarrow x = \pm 1
   $$

   **Vertical Asymptotes**: $x = 1$ and $x = -1$

### 4. Properties of Functions (Continued)

9. **Injective Function**:

   The function $f(x) = 2x + 1$ is **injective** because for every distinct $x_1$ and $x_2$, $f(x_1) \neq f(x_2)$.

10. **Surjective Function**:

   The function $f(x) = x^2$ is **not surjective** over $\mathbb{R}$ because there are real numbers (negative numbers) that are not outputs of $f$.

11. **Bijective Function**:

   The function $f(x) = e^x$ is **not bijective** over $\mathbb{R} \rightarrow \mathbb{R}$ because it is **not surjective** (outputs are always positive).

12. **Even or Odd Function**:

   For $f(x) = x^4 - x^2$:

   $$
   f(-x) = (-x)^4 - (-x)^2 = x^4 - x^2 = f(x)
   $$

   Since $f(-x) = f(x)$, $f$ is an **even function**.

13. **Periodic Function**:

   The function $f(x) = \cos(x)$ is **periodic** with a period of $2\pi$ because:

   $$
   \cos(x + 2\pi) = \cos(x)

### 5. Operations on Functions

14. **Addition of Functions**:

    Given $$f(x) = x + 2$$ and $$g(x) = 3x - 1$$:

    $$
    (f + g)(x) = (x + 2) + (3x - 1) = 4x + 1
    $$

15. **Multiplication of Functions**:

    Given $$f(x) = 2x$$ and $$g(x) = x^2$$:

    $$
    (f \cdot g)(x) = 2x \cdot x^2 = 2x^3
    $$

16. **Division of Functions**:

    Given $$f(x) = x^2$$ and $$g(x) = x + 1$$:

    $$
    \left(\frac{f}{g}\right)(x) = \frac{x^2}{x + 1}, \quad x \neq -1
    $$

17. **Composition of Functions**:

    Given $$f(x) = 2x$$ and $$g(x) = x + 3$$:

    $$
    (f \circ g)(x) = f(g(x)) = f(x + 3) = 2(x + 3) = 2x + 6
    $$

18. **Inverse Function**:

    Given $$f(x) = \frac{x - 5}{3}$$:

    To find $$f^{-1}(x)$$, solve for $$x$$:

    $$
    y = \frac{x - 5}{3} \Rightarrow 3y = x - 5 \Rightarrow x = 3y + 5
    $$

    **Inverse Function**:

    $$
    f^{-1}(x) = 3x + 5
    $$

### 6. Graphing Functions

19. **Graphing Linear Function**:
    
    **Function**: $$f(x) = -x + 4$$
    
    - **Y-intercept**: $$(0, 4)$$
    - **Slope**: $$-1$$ (downward slope)
    
    ![Graph of f(x) = -x + 4](https://i.imgur.com/OxQh7Vq.png)
    
20. **Graphing Quadratic Function**:
    
    **Function**: $$f(x) = x^2 - 6x + 8$$
    
    - **Vertex**: $$(3, -1)$$
    - **Axis of Symmetry**: $$x = 3$$
    
    ![Graph of f(x) = x^2 - 6x + 8](https://i.imgur.com/1VxP5jR.png)
    
21. **Identifying Asymptotes**:
    
    For $$f(x) = \frac{2}{x - 2}$$:
    
    - **Vertical Asymptote**: $$x = 2$$ (denominator zero)
    - **Horizontal Asymptote**: $$y = 0$$ (degree of denominator > degree of numerator)
    
    ![Graph of f(x) = 2/(x-2)](https://i.imgur.com/MDJpC3Y.png)

### 7. Advanced Properties

22. **Finding Function Inverse**:

Given $$f(x) = \frac{3x + 2}{x - 1}$$:

To find $$f^{-1}(x)$$:

$$
y = \frac{3x + 2}{x - 1} \Rightarrow y(x - 1) = 3x + 2 \Rightarrow yx - y = 3x + 2
$$

$$
yx - 3x = y + 2 \Rightarrow x(y - 3) = y + 2 \Rightarrow x = \frac{y + 2}{y - 3}
$$

**Inverse Function**:

$$
f^{-1}(x) = \frac{x + 2}{x - 3}
$$

23. **Determining Injectivity**:

The function $$f(x) = |x|$$ is **not injective** because $$f(-a) = f(a)$$ for any $$a \neq 0$$, meaning different inputs can produce the same output.

24. **Determining Surjectivity**:

The function $$f(x) = \sqrt{x}$$ is **not surjective** when $$f: \mathbb{R} \rightarrow \mathbb{R}$$ because there are real numbers (negative numbers) that are not outputs of $$f$$. However, if the codomain is $$[0, \infty)$$, then $$f$$ is surjective.

---

# Solutions

*Solutions to the exercises are provided below for self-assessment.*

### 1. Definition and Notation

1. **Function Identification**:

   The relation $$\{(1, 2), (2, 3), (3, 4), (2, 5)\}$$ is **not** a function because the input $$2$$ maps to two different outputs $$3$$ and $$5$$.

2. **Function Notation**:

   The function $$f$$ mapping $$x$$ to $$x^3 - 2x$$ is written as:

   $$
   f(x) = x^3 - 2x
   $$

### 2. Domain and Range

3. **Finding Domain**:

   For $$f(x) = \frac{1}{x - 4}$$, the denominator cannot be zero:

   $$
   x - 4 \neq 0 \Rightarrow x \neq 4
   $$

   **Domain**: $$\mathbb{R} \setminus \{4\}$$

4. **Finding Range**:

   For $$f(x) = \sqrt{9 - x^2}$$, the expression under the square root must be non-negative:

   $$
   9 - x^2 \geq 0 \Rightarrow x^2 \leq 9 \Rightarrow -3 \leq x \leq 3
   $$

   The range of $$f(x)$$ is $$[0, 3]$$.

### 3. Types of Functions

5. **Linear Function**:

   For $$f(x) = -3x + 7$$:

   - **Slope (m)**: $$-3$$
   - **Y-intercept (b)**: $$7$$

6. **Quadratic Function**:

   For $$f(x) = 2x^2 - 8x + 6$$:

   The vertex $$(h, k)$$ is found using:

   $$
   h = -\frac{b}{2a} = -\frac{-8}{2 \cdot 2} = 2
   $$

   $$
   k = f(2) = 2(2)^2 - 8(2) + 6 = 8 - 16 + 6 = -2
   $$

   **Vertex**: $$(2, -2)$$

7. **Polynomial Function**:

   The degree of $$f(x) = 4x^4 - x^3 + 2x - 5$$ is **4** (the highest exponent).

8. **Rational Function**:

   For $$f(x) = \frac{3x + 2}{x^2 - 1}$$:

   The vertical asymptotes occur where the denominator is zero:

   $$
   x^2 - 1 = 0 \Rightarrow x = \pm 1
   $$

   **Vertical Asymptotes**: $$x = 1$$ and $$x = -1$$

### 4. Properties of Functions

9. **Injective Function**:
    
    The function $f(x) = 2x + 1$ is **injective** because for every distinct $x_1$ and $x_2$, $f(x_1) \neq f(x_2)$.
    
10. **Surjective Function**:
    
    The function $f(x) = x^2$ is **not surjective** over $\mathbb{R}$ because there are real numbers (negative numbers) that are not outputs of $f$.
    
11. **Bijective Function**:
    
    The function $f(x) = e^x$ is **not bijective** over $\mathbb{R} \rightarrow \mathbb{R}$ because it is **not surjective** (outputs are always positive).
    
12. **Even or Odd Function**:
    
    For $f(x) = x^4 - x^2$:
    
    $$
    f(-x) = (-x)^4 - (-x)^2 = x^4 - x^2 = f(x)
    $$
    
    Since $f(-x) = f(x)$, $f$ is an **even function**.
    
13. **Periodic Function**:
    
    The function $f(x) = \cos(x)$ is **periodic** with a period of $2\pi$ because:
    
    $$
    \cos(x + 2\pi) = \cos(x)
    $$

### 5. Operations on Functions

14. **Addition of Functions**:
    
    Given $f(x) = x + 2$ and $g(x) = 3x - 1$:
    
    $$
    (f + g)(x) = (x + 2) + (3x - 1) = 4x + 1
    $$
    
15. **Multiplication of Functions**:
    
    Given $f(x) = 2x$ and $g(x) = x^2$:
    
    $$
    (f \cdot g)(x) = 2x \cdot x^2 = 2x^3
    $$
    
16. **Division of Functions**:
    
    Given $f(x) = x^2$ and $g(x) = x + 1$:
    
    $$
    \left(\frac{f}{g}\right)(x) = \frac{x^2}{x + 1}, \quad x \neq -1
    $$
    
17. **Composition of Functions**:
    
    Given $f(x) = 2x$ and $g(x) = x + 3$:
    
    $$
    (f \circ g)(x) = f(g(x)) = f(x + 3) = 2(x + 3) = 2x + 6
    $$
    
18. **Inverse Function**:
    
    Given $f(x) = \frac{x - 5}{3}$:
    
    To find $f^{-1}(x)$, solve for $x$:
    
    $$
    y = \frac{x - 5}{3} \Rightarrow 3y = x - 5 \Rightarrow x = 3y + 5
    $$
    
    **Inverse Function**:
    
    $$
    f^{-1}(x) = 3x + 5
    $$

### 6. Graphing Functions

19. **Graphing Linear Function**:
    
    **Function**: $ f(x) = -x + 4 $
    
    - **Y-intercept**: $ (0, 4) $
    - **Slope**: $ -1 $ (downward slope)
    
    ![Graph of f(x) = -x + 4](https://i.imgur.com/OxQh7Vq.png)
    
20. **Graphing Quadratic Function**:
    
    **Function**: $ f(x) = x^2 - 6x + 8 $
    
    - **Vertex**: $ (3, -1) $
    - **Axis of Symmetry**: $ x = 3 $
    
    ![Graph of f(x) = x^2 - 6x + 8](https://i.imgur.com/1VxP5jR.png)
    
21. **Identifying Asymptotes**:
    
    For $ f(x) = \frac{2}{x - 2} $:
    
    - **Vertical Asymptote**: $ x = 2 $ (denominator zero)
    - **Horizontal Asymptote**: $ y = 0 $ (degree of denominator > degree of numerator)
    
    ![Graph of f(x) = 2/(x-2)](https://i.imgur.com/MDJpC3Y.png)
    
### 7. Advanced Properties

22. **Finding Function Inverse**:
    
    Given $f(x) = \frac{3x + 2}{x - 1}$:
    
    To find $f^{-1}(x)$:
    
    $$
    y = \frac{3x + 2}{x - 1} \Rightarrow y(x - 1) = 3x + 2 \Rightarrow yx - y = 3x + 2
    $$
    
    $$
    yx - 3x = y + 2 \Rightarrow x(y - 3) = y + 2 \Rightarrow x = \frac{y + 2}{y - 3}
    $$
    
    **Inverse Function**:
    
    $$
    f^{-1}(x) = \frac{x + 2}{x - 3}
    $$

23. **Determining Injectivity**:
    
    The function $f(x) = |x|$ is **not injective** because $f(-a) = f(a)$ for any $a \neq 0$, meaning different inputs can produce the same output.
    
24. **Determining Surjectivity**:
    
    The function $f(x) = \sqrt{x}$ is **not surjective** when $f: \mathbb{R} \rightarrow \mathbb{R}$ because there are real numbers (negative numbers) that are not outputs of $f$. However, if the codomain is $[0, \infty)$, then $f$ is surjective.

---

# Conclusion

Functions are integral to understanding and modeling relationships in mathematics and the real world. By mastering their properties, notation, and various types, you can tackle a wide range of problems with confidence. Regular practice through exercises will enhance your proficiency and deepen your comprehension of functional relationships.

