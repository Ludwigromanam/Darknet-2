import numpy as np
import pandas as pd

# Change the path to annotation file here

annotations=pd.read_csv('home/rohan/Downloads/Training/00000/GT-00000.csv',delimiter=';')
annotations=annotations.drop(['Width','Height'],axis=1)

for x in annotations.iterrows():
    df=pd.DataFrame([[x[1][5],np.nan,np.nan,np.nan],[x[1][1],x[1][2],x[1][3],x[1][4]]])
    df.to_csv(str(x[1][0])+".txt",sep=' ',index=False,header=False)
