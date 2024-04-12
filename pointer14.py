import seaborn as sns
import pandas as pd

df = pdf.read_csv('data.csv') # load data
sns.heatmap(df, annot=True) # visualization 
plt.show # output
