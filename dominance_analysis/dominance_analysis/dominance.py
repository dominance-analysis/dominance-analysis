import numpy as np
from itertools import combinations
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_boston
from tqdm import tqdm
from sklearn.feature_selection import SelectKBest,chi2,f_regression
import pandas as pd
from plotly import offline
from plotly.offline import init_notebook_mode,iplot
import cufflinks as cf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
import statsmodels.api as sm
from functools import  reduce
import math
init_notebook_mode(connected=True)


class Dominance:
	"""docstring for ClassName"""
	def __init__(self,data,target,top_k=None,objective=1,pseudo_r2='mcfadden'):
		# super(ClassName, self).__init__()
		self.data = data
		self.target=target
		self.objective=objective
		self.top_k=top_k if top_k else min((len(self.data.columns)-1),15)
		self.pseudo_r2=pseudo_r2
		assert (self.top_k >1 ) and (self.top_k<(len(self.data.columns))),"Value of top_k ranges from 1 to n-1 !"
		self.complete_model_rsquare()
	
	def conditional_dominance(self,model_rsquares,model_features_k,model_features_k_minus_1,columns):
		# print("#"*25," Calculating Conditional Dominance ","#"*25)
		total_model_r2=model_rsquares[" ".join(model_features_k[0])]
		return dict({(" ".join(set(model_features_k[0])-set(i)),total_model_r2-model_rsquares[" ".join(i)]) for i in model_features_k_minus_1})

	def individual_dominance(self,model_rsquares,model_features,columns):
		# print("#"*25," Calculating individual Dominance ","#"*25)
		return dict({(" ".join(col),model_rsquares[" ".join(col)]) for col in model_features })

	def partial_dominance(self,model_rsquares,model_features_k,model_features_k_minus_1,columns):
		# print(columns)
		pd={col: [] for col in columns}
		[pd[" ".join(set(i)-set(j))].append(model_rsquares[" ".join(i)]-model_rsquares[" ".join(j)]) for i in model_features_k for j in model_features_k_minus_1 if(len(set(i)-set(j))==1)]
		return pd

	def model_features_combination(self,columns):
		return [list(combinations(columns,i)) for i in range(1,len(columns)+1)]

	def McFadden_RSquare(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[columns])
		result=log_clf.fit(disp=0)
		mcfadden_rsquare=result.prsquared
		return mcfadden_rsquare

	def Nagelkerke_Rsquare(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[columns])
		N=self.data.shape[0]
		result=log_clf.fit(disp=0)
		llf=result.llf
		llnull=result.llnull
		lm=np.exp(llf)
		lnull=np.exp(llnull)
		naglkerke_rsquare=(1-(lnull/lm)**(2/N))/(1-lnull**(2/N))
		return naglkerke_rsquare

	def Cox_and_Snell_Rsquare(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[columns])
		N=self.data.shape[0]
		result=log_clf.fit(disp=0)
		llf=result.llf
		llnull=result.llnull
		lm=np.exp(llf)
		lnull=np.exp(llnull)
		cox_and_snell_rsquare=(1-(lnull/lm)**(2/N))
		return cox_and_snell_rsquare

	def Estrella(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[columns])
		N=self.data.shape[0]
		result=log_clf.fit(disp=0)
		llf=result.llf
		llnull=result.llnull
		estrella_rsquare=1-((llf/llnull)**(-(2/N)*llnull))
		return estrella_rsquare

	def Adjusted_McFadden_RSquare(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[columns])
		result=log_clf.fit(disp=0)
		llf=result.llf
		llnull=result.llnull
		adjusted_mcfadden_rsquare=1-((llf-len(columns))/llnull)
		return adjusted_mcfadden_rsquare

	def model_stats(self):
		# columns=list(self.data.columns.values)
		# columns.remove(self.target)
		# # print("Independent Variables : ",columns)

		## Calculating Incremental R2 for Top_K_Variables 
		columns=self.get_top_k()

		model_combinations=self.model_features_combination(columns)
		model_rsquares={}
		if(self.objective==1):
			for i in tqdm(model_combinations):
			    for j in i:
			        train_features=list(j)
			        lin_reg=LinearRegression()
			        lin_reg.fit(self.data[train_features],self.data[self.target])
			        r_squared=lin_reg.score(self.data[list(j)],self.data[self.target])
			        model_rsquares[" ".join(train_features)]=r_squared
		else:
			for i in tqdm(model_combinations):
			    for j in i:
			        train_features=list(j)
			        if(self.pseudo_r2=='mcfadden'):
			        	# print("mcfadden")
			        	r_squared=self.McFadden_RSquare(train_features)
			        # elif(self.pseudo_r2=='adjusted_mcfadden'):
			        # 	r_squared=self.Adjusted_McFadden_RSquare(train_features)
			        elif(self.pseudo_r2=='nagelkerke'):
			        	# print("nagelkerke")
			        	r_squared=self.Nagelkerke_Rsquare(train_features)
			        elif(self.pseudo_r2=='cox_and_snell'):
			        	r_squared=self.Cox_and_Snell_Rsquare(train_features)
			        elif(self.pseudo_r2=='estrella'):
			        	r_squared=self.Estrella(train_features)
			        model_rsquares[" ".join(train_features)]=r_squared
		
		self.model_rsquares=model_rsquares
		return self.model_rsquares

	def variable_statistics(self,model_rsquares,columns):
		stats={}
		# print(columns)
		model_combinations=self.model_features_combination(columns)
		for k in tqdm(range(len(columns),1,-1)):
		    model_features_k=[i for j in model_combinations for i in j if len(i)==k]
		    model_features_k_minus_1=[i for j in model_combinations for i in j if len(i)==k-1]
		    if(k==len(columns)):
		        stats['conditional_dominance']=self.conditional_dominance(model_rsquares,model_features_k,model_features_k_minus_1,columns)
		    else:
		    	stats['partial_dominance_'+str(k)]=self.partial_dominance(model_rsquares,model_features_k,model_features_k_minus_1,columns)

		    if(k==2):
		        stats['individual_dominance']=self.individual_dominance(model_rsquares,model_features_k_minus_1,columns)

		variable_stats={}
		for col in columns:
		    variable_stats[col]={
		            'conditional_dominance':stats['conditional_dominance'][col],
		            'individual_dominance':stats['individual_dominance'][col],
		            'partial_dominance':[np.mean(stats["partial_dominance_"+str(i)][col]) for i in range(len(columns)-1,1,-1)]
		    }

		self.variable_stats=variable_stats
		return self.variable_stats

	def dominance_stats(self):
		tf=pd.DataFrame(self.variable_stats).T
		tf['Interactional Dominance']=tf['conditional_dominance']
		tf['Average Partial Dominance']=tf['partial_dominance'].apply(lambda x:np.mean(x))
		tf['partial_dominance_count']=tf['partial_dominance'].apply(lambda x:len(x))
		tf['Total Dominance']=(tf['partial_dominance_count']*tf['Average Partial Dominance']+tf['conditional_dominance']+tf['individual_dominance'])/(tf['partial_dominance_count']+2)
		tf=tf[['Interactional Dominance','individual_dominance','Average Partial Dominance','Total Dominance']].sort_values("Total Dominance",ascending=False)
		tf.rename(columns={"individual_dominance":"Individual Dominance"},inplace=True)
		return tf



	def get_top_k(self):
		columns=list(self.data.columns.values)
		columns.remove(self.target)
		if(self.objective):
			top_k_vars=SelectKBest(f_regression, k=self.top_k)
		else:
			top_k_vars=SelectKBest(chi2, k=self.top_k)
		top_k_vars.fit_transform(self.data[columns], self.data[self.target])
		return [columns[i] for i in top_k_vars.get_support(indices=True)]

	def plot_incremental_rsquare(self):
		incremental_rsquare_df1=pd.DataFrame()
		incremental_rsquare_df1['Features']=self.incrimental_r2.keys()
		incremental_rsquare_df1['incremental_r2']=self.incrimental_r2.values()
		incremental_rsquare_df1.sort_values('incremental_r2',ascending=False,inplace=True)

		incremental_rsquare_df2=pd.DataFrame()
		incremental_rsquare_df2['Features']=self.percentage_incremental_r2.keys()
		incremental_rsquare_df2['percentage_incremental_r2']=self.percentage_incremental_r2.values()
		incremental_rsquare_df2.sort_values('percentage_incremental_r2',ascending=False,inplace=True)


		incremental_rsquare_df=pd.merge(left=incremental_rsquare_df1,right=incremental_rsquare_df2)
		incremental_rsquare_df['percentage_incremental_r2']=incremental_rsquare_df['percentage_incremental_r2']*100

		iplot(incremental_rsquare_df[['Features','incremental_r2']].set_index("Features").iplot(asFigure=True,kind='bar',title="Incremetal "+("Pseudo " if (self.objective!=1) else " ")+"R Squared for Top "+ str(self.top_k) +" Variables ",yTitle="Incremental R2",xTitle="Estimators"))
		iplot(incremental_rsquare_df[['Features','percentage_incremental_r2']].iplot(asFigure=True,kind='pie',title="Percentage Relative Importance for Top "+ str(self.top_k) +" Variables ",values="percentage_incremental_r2",labels="Features"))

	def incremental_rsquare(self):
		# columns=list(self.data.columns.values)
		# columns.remove(self.target)

		## Calculating Incremental R2 for Top_K_Variables 
		print("Selecting %s Best Predictors for the Model" %self.top_k)
		columns=self.get_top_k()
		print("Selected Predictors : ",columns)
		print()

		print("Creating models for %s possible combinations of %s features :"%((2**len(columns))-1,len(columns)))
		model_rsquares=self.model_stats()

		print("#"*25," Model Training Done!!!!! ", "#"*25)
		print()
		print("#"*25," Calculating Variable Dominances ", "#"*25)

		variable_stats=self.variable_statistics(model_rsquares,columns)

		print("#"*25," Variable Dominance Calculation Done!!!!! ", "#"*25)
		print()

		incrimental_r2={}
		for col in columns:
		    l=[variable_stats[col]['individual_dominance'],variable_stats[col]['conditional_dominance']]
		    l.extend(variable_stats[col]['partial_dominance'])
		    incrimental_r2[col]=np.mean(l)
		    
		self.incrimental_r2=incrimental_r2
		self.percentage_incremental_r2={col:incrimental_r2[col]/np.sum(list(incrimental_r2.values())) for col in columns}
		
		return incrimental_r2

	def complete_model_rsquare(self):
		print("Selecting %s Best Predictors for the Model" %self.top_k)
		columns=self.get_top_k()
		print("Selected Predictors : ",columns)
		print()

		if(self.objective==1):
			print("*"*20," R-Squared of Complete Model : ","*"*20)
			lin_reg=LinearRegression()
			lin_reg.fit(self.data[columns],self.data[self.target])
			r_squared=lin_reg.score(self.data[columns],self.data[self.target])
			print("R Squared : %s" %(r_squared))
			print()
		else:
			print("*"*20," Pseudo R-Squared of Complete Model : ","*"*20)
			print()
			print("MacFadden's R-Squared : %s "%(self.McFadden_RSquare(columns)))
			print()
			print("Nagelkerke R-Squared : %s "%(self.Nagelkerke_Rsquare(columns)))
			print()
			print("Cox and Snell R-Squared : %s "%(self.Cox_and_Snell_Rsquare(columns)))
			print()
			print("Estrella R-Squared : %s "%(self.Estrella(columns)))
			print()



class Dominance_Datasets:
	"""docstring for Dominance_Datasets"""
	
	@classmethod
	def get_breast_cancer(cls):
		print("""The copy of UCI ML Breast Cancer Wisconsin (Diagnostic) dataset is downloaded from: https://goo.gl/U2Uwz2""")
		print("""Internally using load_breast_cancer function from sklearn.datasets """)
		breast_cancer_data=pd.DataFrame(data=load_breast_cancer()['data'],columns=load_breast_cancer()['feature_names'])
		breast_cancer_data['target']=load_breast_cancer()['target']
		target_dict=dict({j for i,j in zip(load_breast_cancer()['target_names'],enumerate(load_breast_cancer()['target_names']))})
		breast_cancer_data['target_names']=breast_cancer_data['target'].map(target_dict)
		return breast_cancer_data.iloc[:,:-1]
	
	@classmethod
	def get_boston(cls):
		print("""The copy of Boston Housing Dataset is downloaded from: https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html""")
		print("""Internally using load_boston function from sklearn.datasets """)
		boston_data=pd.DataFrame(data=load_boston()['data'],columns=load_boston()['feature_names'])
		boston_data['House_Price']=load_boston()['target']
		return boston_data

	def __init__(self):
		print("Datasets for Dominance Analysis")
		
