import pandas as pd
import numpy as np

population_dict = {'china':141500,'japan':12718,'korea':5180,'usa':32676}
gdp_dict = {'korea':16932000,'japan':51670000,'china':1409250000,'usa':2041280000,}
population = pd.Series(population_dict)
gdp = pd.Series(gdp_dict)
country = pd.DataFrame({
    'gdp':gdp,
    'population':population,
    'gdp per capita':gdp/population
})

# .loc
print("\n# .loc")
print(country.loc['china'])
print(country.loc['japan':'korea', :'population'])

# .iloc
print("\n# .iloc")
print(country.iloc[0])
print(country.iloc[1:3,:2])




# DataFrame 새 데이터 추가/수정
dataframe = pd.DataFrame(columns=['이름','나이','주소'])
# print(dataframe)

dataframe.loc[0] = ['임원균', '26', '서울'] # 여기서 iloc은 X : IndexError: iloc cannot enlarge its target object
# print(dataframe)

dataframe.loc[1] = {'이름':'철수', '나이':'25','주소':'인천'}
# print(dataframe)

dataframe.loc[1,'이름'] = '영희'
# print(dataframe)

# 새 컬럼 추가
dataframe['전화번호'] = np.nan
# print(dataframe)

dataframe.loc[0, '전화번호'] = '01012341234'
# print(dataframe)

print("len(dataframe) :", len(dataframe)) # 2

# 누락된 데이터 체크
# print(dataframe.dropna())
# print(dataframe)

dataframe['전화번호'] = dataframe['전화번호'].fillna('전화번호 없음')
# print(dataframe)

# Series 연산
A = pd.Series([2,4,6], index=[0,1,2])
B = pd.Series([1,3,5], index=[1,2,3])
print(A+B)
print(A.add(B, fill_value=0))

# DataFrame 연산
A = pd.DataFrame(np.random.randint(0,10,(2,2)), columns=list("AB"))
B = pd.DataFrame(np.random.randint(0,10,(3,3)), columns=list("BAC"))
print(A)
print(B)
print(A+B)
print(A.add(B,fill_value=0))

# 집계 함수
data = {
	'A':[i+5 for i in range(3)],
	'B':[i**2 for i in range(3)]
}
df = pd.DataFrame(data)
print(df['A'].sum()) # 18
print(df.sum())
print(df.mean())