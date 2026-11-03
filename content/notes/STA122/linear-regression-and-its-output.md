# Linear Regression and Its Output

## The model

**Regression** estimates the relationship between a **dependent** (criterion) variable and one or more **independent** (explanatory, predictor) variables.

- **Simple** linear regression has one predictor, and **multiple** regression has two or more.
- Data that do not follow a straight line need **non-linear** regression.

The model is **Y = β₀ + β₁X + ε**, and the fitted line is **Ŷ = β̂₀ + β̂₁X**, where:

- β₀ is the **intercept** (Ŷ when X = 0);
- β₁ is the **slope**;
- ε is the error.

Each **residual** is e = Y − Ŷ. **Least squares** chooses the line that makes the **sum of squared residuals Σ(Y − Ŷ)²** as small as possible.

Error measures:

- **MSE = Σ(Y − Ŷ)²/n**;
- **MAE = Σ|Y − Ŷ|/n**.

(The board notes leave out the /n and the Σ respectively.)

## The umbrella example

Monthly rainfall (mm) and umbrellas sold over **24 months**, fitted in Excel with the **Analysis ToolPak** (Data → Data Analysis → Regression, with Y the umbrellas and X the rainfall), give **Ŷ = 0.45x − 19.074**.

- At 82 mm, Ŷ = 0.45 × 82 − 19.074 ≈ **17.8**.
- The actual sales were 15, so the residual is **−2.8**.

The same coefficients come from **=SLOPE**, **=INTERCEPT** or **=LINEST**, and **=CORREL** gives r. A scatter chart with a linear trendline displays the equation. Put the independent variable on the **X axis**.

## Reading the output

**Summary statistics**:

- **Multiple R** = 0.958, the correlation coefficient, between −1 and 1;
- **R²** = 0.917, the **coefficient of determination**: about 92% of the variation in umbrella sales is explained by rainfall;
- **adjusted R²** = 0.913, corrected for the number of predictors and used in multiple regression;
- **standard error** = 3.58, the typical distance of points from the line.

(The tutorial rounds R² to 0.91 and says 0 means "no relationship". It means no *linear* relationship.)

**ANOVA** splits the total sum of squares into regression and residual parts (SS 3122.8 and 282.2, with df 1 and 22). It gives **F = 243.5** and **Significance F** (the p-value of F) = 2.2 × 10⁻¹³. A value below 0.05 means the model is significant.

**Coefficients**: the intercept is −19.07 and the rainfall slope 0.450, with SE 0.029, t = 15.6 and p ≈ 2.2 × 10⁻¹³. Its 95% confidence interval is **0.390 to 0.510**. Each extra millimetre of rainfall adds about 0.45 umbrellas.

Source: STA 122 Lecture 5: Regression Analysis in Excel and the board notes
