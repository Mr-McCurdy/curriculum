# 🧮 Problem Set: [Subject/Topic]

## 📋 Instructions
Please attempt each problem before viewing the solution. Click on the "Solution" button below each problem to reveal the answer.

---

## 🔢 Problems

<table>
  <tr>
    <td valign="top" width="50%">

### 📝 **Problem 1**
**Description:**
Calculate the probability that a bath fizzy contains \$10 or more.

**Mathematically, this is represented as:**

$$
P(X \geq 10) = P(X = 10) + P(X = 20) + P(X = 50) + P(X = 100)
$$

<details>
  <summary><strong>💡 Solution</strong></summary>
  
  $$ 
  P(X \geq 10) = 0.05 + 0.05 + 0.01 + 0.01 = 0.12
  $$
  
  Therefore, the proportion of bath fizzies that contain at least \$10 is **0.12** or **12%**.
</details>

    </td>
    <td valign="top" width="50%">

### 📝 **Problem 2**
**Description:**
Determine the expected value \( E[X] \) of the random variable \( X \) representing the amount in dollars contained in a bath fizzy.

**Given Probability Distribution:**

| Value (\$) | Probability \( P(X) \) |
|-----------|-----------------------|
| 1         | 0.20                  |
| 2         | 0.05                  |
| 5         | 0.05                  |
| 10        | 0.01                  |
| 20        | 0.01                  |

<details>
  <summary><strong>💡 Solution</strong></summary>
  
  The expected value \( E[X] \) is calculated as:

  $$
  E[X] = \sum_{i} x_i \cdot P(x_i) = (1 \times 0.20) + (2 \times 0.05) + (5 \times 0.05) + (10 \times 0.01) + (20 \times 0.01) = 0.20 + 0.10 + 0.25 + 0.10 + 0.20 = 0.85
  $$

  Therefore, the expected value \( E[X] \) is **\$0.85**.
</details>

    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">

### 📝 **Problem 3**
**Description:**
If the cost to produce a bath fizzy is \$0.50, calculate the expected profit per bath fizzy sold.

<details>
  <summary><strong>💡 Solution</strong></summary>
  
  **Expected Profit \( E[Profit] \):**

  $$
  E[Profit] = E[X] - Cost = 0.85 - 0.50 = 0.35
  $$

  Therefore, the expected profit per bath fizzy sold is **\$0.35**.
</details>

    </td>
    <td valign="top" width="50%">

### 📝 **Problem 4**
**Description:**
What is the variance \( Var(X) \) of the random variable \( X \) representing the amount in dollars contained in a bath fizzy?

**Given Probability Distribution:**

| Value (\$) | Probability \( P(X) \) |
|-----------|-----------------------|
| 1         | 0.20                  |
| 2         | 0.05                  |
| 5         | 0.05                  |
| 10        | 0.01                  |
| 20        | 0.01                  |

<details>
  <summary><strong>💡 Solution</strong></summary>
  
  First, calculate \( E[X^2] \):

  $$
  E[X^2] = \sum_{i} x_i^2 \cdot P(x_i) = (1^2 \times 0.20) + (2^2 \times 0.05) + (5^2 \times 0.05) + (10^2 \times 0.01) + (20^2 \times 0.01) = 0.20 + 0.20 + 1.25 + 1.00 + 4.00 = 6.65
  $$

  Then, calculate the variance:

  $$
  Var(X) = E[X^2] - (E[X])^2 = 6.65 - (0.85)^2 = 6.65 - 0.7225 = 5.9275
  $$

  Therefore, the variance \( Var(X) \) is **5.9275**.
</details>

    </td>
  </tr>
  <!-- Add more problems as needed -->
</table>

---

## 🔗 **Additional Resources**
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [LaTeX Documentation](https://www.latex-project.org/help/documentation/)

---

## 📢 **Notes:**
- **Emojis:** Enhance the visual appeal and provide intuitive cues for interactive elements like solutions.
- **LaTeX Rendering:** Ensure that LaTeX expressions are correctly formatted. Use `$$ ... $$` for display math and `$ ... $` for inline math.
- **Table Structure:** Utilize HTML tables to create a two-column layout, ensuring that each problem and its corresponding solution are side by side.
- **Expandable Solutions:** Use `<details>` and `<summary>` tags to create collapsible sections for solutions, allowing users to attempt problems before viewing answers.

---

### 📌 **Example Rendered Problems:**

# 🧮 Problem Set: Probability Distributions

## 📋 Instructions
Please attempt each problem before viewing the solution. Click on the "Solution" button below each problem to reveal the answer.

---

## 🔢 Problems

<table>
  <tr>
    <td valign="top" width="50%">

### 📝 **Problem 1**
**Description:**
Calculate the probability that a bath fizzy contains \$10 or more.

**Mathematically, this is represented as:**

$$
P(X \geq 10) = P(X = 10) + P(X = 20) + P(X