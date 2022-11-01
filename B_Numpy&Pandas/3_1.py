import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5,2), columns=["A","B"])
print(df)

# masking 연산
print("\n# masking 연산")
print(df["A"]<0.5)

# DataFrame row 추출
print("\n# DataFrame row 추출")
print(df[(df["A"]<0.5)&(df["B"]>0.3)])
print(df.query("A < 0.5 and B > 0.3"))