# Dominance Analysis for Accurate and Intuitive Relative Importance of Predictors

*This package is designed for regression task where-in provided with a dataset and continous target variable, the package returns the Incremental R-Square that any variable will add to total R-Square of the model. As the complexity of the algorithm increases with number of features, we have in-built functionality that chooses the <b>K=15</b> best features from all the estimators and returns incremental R-Square each variable all to the total R-Square of the model.*

<hr>

**Installation**
```  
pip install dominance-analysis
```  
<hr>

**User Guide**
```
from dominance_analysis import Dominance
import pandas as pd
data=pd.read_excel("./Book2.xlsx")
dominance=Dominance(data=data,target='Y',top_k=10,objective=1)
``` 

<hr>

**Incremental R-Square**
```
incr_variable_rsquare=dominance.incremental_rsquare()
```
<img src='Model Training.JPG'>

<hr>

**Plot Incremental R-Square**
```
dominance.plot_incremental_rsquare()
```
<img src='Bar.png'>
<hr>
<img src='Pie.png'>
<hr>


**Dominance Statistics (R-Square)**
```
dominance.domiance_stats()
```
<img src='dominance_stats.JPG'>

## PSEUDO R-Square for Classification Task / Logistic Regression

**1. McFadden's Pseudo-R Square**

Logistic regression models are fitted using the method of maximum likelihood - i.e. the parameter estimates are those values which maximize the likelihood of the data which have been observed. McFadden's R squared measure is defined as

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" title="\Large R_{McFadden}^{2}=1-\frac{log(L_{full})}{log(L_{null})}" />

where $L_{full}$ denotes the (maximized) likelihood value from the current fitted model, and $L_{null}$ denotes the corresponding value but for the null model - the model with only an intercept and no covariates.

**2. Nagelkerke Pseudo-R Square**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Nagelkerke}^{2}=\frac{1-\{\frac{log(L_{null})}{log(L_{full})}\}^{2/N}}{1-L_{null}^{2/N}}" title="\Large R_{Nagelkerke}^{2}=\frac{1-\{\frac{log(L_{null})}{log(L_{full})}\}^{2/N}}{1-L_{null}^{2/N}}" />



**3. Cox and Snell R-Square**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Cox\&Snell}^{2}=1-[\frac{log(L_{null})}{log(L_{full})}]^{2/N}" title="\Large R_{Cox\&Snell}^{2}=1-[\frac{log(L_{null})}{log(L_{full})}]^{2/N}" />

**4. Estrella R-Square**

<img src="https://latex.codecogs.com/svg.latex?\Large&space;R_{Estrella}^{2}=1-[\frac{LL_full}{LL_{null}}]^{\frac{2}{N}*LL_{null}}" title="\Large R_{Estrella}^{2}=1-[\frac{LL_full}{LL_{null}}]^{\frac{2}{N}*LL_{null}}" />



