Installation and User Guide
=============================================

Use the following command to install the package:

.. code-block:: python
   
   pip install dominance-analysis
   
The ``dominance-analysis`` pakage can then be invoked through the below code.

.. code-block:: python
   
   dominance_classification=Dominance(data=df_data,target='Target',objective=0,pseudo_r2="mcfadden",data_format=0)
   
The overall R-square of the complete model will be displayed as an output.

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


User Guide
--------------------------------------

The package has the below functions that can be used for performing Dominance Analysis and coming up with visualizations that help understand the variable significance and dominance levels.

.. list-table:: **class Dominance**
   :widths: 50 50
   :header-rows: 1

   * - Function
     - Utility
   * - ``incremental_rsquare()``
     - The function will evaluate the Overall Average Incremental R-square contribution of the predictors to the R-square of the complete model.
   * - ``plot_incremental_rsquare()``
     - The function will plot the Incremental R-square contribution of the predictors in the form visulaizations like Bar Graph, Pie Chart and Waterfall chart.
   * - ``dominance_stats()``
     - The function will give the Dominance Statistics for each of the predictor variables.
   * - ``dominance_level()``
     - For each predictor variable, the function will clearly list out all the predictors that are dominated generally, conditionally and completely by it. 
   * - ``complete_model_rsquare()``
     - The function will print the R-squared value of the complete model.
     
.. list-table:: **class Dominance_Datasets**
   :widths: 50 50
   :header-rows: 1

   * - Function
     - Utility
   * - ``get_breast_cancer()``
     - The function will fetch the `UCI ML Breast Cancer Wisconsin (Diagnostic) dataset`_, in the form of a Pandas dataframe, to be able to use it for Dominance Analysis. The response variable in this case is continuos.
   * - ``get_boston()``
     - The function will fetch the `Boston Housing Dataset dataset`_, in the form of a Pandas dataframe, to be able to use it for Dominance Analysis. The response variable in this case is binary.


You can find a more detailed information and examples regarding the package in the `Official Dominance Analysis Documentation`_.

.. _UCI ML Breast Cancer Wisconsin (Diagnostic) dataset: https://goo.gl/U2Uwz2
.. _Boston Housing Dataset dataset: https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html
.. _Official Dominance Analysis Documentation: https://bhagatsajan0073.github.io/dominance-analysis/
