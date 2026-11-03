# Plotting and Anonymous Functions

## Plotting

`plot(x, y)` draws y against x as a line, joining the points in order, so x and y must have the same length. For a smooth curve, use many points, for example `T = linspace(100, 1000, 200)`. A third argument sets the style: `plot(x, y, 'r--')` draws a red dashed line, and markers such as `'o'` show the points.

Every plot should be labelled:

- `title('Pressure of a perfect gas')` gives the plot a title.
- `xlabel('Temperature (K)')` and `ylabel('Pressure (kPa)')` label the axes, with units.
- `grid on` adds a grid, and `legend('curve 1', 'curve 2')` names several curves.

`hold on` keeps the current plot so the next plot command adds to it; `hold off` ends this. `subplot(m, n, k)` divides the figure into an m × n grid and draws in panel k. `figure` opens a new window.

## Parametric curves

A **parametric curve** gives x and y as functions of a parameter t. Compute both from the same t vector, using element-wise operators, then plot y against x: for example `t = linspace(-1, 1, 200); x = t.^2; y = a*t.^3; plot(x, y)`. This is the kind of curve the course's practical test asks for "over the parametric interval −1 ≤ t ≤ 1".

## Anonymous functions

An **anonymous function** is a one-line function defined without a file, using the **@** operator: `p = @(theta) p0*(1 + 2*g/(g+1)*(M^2*sin(theta).^2 - 1));` defines p in terms of theta, using the values of p0, g and M that exist when it is created. It is called like any function, `p(pi/4)`, and can be passed to other functions or plotted with `fplot(p, [a b])`.

## Function files

A **function file** begins with `function [outputs] = name(inputs)` and is saved as name.m. Unlike a script, it has its own local workspace: it receives inputs, computes, and returns outputs, which makes code reusable and testable.

Source: Written from general knowledge of CSC 231; no course file covered this topic.
