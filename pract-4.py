import numpy as np
import pandas as pd
df=pd.DataFrame(np.array([[2,3,4],[5,6,7]]),
index=['tiger','lion'],columns=['one','two','three'])
print(df)
print(df.filter(items=['one','three']))
print(df.filter(regex='e$',axis=1))