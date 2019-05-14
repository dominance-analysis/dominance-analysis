
Dominance Levels
=============================================

Dominance Analysis defines three levels of dominance while comparing each pair of predictors:

1. **Complete Dominance:** A predictor is said to completely dominate another predictor if its dominance holds across all possible subset models (that do not include the two predictors under comparison). For example, in a four-predictor model, X1 is said to have complete dominance over X2 when the additional R-square contribution of X1 is more than that of X2 for all subset models i.e. to the null model, the model consisting of X3, the model consisting of X4, and the model consisting of both X3 and X4.

2. **Conditional Dominance:** When a predictor’s averaged additional contribution within each model size is greater than that of another predictor, then the first predictor is said to conditionally dominate the latter. Here, the model size is indicated by the number of predictors included in a given model. If a predictor’s averaged additional contribution is greater for some model sizes but not for all, then conditional dominance between the two predictors cannot be established.

3. **General Dominance:** If the overall averaged additional R2 contribution of one predictor is greater than the other, then the predictor is said to generally dominate the other.

For each predictor variable, the library clearly lists out all the predictors that are dominated generally, conditionally and completely by it.
