Installation Guide
=============================================

Use the following command to install the package:

.. code-block:: python
   
   pip install dominance-analysis
   
The ``dominance-analysis`` pakage can then be invoked through the below code.

.. code-block:: python
   
   dominance_classification=Dominance(data=df_data,target='Target',objective=0,pseudo_r2="mcfadden",data_format=0)

Parameters   
--------------------------------------------

The descriptions of the parameters to be passed to the Dominance class are provided below.

-  ``data`` 
   -  Complete Dataset, should be a Pandas DataFrame
-  ``target`` 
   -  Name of the target variable, it should be present in passed dataset.
-  ``top_k`` 
   -  No. of features to choose from all available features. By default, the package will run for top 15 features.
-  ``objective`` 
   -  It can take the values 0 or 1.
     ``0`` for Classification 
     
     ``1`` for Regression
     
     By default, the package will run for Regression.
-  ``pseudo_r2`` 
   -  It can take one of the Pseudo R-Squared measures - ``mcfadden``, ``nagelkerke`` , ``cox_and_snell`` or ``estrella``, where default = ``mcfadden``. It is not needed in the case of regression models (i.e. ``objective`` = ``1`` ).
-  ``data_format`` 
   -  It can take the values 0, 1 or 2.
     
     ``0`` when raw data is being passed,
     
     ``1`` when correlation matrix (correlation of predictors with target variable) is being passed,
     
     ``2`` when covariance matrix (covariance of predictors with target variable) is being passed. 
     
     By default, the package will run for raw data (i.e. ``data_format`` = ``0``). This parameter is not needed in case of Classification models.

