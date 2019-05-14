About Dominance Analysis
=============================================

Dominance-Analysis is a Python library built for accurately determining the relative importance of interacting predictors in a statistical model. The variable's individual effect as well as its effect in the presence of other variables is accounted for in identifying its proportionate contribution to the model. 

The library can be used in combination with Principal Component Analysis (PCA) or Factor Analysis or any other feature reduction algorithm for getting accurate and intutive importance of predictors. The purpose of determining predictor importance in the context of Dominance Analysis is not model selection but rather uncovering the individual contributions of the predictors. 

The library can be used for key driver analysis or marginal resource allocation models and helps marketers answer many questions like 

- Which marketing touchpoints in a sales journey have the most impact on conversions.
- Which subgroup prevalence differences in complex surveys are most important.
- Which aspects of a service influence how likely a customer would recommend a company to others.

Package Features
----------------------------------------------
- Evaluates predictor importance when the analysis is either in the form of Ordinary Least Squares Regression or the Logistic Regression. 
- Allows performing Dominance Analysis even in the cases where only the Covariance / Correlation matrix of the predictor variables is available.
- Provides the user the flexibility to choose number of top predictors that they want to compute relative importance for.
- Provides Complete, Conditional and General dominance analysis for models.
