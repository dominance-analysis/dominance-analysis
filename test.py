from dominance_analysis import Dominance
import pandas as pd
data=pd.read_csv("data/Data_4_Variables.csv")
dominance=Dominance(data,'Y')

print("Incremental R Square : ")
print(dominance.incremental_rsquare())
print("Model R Square Stats : ")
print(dominance.model_stats())
