# Chi-square Tests, ANOVA and Regression

## The chi-square distribution

It takes only **non-negative** values, is **positively skewed**, has **mean equal to its degrees of freedom (k)** and **variance 2k**, approaches the normal as k grows, and sums of independent chi-squares are chi-square.

## Goodness of fit

**χ² = Σ (O − E)²/E** compares observed and expected frequencies. The degrees of freedom are **k − 1 − r**, where k is the number of classes (after merging) and r the number of parameters estimated from the data. Classes with expected frequency below 5 are combined.

For a **Poisson** fit, estimate λ by the sample mean: the 100 pond samples (13, 20, 24, 30, 7, 5, 1, 0 for 0 to 7 organisms) give λ̂ = 217/100 = **2.17**. For a **binomial** fit with n trials, estimate p = x̄/n.

## Independence

For an r × c **contingency table**, **E = (row total × column total)/grand total** and the degrees of freedom are **(r − 1)(c − 1)**. Blood type (4 columns) against severity (3 rows) has **6** degrees of freedom.

## Experimental design and ANOVA

A **treatment** is a condition compared; **replication** repeats it on several units; **randomization** assigns units by chance; **blocking** groups similar units to remove known variation. ANOVA assumes **normal** populations, **independent** observations and **equal variances**.

**One-way ANOVA** (completely randomized design): total SS = treatment SS + error SS, and **F = MST/MSE** with **(k − 1, N − k)** degrees of freedom. Three packaging methods with 7 values each give F on (2, 18) degrees of freedom.

**Two-way ANOVA** (randomized complete block design): total SS = treatment SS + block SS + error SS, with error degrees of freedom (t − 1)(b − 1); both treatments and blocks can be tested.

## Regression and correlation

The least-squares line **ŷ = a + bx** has **b = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²)** and **a = ȳ − b x̄**. For the 2012/13 data, n = 10, Σx = 175, Σy = 101, Σxy = 2414 and Σx² = 4205. So b = 6465/11425 = **0.566** and a = 10.1 − 0.566(17.5) = 0.197, giving ŷ = 0.197 + 0.566x.

The correlation coefficient **r** lies between −1 and 1; H0: ρ = 0 is tested with **t = r√(n − 2)/√(1 − r²)** on n − 2 degrees of freedom.

Source: STA 221 course outline (STA 221_merged.pdf); STA 221 past papers; General knowledge of STA 221, as no slides on these weeks are in the folder
