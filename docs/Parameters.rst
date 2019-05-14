Parameters
===========================

This page contains descriptions of the important parameters in the Dominance-Analysis package.

-  ``data`` 
   -  Complete Dataset, should be a Pandas DataFrame
-  ``target`` 
   -  Name of the target variable, it should be present in passed dataset.
-  ``top_k`` 
   -  No. of features to choose from all available features. By default, the package will run for top 15 features.
-  ``objective`` 
   -  It can take value either 0 or 1.
     ``0`` for Classification 
     
     ``1`` for Regression
     
     By default, the package will run for Regression.
-  ``pseudo_r2`` 
   -  It can take one of the Pseudo R-Squared measures - ``mcfadden``, ``nagelkerke`` , ``cox_and_snell`` or ``estrella``, where default = ``mcfadden``. It is not needed in case of regression (objective= ``1`` ).
-  ``data_format`` 
   -  It can take value 0, 1 or 2.
     
     ``0`` when raw data is being passed,
     
     ``1`` when correlation matrix (correlation of predictors with target variable) is being passed,
     
     ``2`` when covraiance matrix (covariance of predictors with target variable) is being passed. 
     
     By default, the package will run for raw data (``data_format`` = ``0``). This parameter is not needed in case of classification.

