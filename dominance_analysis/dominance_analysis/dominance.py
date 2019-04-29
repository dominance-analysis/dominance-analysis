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
import random

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models.formatters import NumeralTickFormatter
output_notebook()
init_notebook_mode(connected=True)


class Dominance:
	"""docstring for ClassName"""
	def __init__(self,data,target,top_k=None,objective=1,pseudo_r2='mcfadden',data_format = 0): # Bala changes
		# super(ClassName, self).__init__()
		self.data = data
		self.target=target
		self.objective=objective
#Bala changes start        
		self.data_format = data_format
		if(self.data_format==0):
#Bala changes end            
			if(self.objective==0):
				self.data['intercept']=1
			self.top_k=top_k if top_k else min((len(self.data.columns)-1),15)
			self.pseudo_r2=pseudo_r2
			assert (self.top_k >1 ) and (self.top_k<(len(self.data.columns))),"Value of top_k ranges from 1 to n-1 !"
		self.complete_model_rsquare()

            

	
	def conditional_dominance(self,model_rsquares,model_features_k,model_features_k_minus_1,columns):
		# print("#"*25," Calculating Conditional Dominance ","#"*25)
		total_model_r2=model_rsquares[" ".join(model_features_k[0])]
		
		interactional_comp_dom={}
		for i in model_features_k_minus_1:
			interactional_comp_dom[" ".join(set(model_features_k[0])-set(i))]={" ".join(set(i)):total_model_r2-model_rsquares[" ".join(i)]}
		# print("Interactional Dominance",interactional_comp_dom)

		interactional_dominance=dict({(" ".join(set(model_features_k[0])-set(i)),total_model_r2-model_rsquares[" ".join(i)]) for i in model_features_k_minus_1})
		return (interactional_dominance,interactional_comp_dom)

	def individual_dominance(self,model_rsquares,model_features,columns):
		# print("#"*25," Calculating individual Dominance ","#"*25)
		return dict({(" ".join(col),model_rsquares[" ".join(col)]) for col in model_features })

	def partial_dominance(self,model_rsquares,model_features_k,model_features_k_minus_1,columns):
		# print(columns)
		pd={col: [] for col in columns}
		[pd[" ".join(set(i)-set(j))].append(model_rsquares[" ".join(i)]-model_rsquares[" ".join(j)]) for i in model_features_k for j in model_features_k_minus_1 if(len(set(i)-set(j))==1)]

		pd_comp_dom={col: {} for col in columns}

		for i in model_features_k:
			for j in model_features_k_minus_1:
				if(len(set(i)-set(j))==1):
					pd_comp_dom[" ".join(set(i)-set(j))].update({
					" ".join(j):model_rsquares[" ".join(i)]-model_rsquares[" ".join(j)]
					})

		# [pd_comp_dom[" ".join(set(i)-set(j))].append({" ".join(j):model_rsquares[" ".join(i)]-model_rsquares[" ".join(j)]}) for i in model_features_k for j in model_features_k_minus_1 if(len(set(i)-set(j))==1)]
		# print(" Partial Dominance ",pd_comp_dom)

		return (pd,pd_comp_dom)

	def model_features_combination(self,columns):
		return [list(combinations(columns,i)) for i in range(1,len(columns)+1)]

	def McFadden_RSquare(self,columns):
		cols=columns.copy()
		cols.append('intercept')
		# print("model columns :",cols)
		log_clf=sm.Logit(self.data[self.target],self.data[cols])
		# result=log_clf.fit(disp=0,method='powell')
		try:
			result=log_clf.fit(disp=0)
		except:
			result=log_clf.fit(disp=0,method='powell')
		mcfadden_rsquare=result.prsquared
		return mcfadden_rsquare

	def Nagelkerke_Rsquare(self,columns):
		cols=columns.copy()
		cols.append('intercept')
		log_clf=sm.Logit(self.data[self.target],self.data[cols])
		N=self.data.shape[0]
		# result=log_clf.fit(disp=0,method='powell')
		try:
			result=log_clf.fit(disp=0)
		except:
			result=log_clf.fit(disp=0,method='powell')
		llf=result.llf
		llnull=result.llnull
		lm=np.exp(llf)
		lnull=np.exp(llnull)
		naglkerke_rsquare=(1-(lnull/lm)**(2/N))/(1-lnull**(2/N))
		return naglkerke_rsquare

	def Cox_and_Snell_Rsquare(self,columns):
		cols=columns.copy()
		cols.append('intercept')
		log_clf=sm.Logit(self.data[self.target],self.data[cols])
		N=self.data.shape[0]
		# result=log_clf.fit(disp=0,method='powell')
		try:
			result=log_clf.fit(disp=0)
		except:
			result=log_clf.fit(disp=0,method='powell')
		llf=result.llf
		llnull=result.llnull
		lm=np.exp(llf)
		lnull=np.exp(llnull)
		cox_and_snell_rsquare=(1-(lnull/lm)**(2/N))
		return cox_and_snell_rsquare

	def Estrella(self,columns):
		cols=columns.copy()
		cols.append('intercept')
		log_clf=sm.Logit(self.data[self.target],self.data[cols])
		N=self.data.shape[0]
		# result=log_clf.fit(disp=0,method='powell')
		try:
			result=log_clf.fit(disp=0)
		except:
			result=log_clf.fit(disp=0,method='powell')
		llf=result.llf
		llnull=result.llnull
		estrella_rsquare=1-((llf/llnull)**(-(2/N)*llnull))
		return estrella_rsquare

	def Adjusted_McFadden_RSquare(self,columns):
		log_clf=sm.Logit(self.data[self.target],self.data[cols])
		# result=log_clf.fit(disp=0,method='powell')
		try:
			result=log_clf.fit(disp=0)
		except:
			result=log_clf.fit(disp=0,method='powell')
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
		complete_dominance_stats={}
		# print(columns)
		model_combinations=self.model_features_combination(columns)
		for k in tqdm(range(len(columns),1,-1)):
		    model_features_k=[i for j in model_combinations for i in j if len(i)==k]
		    model_features_k_minus_1=[i for j in model_combinations for i in j if len(i)==k-1]
		    if(k==len(columns)):
		        stats['conditional_dominance'],complete_dominance_stats['interactional_dominance']=self.conditional_dominance(model_rsquares,model_features_k,model_features_k_minus_1,columns)
		    else:
		    	stats['partial_dominance_'+str(k)],complete_dominance_stats['partial_dominance_'+str(k)]=self.partial_dominance(model_rsquares,model_features_k,model_features_k_minus_1,columns)

		    if(k==2):
		        stats['individual_dominance']=self.individual_dominance(model_rsquares,model_features_k_minus_1,columns)
		        complete_dominance_stats['individual_dominance']=stats['individual_dominance']

		variable_stats={}
		for col in columns:
		    variable_stats[col]={
		            'conditional_dominance':stats['conditional_dominance'][col],
		            'individual_dominance':stats['individual_dominance'][col],
		            'partial_dominance':[np.mean(stats["partial_dominance_"+str(i)][col]) for i in range(len(columns)-1,1,-1)]
		    }

		self.stats=stats
		self.complete_dominance_stats=complete_dominance_stats
		self.variable_stats=variable_stats
		return self.variable_stats

	def dominance_stats(self):
		tf=pd.DataFrame(self.variable_stats).T
		tf['Interactional Dominance']=tf['conditional_dominance']
		tf['Average Partial Dominance']=tf['partial_dominance'].apply(lambda x:np.mean(x))
		tf['partial_dominance_count']=tf['partial_dominance'].apply(lambda x:len(x))
		tf['Total Dominance']=(tf['partial_dominance_count']*tf['Average Partial Dominance']+tf['conditional_dominance']+tf['individual_dominance'])/(tf['partial_dominance_count']+2)
		tf['Percentage Relative Importance']=(tf['Total Dominance']*100)/tf['Total Dominance'].sum()
		tf=tf[['Interactional Dominance','individual_dominance','Average Partial Dominance','Total Dominance','Percentage Relative Importance']].sort_values("Total Dominance",ascending=False)
		tf.rename(columns={"individual_dominance":"Individual Dominance"},inplace=True)
		return tf



	def get_top_k(self):
		columns=list(self.data.columns.values)
		columns.remove(self.target)
		# remove intercept from top_k
		if(self.objective):
			top_k_vars=SelectKBest(f_regression, k=self.top_k)
		else:
			columns.remove('intercept')
			top_k_vars=SelectKBest(chi2, k=self.top_k)
		top_k_vars.fit_transform(self.data[columns], self.data[self.target])
		return [columns[i] for i in top_k_vars.get_support(indices=True)]

	def plot_waterfall_relative_importance(self,incremental_rsquare_df):
		index = list(incremental_rsquare_df['Features'].values)
		data = {'Percentage Relative Importance': list(incremental_rsquare_df['percentage_incremental_r2'].values)}
		df = pd.DataFrame(data=data,index=index)
		
		net = df['Percentage Relative Importance'].sum()
		# print("Net ",net)

		df['running_total'] = df['Percentage Relative Importance'].cumsum()
		df['y_start'] = df['running_total'] - df['Percentage Relative Importance']

		df['label_pos'] = df['running_total']

		df_net = pd.DataFrame.from_records([(net, net, 0, net)],
			columns=['Percentage Relative Importance', 'running_total', 'y_start', 'label_pos'],index=["net"])
		
		df = df.append(df_net)

		df['color'] = '#1de9b6'
		df.loc[df['Percentage Relative Importance'] == 100, 'color'] = '#29b6f6'
		df.loc[df['Percentage Relative Importance'] < 0, 'label_pos'] = df.label_pos - 10000
		df["bar_label"] = df["Percentage Relative Importance"].map('{:,.1f}'.format)

		TOOLS = "reset,save"
		source = ColumnDataSource(df)
		p = figure(tools=TOOLS, x_range=list(df.index), y_range=(0, net+10),
			plot_width=1000, title = "Percentage Relative Importance Waterfall")

		p.segment(x0='index', y0='y_start', x1="index", y1='running_total',
			source=source, color="color", line_width=35)

		p.grid.grid_line_alpha=0.4
		p.yaxis[0].formatter = NumeralTickFormatter(format="(0 a)")
		p.xaxis.axis_label = "Predictors"
		p.yaxis.axis_label = "Percentage Relative Importance(%)"
		p.xaxis.axis_label_text_font_size='12pt'
		p.yaxis.axis_label_text_font_size='12pt'

		labels = LabelSet(x='index', y='label_pos', text='bar_label',
		text_font_size="11pt", level='glyph',
		x_offset=-14, y_offset=0, source=source)
		p.add_layout(labels)
		p.xaxis.major_label_orientation = -math.pi/4
		show(p)

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
#Bala changes start        
		if(self.data_format==0):
			iplot(incremental_rsquare_df[['Features','incremental_r2']].set_index("Features").iplot(asFigure=True,kind='bar',title="Incremetal "+("Pseudo " if (self.objective!=1) else " ")+"R Squared for Top "+ str(self.top_k) +" Variables ",yTitle="Incremental R2",xTitle="Estimators"))
			iplot(incremental_rsquare_df[['Features','percentage_incremental_r2']].iplot(asFigure=True,kind='pie',title="Percentage Relative Importance for Top "+ str(self.top_k) +" Variables ",values="percentage_incremental_r2",labels="Features"))
		else:
			iplot(incremental_rsquare_df[['Features','incremental_r2']].set_index("Features").iplot(asFigure=True,kind='bar',title="Incremetal "+("Pseudo " if (self.objective!=1) else " ")+"R Squared of " +" Variables ",yTitle="Incremental R2",xTitle="Estimators"))
			iplot(incremental_rsquare_df[['Features','percentage_incremental_r2']].iplot(asFigure=True,kind='pie',title="Percentage Relative Importance of " +" Variables ",values="percentage_incremental_r2",labels="Features"))
#Bala changes end#Bala changes end
		self.plot_waterfall_relative_importance(incremental_rsquare_df[['Features','percentage_incremental_r2']])

	def predict_general_dominance(self):
		general_dominance=[]
		l=list(self.dominance_stats().index)
		for index,i in enumerate(l):
			general_dominance.append({"Predictors":i,"Dominating":l[index+1:]})

		return pd.DataFrame(general_dominance)[['Predictors','Dominating']]

	def predict_conditional_dominance(self):
		
		general_dominance=[]
		l=list(self.dominance_stats().index)
		for index,i in enumerate(l):
			general_dominance.append({"Predictors":i,"Dominating":l[index+1:]})

		conditinal_dominance=[]    
		for x in general_dominance:
			predictor=x['Predictors']
			cd=True
			if(len(x['Dominating'])>0):
				for j in x['Dominating']:
					if((self.variable_stats[predictor]['individual_dominance']<self.variable_stats[j]['individual_dominance']) or (self.variable_stats[predictor]['conditional_dominance']<self.variable_stats[j]['conditional_dominance'])):
						cd=False
						break

					if(cd):
						for index,i in enumerate(self.variable_stats[predictor]['partial_dominance']):
							if(i<self.variable_stats[j]['partial_dominance'][index]):
								cd=False
								break
			else:
				cd=False

			if(cd):
				conditinal_dominance.append({"Predictors":predictor,"Conditional Dominance":True,"Dominating":x['Dominating']})
			else:
				conditinal_dominance.append({"Predictors":predictor,"Conditional Dominance":False,"Dominating":None})
		    
		return pd.DataFrame(conditinal_dominance)[['Predictors','Conditional Dominance','Dominating']]

	def predict_complete_dominance(self):
		conditional_dominance_df=self.predict_conditional_dominance()
		conditional_dominant_predictors=list(conditional_dominance_df[conditional_dominance_df['Conditional Dominance']==True]['Predictors'].values)
		predictors=list(conditional_dominance_df['Predictors'].values)

		# print(conditional_dominant_predictors,predictors)

		cd_df=[]

		cds=self.complete_dominance_stats
		# print(conditional_dominant_predictors)

		for i in conditional_dominant_predictors:
			# print(i,conditional_dominance_df)
			dominating=conditional_dominance_df[conditional_dominance_df['Predictors']==i]['Dominating'].values[0]
			complete_dominance=True
			for j in [p for p in list(cds.keys()) if p !='interactional_dominance']:
				if(j=='individual_dominance'):
					if(sum(cds[j][i]>[cds[j][key] for key in dominating])!=len(dominating)):
						complete_dominance=False
						break
				else:
					search_index=[]
					for k in dominating:
						if(complete_dominance):
							for key in cds[j][i].keys():
								l=list(set(predictors)-set(key.split(" "))-set([i]))
								[search_index.append((i,key,c)) for c in l]
					
					search_index=list(set(search_index))
					
					if(complete_dominance):
						for search in search_index:
							# print(search[0],search[1],search[2],cds[j][search[0]][search[1]],cds[j][search[2]][search[1]])
							if(cds[j][search[0]][search[1]]<cds[j][search[2]][search[1]]):
								complete_dominance=False
								break

			cd_df.append({"Predictors":i,"Dominating":dominating})
		    
		return pd.DataFrame(cd_df)[['Predictors','Dominating']]

	def dominance_level(self):
		gen_dom=self.predict_general_dominance()
		condition_dom=self.predict_conditional_dominance()
		comp_dom=self.predict_complete_dominance()

		gen_dom.rename(columns={'Dominating':'Generally Dominating'},inplace=True)
		condition_dom.drop('Conditional Dominance',inplace=True,axis=1)
		condition_dom.rename(columns={'Dominating':'Conditionally Dominating'},inplace=True)
		comp_dom.rename(columns={'Dominating':'Completelly Dominating'},inplace=True)

		return pd.merge(pd.merge(left=gen_dom,right=condition_dom[['Predictors','Conditionally Dominating']],how='left'),comp_dom,how='left').fillna("")

	def incremental_rsquare(self):
		# columns=list(self.data.columns.values)
		# columns.remove(self.target)

		## Calculating Incremental R2 for Top_K_Variables 
		if(self.data_format==0): #Bala changes
			print("Selecting %s Best Predictors for the Model" %self.top_k)
			columns=self.get_top_k()
			print("Selected Predictors : ",columns)
			print()
			print("Creating models for %s possible combinations of %s features :"%((2**len(columns))-1,len(columns)))
			model_rsquares=self.model_stats()
#Bala changes starts
		else:
			if(self.data_format == 2):
				columns = list(self.data.columns.values)
				d = np.sqrt(self.data.values.diagonal())   
				corr_array = ((self.data.values.T/d).T)/d
				self.data = pd.DataFrame(data=corr_array,index=columns)
				self.data.columns = columns
			model_rsquares=self.Dominance_correlation()
			columns=list(self.data.columns.values)
			columns.remove(self.target)
#Bala changes ends
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
		if(self.data_format==0): #Bala changes
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
				
				if(self.pseudo_r2=='mcfadden'):
					print("MacFadden's R-Squared : %s "%(self.McFadden_RSquare(columns)))
				elif(pseudo_r2=='nagelkerke'):
					print("Nagelkerke R-Squared : %s "%(self.Nagelkerke_Rsquare(columns)))
				elif(pseudo_r2=='cox_and_snell'):
					print("Cox and Snell R-Squared : %s "%(self.Cox_and_Snell_Rsquare(columns)))
				else:
					print("Estrella R-Squared : %s "%(self.Estrella(columns)))
				print()
#Bala changes start
		else:
			if(self.data_format == 2):
				columns = list(self.data.columns.values)
				d = np.sqrt(self.data.values.diagonal())   
				corr_array = ((self.data.values.T/d).T)/d
				self.data = pd.DataFrame(data=corr_array,index=columns)
				self.data.columns = columns
				print()
			columns=list(self.data.columns.values)
			columns.remove(self.target)
			corr_all_matrix=self.data.loc[columns,[self.target]]
			corr_pred_matrix = self.data.loc[columns,columns]
			corr_pred_matrix_inverse = pd.DataFrame(np.linalg.pinv(corr_pred_matrix.values), corr_pred_matrix.columns, corr_pred_matrix.index)
			beta = corr_pred_matrix_inverse.dot(corr_all_matrix)
			corr_all_matrix_transpose = corr_all_matrix.transpose()
			r_squared = corr_all_matrix_transpose.dot(beta)
			print("R Squared : %s" %(r_squared.iloc[0,0]))
			print()
#Bala changes ends

#Bala changes starts
	def Dominance_correlation(self):
    ## Calculating Incremental R2 from Correlation Matrix
		columns=list(self.data.columns.values)
		columns.remove(self.target)
		print("Predictors : ",columns)
		print()

		print("Calculating R2 for %s possible combinations of %s features :"%((2**len(columns))-1,len(columns)))
		model_combinations=self.model_features_combination(columns)
		model_rsquares={}
		for i in tqdm(model_combinations):
			for j in i:
				model_combinations = list(j)
				corr_all_matrix = self.data.loc[model_combinations,[self.target]]
				corr_pred_matrix = self.data.loc[model_combinations,model_combinations]
				corr_pred_matrix_inverse = pd.DataFrame(np.linalg.pinv(corr_pred_matrix.values), corr_pred_matrix.columns, corr_pred_matrix.index)
				beta = corr_pred_matrix_inverse.dot(corr_all_matrix)
				corr_all_matrix_transpose = corr_all_matrix.transpose()
				r_square = corr_all_matrix_transpose.dot(beta)
				model_rsquares[" ".join(model_combinations)]=r_square.iloc[0,0]
		self.model_rsquares=model_rsquares
		return self.model_rsquares
#Bala changes ends

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
		

