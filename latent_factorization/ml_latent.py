import CF_model, math
import numpy as np
import pandas as pd

components = 50

dataset = "ml-20m/ratings.csv"

df=pd.read_csv(dataset)
df=df[:100000]
X=df[['userId', 'movieId', 'rating']].as_matrix()
n_users=len(df['userId'].unique())
n_items=len(df['movieId'].unique())

media_to_id=dict(zip(sorted(df.movieId.unique()), range(n_items)))
del df
print("For dataset number of users %d and songs %d"%(n_users,n_items))
np.random.shuffle(X)
size=X.shape[0]
X_train=X[:int(size*0.7)]
X_test=X[int(size*0.7):]
del X
cf = CF_model.CFModel(n_items=n_items, n_users=n_users, n_components=components, media_to_id=media_to_id)
Rui_tr = cf.createMap(X_train)
Rui_te = cf.createMap(X_test)
print ("Started Training...")
cf.run(Rui_tr)
temp = cf.eval_MAE(Rui_te)
print("Round MAE = %f"%(temp))
temp = cf.eval_RMSE(Rui_te)
print("Round RMSE = %f"%(temp))