---
title: 'Dominance-Analysis : A Python Library for Accurate and Intuitive Relative Importance of Predictors'
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
date: 13 August 2017
bibliography: paper.bib

---
# Summary

This package is designed to determine relative importance of predictors for both regression and classification models. The determination of relative importance depends on how one defines importance; Budescu (1993) and Azen and Budescu (2003) proposed using dominance analysis (DA) because it invokes a general and intuitive definition of “relative importance” that is based on the additional contribution of a predictor in all subset models. The purpose of determining predictor importance in the context of DA is not model selection but rather uncovering the individual contributions of the predictors.

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
