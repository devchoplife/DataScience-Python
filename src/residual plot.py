import seaborn as sns 

#creating a residual olot 
sns.residplot(df['highway-mpg'], df['price'])#the fisr one is independend and the last one is the target 
#if hist is set to true, th number of bins must precede it 