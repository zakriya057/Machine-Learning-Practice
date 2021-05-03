import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial import distance


df=pd.read_csv("Mall_Customers.csv")
#preprocessing the data
df.drop('CustomerID',axis=1,inplace=True)
enc=LabelEncoder()
df['Gender']=enc.fit_transform(df['Gender'])
#scaling
scale=StandardScaler()
dfs=pd.DataFrame(scale.fit_transform(df),columns=df.columns)

kmns=KMeans(n_clusters=5,n_init=10).fit(dfs)#5 clusters and 10 iterations choose the best one
clusters=kmns.predict(dfs)
centers=kmns.cluster_centers_

print("Clusters appointed to Each index updated dataframe =::")
dfs['Cluster_num']=clusters
print(dfs)

# to predict a new point to see which cluster it belong
topredict=np.array([1.1,-1.0,1.3,-0.5])
m=4
cluster_no=4
for i,x in enumerate(centers):
	dst=distance.euclidean(topredict,i)
	if m>dst:
		cluster_no=i
print("New point belongs to cluster{}",cluster_no)

