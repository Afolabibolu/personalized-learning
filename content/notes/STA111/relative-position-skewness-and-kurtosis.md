# Relative Position, Skewness and Kurtosis

## Relative position

- The **quartiles** Q₁, Q₂ and Q₃ are the three points that divide ordered data into **four equal parts**; Q₂ is the median.
- **Deciles** divide the data into ten parts and **percentiles** into a hundred.
- For grouped data, the formula is like the median's: Qₖ = L + ((kn/4 − F)/f) × c.
- The **interquartile range** IQR = Q₃ − Q₁ is the spread of the middle 50%.
- The **five-number summary** (minimum, Q₁, median, Q₃, maximum) is drawn as a box plot.

A **z-score** z = (x − x̄)/s says how many standard deviations a value lies from the mean.

**Outliers**: a value is an outlier if it falls **outside** the fences **Q₁ − 1.5 IQR** or **Q₃ + 1.5 IQR**. Values beyond 3 IQR are extreme outliers.

## Skewness

**Skewness** measures asymmetry.

- In a **positively skewed (skewed right)** distribution, the **right tail is longer**, and mean > median > mode.
- In a **negatively skewed (skewed left)** distribution, the left tail is longer, and mean < median < mode.

The coefficients:

- **Pearson's first coefficient**: Sk = (mean − mode)/s. If the mean is twice the mode and s = mean/5, then Sk = (m − m/2)/(m/5) = **5/2**.
- **Pearson's second coefficient**: Sk = 3(mean − median)/s.
- **Moment coefficient**: **g₁ = m₃/m₂^(3/2)**, where mₖ is the kth moment about the mean. With m₂ = 8.53 and m₃ = −2.69, g₁ = −2.69/24.91 = **−0.108**, slightly negative.

## Kurtosis

**Kurtosis** measures peakedness or tail weight: **b₂ = m₄/m₂²**.

- **b₂ = 3**: **mesokurtic** (the normal curve).
- **b₂ > 3**: **leptokurtic** (sharp peak, heavy tails).
- **b₂ < 3**: **platykurtic** (flat).

With m₂ = 2.5 and m₄ = 3.2, b₂ = 3.2/6.25 = **0.512**, so the distribution is platykurtic. **Excess kurtosis** = b₂ − 3, which is 0 for the normal distribution. A negative excess means platykurtic.

Source: STA 114 Lectures 5 and 6: Relative Position; Skewness and Kurtosis (Ogunde, Adepoju); STA 111 2025 test
