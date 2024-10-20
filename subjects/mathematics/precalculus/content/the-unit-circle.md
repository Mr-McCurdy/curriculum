# The Unit Circle
---

## Introduction

The unit circle fundamental concepts in trigonometry and mathematics as a whole. While degrees are commonly used to measure angles in everyday contexts, radians provide a more natural and mathematically convenient unit of angular measure, especially in calculus and advanced mathematics. The unit circle—a circle with a radius of one unit centered at the origin of a coordinate system—serves as a powerful tool for understanding trigonometric functions and their relationships. By exploring radians and the unit circle together, we can gain deeper insights into the behavior of trigonometric functions and their applications in various fields.

---

## The Content

### Understanding Radians

A **radian** is an alternative unit of measuring angles, defined based on the radius of a circle. One radian is the angle created when the arc length is equal to the radius of the circle.

#### Radians and Degrees Conversion

$$
360^\circ = 2\pi \text{ radians}
$$

Therefore, to convert degrees to radians:

$$
\text{Radians} = \left( \frac{\pi}{180^\circ} \right) \times \text{Degrees}
$$

And to convert radians to degrees:

$$
\text{Degrees} = \left( \frac{180^\circ}{\pi} \right) \times \text{Radians}
$$

### The Unit Circle

The **unit circle** is a circle with a radius of 1 unit, centered at the origin (0, 0) in the Cartesian coordinate system. It is a crucial tool for defining trigonometric functions for all real numbers.

- **Coordinates on the Unit Circle:**
  Any point on the unit circle can be defined using an angle $\theta$ from the positive x-axis:

  $$
  (\cos \theta, \sin \theta)
  $$

  This means that for any angle $\theta$, the x-coordinate is $\cos \theta$, and the y-coordinate is $\sin \theta$.

---

<!-- Placeholder for the Unit Circle image -->


<!-- Centered and resized image using HTML tags -->
<p align="center">
  <img src="../assets/unit-circle.png" alt="Unit Circle Diagram" width="600">
</p>

*Figure 1: The Unit Circle illustrating angles in radians and degrees, with coordinates of key points.*

---

### Trigonometric Functions on the Unit Circle

- **Sine Function ($\sin \theta$):**
  Represents the y-coordinate of the point on the unit circle corresponding to angle $\theta$.

- **Cosine Function ($\cos \theta$):**
  Represents the x-coordinate of the point on the unit circle corresponding to angle $\theta$.

- **Tangent Function ($\tan \theta$):**
  Defined as the ratio of the sine and cosine functions:

  $$
  \tan \theta = \frac{\sin \theta}{\cos \theta}
  $$

### Special Angles and Their Coordinates

Some commonly used angles and their coordinates on the unit circle:

- **$0^\circ$ or $0$ radians:**

  $$
  (\cos 0, \sin 0) = (1, 0)
  $$

- **$90^\circ$ or $\frac{\pi}{2}$ radians:**

  $$
  \left( \cos \frac{\pi}{2}, \sin \frac{\pi}{2} \right) = (0, 1)
  $$

- **$180^\circ$ or $\pi$ radians:**

  $$
  (\cos \pi, \sin \pi) = (-1, 0)
  $$

- **$270^\circ$ or $\frac{3\pi}{2}$ radians:**

  $$
  \left( \cos \frac{3\pi}{2}, \sin \frac{3\pi}{2} \right) = (0, -1)
  $$

### Quadrants and Sign of Trigonometric Functions

- **Quadrant I ($0^\circ$ to $90^\circ$):**
  - $\cos \theta > 0$
  - $\sin \theta > 0$
  - $\tan \theta > 0$

- **Quadrant II ($90^\circ$ to $180^\circ$):**
  - $\cos \theta < 0$
  - $\sin \theta > 0$
  - $\tan \theta < 0$

- **Quadrant III ($180^\circ$ to $270^\circ$):**
  - $\cos \theta < 0$
  - $\sin \theta < 0$
  - $\tan \theta > 0$

- **Quadrant IV ($270^\circ$ to $360^\circ$):**
  - $\cos \theta > 0$
  - $\sin \theta < 0$
  - $\tan \theta < 0$

### Reference Angles

A **reference angle** is the acute angle formed by the terminal side of an angle $\theta$ and the x-axis. It helps in finding the values of trigonometric functions for angles greater than $90^\circ$ or less than $0^\circ$.

---

## Worked Examples

### Example 1

**Convert $150^\circ$ to radians.**

**Solution:**

Using the conversion formula:

$$
\text{Radians} = \left( \frac{\pi}{180^\circ} \right) \times 150^\circ = \frac{5\pi}{6} \text{ radians}
$$

### Example 2

**Find $\sin \theta$ and $\cos \theta$ for $\theta = \frac{\pi}{4}$.**

**Solution:**

For $\theta = \frac{\pi}{4}$ (which is $45^\circ$):

$$
\sin \frac{\pi}{4} = \frac{\sqrt{2}}{2}, \quad \cos \frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$

### Example 3

**Determine the coordinates of the point on the unit circle corresponding to $\theta = 210^\circ$.**

**Solution:**

First, convert $210^\circ$ to radians:

$$
\theta = 210^\circ = \left( \frac{\pi}{180^\circ} \right) \times 210^\circ = \frac{7\pi}{6}
$$

Find the reference angle:

$$
\theta_{\text{ref}} = 210^\circ - 180^\circ = 30^\circ
$$

Compute $\cos \theta$ and $\sin \theta$:
- Since $210^\circ$ is in Quadrant III, both sine and cosine are negative.

Using known values for $30^\circ$:

$$
\cos 30^\circ = \frac{\sqrt{3}}{2}, \quad \sin 30^\circ = \frac{1}{2}
$$

Therefore:

$$
\cos 210^\circ = -\frac{\sqrt{3}}{2}, \quad \sin 210^\circ = -\frac{1}{2}
$$

The coordinates are:

$$
\left( -\frac{\sqrt{3}}{2}, -\frac{1}{2} \right)
$$

### Example 4

**Calculate $\tan \theta$ when $\theta = \frac{2\pi}{3}$.**

**Solution:**

Convert $\theta$ to degrees if necessary:

$$
\theta = \frac{2\pi}{3} = 120^\circ
$$

Determine $\sin \theta$ and $\cos \theta$:
- $\sin 120^\circ = \sin (180^\circ - 60^\circ) = \sin 60^\circ = \frac{\sqrt{3}}{2}$
- $\cos 120^\circ = -\cos 60^\circ = -\frac{1}{2}$

Compute $\tan \theta$:

$$
\tan \theta = \frac{\sin \theta}{\cos \theta} = \frac{\frac{\sqrt{3}}{2}}{-\frac{1}{2}} = -\sqrt{3}
$$

---

## Exercises

1. Convert $225^\circ$ to radians.
2. Convert $\frac{5\pi}{4}$ radians to degrees.
3. Find $\sin \theta$ and $\cos \theta$ when $\theta = 60^\circ$.
4. Determine the coordinates on the unit circle for $\theta = 330^\circ$.
5. Calculate $\tan \theta$ when $\theta = \frac{\pi}{6}$.
6. Find the reference angle for $\theta = 240^\circ$.
7. Convert $-90^\circ$ to radians.
8. If $\theta = \frac{7\pi}{4}$, what are $\sin \theta$ and $\cos \theta$?
9. Determine which quadrant $\theta = 135^\circ$ lies in and the signs of $\sin \theta$ and $\cos \theta$.
10. Find $\cos \theta$ when $\theta = 270^\circ$.
11. What is $\sin \theta$ for $\theta = \frac{3\pi}{2}$?
12. Convert $300^\circ$ to radians.
13. Calculate $\tan \theta$ when $\theta = 45^\circ$.
14. Determine the exact value of $\cos \left( \frac{2\pi}{3} \right)$.
15. Find the coordinates of the point on the unit circle corresponding to $\theta = 150^\circ$.
16. What is the reference angle for $\theta = 315^\circ$?
17. Convert $540^\circ$ to radians.
18. Find $\sin \left( -\frac{\pi}{4} \right)$.
19. Determine the signs of $\sin \theta$ and $\cos \theta$ in Quadrant IV.
20. If $\cos \theta = \frac{1}{2}$, and $\theta$ is in Quadrant I, find $\theta$ in degrees.
21. Convert $\theta = -\frac{\pi}{6}$ to degrees.
22. Calculate $\tan \theta$ when $\theta = 180^\circ$.
23. What are the coordinates of the point on the unit circle at $\theta = 0$?
24. Determine $\sin \theta$ and $\cos \theta$ when $\theta = 90^\circ$.

---

## Solutions

1. **Convert $225^\circ$ to radians:**

   $$
   \theta = 225^\circ \times \left( \frac{\pi}{180^\circ} \right) = \frac{5\pi}{4} \text{ radians}
   $$

2. **Convert $\frac{5\pi}{4}$ radians to degrees:**

   $$
   \theta = \frac{5\pi}{4} \times \left( \frac{180^\circ}{\pi} \right) = 225^\circ
   $$

3. **Find $\sin 60^\circ$ and $\cos 60^\circ$:**

   $$
   \sin 60^\circ = \frac{\sqrt{3}}{2}, \quad \cos 60^\circ = \frac{1}{2}
   $$

4. **Coordinates for $\theta = 330^\circ$:**

   Reference angle:

   $$
   \theta_{\text{ref}} = 360^\circ - 330^\circ = 30^\circ
   $$

   Since $\theta$ is in Quadrant IV:
   - $\cos \theta > 0$
   - $\sin \theta < 0$

   Compute:

   $$
   \cos 330^\circ = \cos 30^\circ = \frac{\sqrt{3}}{2}
   $$

   $$
   \sin 330^\circ = -\sin 30^\circ = -\frac{1}{2}
   $$

   Coordinates:
   $$
   \left( \frac{\sqrt{3}}{2}, -\frac{1}{2} \right)
   $$

5. **Calculate $\tan \frac{\pi}{6}$:**

   $$
   \tan \frac{\pi}{6} = \tan 30^\circ = \frac{\sqrt{3}}{3}
   $$

6. **Reference angle for $\theta = 240^\circ$:**

   Since $180^\circ < 240^\circ < 270^\circ$, subtract $180^\circ$:

   $$
   \theta_{\text{ref}} = 240^\circ - 180^\circ = 60^\circ
   $$

7. **Convert $-90^\circ$ to radians:**

   $$
   \theta = -90^\circ \times \left( \frac{\pi}{180^\circ} \right) = -\frac{\pi}{2}
   $$

8. **Find $\sin \theta$ and $\cos \theta$ for $\theta = \frac{7\pi}{4}$:**

   Convert to degrees:

   $$
   \theta = \frac{7\pi}{4} \times \left( \frac{180^\circ}{\pi} \right) = 315^\circ
   $$

   Reference angle:

   $$
   \theta_{\text{ref}} = 360^\circ - 315^\circ = 45^\circ
   $$

   Since $\theta$ is in Quadrant IV:
   - $\cos \theta > 0$
   - $\sin \theta < 0$

   Compute:

   $$
   \cos \theta = \cos 45^\circ = \frac{\sqrt{2}}{2}
   $$

   $$
   \sin \theta = -\sin 45^\circ = -\frac{\sqrt{2}}{2}
   $$

9. **Quadrant and signs for $\theta = 135^\circ$:**

   - Quadrant II (between $90^\circ$ and $180^\circ$)
   - $\sin \theta > 0$
   - $\cos \theta < 0$

10. **Find $\cos 270^\circ$:**

    $$
    \cos 270^\circ = 0
    $$

11. **What is $\sin \frac{3\pi}{2}$:**

    $$
    \sin \frac{3\pi}{2} = \sin 270^\circ = -1
    $$

12. **Convert $300^\circ$ to radians:**

    $$
    \theta = 300^\circ \times \left( \frac{\pi}{180^\circ} \right) = \frac{5\pi}{3}
    $$

13. **Calculate $\tan 45^\circ$:**

    $$
    \tan 45^\circ = 1
    $$

14. **Determine $\cos \left( \frac{2\pi}{3} \right)$:**

    Convert to degrees:

    $$
    \frac{2\pi}{3} = 120^\circ
    $$

    Since $\theta$ is in Quadrant II:
    - $\cos \theta < 0$

    Reference angle:

    $$
    \theta_{\text{ref}} = 180^\circ - 120^\circ = 60^\circ
    $$

    Compute:

    $$
    \cos \theta = -\cos 60^\circ = -\frac{1}{2}
    $$

15. **Coordinates for $\theta = 150^\circ$:**

    Reference angle:

    $$
    \theta_{\text{ref}} = 180^\circ - 150^\circ = 30^\circ
    $$

    Since $\theta$ is in Quadrant II:
    - $\cos \theta < 0$
    - $\sin \theta > 0$

    Compute:

    $$
    \cos 150^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2}
    $$

    $$
    \sin 150^\circ = \sin 30^\circ = \frac{1}{2}
    $$

    Coordinates:
    $$
    \left( -\frac{\sqrt{3}}{2}, \frac{1}{2} \right)
    $$

16. **Reference angle for $\theta = 315^\circ$:**

    $$
    \theta_{\text{ref}} = 360^\circ - 315^\circ = 45^\circ
    $$

17. **Convert $540^\circ$ to radians:**

    $$
    \theta = 540^\circ \times \left( \frac{\pi}{180^\circ} \right) = 3\pi \text{ radians}
    $$

18. **Find $\sin \left( -\frac{\pi}{4} \right)$:**

    $$
    \sin \left( -\frac{\pi}{4} \right) = -\sin \frac{\pi}{4} = -\frac{\sqrt{2}}{2}
    $$

19. **Signs in Quadrant IV:**

    - $\cos \theta > 0$
    - $\sin \theta < 0$

20. **Find $\theta$ if $\cos \theta = \frac{1}{2}$ in Quadrant I:**

    $$
    \cos \theta = \frac{1}{2} \implies \theta = 60^\circ
    $$

21. **Convert $-\frac{\pi}{6}$ to degrees:**

    $$
    \theta = -\frac{\pi}{6} \times \left( \frac{180^\circ}{\pi} \right) = -30^\circ
    $$

22. **Calculate $\tan 180^\circ$:**

    $$
    \tan 180^\circ = 0
    $$

23. **Coordinates at $\theta = 0$:**

    $$
    (\cos 0, \sin 0) = (1, 0)
    $$

24. **Find $\sin 90^\circ$ and $\cos 90^\circ$:**

    $$
    \sin 90^\circ = 1, \quad \cos 90^\circ = 0
    $$

