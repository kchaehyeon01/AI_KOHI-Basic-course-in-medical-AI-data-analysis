import pandas as pd

# Series
data = pd.Series([1,2,3,4])
print(data)

# 인덱스로 접근 가능
data = pd.Series([1,2,3,4], index=['a','b','c','d'], name="Title")
print(data)
print(data['b'])

# 딕셔너리로 변환 가능
print("\n===== 딕셔너리로 변환 ========================\n")
population_dict = {
    'korea':5180,
    'japan':12718,
    'china':141500,
    'usa':32676
}
population = pd.Series(population_dict, name="population")
print("[[population]]==============\n", population)
print("[[popluation.index]]========\n", population.index, "\n", type(population.index))
print("[[population.values]]=======\n", population.values, "\n", type(population.values))
