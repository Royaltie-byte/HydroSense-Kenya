 Entry 1

Prompt Used: Generate a 500–700 word scientific problem statement for HydroSense-Kenya based on the project brief.
AI Output Summary: Produced a problem statement explaining the irrigation challenge, datasets, scientific question, and computational objectives.
Accepted: Yes
Modified: Minor wording edits if needed.
Validation Method: Compared against project brief requirements and project scenario section.

Entry 2

Prompt Used: Generate text content for Level 1 tasks including dataset loading code, data dictionary, ET and water balance functions with docstrings, symbol explanations for both formulas, a pre-plot markdown section describing the two visualisations, and graph interpretations for both plots.
AI Output Summary: Generated pandas loading and inspection code, a full data dictionary for all three datasets, two core Python functions (calculate_et and water_balance) with docstrings, symbol explanations for ET and water balance formulas, a pre-plot markdown section, graph interpretations for both plots, and a structured assumptions and limitations section.
Accepted: Partly
Modified: Plot code was written independently by the student. AI was used only for troubleshooting plot-related issues and generating all text-based content.
Validation Method: Functions verified by manually substituting known values and checking output against the ET formula and water balance equation. Plot verified visually by the student against the raw dataset values. Text content checked against project brief requirements and project scenario section.


Entry 3.

Prompt Used: Generate the error propagation experiment for Level 2 Task 5, including noise simulation across 1000 iterations, summary statistics, and a plot showing ET and irrigation distributions under sensor noise.
AI Output Summary: Generated a 1000-simulation error propagation experiment with random noise added to all four weather variables, summary statistics for both ET and irrigation recommendations, and a dual-panel matplotlib plot showing the distributions under noise.
Accepted: Partly
Modified: Syntax simplified to match student coding style. Plot styling adjusted to be consistent with the rest of the notebook.
Validation Method: Results checked for statistical reasonableness — ET spread should be small relative to the clean ET mean. Irrigation recommendation range checked against known target and current moisture values.

Entry 4

Prompt Used: Help debug the bisection, Newton-Raphson, and secant root finding functions in Level 3.
AI Output Summary: Identified and explained issues in the root finding functions including derivative handling in Newton-Raphson and interval setup in bisection. Explained the logic behind error calculation in bisection and how the secant method approximates the slope using two previous points.
Accepted: Partly
Modified: All three functions were written by the student. AI was only consulted when specific parts of the functions were not behaving as expected.
Validation Method: All three methods verified by comparing their results against the direct algebraic solution using np.isclose(). Gaussian elimination verified against NumPy's np.linalg.solve(). Integration results verified by checking against expected cumulative deficit range given the raw moisture values.



Entry 5.

Prompt Used: Generate documentation text, explanatory write-ups, and repetitive boilerplate code for Level 4 tasks, including data-cleaning descriptions, markdown explanations, and routine implementation patterns.

AI Output Summary: Generated supporting documentation text, explanatory markdown content, and repetitive code structures used during Level 4. Core analytical logic, data-cleaning decisions, validation procedures, and project-specific implementation details were developed and written by the student.

Accepted: Partly

Modified: Documentation was edited for clarity and alignment with project requirements. Generated code was reviewed, adapted, and integrated with student-written analysis and implementation. Project-specific logic and decisions were implemented independently.

Validation Method: All generated text was checked against project instructions and dataset characteristics. Generated code was executed, reviewed line-by-line, and verified to produce expected outputs before inclusion in the final notebook.