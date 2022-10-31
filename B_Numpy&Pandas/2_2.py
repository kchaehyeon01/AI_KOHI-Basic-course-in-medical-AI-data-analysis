import pandas as pd

# 딕서너리 -> DataFrame 만들기 =============================================

population_dict = {'korea':5180,'japan':12718,'china':141500,'usa':32676}
gdp_dict = {'korea':16932000,'japan':51670000,'china':1409250000,'usa':2041280000,}
population = pd.Series(population_dict)
gdp = pd.Series(gdp_dict)

country = pd.DataFrame({
    'gdp':gdp,
    'population':population,
})

print("\n# country Series ====================\n")
print(country)

print("\n# country.index")
print(country.index)
print("\n# country.columns")
print(country.columns)

print("\n# country['gdp'], type(country['gdp']")
print(country['gdp'], "\n", type(country['gdp']))

# DataFrame의 연산자 활용 ===================================================
print("\n# 연산자 활용 ==========================\n")
gdp_per_capita = country['gdp']/country['population']
print("# gdp_per_capita, type(gdp_per_capita)")
print(gdp_per_capita, type(gdp_per_capita))

country['gdp per capita'] = gdp_per_capita

print("\n# country")
print(country)
print("\n# country.index")
print(country.index)
print("\n# country.columns")
print(country.columns)

# DataFrame 저장과 불러오기 =================================================
print("\n# DataFrame 저장과 불러오기 ==============\n")
country.to_csv("./country.csv") # comma separated values
country.to_excel("country.xlsx") # DataFrame 형태

country_load_csv = pd.read_csv("./country.csv")
country_load_xls = pd.read_excel("country.xlsx")

print(country_load_csv)
print(country_load_xls)