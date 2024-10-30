# Problem Set: Mathematics

## Table of Contents
1. [Factoring](#factoring)
2. [Trigonometric Ratios](#trigonometric-ratios)
3. [Additional Sections](#additional-sections)
4. [Additional Resources](#additional-resources)

---

## Instructions
- **Attempt Each Problem First**: Try to solve each problem on your own before revealing the solution.
- **View Solutions**: Click on the "Solution" button below each problem to see the detailed answer.

---

## Factoring

### Problem 1
**Factor the quadratic equation:**

$x^2 - 5x + 6 = 0$

 <details>
   <summary><strong>🔎 Hint</strong></summary>
 
   > ##### We need to find the probability that a bath fizzy contains \$10 or more.
   >
   > ##### Mathematically, this is represented as: 
   >
   > $$P(X \geq 10) = P(X = 10) + P(X = 20) + P(X = 50) + P(X = 100) = 0.05 + 0.05 + 0.01 + 0.01 = 0.12$$
   >
   > ##### Therefore, the proportion of bath fizzies that contain at least \$10 is 0.12 or 12%.
 
 </details>

 <details>
   <summary><strong>💡 Answer</strong></summary>
 
   ##### We need to find the probability that a bath fizzy contains \$10 or more.
 
   ##### Mathematically, this is represented as: 
 
   $$P(X \geq 10) = P(X = 10) + P(X = 20) + P(X = 50) + P(X = 100) = 0.05 + 0.05 + 0.01 + 0.01 = 0.12$$
 
   ##### Therefore, the proportion of bath fizzies that contain at least \$10 is 0.12 or 12%.
 
 </details>

> <details>
>   <summary><strong>🔓 Solution</strong></summary>
> 
>   ##### We need to find the probability that a bath fizzy contains \$10 or more.
> 
>   ##### Mathematically, this is represented as: 
> 
>   $$P(X \geq 10) = P(X = 10) + P(X = 20) + P(X = 50) + P(X = 100) = 0.05 + 0.05 + 0.01 + 0.01 = 0.12$$
> 
>   ##### Therefore, the proportion of bath fizzies that contain at least \$10 is 0.12 or 12%.
> 
> </details>

$x^3 - 6x^2 + 11x - 6 = 0$

<details>
  <summary><strong>Solution</strong></summary>
  
To factor \( x^3 - 6x^2 + 11x - 6 = 0 \), we can use the Rational Root Theorem to find possible rational roots.

Testing \( x = 1 \):
$$
1 - 6 + 11 - 6 = 0 \quad \text{(Thus, } x = 1 \text{ is a root)}
$$

Perform polynomial division or synthetic division to factor out \( (x - 1) \):
$$
(x - 1)(x^2 - 5x + 6) = 0
$$

Factor the quadratic:
$$
(x - 1)(x - 2)(x - 3) = 0
$$

Solutions:
$$
x = 1, \quad x = 2, \quad x = 3
$$

</details>

$9x^2 - 25 = 0$

<details>
  <summary><strong>Solution</strong></summary>
  
The expression \( 9x^2 - 25 \) is a difference of squares:
$$
9x^2 - 25 = (3x)^2 - 5^2
$$

Using the identity \( a^2 - b^2 = (a - b)(a + b) \):
$$
(3x - 5)(3x + 5) = 0
$$

Solutions:
$$
3x - 5 = 0 \quad \Rightarrow \quad x = \frac{5}{3}
$$
$$
3x + 5 = 0 \quad \Rightarrow \quad x = -\frac{5}{3}
$$

</details>

---

## Trigonometric Ratios

### Problem 1
**Find the value of \( \sin(\theta) \) if \( \cos(\theta) = \frac{4}{5} \) and \( \theta \) is in the first quadrant.**

<details>
  <summary><strong>Solution</strong></summary>
  
Given \( \cos(\theta) = \frac{4}{5} \) and \( \theta \) is in the first quadrant, we can find \( \sin(\theta) \) using the Pythagorean identity:
$$
\sin^2(\theta) + \cos^2(\theta) = 1
$$

Substitute \( \cos(\theta) \):
$$
\sin^2(\theta) + \left(\frac{4}{5}\right)^2 = 1 \\
\sin^2(\theta) + \frac{16}{25} = 1 \\
\sin^2(\theta) = 1 - \frac{16}{25} = \frac{9}{25} \\
\sin(\theta) = \frac{3}{5} \quad \text{(since \( \theta \) is in the first quadrant)}
$$

</details>

---

### Problem 2
**Simplify the expression:**
$$
\frac{\tan(\theta)}{1 + \cot(\theta)}
$$

<details>
  <summary><strong>Solution</strong></summary>
  
Start by expressing \( \tan(\theta) \) and \( \cot(\theta) \) in terms of sine and cosine:
$$
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} \\
\cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
$$

Substitute into the original expression:
$$
\frac{\frac{\sin(\theta)}{\cos(\theta)}}{1 + \frac{\cos(\theta)}{\sin(\theta)}} = \frac{\sin(\theta)}{\cos(\theta)} \div \left( \frac{\sin(\theta) + \cos(\theta)}{\sin(\theta)} \right) = \frac{\sin^2(\theta)}{\cos(\theta)(\sin(\theta) + \cos(\theta))}
$$

Simplify by factoring:
$$
\frac{\sin(\theta)}{\cos(\theta)} \cdot \frac{\sin(\theta)}{\sin(\theta) + \cos(\theta)} = \tan(\theta) \cdot \frac{\sin(\theta)}{\sin(\theta) + \cos(\theta)}
$$

Final simplified form:
$$
\frac{\sin^2(\theta)}{\cos(\theta)(\sin(\theta) + \cos(\theta))}
$$

</details>

---

### Problem 3
**Prove that \( \tan(\theta) + \cot(\theta) = \frac{2}{\sin(2\theta)} \).**

<details>
  <summary><strong>Solution</strong></summary>
  
Start with the left-hand side (LHS):
$$
\tan(\theta) + \cot(\theta) = \frac{\sin(\theta)}{\cos(\theta)} + \frac{\cos(\theta)}{\sin(\theta)} = \frac{\sin^2(\theta) + \cos^2(\theta)}{\sin(\theta)\cos(\theta)} = \frac{1}{\sin(\theta)\cos(\theta)}
$$

Recall the double-angle identity for sine:
$$
\sin(2\theta) = 2\sin(\theta)\cos(\theta) \quad \Rightarrow \quad \sin(\theta)\cos(\theta) = \frac{\sin(2\theta)}{2}
$$

Substitute into the LHS:
$$
\frac{1}{\sin(\theta)\cos(\theta)} = \frac{2}{\sin(2\theta)}
$$

Therefore:
$$
\tan(\theta) + \cot(\theta) = \frac{2}{\sin(2\theta)}
$$

</details>

---

## Additional Sections

> **Note:** This section is a placeholder. You can add more sections for different types of problems following the structure used in the "Factoring" and "Trigonometric Ratios" sections.

### Section Title
**Description:**
Brief description of the problem type.

### Problem X
**Description:**
Detailed problem statement.

<details>
  <summary><strong>Solution</strong></summary>
  
Detailed solution steps, including any necessary LaTeX expressions.

</details>

---

## Additional Resources
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [LaTeX Project](https://www.latex-project.org/)
- [Wolfram MathWorld](https://mathworld.wolfram.com/)

---

## Notes
- **LaTeX Rendering:** Ensure that LaTeX expressions are correctly formatted. Use `$$ ... $$` for display math and `$ ... $` for inline math.
- **Table of Contents:** Update the Table of Contents as you add new sections to maintain easy navigation.
- **Consistent Formatting:** Maintain a uniform structure for each problem and solution to ensure readability.
- **Expandability:** Easily add more sections and problems by following the established template structure.
- **Previewing:** Regularly push your Markdown file to GitHub and use the platform's preview feature to ensure everything renders correctly.

---