.. dominance-analysis documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Dominance-Analysis documentation!
=============================================

Dominance-Analysis is a Python package built for accurately determining the relative importance of interacting predictors in a statistical model. The variable's individual effect as well as its effect in the presence of other variables is accounted for in identifying its proportionate contribution to the model. The library can be used in combination with Principal Component Analysis (PCA) or Factor Analysis or any other feature reduction algorithm for getting accurate and intutive importance of predictors. The purpose of determining predictor importance in the context of Dominance Analysis is not model selection but rather uncovering the individual contributions of the predictors. 

The library can be used for key driver analysis or marginal resource allocation models and helps marketers answer many questions like 

- Which marketing touchpoints in a sales journey have the maximum impact on product adoptions.
- Which subgroup prevalence differences in complex surveys are most important.
- Which aspects of the service influence how likely a customer would recommend a company to others.

Package Features
=============================================
- Evaluates predictor importance when the analysis is either in the form of Ordinary Least Squares Regression or the Logistic Regression. 
- Allows performing Dominance Analysis even in the cases where only the Covariance/Correlation matrix of the predictor variables is available.
- Provides the user the flexibility to choose number of top predictors that they want to compute relative importance for.
- Provides Complete, Conditional and General dominance analysis for models.

The package is currently compatible with Python 2.7, 3.5 and 3.6.

You can find out more regarding the package in the `Official Dominance Analysis Documentation`_.

.. _Official Dominance Analysis Documentation: https://bhagatsajan0073.github.io/dominance-analysis/

Installation
=============================================

Use the following command to install the package:

``pip install dominance-analysis`` 

.. toctree::
   :maxdepth: 1
   :caption: Contents:

.. toctree::
   :maxdepth: 1

   Our Approach
   Dominance Statistics
   Examples
   
Authors & License
-----------------

This package is released under an open source MIT license. The Dominance Analysis package is based on the concept developed by
Azen and Budescu. Pull requests submitted to the `GitHub Repo`_ are highly encouraged! Dominance Analysis Python package has been developed by  `Shashank Shekhar`_, `Sajan Bhagat`_, `Kunjithapatham Sivakumar`_ and `Bala Koteshwar Kolluri`_.

The latest build status can be found at `Travis CI`_.

.. _Shashank Shekhar: https://github.com/quintshekhar
.. _Sajan Bhagat: https://github.com/bhagatsajan0073
.. _Kunjithapatham Sivakumar: https://github.com/Vibish
.. _Bala Koteshwar Kolluri: https://github.com/balakolluri
.. _GitHub Repo: https://github.com/bhagatsajan0073/dominance-analysis
.. _Travis CI: https://travis-ci.org/bhagatsajan0073/dominance-analysis


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

