#ANOVA between Honda and Subaru 

df_anova= df[["make", "price"]]#this code is for the analysis of variance
grouped_anova = df_anova.groupby(["make"])#group the make to prepare it for analysis 

#.f_oneway is a Scipy function used for the purpose of analysis of variance
anova_results = stats.f_oneway(grouped_anova.get_group ["honda"]["price"], grouped_anova.get_group ["subaru"]["price"])
#this performs the analysis of variance between the subsets honda and subaru 
