---
title: 'Dominance-Analysis : A Python Library for Global Explainability of Machine Learning Models'
tags:
  - Python
  - Dominance Analysis
  - Feature Importance
  - Feature Selection
  - Explainable AI
  - Global Explainability
  - Shapley Value 
authors:
  - name:  Shashank Shekhar
    orcid: 
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Kunjithapatham Sivakumar
    affiliation: 2
  - name: Sajan Kumar Bhagat
    affiliation: 3
  - name:  Bala Koteshwar Kolluri
    affiliation: 4
affiliations:
 - name: Head of Advanced Analytics, Subex Limited
   index: 1
 - name: Associate Director Advanced Analytics, Subex Limited
   index: 2
 - name: Senior Data Scientist, Subex Limited
   index: 3
 - name: Assistant Manager, Latent View Analytics
   index: 4
date: 17 July 2020
bibliography: paper.bib

---
# Summary

This package is designed for ***Global Explainability*** of machine learning model in terms of relative importance of predictors for both regression and classification models. The determination of relative importance depends on how one defines importance; Budescu (1993) and Azen and Budescu (2003) proposed using dominance analysis (DA) because it invokes a general and intuitive definition of “relative importance” that is based on the additional contribution of a predictor in all subset models. The purpose of determining predictor importance in the context of DA is not model selection but rather uncovering the individual contributions of the predictors.

In case the target is a continuous variable, the package determines the dominance of one predictor over another by comparing their incremental R-squared contribution across all subset models. In case the target variable is binary, the package determines the dominance over another by comparing their incremental Pseudo R-Squared contribution across all subset models.

# Dominance Analysis - The Significance!

Dominance Analysis, according to Azen and Budescu meets three important criteria for measuring relative importance. First, the technique should be defined in terms of its ability to reduce error in predicting the outcome variable. Next, it should permit direct comparison of measures within a model (that is, X<sub>1</sub> is twice as important as X<sub>2</sub>). Finally, the technique should permit inferences concerning an attribute's direct effect (that is, when considered by itself), total effect (that is, when considered with other attributes) and partial effect (that is, when considered with various combinations of other predictors). Hence, Dominance analysis is both robust and intuitive and its interpretation is also very straightforward.


# Dominance Analysis - The Math!

Dominance Analysis is unique as it measures relative importance in a pairwise fashion, and the two predictors are compared
in the context of all 2<sup>(p−2)</sup> models that contain some subset of the other predictors. So, if we have a total of 'p' predictors, we will build 2<sup>p</sup>-1 models (all possible subset models) and compute the incremental R<sup>2</sup> contribution of each predictor to the subset model of all other predictors. The additional contribution of a given predictor is measured by the increase in R<sup>2</sup> that results from adding that predictor to the regression model.

Let's consider a scenario when we have 4 predictors; X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub> and X<sub>4</sub>. We will have to build a total of 2<sup>4</sup>-1 models i.e. 15 models- <sup>4</sup>C<sub>1</sub> = 4 models with only one predictor, <sup>4</sup>C<sub>2</sub> = 6 models with two predictors each, <sup>4</sup>C<sub>3</sub> = 4 models with three predictors each and 1  (<sup>4</sup>C<sub>4</sub>) complete model with all 4 predictors. Thus, the additional contributions of X<sub>1</sub> are computed as the increases in the proportion of variance accounted for when X<sub>1</sub> is added to each subset of the remaining predictors (i.e., the null subset {.}, {X<sub>2</sub>}, {X<sub>3</sub>}, {X<sub>4</sub>}, {X<sub>2</sub>X<sub>3</sub>}, {X<sub>2</sub>X<sub>4</sub>}, {X<sub>3</sub>X<sub>4</sub>} and {X<sub>2</sub>X<sub>3</sub>X<sub>4</sub>}). Similarly, the additional contributions of X<sub>2</sub> are the increases in the proportion of variance accounted for when X<sub>2</sub> is added to each subset of the remaining predictors (i.e., the null subset {.}, {X<sub>1</sub>}, {X<sub>3</sub>}, {X<sub>4</sub>}, {X<sub>1</sub>X<sub>3</sub>}, {X<sub>1</sub>X<sub>4</sub>}, {X<sub>3</sub>X<sub>4</sub>} and {X<sub>1</sub>X<sub>3</sub>X<sub>4</sub>})

Below is the illustration of formulas used to compute the averaged additional contributions of X<sub>1</sub> and X<sub>2</sub> within model size in the poupulation with four predictors (We use the notation <img src='images/formula1.JPG'> to represent the proportion of variance in Y that is accounted for by the predictors in the model X. For example,<img src='images/formula2.JPG'> represents the proportion of variance in Y that is accounted for by the model consisting of X<sub>1</sub> and X<sub>3</sub>. The additional contribution of a given predictor is measured by the increase in proportion of variance that results from adding that predictor to the regression model):

<img src='images/formulas.JPG'> 
<p align="center"> Table 1</p>


The measure for proportion of variance that we have used for regression is R<sup>2</sup> but since we don't have R<sup>2</sup> in logsitic regression/classification models, we have used Pseudo R<sup>2</sup>.


The beauty of the math of Dominance Analysis is that the sum of the  overall average incremental R<sup>2</sup> of all predictors is equal to the R<sup>2</sup> of the complete model (model with all predictors). Hence, the total R<sup>2</sup> can be attributed to each predictor in the model. Below is an illustration of Dominance Analysis in the Population for Hypothetical example with four predictors:

<img src='images/PercentRel.jpg'>
<p align="center"> Table 2</p>

It can bee seen that the Percentage Relative Importance of predictors has been computed by dividing the Overall Average Incremental R<sup>2</sup> contribution of predictors by the R<sup>2</sup> of the complete model. This explains the intuitive nature of Dominance Analysis wherein the overall R<sup>2</sup> of the model can be attributed to individual predictors within the model.

# Pseudo R-Squared for Classification Task / Logistic Regression

Measures of fit in logistic regression can be classified by those based on sums of squares and those based on maximum likelihood statistics. Reviews of a variety of measures of fit proposed for logistic regression can be found in Amemiya (1981), Menard (2000), Mittlbock and Schemper (1996) and Zheng and Agresti (2000). Given the large number of proposed measures, criteria for defining appropriate R<sup>2</sup> analogues need to he determined. The following criteria, which are also found in the linear regression literature (e.g., Kvilseth. 1985: Van den Burg & Lewis, 1988), were used to select R<sup>2</sup> analogues for logistic regression:
1. Boundedness: The measure should vary between a minimum of zero, indicating complete lack of fit, and a maximum of one, indicating perfect fit. 
2. Linear invariance: The measure should be invariant to nonsingular linear transformations of the variables (Ys and Xs). 
3. Monotonicity: The measure should not decrease with the addition of a predictor.
4. Intuitive Interpretability: The measure of fit is intuitively interpretable, in that it agrees with the scale of the linear case for intermediate values.

Based on these criteria, the following four R<sup>2</sup> analogues were chosen that satisfied at least three of these four properties:

**1. McFadden's Pseudo-R Squared**

 McFadden's Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" title="\Large R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" />

This measure satisfies all the four properties.

**2. Nagelkerke Pseudo-R Squared**

Nagelkerke Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Nagelkerke}^{2}=\frac{1-\{\frac{L_{null}}{L_{full}}\}^{2/N}}{1-L_{null}^{2/N}}" title="\Large R_{Nagelkerke}^{2}=\frac{1-\{\frac{L_{null}}{L_{full}}\}^{2/N}}{1-L_{null}^{2/N}}" />

This measure satisfies three of the four properties and doesn't satisfy the property of Interpretability.

**3. Cox and Snell R-Squared**

Cox and Snell Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Cox\&Snell}^{2}=1-\{\frac{L_{null}}{L_{full}}\}^{2/N}" title="\Large R_{Cox\&Snell}^{2}=1-\{\frac{L_{null}}{L_{full}}\}^{2/N}" />

This measure satisfies three of the four properties.

**4. Estrella R-Squared**

Estrella Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Estrella}^{2}=1-\{\frac{LL_{full}}{LL_{null}}\}^{\frac{-2}{N}*LL_{null}}" title="\Large R_{Estrella}^{2}=1-\}\frac{LL_{full}}{LL_{null}}\}^{\frac{2}{N}*LL_{null}}" />

This measure satisfies all the four properties.

Using each of these four R<sup>2</sup> analogues, the additional contribution of a given predictor to a specific logistic model can be measured as the change (i.e., increase) in the R<sup>2</sup> analogues when the predictor is added to the model. Even though, all the four measures will give similar results, we recommend using either Estrella's (1998) model fit measure or McFadden's (1974) measure for conducting dominance analysis in logistic regression. We have a slight preference for McFadden's measure (and that is what the package will compute by default) because it is computationally simpler, but both McFadden's and Estrella’s measures satisfy the minimum requirements for an R<sup>2</sup> analogues.

Note: Since, Dominance Analysis is computationally intensive as it builds all subset model (2<sup>p</sup>-1 models), we have provided the user the flexibility to choose number of top predictors that they want to compute relative importance for. For regression, Top K features are selected based on F-regression and for classification it is based on Chi-Squared statistic. Dominance Analysis can be used in combination with Principal Component Analysis (PCA) or Factor Analysis or any other feature reduction algorithm for getting accurate and intutive importance of predictors.

<hr>

# Dominance Statistics

As described earlier, a relative importance measure should be able to describe a predictor's direct, total and partial effect, therefore in the Dominance Statistics, we have come up with four different types of Dominance measures. **These measures have been conceptualized, defined and formulated by us and are unique to this library**. Below are the definitions and interpretations of the measures:

1. **Interactional Dominance** - This is the incremental R<sup>2</sup> contribution of the predictor to the complete model. Hence, the Interactional Dominance of a particular predictor 'X' will be the diffrence between the R<sup>2</sup> of the complete model and the R<sup>2</sup> of the model with all other predictors except the particular predictor 'X'. <br>
Consider a scenario when we have Y as the dependent variable and four predictors X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub> and X<sub>4</sub>, let  R<sup>2</sup><sub>Y.X<sub>1</sub>,X<sub>2</sub></sub> be the R<sup>2</sup> of the model between Y and X<sub>1</sub>, X<sub>2</sub> ;
R<sup>2</sup><sub>Y.X<sub>1</sub>,X<sub>3</sub></sub> be the R<sup>2</sup> of the model between Y and X<sub>1</sub>, X<sub>3</sub> so on and so forth. In this case, the interactional dominance of predictor X<sub>1</sub> will be R<sup>2</sup><sub>Y.X<sub>1</sub>,X<sub>2</sub>,X<sub>3</sub>,X<sub>4</sub></sub> - R<sup>2</sup><sub>Y.X<sub>2</sub>,X<sub>3</sub>,X<sub>4</sub></sub>. <br>
Hence, interactional dominance can be interpreted as the incremental impact or incremental variability explained by the predictor in presence of all other predictors.

2. **Individual Dominance -** The individual dominance of a predictor is the R<sup>2</sup> of the model between the dependent variable and the predictor. So, the individual dominanace of predictor X<sub>1</sub> will be R<sup>2</sup><sub>Y.X<sub>1</sub></sub>. <br>
Hence, individual dominance can be interpreted as the variability explained by the predictor alone or the quantum of impact that a predictor will have in absence of all other predictors.

3. **Average Partial Dominance -** This is average of average incremental R<sup>2</sup> contributions of the predictor to all subset models except complete model and bi-variate (when only one predcitor is present) model. <br>
Hence, this can be interpreted as the average impact that a predictor has when it is available in all possible combinations with other predictors except the combination when all predcitors are available.

4. **Total Dominance -** The last measure of dominance summarizes the additional contributions of each predictor to all subset models by averaging all the conditional values. In the example on table 3, this consists of averaging the four averaged entries in each column. <br>

In below table, we have illustrated the calculation used to arrive at the four measures of dominance.

<img src='images/Dom Stat.jpg'>
<p align="center"> Table 3</p>
<br>
If we calculate the four measures of dominance from the above example, we will get the following values:
<img src='images/Dominance_Analysis.JPG'>
<p align="center"> Table 4</p>

# Dominance Levels

The following three levels of dominance can be achieved between each pair of predictors in Dominance Analysis: 
* **Complete Dominance** - One predictor is said to completely dominate another predictor if its dominance holds across all possible subset models (that do not include the two predictors under comparison). Back to the four-predictor model, for example, complete dominance of X<sub>1</sub> over X<sub>2</sub> is achieved if the additional R<sup>2</sup> contribution of X<sub>1</sub> is more than that of X<sub>2</sub> to the null model, the model consisting of X<sub>3</sub>, the model consisting of X<sub>4</sub>, and the model consisting of both X<sub>3</sub> and X<sub>4</sub>. In Table 3, we can see that incremental R<sup>2</sup> of X<sub>1</sub> is greater than that of X<sub>2</sub> for all subset models and hence X<sub>1</sub> completely dominates X<sub>2</sub>.
<br> If the additional contributions are inconsistent in favoring the same predictor across all subset models, then complete dominance is undetermined while weaker levels of dominance may still be achieved. 
* **Conditional Dominance** - If a predictor’s averaged additional contribution within each model size is greater than that of another predictor, then the first predictor is said to conditionally dominate the latter. Here, the model size is indicated by the number of predictors included in a given model. If a predictor’s averaged additional contribution is greater for some model sizes but not for all, then conditional dominance between the two predictors cannot be established.
* **General Dominance** - If overall averaged additional R<sup>2</sup> contribution of one predictor is greater than the other then that predictor is said to generally dominate the other. <br>

The three levels of dominance (complete, conditional,and general) are related to each other in a hierarchical fashion: Complete dominance implies conditional dominance, which, in turn, implies general dominance. However, for p > 3 the converse may not
hold; that is, general dominance does not imply conditional dominance and conditional dominance does not necessarily imply complete dominance.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
