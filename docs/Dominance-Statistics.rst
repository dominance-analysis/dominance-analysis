
Dominance Statistics
=============================================

In order to intuitively determine the dominance of one predictor over another, Dominance Analysis compares their incremental R-square contribution across all subset models. Further, a relative importance measure should be able to describe a predictor’s direct, total and partial effect. To address this quantitatively, we have conceptualized and formulated four different types of Dominance measures in our library i.e. Interactional dominance, Individual dominance, Average Partial dominance and Total dominance.

1. **Interactional Dominance:** This measure gives an idea about the predictor's incremental impact in the presence of all other predictors. It is arrived at by subtracting the R-square value of a model with all other predictors from the R-square value of the complete model.

2. **Individual Dominance:** This measure shows the variability explained by the predictor alone in the absence of all other predictors. Mathematically, the individual dominance of a predictor is the R-square of the model between the dependent variable and the predictor variable.

3. **Average Partial Dominance:** This measure is the average of average incremental R-square contributions of the predictor to all subset models except complete model and bi-variate (when only one predcitor is present) model. Hence, this can be interpreted as the average impact that a predictor has when it is available in all possible combinations with other predictors except the combination when all predcitors are available.

4. **Total Dominance:** This measure of dominance summarizes the additional contributions of each predictor to all subset models by averaging all the conditional values.

The below example explains how each of these measures of dominance are arrived at.

.. image:: /images/Dom_Stat.jpg
  :width: 600


The measures of dominance calculated for these predictors can be seen below.

.. image:: /images/Dominance_Analysis.JPG
  :width: 600
