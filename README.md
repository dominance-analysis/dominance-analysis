# Dominance Analysis for Accurate and Intuitive Relative Importance of Predictors

*This package is designed to determine relative importance of predictors for both regression and classification models. The determination of relative importance depends on how one defines importance; Budescu (1993) and Azen and Budescu (2003) proposed using dominance analysis (DA) because it invokes a general and intuitive definition of "relative importance" that is based on the additional contribution of a predictor in all subset models. The purpose of determining predictor importance in the context of DA is not model selection but rather uncovering the individual contributions of the predictors. *

*In case the target is a continuous variable, the package determines the dominance of one predictor over another by comparing their incremental R-squared contribution across all subset models. In case the target variable is binary, the package determines the dominance over another by comparing their incremental Pseudo R-Squared contribution across all subset models.*

<hr>

**Installation**
```  
pip install dominance-analysis
```  
<hr>

**Important Parameters**
 
  * data : Complete Dataset, should be a Pandas DataFrame.   
  * target : Name of target variable, it should be present in passed dataset.
  * top_k : No. of features to choose from all available features.
  * objective : It can take value either 0 or 1.    0 for Classification Task and 1 for Regression Task
  * pseudo_r2 : It can have value "mcfadden","nagelkerke","cox_and_snell" or "estrella" where default="mcfadden". It's not needed in         case of regression task (objective=1)

### PSEUDO R-Square for Classification Task / Logistic Regression
Logistic regression models are fitted using the method of maximum likelihood - i.e. the parameter estimates are those values which maximize the likelihood of the data which have been observed.

**1. McFadden's Pseudo-R Square**

 McFadden's Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" title="\Large R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" />


**2. Nagelkerke Pseudo-R Square**

Nagelkerke Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Nagelkerke}^{2}=\frac{1-\{\frac{L_{null}}{L_{full}}\}^{2/N}}{1-L_{null}^{2/N}}" title="\Large R_{Nagelkerke}^{2}=\frac{1-\{\frac{L_{null}}{L_{full}}\}^{2/N}}{1-L_{null}^{2/N}}" />


**3. Cox and Snell R-Square**

Cox and Snell Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Cox\&Snell}^{2}=1-\{\frac{L_{null}}{L_{full}}\}^{2/N}" title="\Large R_{Cox\&Snell}^{2}=1-\{\frac{L_{null}}{L_{full}}\}^{2/N}" />

**4. Estrella R-Square**

Estrella Pseudo-R squared measure is defined as :

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Estrella}^{2}=1-\{\frac{LL_{full}}{LL_{null}}\}^{\frac{2}{N}*LL_{null}}" title="\Large R_{Estrella}^{2}=1-\}\frac{LL_{full}}{LL_{null}}\}^{\frac{2}{N}*LL_{null}}" />

<hr>

**User Guide for Regression Task**
```
from dominance_analysis import Dominance
import pandas as pd
data=pd.read_excel("./Book2.xlsx")                           # file is available in data folder 
dominance=Dominance(data=data,target='Y',top_k=10,objective=1)
``` 
<img src='images/Regression Domiance.JPG'>

<hr>

**Incremental R-Square**
```
incr_variable_rsquare=dominance.incremental_rsquare()
```
<img src='images/Model Training.JPG'>

<hr>

**Plot Incremental R-Square**
```
dominance.plot_incremental_rsquare()
```
<img src='images/Bar.png'>
<hr>
<img src='images/Pie.png'>
<hr>


**Dominance Statistics (R-Square)**
```
dominance.domiance_stats()
```
<img src='images/dominance_stats_reg.JPG'>


<hr>


**User Guide for Classification Task**
```
from dominance_analysis import Dominance
import pandas as pd
data=pd.read_excel("./Dominance_Classification_Task_Data.xlsx")                           # file is available in data folder 
dominance_classification=Dominance(data=data,target='Y',top_k=4,objective=0,pseudo_r2="mcfadden")
``` 
<img src='images/Classification Domiance.JPG'>

<hr>

**Incremental Pseudo R-Square**
```
incr_variable_rsquare=dominance_classification.incremental_rsquare()
```
<img src='images/Incremental_Pseudo_RSquare_Classification.JPG'>

<hr>

**Plot Incremental Pseudo R-Square**
```
dominance_classification.plot_incremental_rsquare()
```
<img src='images/Bar_Classification.png'>
<hr>
<img src='images/Pie_Classification.png'>
<hr>


**Dominance Statistics (R-Square)**
```
dominance_classification.domiance_stats()
```
<img src='images/dominance_stats_classification.JPG'>

