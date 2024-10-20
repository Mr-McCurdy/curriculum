# 2. Applying Set Theory to Probability

## 2.1. What is Probability?

Probability is a measure of how likely an event is to occur. The set of all possible outcomes of an experiment is called the *sample space*.

- **Sample Space ( $S$ ):** The set of all possible outcomes. For example, when flipping a coin:

  $S = \{\text{Heads, Tails}\}$

- **Event ( $A$ ):** A subset of the sample space, representing outcomes of interest. For example, $A$ could be the event of flipping a heads:

  $A = \{\text{Heads}\}$

- **Probability of an Event ( $p$ ):** The probability of a specific event occurring is often denoted by the lowercase letter $p$. For example, if $p$ is the probability of flipping heads with a fair coin, then $p = 0.5$.

**Question 1:** *What are elements in a sample space called?*

**Answer:** In the context of probability theory, elements in a sample space are called *outcomes* or *sample points*.

**Question 2:** *How do we represent an event that includes multiple outcomes?*

**Answer:** An event that includes multiple outcomes is represented as a subset of the sample space. For example, if $S = \{1, 2, 3, 4, 5, 6\}$ represents the possible outcomes of a die roll, the event $ B $ of rolling an even number could be represented as $B = \{2, 4, 6\}$.

**Question 3:** *Can the sample space contain events that are not equally likely?*

**Answer:** Yes, the sample space can contain events that are not equally likely. For instance, if a die is biased, some numbers may be more likely to occur than others, affecting the probability of each outcome.

---

**Sample Exercise 1:**

Consider rolling a standard six-sided die. What is the probability of rolling a number greater than 4?

**Step-by-Step Solution:**

1. **Identify the sample space $S$:**

   $S = \{1, 2, 3, 4, 5, 6\}$

2. **Define the event $A$:**

   Let $A$ be the event of rolling a number greater than 4, so $A = \{5, 6\}$.

3. **Calculate the probability:**

   $$
   P(A) = \frac{|A|}{|S|} = \frac{2}{6} = \frac{1}{3}
   $$

**Answer:** The probability of rolling a number greater than 4 is $\frac{1}{3}$.

---

**Sample Exercise 2:**

A bag contains 7 red balls, 5 blue balls, and 3 yellow balls. What is the probability of drawing a yellow ball?

**Step-by-Step Solution:**

1. **Identify the total number of balls:**

   $|S| = 7 + 5 + 3 = 15$

2. **Define the event $Y$:**

   Let $Y$ be the event of drawing a yellow ball, so $|Y| = 3$.

3. **Calculate the probability:**

   $$
   P(Y) = \frac{|Y|}{|S|} = \frac{3}{15} = \frac{1}{5}
   $$

**Answer:** The probability of drawing a yellow ball is $\frac{1}{5}$.

---

**Sample Exercise 3:**

A box contains 3 red, 4 blue, and 5 green balls. If you randomly select a ball, what is the probability that it is neither red nor blue?

**Step-by-Step Solution:**

1. **Identify the total number of balls:**

   $|S| = 3 + 4 + 5 = 12$

2. **Define the event $G$:**

   Let $G$ be the event of drawing a green ball, so $|G| = 5$.

3. **Calculate the probability:**

   $$
   P(G) = \frac{|G|}{|S|} = \frac{5}{12}
   $$

**Answer:** The probability that the ball is neither red nor blue is $\frac{5}{12}$.

---

## 2.2. Probability Function

The probability function $P$ assigns a probability to each event in the sample space. This is often denoted as $P(A)$, where $A$ is an event.

- **Lowercase $p$:** As noted earlier, lowercase $p$ is commonly used to denote the probability of a specific event occurring, especially in situations involving multiple or repetitive trials, such as in the binomial distribution.

- **Example:** If the event $A$ is flipping a heads, and we assume the coin is fair, then:

  $P(\text{Heads}) = 0.5 \quad \text{or} \quad p = 0.5$

**Question 1:** *How does $P$ fit into the context of a function?*

**Answer:** $P$ is a function that maps events (which are sets of outcomes) to a number between 0 and 1, representing the likelihood of the event occurring. So, $P: \text{Events} \rightarrow [0, 1]$.

**Question 2:** *What is the sum of the probabilities of all possible outcomes in a sample space?*

**Answer:** The sum of the probabilities of all possible outcomes in a sample space is always 1. This is because one of the outcomes must occur, making the total probability 1.

**Question 3:** *Can the probability of an event be greater than 1 or less than 0?*

**Answer:** No, the probability of an event must always be between 0 and 1, inclusive. A probability of 0 means the event cannot occur, while a probability of 1 means the event is certain to occur.

---

**Sample Exercise 1:**

A jar contains 4 red, 6 blue, and 10 green marbles. What is the probability of drawing a green marble?

**Step-by-Step Solution:**

1. **Identify the total number of marbles:**

   $|S| = 4 + 6 + 10 = 20$

2. **Define the event $G$:**

   Let $G$ be the event of drawing a green marble, so $|G| = 10$.

3. **Calculate the probability:**

   $$
   P(G) = \frac{|G|}{|S|} = \frac{10}{20} = \frac{1}{2}
   $$

**Answer:** The probability of drawing a green marble is $\frac{1}{2}$.

---

**Sample Exercise 2:**

If a die is rolled, what is the probability of rolling a number greater than 4?

**Step-by-Step Solution:**

1. **Identify the sample space $S$:**

   $S = \{1, 2, 3, 4, 5, 6\}$

2. **Define the event $A$:**

   Let $A$ be the event of rolling a number greater than 4, so $A = \{5, 6\}$.

3. **Calculate the probability:**

   $$
   P(A) = \frac{|A|}{|S|} = \frac{2}{6} = \frac{1}{3}
   $$

**Answer:** The probability of rolling a number greater than 4 is $\frac{1}{3}$.

---

**Sample Exercise 3:**

In a group of 8 people, what is the probability that at least two of them share the same birthday?

**Step-by-Step Solution:**

1. **Identify the total number of possible outcomes for each person:**

   $|S| = 365^8$ (assuming a non-leap year with 365 days).

2. **Define the event $A$:**

   Let $A$ be the event that at least two people share the same birthday.

3. **Use the complement rule:**

   Calculate the probability that no one shares a birthday and subtract from 1.

   $$
   P(\text{no shared birthday}) = \frac{365}{365} \times \frac{364}{365} \times \dots \times \frac{358}{365}
   $$

   $$
   P(A) = 1 - P(\text{no shared birthday})
   $$

**Answer:** The exact probability would require further computation, but $P(A)$ gives the probability that at least two people share the same birthday.

---

## 2.3. Probability Rules

### 2.3.1. Addition Rule and Disjoint Events

The addition rule is used to find the probability that at least one of two events occurs.

- **Addition Rule:** If $A$ and $B$ are two events in a sample space:

  $$
  P(A \cup B) = P(A) + P(B) - P(A \cap B)
  $$

  If $A$ and $B$ are disjoint (i.e., mutually exclusive events with no outcomes in common), then:

  $$
  P(A \cup B) = P(A) + P(B)
  $$

**Question 1:** *What is the probability of the union of two disjoint events?*

**Answer:** If two events are disjoint, the probability of their union is the sum of their individual probabilities. For example, if $A$ and $B$ are disjoint, then $P(A \cup B) = P(A) + P(B)$.

**Question 2:** *Can the addition rule be used for non-disjoint events?*

**Answer:** Yes, but you must subtract the probability of the intersection $P(A \cap B)$ to avoid double-counting the overlap.

**Question 3:** *What does it mean for two events to be disjoint?*

**Answer:** Two events are disjoint if they have no outcomes in common. For example, in a single roll of a die, the events "rolling a 1" and "rolling a 2" are disjoint.

---

**Sample Exercise 1:**

What is the probability of drawing a red or black card from a deck of 52 playing cards?

**Step-by-Step Solution:**

1. **Define the events:**

   Let $R$ be the event of drawing a red card and $B$ be the event of drawing a black card.

   - $|R| = 26$ (since there are 26 red cards).
   - $|B| = 26$ (since there are 26 black cards).
   - $|R \cap B| = 0$ (red and black are disjoint).

2. **Apply the addition rule:**

   $$
   P(R \cup B) = P(R) + P(B) = \frac{26}{52} + \frac{26}{52} = 1
   $$

**Answer:** The probability of drawing a red or black card is 1 (since all cards are either red or black).

---

**Sample Exercise 2:**

If two dice are rolled, what is the probability of getting a sum of 7 or 11?

**Step-by-Step Solution:**

1. **Define the events:**

   Let $A$ be the event of getting a sum of 7, and $B$ be the event of getting a sum of 11.

   - $|A| = 6$ (combinations: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)).
   - $|B| = 2$ (combinations: (5,6), (6,5)).
   - $|A \cap B| = 0$ (events are disjoint).

2. **Apply the addition rule:**

   $$
   P(A \cup B) = P(A) + P(B) = \frac{6}{36} + \frac{2}{36} = \frac{8}{36} = \frac{2}{9}
   $$

**Answer:** The probability of getting a sum of 7 or 11 is $\frac{2}{9}$.

---

**Sample Exercise 3:**

A bag contains 4 red, 3 blue, and 2 green marbles. What is the probability of drawing a red or a green marble?

**Step-by-Step Solution:**

1. **Define the events:**

   - Let $R$ be the event of drawing a red marble: $|R| = 4$.
   - Let $G$ be the event of drawing a green marble: $|G| = 2$.
   - Total marbles: $|S| = 9$.
   - $R$ and $G$ are disjoint.

2. **Apply the addition rule:**

   $$
   P(R \cup G) = P(R) + P(G) = \frac{4}{9} + \frac{2}{9} = \frac{6}{9} = \frac{2}{3}
   $$

**Answer:** The probability of drawing a red or a green marble is $\frac{2}{3}$.

---

### 2.3.2. Conditional Probability

Conditional probability measures the probability of one event occurring given that another event has already occurred.

- **Conditional Probability:** The probability of $A$ occurring given that $B$ has occurred:

  $$
  P(A | B) = \frac{P(A \cap B)}{P(B)}
  $$

  where $P(B) > 0$.

**Question 1:** *Why do we need conditional probability?*

**Answer:** Conditional probability allows us to update the probability of an event based on new information, specifically the occurrence of another event.

**Question 2:** *What happens if $P(B) = 0$ in conditional probability?*

**Answer:** If $P(B) = 0$, the conditional probability $P(A | B)$ is undefined because division by zero is not possible.

**Question 3:** *How does conditional probability relate to the concept of independence?*

**Answer:** If two events are independent, the occurrence of one does not affect the probability of the other, so $P(A | B) = P(A)$.

---

**Sample Exercise 1:**

Given that a card drawn from a deck is a king, what is the probability that it is the king of hearts?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $K$: drawing a king ($|K| = 4$).
   - $H$: the king of hearts ($|H| = 1$).
   - $H \cap K$: the king of hearts ($|H \cap K| = 1$).

2. **Apply the conditional probability formula:**

   $$
   P(H | K) = \frac{P(H \cap K)}{P(K)} = \frac{\frac{1}{52}}{\frac{4}{52}} = \frac{1}{4}
   $$

**Answer:** The probability that the card is the king of hearts, given that it is a king, is $\frac{1}{4}$.

---

**Sample Exercise 2:**

A bag contains 8 red, 5 green, and 2 blue balls. If a ball is drawn and is known to be red, what is the probability that it is one of the three smallest red balls?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $R$: drawing a red ball ($|R| = 8$).
   - $S$: drawing one of the three smallest red balls ($|S \cap R| = 3$).

2. **Apply the conditional probability formula:**

   $$
   P(S | R) = \frac{P(S \cap R)}{P(R)} = \frac{\frac{3}{15}}{\frac{8}{15}} = \frac{3}{8}
   $$

**Answer:** The probability that it is one of the three smallest red balls, given that it is red, is $\frac{3}{8}$.

---

**Sample Exercise 3:**

In a deck of 52 playing cards, what is the probability of drawing a heart given that the card is red?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $R$: drawing a red card ($|R| = 26$).
   - $H$: drawing a heart ($|H \cap R| = 13$).

2. **Apply the conditional probability formula:**

   $$
   P(H | R) = \frac{P(H \cap R)}{P(R)} = \frac{\frac{13}{52}}{\frac{26}{52}} = \frac{13}{26} = \frac{1}{2}
   $$

**Answer:** The probability of drawing a heart given that the card is red is $\frac{1}{2}$.

---

### 2.3.3. Multiplication Rule and Independent Events

The multiplication rule is used to find the probability of the intersection of two events.

- **Multiplication Rule:** For any two events $A$ and $B$, the probability of both events occurring is:

  $$
  P(A \cap B) = P(A | B) \times P(B)
  $$

- **Independent Events:** Two events $A$ and $B$ are independent if the occurrence of one does not affect the probability of the other. Mathematically, $A$ and $B$ are independent if:

  $$
  P(A | B) = P(A)
  $$

  Substituting this into the multiplication rule gives:

  $$
  P(A \cap B) = P(A) \times P(B)
  $$

**Question 1:** *How do you know if two events are independent?*

**Answer:** Two events are independent if the probability of one event occurring does not change the probability of the other event. This can be tested using the formula $P(A | B) = P(A)$.

**Question 2:** *What is the difference between independent and disjoint events?*

**Answer:** Disjoint events cannot happen at the same time (they have no outcomes in common), while independent events can occur simultaneously, but the occurrence of one does not affect the occurrence of the other.

**Question 3:** *Can the multiplication rule be used for dependent events?*

**Answer:** Yes, but you must use the general multiplication rule $P(A \cap B) = P(A | B) \times P(B)$, where you account for the dependency by using the conditional probability $P(A | B)$.

---

**Sample Exercise 1:**

If a die is rolled twice, what is the probability of getting a 6 on both rolls?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $A$: rolling a 6 on the first roll ($P(A) = \frac{1}{6}$).
   - $B$: rolling a 6 on the second roll ($P(B) = \frac{1}{6}$).
   - $A$ and $B$ are independent.

2. **Apply the multiplication rule:**

   $$
   P(A \cap B) = P(A) \times P(B) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}
   $$

**Answer:** The probability of getting a 6 on both rolls is $\frac{1}{36}$.

---

**Sample Exercise 2:**

If a coin is flipped three times, what is the probability of getting heads on all three flips?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $H_1$: heads on first flip ($P(H_1) = \frac{1}{2}$).
   - $H_2$: heads on second flip ($P(H_2) = \frac{1}{2}$).
   - $H_3$: heads on third flip ($P(H_3) = \frac{1}{2}$).
   - Events are independent.

2. **Apply the multiplication rule:**

   $$
   P(H_1 \cap H_2 \cap H_3) = P(H_1) \times P(H_2) \times P(H_3) = \left( \frac{1}{2} \right)^3 = \frac{1}{8}
   $$

**Answer:** The probability of getting heads on all three flips is $\frac{1}{8}$.

---

**Sample Exercise 3:**

A card is drawn from a deck, and then another card is drawn without replacement. What is the probability that both cards are aces?

**Step-by-Step Solution:**

1. **Identify the events:**

   - $A_1$: first card is an ace ($P(A_1) = \frac{4}{52} = \frac{1}{13}$).
   - $A_2$: second card is an ace given the first was an ace ($P(A_2 | A_1) = \frac{3}{51}$).

2. **Apply the multiplication rule:**

   $$
   P(A_1 \cap A_2) = P(A_1) \times P(A_2 | A_1) = \frac{1}{13} \times \frac{3}{51} = \frac{3}{663} = \frac{1}{221}
   $$

**Answer:** The probability that both cards are aces is $\frac{1}{221}$.

---

## 2.4. Discrete vs. Continuous Events

### 2.4.1. Discrete Events

Discrete events are those where the outcomes can be counted, even if infinite (e.g., rolling a die, flipping a coin).

**Question 1:** *What defines a discrete event?*

**Answer:** A discrete event is characterized by a finite or countable set of outcomes. For example, the number of heads in 10 coin flips is a discrete event.

**Question 2:** *How does the probability of a discrete event differ from a continuous event?*

**Answer:** The probability of a discrete event is the sum of the probabilities of individual outcomes, while the probability of a continuous event involves integrating the probability density function over a range of values.

**Question 3:** *Can a discrete event have an infinite number of outcomes?*

**Answer:** Yes, a discrete event can have an infinite number of outcomes, such as counting the number of trials until the first success in a geometric distribution.

---

**Sample Exercise 1:**

What is the probability of rolling a 2 or a 5 on a standard six-sided die?

**Step-by-Step Solution:**

1. **Identify the sample space $S$:**

   $S = \{1, 2, 3, 4, 5, 6\}$

2. **Define the event $A$:**

   $A = \{2, 5\}$

3. **Calculate the probability:**

   $$
   P(A) = \frac{|A|}{|S|} = \frac{2}{6} = \frac{1}{3}
   $$

**Answer:** The probability of rolling a 2 or a 5 is $\frac{1}{3}$.

---

**Sample Exercise 2:**

If a die is rolled four times, what is the probability of getting at least one 6?

**Step-by-Step Solution:**

1. **Calculate the probability of not getting a 6 in any roll:**

   $$
   P(\text{no 6 in one roll}) = \frac{5}{6}
   $$

   $$
   P(\text{no 6 in four rolls}) = \left( \frac{5}{6} \right)^4
   $$

2. **Calculate the probability of getting at least one 6:**

   $$
   P(\text{at least one 6}) = 1 - P(\text{no 6 in four rolls}) = 1 - \left( \frac{5}{6} \right)^4 \approx 1 - 0.4823 = 0.5177
   $$

**Answer:** The probability of getting at least one 6 is approximately $0.5177$.

---

**Sample Exercise 3:**

In a lottery where you must choose a number between 1 and 100, what is the probability of selecting a number divisible by 10?

**Step-by-Step Solution:**

1. **Identify the numbers divisible by 10:**

   $A = \{10, 20, 30, \dots, 100\}$

   Total numbers divisible by 10: $|A| = 10$

2. **Calculate the probability:**

   $$
   P(A) = \frac{|A|}{|S|} = \frac{10}{100} = \frac{1}{10}
   $$

**Answer:** The probability of selecting a number divisible by 10 is $\frac{1}{10}$.

---

### 2.4.2. Continuous Events

Continuous events are those where the outcomes cannot be counted individually, but rather, they form a continuum (e.g., time, temperature).

**Question 1:** *What defines a continuous event?*

**Answer:** A continuous event is characterized by an infinite number of possible outcomes within a given range. For example, the exact time it takes to run a race is a continuous variable.

**Question 2:** *How is probability represented in a continuous event?*

**Answer:** In continuous events, probability is represented as the area under the probability density function (PDF) curve within a specific interval.

**Question 3:** *Can a continuous event have a probability of zero?*

**Answer:** Yes, in continuous distributions, the probability of any single exact outcome (like $P(X = a)$) is zero, but the probability of an interval of outcomes (like $P(a < X < b)$) is greater than zero.

---

**Sample Exercise 1:**

If the time it takes to complete a task is uniformly distributed between 30 and 60 minutes, what is the probability that the task takes between 40 and 50 minutes?

**Step-by-Step Solution:**

1. **Identify the interval:**

   - Total interval: $[30, 60]$.
   - Interval of interest: $[40, 50]$.

2. **Calculate the probability:**

   $$
   P(40 \leq X \leq 50) = \frac{50 - 40}{60 - 30} = \frac{10}{30} = \frac{1}{3}
   $$

**Answer:** The probability that the task takes between 40 and 50 minutes is $\frac{1}{3}$.

---

**Sample Exercise 2:**

The weight of a certain fruit is normally distributed with a mean of 200 grams and a standard deviation of 20 grams. What is the probability that a randomly selected fruit weighs more than 240 grams?

**Step-by-Step Solution:**

1. **Calculate the z-score:**

   $$
   z = \frac{240 - 200}{20} = 2
   $$

2. **Find the probability:**

   Using the standard normal distribution table:

   $$
   P(Z > 2) = 1 - P(Z < 2) = 1 - 0.9772 = 0.0228
   $$

**Answer:** The probability that a randomly selected fruit weighs more than 240 grams is approximately $0.0228$.

---

**Sample Exercise 3:**

The length of time customers spend on a website is exponentially distributed with a mean of 5 minutes. What is the probability that a customer spends more than 10 minutes on the website?

**Step-by-Step Solution:**

1. **Determine the rate parameter $ \lambda $:**

   $$
   \lambda = \frac{1}{\text{mean}} = \frac{1}{5} = 0.2
   $$

2. **Calculate the probability:**

   $$
   P(X > 10) = e^{-\lambda x} = e^{-0.2 \times 10} = e^{-2} \approx 0.1353
   $$

**Answer:** The probability that a customer spends more than 10 minutes on the website is approximately $0.1353$.

---

## 2.5. Probability Distributions

### 2.5.1. Uniform Distribution

The uniform distribution is a type of probability distribution where all outcomes are equally likely within a given interval.

**Question 1:** *What is a uniform distribution?*

**Answer:** A uniform distribution is one where all outcomes are equally likely within a specified range. The probability of any interval is proportional to its length.

**Question 2:** *How do you calculate the probability of an event in a uniform distribution?*

**Answer:** The probability is calculated as the ratio of the length of the desired interval to the length of the total interval.

**Question 3:** *Can a uniform distribution be applied to discrete events?*

**Answer:** Yes, a uniform distribution can apply to both discrete and continuous events, depending on whether the outcomes are countable.

---

**Sample Exercise 1:**

What is the probability of selecting a number between 4 and 7 from a uniform distribution on the interval $[0, 10]$?

**Step-by-Step Solution:**

1. **Identify the interval:**

   - Total interval: $[0, 10]$.
   - Interval of interest: $[4, 7]$.

2. **Calculate the probability:**

   $$
   P(4 \leq X \leq 7) = \frac{7 - 4}{10 - 0} = \frac{3}{10} = 0.3
   $$

**Answer:** The probability of selecting a number between 4 and 7 is $0.3$.

---

**Sample Exercise 2:**

If a spinner is equally divided into 8 sections, what is the probability of landing on section 3?

**Step-by-Step Solution:**

1. **Total sections:**

   $|S| = 8$

2. **Probability:**

   $$
   P(\text{section 3}) = \frac{1}{8}
   $$

**Answer:** The probability of landing on section 3 is $\frac{1}{8}$.

---

**Sample Exercise 3:**

In a uniform distribution over the interval $[0, 20]$, what is the probability of selecting a number between 5 and 15?

**Step-by-Step Solution:**

1. **Identify the interval:**

   - Total interval: $[0, 20]$.
   - Interval of interest: $[5, 15]$.

2. **Calculate the probability:**

   $$
   P(5 \leq X \leq 15) = \frac{15 - 5}{20 - 0} = \frac{10}{20} = \frac{1}{2}
   $$

**Answer:** The probability of selecting a number between 5 and 15 is $\frac{1}{2}$.

---

### 2.5.2. Binomial Distribution

The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials.

**Question 1:** *What is the binomial distribution used for?*

**Answer:** The binomial distribution is used to model the number of successes in a fixed number of independent trials, where each trial has two possible outcomes (success or failure).

**Question 2:** *How do you calculate binomial probabilities?*

**Answer:** Binomial probabilities are calculated using the formula:

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

where $n$ is the number of trials, $k$ is the number of successes, and $p$ is the probability of success on each trial.

**Question 3:** *Can the binomial distribution be applied to continuous events?*

**Answer:** No, the binomial distribution applies only to discrete events with a fixed number of trials and two possible outcomes per trial.

---

**Sample Exercise 1:**

In a batch of 15 light bulbs, 4 are defective. If you randomly select 3 bulbs, what is the probability that exactly 1 is defective?

**Step-by-Step Solution:**

1. **Parameters:**

   - $n = 3$
   - $k = 1$
   - $p = \frac{4}{15}$
   - $q = 1 - p = \frac{11}{15}$

2. **Calculate probability:**

   $$
   P(X = 1) = \binom{3}{1} \left( \frac{4}{15} \right)^1 \left( \frac{11}{15} \right)^{2} = 3 \times \frac{4}{15} \times \left( \frac{121}{225} \right) \approx 0.43
   $$

**Answer:** The probability that exactly 1 bulb is defective is approximately $0.43$.

---

**Sample Exercise 2:**

If you flip a coin 5 times, what is the probability of getting exactly 3 heads?

**Step-by-Step Solution:**

1. **Parameters:**

   - $n = 5$
   - $k = 3$
   - $p = 0.5$

2. **Calculate probability:**

   $$
   P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^{2} = 10 \times 0.125 \times 0.25 = 0.3125
   $$

**Answer:** The probability of getting exactly 3 heads is $0.3125$.

---

**Sample Exercise 3:**

A basketball player makes 70% of free throws. What is the probability that she makes exactly 4 out of 6 free throws?

**Step-by-Step Solution:**

1. **Parameters:**

   - $n = 6$
   - $k = 4$
   - $p = 0.7$
   - $q = 0.3$

2. **Calculate probability:**

   $$
   P(X = 4) = \binom{6}{4} (0.7)^4 (0.3)^2 = 15 \times 0.2401 \times 0.09 \approx 0.324
   $$

**Answer:** The probability that she makes exactly 4 out of 6 free throws is approximately $0.324$.

---

### 2.5.3. Normal Distribution

The normal distribution is a continuous probability distribution characterized by a symmetric, bell-shaped curve.

**Question 1:** *What are the properties of a normal distribution?*

**Answer:** The normal distribution is symmetric around the mean, with the majority of the data falling within one standard deviation of the mean. It is defined by its mean $\mu$ and standard deviation $\sigma$.

**Question 2:** *How do you calculate probabilities in a normal distribution?*

**Answer:** Probabilities are calculated using the z-score formula and standard normal distribution tables:

$$
z = \frac{X - \mu}{\sigma}
$$

**Question 3:** *Can the normal distribution be used for discrete events?*

**Answer:** The normal distribution is primarily used for continuous events but can approximate certain discrete distributions (e.g., binomial) under specific conditions (e.g., large sample sizes).

---

**Sample Exercise 1:**

Find the probability that a normally distributed variable $ X $ with a mean of 100 and a standard deviation of 20 falls between 90 and 110.

**Step-by-Step Solution:**

1. **Calculate z-scores:**

   - For $X = 90$:

     $$
     z_1 = \frac{90 - 100}{20} = -0.5
     $$

   - For $X = 110$:

     $$
     z_2 = \frac{110 - 100}{20} = 0.5
     $$

2. **Find probabilities:**

   - $P(Z < 0.5) \approx 0.6915$
   - $P(Z < -0.5) \approx 0.3085$

3. **Calculate the probability:**

   $$
   P(90 \leq X \leq 110) = P(Z < 0.5) - P(Z < -0.5) = 0.6915 - 0.3085 = 0.383
   $$

**Answer:** The probability that $X$ falls between 90 and 110 is $0.383$.

---

**Sample Exercise 2:**

A standardized test has scores that are normally distributed with a mean of 600 and a standard deviation of 100. What is the probability that a student scores between 500 and 700?

**Step-by-Step Solution:**

1. **Calculate z-scores:**

   - For $X = 500$:

     $$
     z_1 = \frac{500 - 600}{100} = -1
     $$

   - For $X = 700$:

     $$
     z_2 = \frac{700 - 600}{100} = 1
     $$

2. **Find probabilities:**

   - $P(Z < 1) \approx 0.8413$
   - $P(Z < -1) \approx 0.1587$

3. **Calculate the probability:**

   $$
   P(500 \leq X \leq 700) = P(Z < 1) - P(Z < -1) = 0.8413 - 0.1587 = 0.6826
   $$

**Answer:** The probability that a student scores between 500 and 700 is $0.6826$.

---

**Sample Exercise 3:**

What is the probability that a normally distributed variable with a mean of 50 and a standard deviation of 10 is greater than 60?

**Step-by-Step Solution:**

1. **Calculate the z-score:**

   $$
   z = \frac{60 - 50}{10} = 1
   $$

2. **Find the probability:**

   $$
   P(X > 60) = 1 - P(Z < 1) = 1 - 0.8413 = 0.1587
   $$

**Answer:** The probability that $X$ is greater than 60 is $0.1587$.

---

### 2.5.4. Geometric Distribution

The geometric distribution models the number of trials until the first success in a series of independent Bernoulli trials.

**Question 1:** *What is the geometric distribution used for?*

**Answer:** It is used to model the number of trials needed to achieve the first success in a sequence of independent trials with two possible outcomes.

**Question 2:** *How do you calculate geometric probabilities?*

**Answer:** Using the formula:

$$
P(X = k) = (1 - p)^{k - 1} p
$$

where $k$ is the trial number of the first success, and $p$ is the probability of success.

**Question 3:** *Can the geometric distribution be applied to continuous events?*

**Answer:** No, it applies only to discrete events.

---

**Sample Exercise 1:**

What is the probability that the first success occurs on the 4th trial if the probability of success on each trial is 0.3?

**Step-by-Step Solution:**

1. **Parameters:**

   - $p = 0.3$
   - $q = 1 - p = 0.7$
   - $k = 4$

2. **Calculate probability:**

   $$
   P(X = 4) = (0.7)^{3} \times 0.3 = 0.343 \times 0.3 = 0.1029
   $$

**Answer:** The probability that the first success occurs on the 4th trial is $0.1029$.

---

**Sample Exercise 2:**

If the probability of hitting a target is 0.6, what is the probability that the first hit occurs on the 2nd shot?

**Step-by-Step Solution:**

1. **Parameters:**

   - $p = 0.6$
   - $q = 0.4$
   - $k = 2$

2. **Calculate probability:**

   $$
   P(X = 2) = (0.4)^{1} \times 0.6 = 0.4 \times 0.6 = 0.24
   $$

**Answer:** The probability that the first hit occurs on the 2nd shot is $ 0.24 $.

---

**Sample Exercise 3:**

A factory tests items for defects with a 10% defect rate. What is the probability that the first defective item is found on the 5th test?

**Step-by-Step Solution:**

1. **Parameters:**

   - $p = 0.1$
   - $q = 0.9$
   - $k = 5$

2. **Calculate probability:**

   $$
   P(X = 5) = (0.9)^{4} \times 0.1 = 0.6561 \times 0.1 = 0.06561
   $$

**Answer:** The probability that the first defective item is found on the 5th test is $0.06561$.

---

## 2. Exercises

### 2.1. What is Probability?

1. A bag contains 5 red, 4 green, and 6 yellow balls. What is the probability of drawing a red or green ball?
2. In a standard deck of cards, what is the probability of drawing an ace or a king?
3. A box contains 3 defective and 7 non-defective light bulbs. What is the probability of randomly selecting a defective bulb?
4. What is the probability of rolling an even number on a six-sided die?
5. A basket contains 8 apples and 4 oranges. What is the probability of randomly selecting an apple?
6. If a number is randomly selected from 1 to 100, what is the probability that it is a multiple of 5?
7. A spinner is divided into 5 equal sections. What is the probability of the spinner landing on section 1 or 2?

### 2.2. Probability Function

8. In a group of 10 people, what is the probability that at least two people share the same birthday?
9. A die is rolled twice. What is the probability of getting a sum of 8 or more?
10. If a card is drawn from a standard deck, what is the probability of drawing a face card (jack, queen, or king)?
11. A lottery ticket has a 1 in 1000 chance of winning. What is the probability of not winning if you buy one ticket?
12. If two dice are rolled, what is the probability of getting a sum of 4 or 7?
13. In a class of 30 students, what is the probability that at least one student has the same birthday as you?
14. A jar contains 10 blue, 15 red, and 5 green marbles. What is the probability of drawing a blue or green marble?

### 2.3. Probability Rules

#### 2.3.1. Addition Rule and Disjoint Events

15. What is the probability of drawing a heart or a spade from a deck of cards?
16. A bag contains 3 white, 4 black, and 5 red balls. What is the probability of drawing a white or red ball?
17. If a die is rolled, what is the probability of getting a 3 or a 5?
18. In a class of 25 students with 4 freshmen, 6 sophomores, 7 juniors, and the rest seniors, what is the probability that a randomly selected student is either a sophomore or a junior?
19. A coin is flipped twice. What is the probability of getting at least one head?
20. What is the probability of drawing a queen or a king from a deck of cards?
21. A lottery has 10 prizes and 90 blanks. What is the probability of drawing a prize or a blank?

#### 2.3.2. Conditional Probability

22. Given that a card drawn from a deck is a spade, what is the probability that it is the ace of spades?
23. A bag contains 6 black and 4 white balls. If one ball is drawn and it is black, what is the probability that it is the largest black ball?
24. If a card is drawn from a deck and is known to be a face card, what is the probability that it is a queen?
25. A box contains 5 red and 5 blue marbles. If a marble is drawn and is known to be red, what is the probability that it is the smallest red marble?
26. In a deck of 52 cards, what is the probability of drawing a diamond given that the card is red?
27. A bag contains 10 balls numbered 1 to 10. If a ball is drawn and is known to be even, what is the probability that it is a 4?
28. In a class of 30 students, what is the probability that a randomly selected student is a senior given that they are in the top 5 of the class?

#### 2.3.3. Multiplication Rule and Independent Events

29. If a die is rolled twice, what is the probability of getting a 4 on both rolls?
30. A coin is flipped four times. What is the probability of getting heads on all four flips?
31. A card is drawn from a deck, and another card is drawn without replacement. What is the probability that both cards are hearts?
32. A box contains 5 red and 5 green balls. If two balls are drawn with replacement, what is the probability that both are red?
33. In a group of 3 people, what is the probability that all three were born on different days of the week?
34. If a die is rolled twice, what is the probability of getting a sum of 7 on both rolls?
35. A lottery ticket has a 1 in 1000 chance of winning. What is the probability of winning twice if two tickets are purchased?

### 2.4. Discrete vs. Continuous Events

#### 2.4.1. Discrete Events

36. What is the probability of drawing a red card or a face card from a deck of cards?
37. A die is rolled three times. What is the probability of getting at least one 6?
38. In a lottery where you must choose a number between 1 and 50, what is the probability of selecting a prime number?
39. A box contains 3 defective and 7 non-defective light bulbs. What is the probability of randomly selecting at least one defective bulb?
40. If a coin is flipped five times, what is the probability of getting exactly three heads?
41. A die is rolled twice. What is the probability of getting a sum of 8 or more on both rolls?
42. In a class of 20 students, what is the probability that at least two students share the same birthday?

#### 2.4.2. Continuous Events

43. If the height of students in a school is normally distributed with a mean of 160 cm and a standard deviation of 10 cm, what is the probability that a randomly selected student is taller than 170 cm?
44. The time it takes to complete a task is uniformly distributed between 30 and 90 minutes. What is the probability that the task takes between 50 and 70 minutes?
45. The weight of apples in a basket is normally distributed with a mean of 150 grams and a standard deviation of 20 grams. What is the probability that a randomly selected apple weighs more than 180 grams?
46. The length of time customers spend on a website is exponentially distributed with a mean of 10 minutes. What is the probability that a customer spends more than 20 minutes on the website?
47. If the time taken to answer a question is uniformly distributed between 1 and 5 minutes, what is the probability that the answer is given in less than 2 minutes?
48. The temperature in a city is normally distributed with a mean of 25°C and a standard deviation of 5°C. What is the probability that the temperature is between 20°C and 30°C?
49. The amount of time a student spends on homework each night is normally distributed with a mean of 2 hours and a standard deviation of 30 minutes. What is the probability that a student spends more than 2.5 hours on homework?

### 2.5. Probability Distributions

#### 2.5.1. Uniform Distribution

50. What is the probability of selecting a number between 3 and 8 from a uniform distribution on the interval [0, 10]?
51. If a spinner is equally divided into 10 sections, what is the probability of landing on section 7?
52. In a uniform distribution over the interval [0, 50], what is the probability of selecting a number between 20 and 30?
53. If the time to complete a task is uniformly distributed between 20 and 60 minutes, what is the probability that the task takes less than 40 minutes?
54. A number is randomly selected from 1 to 100. What is the probability that the number is between 25 and 75?
55. The probability of selecting a random number from 1 to 10 in a uniform distribution is the same for each number. What is the probability of selecting a number greater than 5?
56. In a uniform distribution over the interval [0, 100], what is the probability of selecting a number between 10 and 90?

#### 2.5.2. Binomial Distribution

57. A basketball player makes 80% of free throws. What is the probability that she makes exactly 5 out of 7 free throws?
58. In a class of 20 students, what is the probability that exactly 15 students passed the exam if the probability of passing is 0.75?
59. If you flip a coin 6 times, what is the probability of getting exactly 4 heads?
60. In a batch of 50 light bulbs, 10 are defective. If you randomly select 5 bulbs, what is the probability that exactly 2 are defective?
61. A game has a 1 in 5 chance of winning. What is the probability of winning exactly 3 times out of 10 tries?
62. In a survey, 60% of respondents preferred a particular brand. What is the probability that exactly 8 out of 10 respondents preferred that brand?
63. If you roll a die 10 times, what is the probability of getting exactly 4 sixes?

#### 2.5.3. Normal Distribution

64. The weight of a product is normally distributed with a mean of 50 grams and a standard deviation of 5 grams. What is the probability that a randomly selected product weighs between 45 and 55 grams?
65. A standardized test has scores that are normally distributed with a mean of 500 and a standard deviation of 100. What is the probability that a student scores between 400 and 600?
66. The height of a population is normally distributed with a mean of 170 cm and a standard deviation of 10 cm. What is the probability that a randomly selected person is shorter than 160 cm?
67. In a normal distribution with a mean of 75 and a standard deviation of 15, what is the probability that a value is greater than 90?
68. The IQ scores in a population are normally distributed with a mean of 100 and a standard deviation of 15. What is the probability that a randomly selected person has an IQ between 85 and 115?
69. The time to complete a task is normally distributed with a mean of 30 minutes and a standard deviation of 5 minutes. What is the probability that the task takes more than 35 minutes?
70. A test score is normally distributed with a mean of 70 and a standard deviation of 10. What is the probability that a student scores less than 60?

#### 2.5.4. Geometric Distribution

71. If the probability of success in a trial is 0.25, what is the probability that the first success occurs on the 3rd trial?
72. A factory tests items for defects with a 5% defect rate. What is the probability that the first defective item is found on the 4th test?
73. If the probability of hitting a target is 0.4, what is the probability that the first hit occurs on the 3rd shot?
74. What is the probability that the first success in a series of Bernoulli trials occurs on the 5th trial if the probability of success on each trial is 0.2?
75. A factory has a 2% defect rate. What is the probability that the first defective item is found on the 6th test?
76. If the probability of a machine producing a defective item is 0.1, what is the probability that the first defective item is produced on the 7th trial?
77. In a quality control test, what is the probability that the first defective item is found on the 3rd test if the defect rate is 0.05?

---

## Solutions

### 2.1. What is Probability?

**2.** **Solution:**

Total number of cards in a standard deck:

$$
\text{Total cards} = 52
$$

Number of aces:

$$
\text{Aces} = 4
$$

Number of kings:

$$
\text{Kings} = 4
$$

Since aces and kings are distinct cards, the total number of aces or kings is:

$$
\text{Aces or Kings} = 4 + 4 = 8
$$

Probability:

$$
P(\text{Ace or King}) = \frac{8}{52} = \frac{2}{13}
$$

---

**3.** **Solution:**

Total number of bulbs:

$$
\text{Total bulbs} = 3 + 7 = 10
$$

Number of defective bulbs:

$$
\text{Defective bulbs} = 3
$$

Probability:

$$
P(\text{Defective}) = \frac{3}{10}
$$

---

**4.** **Solution:**

Possible outcomes when rolling a six-sided die:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

Even numbers:

$$
E = \{2, 4, 6\}
$$

Number of even outcomes:

$$
|E| = 3
$$

Total outcomes:

$$
|S| = 6
$$

Probability:

$$
P(\text{Even}) = \frac{3}{6} = \frac{1}{2}
$$

---

**5.** **Solution:**

Total number of fruits:

$$
\text{Total fruits} = 8 + 4 = 12
$$

Number of apples:

$$
\text{Apples} = 8
$$

Probability:

$$
P(\text{Apple}) = \frac{8}{12} = \frac{2}{3}
$$

---

**6.** **Solution:**

Numbers from 1 to 100:

$$
\text{Total numbers} = 100
$$

Multiples of 5 between 1 and 100:

$$
\text{Multiples of 5} = \frac{100}{5} = 20
$$

Probability:

$$
P(\text{Multiple of 5}) = \frac{20}{100} = \frac{1}{5}
$$

---

**7.** **Solution:**

Total sections on the spinner:

$$
\text{Total sections} = 5
$$

Sections 1 or 2:

$$
\text{Favorable sections} = 2
$$

Probability:

$$
P(\text{Section 1 or 2}) = \frac{2}{5}
$$

---

### 2.2. Probability Function

**8.** **Solution:**

This is the classic birthday problem. The probability that at least two people share the same birthday can be calculated using the complement rule.

1. **Calculate the probability that all birthdays are different:**

Assuming 365 days in a year and ignoring leap years.

$$
P(\text{All different}) = \frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \cdots \times \frac{356}{365}
$$

For 10 people:

$$
P(\text{All different}) = \prod_{k=0}^{9} \frac{365 - k}{365}
$$

Calculating:

$$
P(\text{All different}) \approx 0.883
$$

2. **Calculate the probability that at least two people share a birthday:**

$$
P(\text{At least two share}) = 1 - P(\text{All different}) = 1 - 0.883 = 0.117
$$

**Answer:** Approximately $11.7\%$ chance that at least two people share the same birthday.

---

**9.** **Solution:**

Possible sums when rolling two dice range from 2 to 12.

First, find the total number of possible outcomes:

$$
\text{Total outcomes} = 6 \times 6 = 36
$$

Number of outcomes where the sum is 8 or more (sums 8, 9, 10, 11, 12):

- Sum of 8: 5 combinations
- Sum of 9: 4 combinations
- Sum of 10: 3 combinations
- Sum of 11: 2 combinations
- Sum of 12: 1 combination

Total favorable outcomes:

$$
\text{Favorable outcomes} = 5 + 4 + 3 + 2 + 1 = 15
$$

Probability:

$$
P(\text{Sum} \geq 8) = \frac{15}{36} = \frac{5}{12}
$$

---

**10.** **Solution:**

Number of face cards in a standard deck:

- Jacks: 4
- Queens: 4
- Kings: 4

Total face cards:

$$
\text{Face cards} = 4 + 4 + 4 = 12
$$

Total cards:

$$
\text{Total cards} = 52
$$

Probability:

$$
P(\text{Face card}) = \frac{12}{52} = \frac{3}{13}
$$

---

**11.** **Solution:**

Probability of winning:

$$
P(\text{Win}) = \frac{1}{1000}
$$

Probability of not winning:

$$
P(\text{Not win}) = 1 - P(\text{Win}) = 1 - \frac{1}{1000} = \frac{999}{1000}
$$

---

**12.** **Solution:**

Total possible outcomes when rolling two dice: 36

Sums of 4:

- (1,3), (2,2), (3,1): 3 combinations

Sums of 7:

- (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): 6 combinations

Total favorable outcomes:

$$
\text{Favorable outcomes} = 3 + 6 = 9
$$

Probability:

$$
P(\text{Sum of 4 or 7}) = \frac{9}{36} = \frac{1}{4}
$$

---

**13.** **Solution:**

Probability that at least one student shares your birthday:

1. **Probability that no one shares your birthday:**

Assuming birthdays are equally likely and there are 365 days in a year.

$$
P(\text{No one shares your birthday}) = \left( \frac{364}{365} \right)^{29}
$$

2. **Calculate the probability:**

$$
P(\text{At least one shares}) = 1 - P(\text{No one shares}) = 1 - \left( \frac{364}{365} \right)^{29}
$$

Calculating:

$$
P(\text{At least one shares}) \approx 1 - e^{-29/365} \approx 1 - e^{-0.0795} \approx 1 - 0.9231 = 0.0769
$$

**Answer:** Approximately $7.69\%$ chance that at least one student shares your birthday.

---

**14.** **Solution:**

Total marbles:

$$
\text{Total marbles} = 10 + 15 + 5 = 30
$$

Number of blue or green marbles:

$$
\text{Blue or Green} = 10 + 5 = 15
$$

Probability:

$$
P(\text{Blue or Green}) = \frac{15}{30} = \frac{1}{2}
$$

---

### 2.3. Probability Rules

#### 2.3.1. Addition Rule and Disjoint Events

**15.** **Solution:**

Number of hearts in a deck:

$$
\text{Hearts} = 13
$$

Number of spades in a deck:

$$
\text{Spades} = 13
$$

Total cards:

$$
\text{Total cards} = 52
$$

Since hearts and spades are disjoint:

$$
P(\text{Heart or Spade}) = P(\text{Heart}) + P(\text{Spade}) = \frac{13}{52} + \frac{13}{52} = \frac{26}{52} = \frac{1}{2}
$$

---

**16.** **Solution:**

Total balls:

$$
\text{Total balls} = 3 + 4 + 5 = 12
$$

Number of white or red balls:

$$
\text{White or Red} = 3 + 5 = 8
$$

Probability:

$$
P(\text{White or Red}) = \frac{8}{12} = \frac{2}{3}
$$

---

**17.** **Solution:**

Possible outcomes when rolling a die:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

Favorable outcomes:

$$
A = \{3, 5\}
$$

Probability:

$$
P(A) = \frac{2}{6} = \frac{1}{3}
$$

---

**18.** **Solution:**

Total students:

$$
\text{Total} = 4 + 6 + 7 + (\text{Seniors})
$$

Number of seniors:

$$
\text{Seniors} = 25 - (4 + 6 + 7) = 25 - 17 = 8
$$

Number of sophomores or juniors:

$$
\text{Sophomores or Juniors} = 6 + 7 = 13

$$

Probability:

$$
P(\text{Sophomore or Junior}) = \frac{13}{25}
$$

---

**19.** **Solution:**

Total possible outcomes when flipping a coin twice: 4

Possible outcomes:

- HH
- HT
- TH
- TT

Number of outcomes with at least one head: 3

Probability:

$$
P(\text{At least one head}) = \frac{3}{4}
$$

Alternatively, using complement rule:

$$
P(\text{At least one head}) = 1 - P(\text{No heads}) = 1 - \left( \frac{1}{2} \times \frac{1}{2} \right) = 1 - \frac{1}{4} = \frac{3}{4}
$$

---

**20.** **Solution:**

Number of queens:

$$
\text{Queens} = 4
$$

Number of kings:

$$
\text{Kings} = 4
$$

Total cards:

$$
\text{Total cards} = 52
$$

Since queens and kings are disjoint:

$$
P(\text{Queen or King}) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52} = \frac{2}{13}
$$

---

**21.** **Solution:**

Total tickets:

$$
\text{Total tickets} = 10 + 90 = 100
$$

Probability of drawing a prize:

$$
P(\text{Prize}) = \frac{10}{100} = \frac{1}{10}
$$

Probability of drawing a blank:

$$
P(\text{Blank}) = \frac{90}{100} = \frac{9}{10}
$$

Since every ticket is either a prize or a blank, the sum of probabilities is 1.

---

#### 2.3.2. Conditional Probability

**22.** **Solution:**

Given that the card is a spade.

Number of spades:

$$
\text{Spades} = 13
$$

Number of ace of spades:

$$
\text{Ace of spades} = 1
$$

Conditional probability:

$$
P(\text{Ace of spades} | \text{Spade}) = \frac{1}{13}
$$

---

**23.** **Solution:**

Given that the ball drawn is black.

Number of black balls:

$$
\text{Black balls} = 6
$$

Assuming the largest black ball is distinguishable (e.g., numbered or labeled).

Probability:

$$
P(\text{Largest black ball} | \text{Black}) = \frac{1}{6}

$$

---

**24.** **Solution:**

Given that the card is a face card.

Number of face cards:

$$
\text{Face cards} = 12
$$

Number of queens:

$$
\text{Queens} = 4
$$

Conditional probability:

$$
P(\text{Queen} | \text{Face card}) = \frac{4}{12} = \frac{1}{3}
$$

---

**25.** **Solution:**

Given that the marble drawn is red.

Number of red marbles:

$$
\text{Red marbles} = 5
$$

Assuming the smallest red marble is distinguishable.

Probability:

$$
P(\text{Smallest red marble} | \text{Red}) = \frac{1}{5}
$$

---

**26.** **Solution:**

Given that the card is red.

Number of red cards:

$$
\text{Red cards} = 26
$$

Number of diamonds:

$$
\text{Diamonds} = 13
$$

Since all diamonds are red:

$$
P(\text{Diamond} | \text{Red}) = \frac{13}{26} = \frac{1}{2}
$$

---

**27.** **Solution:**

Given that the ball drawn is even-numbered.

Total balls:

$$
\text{Total balls} = 10
$$

Even-numbered balls:

$$
\text{Even-numbered balls} = \{2, 4, 6, 8, 10\}
$$

Number of even-numbered balls:

$$
5
$$

Probability:

$$
P(\text{Ball is 4} | \text{Even}) = \frac{1}{5}
$$

---

**28.** **Solution:**

Given that the student is in the top 5 of the class.

Total students:

$$
\text{Total students} = 30
$$

Number of seniors (assuming "senior" is a class level):

Let's assume the class has seniors, juniors, etc., but since we don't have specific numbers, we'll assume that seniors are equally represented.

Probability:

Without specific data, we cannot compute an exact probability.

But if, for example, there are 10 seniors in the class:

$$
P(\text{Senior} | \text{Top 5}) = \frac{\text{Number of seniors in top 5}}{5}
$$

Without specific numbers, the probability cannot be determined.

---

#### 2.3.3. Multiplication Rule and Independent Events

**29.** **Solution:**

Probability of getting a 4 on one roll:

$$
P(\text{4}) = \frac{1}{6}
$$

Since the rolls are independent:

$$
P(\text{4 on both rolls}) = P(\text{4}) \times P(\text{4}) = \left( \frac{1}{6} \right)^2 = \frac{1}{36}
$$

---

**30.** **Solution:**

Probability of getting heads on one flip:

$$
P(\text{Heads}) = \frac{1}{2}
$$

Since flips are independent:

$$
P(\text{4 heads}) = \left( \frac{1}{2} \right)^4 = \frac{1}{16}
$$

---

**31.** **Solution:**

First card is a heart:

$$
P(\text{First heart}) = \frac{13}{52} = \frac{1}{4}
$$

Second card is a heart (without replacement):

$$
P(\text{Second heart} | \text{First heart}) = \frac{12}{51}
$$

Probability both cards are hearts:

$$
P(\text{Both hearts}) = P(\text{First heart}) \times P(\text{Second heart} | \text{First heart}) = \frac{1}{4} \times \frac{12}{51} = \frac{12}{204} = \frac{3}{51} \approx 0.0588
$$

---

**32.** **Solution:**

Since the balls are drawn with replacement, each draw is independent.

Probability of drawing a red ball:

$$
P(\text{Red}) = \frac{5}{10} = \frac{1}{2}
$$

Probability both are red:

$$
P(\text{Both red}) = P(\text{Red}) \times P(\text{Red}) = \left( \frac{1}{2} \right)^2 = \frac{1}{4}
$$

---

**33.** **Solution:**

Number of days in a week:

$$
7
$$

Probability that one person is born on any day:

$$
P(\text{Any day}) = \frac{1}{7}
$$

Probability that all three were born on different days:

$$
P(\text{Different days}) = 1 \times \frac{6}{7} \times \frac{5}{7} = \frac{30}{49}
$$

---

**34.** **Solution:**

Probability of getting a sum of 7 in one roll of two dice:

$$
P(\text{Sum 7}) = \frac{6}{36} = \frac{1}{6}
$$

Since rolls are independent:

$$
P(\text{Sum 7 on both rolls}) = \left( \frac{1}{6} \right)^2 = \frac{1}{36}
$$

---

**35.** **Solution:**

Probability of winning once:

$$
P(\text{Win}) = \frac{1}{1000}
$$

Probability of winning twice (assuming tickets are independent):

$$
P(\text{Win twice}) = \left( \frac{1}{1000} \right)^2 = \frac{1}{1,000,000}
$$

---

### 2.4. Discrete vs. Continuous Events

#### 2.4.1. Discrete Events

**36.** **Solution:**

Number of red cards:

$$
\text{Red cards} = 26
$$

Number of face cards:

$$
\text{Face cards} = 12
$$

Number of red face cards (overlap):

$$
\text{Red face cards} = 6
$$

Use the inclusion-exclusion principle:

$$
P(\text{Red or Face card}) = P(\text{Red}) + P(\text{Face card}) - P(\text{Red face cards}) = \frac{26}{52} + \frac{12}{52} - \frac{6}{52} = \frac{32}{52} = \frac{8}{13}
$$

---

**37.** **Solution:**

Probability of not getting a 6 on one roll:

$$
P(\text{Not 6}) = \frac{5}{6}
$$

Probability of not getting a 6 on three rolls:

$$
P(\text{No 6 in 3 rolls}) = \left( \frac{5}{6} \right)^3 \approx 0.5787
$$

Probability of getting at least one 6:

$$
P(\text{At least one 6}) = 1 - P(\text{No 6 in 3 rolls}) = 1 - 0.5787 = 0.4213
$$

---

**38.** **Solution:**

Total numbers from 1 to 50:

$$
50
$$

Prime numbers between 1 and 50: There are 15 primes (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

Probability:

$$
P(\text{Prime}) = \frac{15}{50} = \frac{3}{10}
$$

---

**39.** **Solution:**

Probability of selecting at least one defective bulb:

First, find the probability of selecting no defective bulbs.

Total bulbs:

$$
\text{Total bulbs} = 3 + 7 = 10
$$

Probability of selecting no defective bulbs (all non-defective):

$$
P(\text{All non-defective}) = \frac{7}{10}
$$

Probability of selecting at least one defective bulb:

$$
P(\text{At least one defective}) = 1 - P(\text{All non-defective}) = 1 - \frac{7}{10} = \frac{3}{10}
$$

---

**40.** **Solution:**

Using the binomial probability formula with $ n = 5 $, $ k = 3 $, $ p = 0.5 $.

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^{2} = 10 \times 0.125 \times 0.25 = 0.3125
$$

---

**41.** **Solution:**

First, find the probability of getting a sum of 8 or more in one roll.

Possible sums of 8 or more:

- Sum of 8: 5 combinations
- Sum of 9: 4 combinations
- Sum of 10: 3 combinations
- Sum of 11: 2 combinations
- Sum of 12: 1 combination

Total favorable outcomes in one roll:

$$
15
$$

Probability in one roll:

$$
P(\text{Sum} \geq 8) = \frac{15}{36} = \frac{5}{12}
$$

Since the rolls are independent, the probability of getting a sum of 8 or more on both rolls:

$$
P(\text{Sum} \geq 8 \text{ on both rolls}) = \left( \frac{5}{12} \right)^2 = \frac{25}{144}
$$

---

**42.** **Solution:**

This is the birthday problem with 20 people.

Probability that at least two people share a birthday:

$$
P(\text{At least two share}) = 1 - P(\text{All different})
$$

Calculate $ P(\text{All different}) $:

$$
P(\text{All different}) = \prod_{k=0}^{19} \frac{365 - k}{365}
$$

Calculating:

$$
P(\text{At least two share}) \approx 1 - 0.5886 = 0.4114
$$

**Answer:** Approximately $41.14\%$ chance that at least two students share the same birthday.

---

#### 2.4.2. Continuous Events

**43.** **Solution:**

Given:

- Mean (\m$): 160 cm
- Standard deviation (\sigm$): 10 cm
- We need P(X > 170$

Calculate z-score:

$$
z = \frac{170 - 160}{10} = 1
$$

Use standard normal distribution table:

$$
P(Z > 1) = 1 - P(Z < 1) = 1 - 0.8413 = 0.1587
$$

---

**44.** **Solution:**

Uniform distribution between 30 and 90 minutes.

Probability that the task takes between 50 and 70 minutes:

$$
P(50 \leq X \leq 70) = \frac{70 - 50}{90 - 30} = \frac{20}{60} = \frac{1}{3}
$$

---

**45.** **Solution:**

Given:

- Mean ($\mu$): 150 grams
- Standard deviation ($\sigma$): 20 grams
- We need $P(X > 180)$

Calculate z-score:

$$
z = \frac{180 - 150}{20} = 1.5
$$

Use standard normal distribution table:

$$
P(Z > 1.5) = 1 - P(Z < 1.5) = 1 - 0.9332 = 0.0668
$$

---

**46.** **Solution:**

Exponential distribution with mean ($\mu$) = 10 minutes.

Rate parameter:

$$
\lambda = \frac{1}{\mu} = \frac{1}{10} = 0.1
$$

Probability:

$$
P(X > 20) = e^{-\lambda x} = e^{-0.1 \times 20} = e^{-2} \approx 0.1353
$$

---

**47.** **Solution:**

Uniform distribution between 1 and 5 minutes.

Probability that the answer is given in less than 2 minutes:

$$
P(1 \leq X \leq 2) = \frac{2 - 1}{5 - 1} = \frac{1}{4} = 0.25
$$

---

**48.** **Solution:**

Given:

- Mean ($\mu$): 25°C
- Standard deviation ($\sigma$): 5°C
- We need $P(20 \leq X \leq 30)$

Calculate z-scores:

- For 20°C:

  $$
  z_1 = \frac{20 - 25}{5} = -1
  $$

- For 30°C:

  $$
  z_2 = \frac{30 - 25}{5} = 1
  $$

Probability:

$$
P(20 \leq X \leq 30) = P(Z < 1) - P(Z < -1) = 0.8413 - 0.1587 = 0.6826
$$

---

**49.** **Solution:**

Given:

- Mean ($\mu$): 2 hours
- Standard deviation ($\sigma$): 30 minutes = 0.5 hours
- We need $P(X > 2.5)$

Calculate z-score:

$$
z = \frac{2.5 - 2}{0.5} = 1
$$

Probability:

$$
P(X > 2.5) = 1 - P(Z < 1) = 1 - 0.8413 = 0.1587
$$

---

### 2.5. Probability Distributions

#### 2.5.1. Uniform Distribution

**50.** **Solution:**

Uniform distribution over [0, 10].

Probability of selecting a number between 3 and 8:

$$
P(3 \leq X \leq 8) = \frac{8 - 3}{10 - 0} = \frac{5}{10} = 0.5
$$

---

**51.** **Solution:**

Total sections:

$$
10
$$

Probability of landing on section 7:

$$
P(\text{Section 7}) = \frac{1}{10}
$$

---

**52.** **Solution:**

Uniform distribution over [0, 50].

Probability of selecting a number between 20 and 30:

$$
P(20 \leq X \leq 30) = \frac{30 - 20}{50 - 0} = \frac{10}{50} = 0.2
$$

---

**53.** **Solution:**

Uniform distribution between 20 and 60 minutes.

Probability that the task takes less than 40 minutes:

$$
P(20 \leq X \leq 40) = \frac{40 - 20}{60 - 20} = \frac{20}{40} = 0.5
$$

---

**54.** **Solution:**

Numbers from 1 to 100.

Probability that the number is between 25 and 75:

$$
P(25 \leq X \leq 75) = \frac{75 - 25}{100 - 1} = \frac{50}{99} \approx 0.5051
$$

---

**55.** **Solution:**

Probability of selecting a number greater than 5 from 1 to 10:

Numbers greater than 5: 5 numbers (6, 7, 8, 9, 10)

Probability:

$$
P(X > 5) = \frac{5}{10} = 0.5
$$

---

**56.** **Solution:**

Uniform distribution over [0, 100].

Probability of selecting a number between 10 and 90:

$$
P(10 \leq X \leq 90) = \frac{90 - 10}{100 - 0} = \frac{80}{100} = 0.8
$$

---

#### 2.5.2. Binomial Distribution

**57.** **Solution:**

Parameters:

- $n = 7$
- $k = 5 $
- $p = 0.8$
- $q = 1 - p = 0.2$

Using binomial formula:

$$
P(X = 5) = \binom{7}{5} (0.8)^5 (0.2)^2 = 21 \times 0.32768 \times 0.04 \approx 0.275
$$

---

**58.** **Solution:**

Parameters:

- $n = 20$
- $k = 15$
- $p = 0.75$
- $q = 0.25$

Using binomial formula:

$$
P(X = 15) = \binom{20}{15} (0.75)^{15} (0.25)^5
$$

Calculating:

$$
P(X = 15) \approx 0.202
$$

---

**59.** **Solution:**

Parameters:

- $n = 6$
- $k = 4$
- $p = 0.5$

Using binomial formula:

$$
P(X = 4) = \binom{6}{4} (0.5)^4 (0.5)^2 = 15 \times 0.0625 \times 0.25 = 0.2344
$$

---

**60.** **Solution:**

This is actually a hypergeometric distribution since we are sampling without replacement.

However, if we approximate using binomial:

Parameters:

- $n = 5$
- $k = 2$
- $p = \frac{10}{50} = 0.2$

Using binomial formula:

$$
P(X = 2) = \binom{5}{2} (0.2)^2 (0.8)^3 = 10 \times 0.04 \times 0.512 = 0.2048
$$

---

**61.** **Solution:**

Parameters:

- $n = 10$
- $k = 3$
- $p = \frac{1}{5} = 0.2$

Using binomial formula:

$$
P(X = 3) = \binom{10}{3} (0.2)^3 (0.8)^7 \approx 0.2013
$$

---

**62.** **Solution:**

Parameters:

- $n = 10$
- $k = 8$
- $p = 0.6$

Using binomial formula:

$$
P(X = 8) = \binom{10}{8} (0.6)^8 (0.4)^2 \approx 0.1209
$$

---

**63.** **Solution:**

Parameters:

- $n = 10$
- $k = 4$
- $p = \frac{1}{6}$

Using binomial formula:

$$
P(X = 4) = \binom{10}{4} \left( \frac{1}{6} \right)^4 \left( \frac{5}{6} \right)^6 \approx 0.054
$$

---

#### 2.5.3. Normal Distribution

**64.** **Solution:**

Given:

- Mean ($\mu$): 50 grams
- Standard deviation ($\sigma$): 5 grams
- Need $P(45 \leq X \leq 55)$

Calculate z-scores:

- For 45 grams:

  $$
  z_1 = \frac{45 - 50}{5} = -1
  $$

- For 55 grams:

  $$
  z_2 = \frac{55 - 50}{5} = 1
  $$

Probability:

$$
P(45 \leq X \leq 55) = P(Z < 1) - P(Z < -1) = 0.8413 - 0.1587 = 0.6826
$$

---

**65.** **Solution:**

Given:

- Mean ($\mu$): 500
- Standard deviation ($\sigma$): 100
- Need $P(400 \leq X \leq 600)$

Calculate z-scores:

- For 400:

  $$
  z_1 = \frac{400 - 500}{100} = -1
  $$

- For 600:

  $$
  z_2 = \frac{600 - 500}{100} = 1
  $$

Probability:

$$
P(400 \leq X \leq 600) = 0.8413 - 0.1587 = 0.6826
$$

---

**66.** **Solution:**

Given:

- Mean ($\mu$): 170 cm
- Standard deviation ($\sigma$): 10 cm
- Need $P(X < 160)$

Calculate z-score:

$$
z = \frac{160 - 170}{10} = -1
$$

Probability:

$$
P(X < 160) = P(Z < -1) = 0.1587
$$

---

**67.** **Solution:**

Given:

- Mean ($\mu$): 75
- Standard deviation ($\sigma$): 15
- Need $P(X > 90)$

Calculate z-score:

$$
z = \frac{90 - 75}{15} = 1
$$

Probability:

$$
P(X > 90) = 1 - P(Z < 1) = 1 - 0.8413 = 0.1587
$$

---

**68.** **Solution:**

Given:

- Mean ($\mu$): 100
- Standard deviation ($\sigma$): 15
- Need $P(85 \leq X \leq 115)$

Calculate z-scores:

- For 85:

  $$
  z_1 = \frac{85 - 100}{15} = -1
  $$

- For 115:

  $$
  z_2 = \frac{115 - 100}{15} = 1
  $$

Probability:

$$
P(85 \leq X \leq 115) = 0.8413 - 0.1587 = 0.6826
$$

---

**69.** **Solution:**

Given:

- Mean ($\mu$): 30 minutes
- Standard deviation ($\sigma$): 5 minutes
- Need $P(X > 35)$

Calculate z-score:

$$
z = \frac{35 - 30}{5} = 1
$$

Probability:

$$
P(X > 35) = 1 - P(Z < 1) = 0.1587
$$

---

**70.** **Solution:**

Given:

- Mean ($\mu$): 70
- Standard deviation ($\sigma$): 10
- Need $P(X < 60)$

Calculate z-score:

$$
z = \frac{60 - 70}{10} = -1
$$

Probability:

$$
P(X < 60) = P(Z < -1) = 0.1587
$$

---

#### 2.5.4. Geometric Distribution

**71.** **Solution:**

Given:

- $p = 0.25$
- $q = 1 - p = 0.75$
- $k = 3$

Probability:

$$
P(X = 3) = q^{k - 1} p = (0.75)^{2} \times 0.25 = 0.1406
$$

---

**72.** **Solution:**

Given:

- $p = 0.05$
- $q = 0.95$
- $k = 4$

Probability:

$$
P(X = 4) = (0.95)^{3} \times 0.05 = 0.8574 \times 0.05 = 0.0429
$$

---

**73.** **Solution:**

Given:

- $p = 0.4$
- $q = 0.6$
- $k = 3$

Probability:

$$
P(X = 3) = (0.6)^{2} \times 0.4 = 0.36 \times 0.4 = 0.144
$$

---

**74.** **Solution:**

Given:

- $p = 0.2$
- $q = 0.8$
- $k = 5$

Probability:

$$
P(X = 5) = (0.8)^{4} \times 0.2 = 0.4096 \times 0.2 = 0.08192
$$

---

**75.** **Solution:**

Given:

- $p = 0.02$
- $q = 0.98$
- $k = 6$

Probability:

$$
P(X = 6) = (0.98)^{5} \times 0.02 \approx 0.9039 \times 0.02 = 0.01808
$$

---

**76.** **Solution:**

Given:

- $p = 0.1$
- $q = 0.9$
- $k = 7$

Probability:

$$
P(X = 7) = (0.9)^{6} \times 0.1 \approx 0.5314 \times 0.1 = 0.05314
$$

---

**77.** **Solution:**

Given:

- $p = 0.05$
- $q = 0.95$
- $k = 3$

Probability:

$$
P(X = 3) = (0.95)^{2} \times 0.05 = 0.9025 \times 0.05 = 0.045125
$$

---

**Note:** All probabilities are approximate and may vary slightly due to rounding.