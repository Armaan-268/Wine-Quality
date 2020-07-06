import numpy as np
import pandas as pd
data = pd.read_csv('dataset.csv')
q = data.iloc[:,-1].values
remark = []
for i in q:
    if i>=6:
        remark.append(1)
    else:
        remark.append(0)

data["remark"] = remark
data.to_csv("new_dataset.csv", index=False)