import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

# Example
series = Series([1, 1, 2, 3, 5, 8, 13])
print(series) #represent a series

# Alphabetize the index
series_i = Series(
    [1, 1, 2, 3, 5, 8, 13],
    index=['a', 'b', 'c', 'd', 'e', 'f','g']
)

print(series_i)

#DataFrame Object
data = {
    'ID':['100', '101', '102', '103', '104'],
    'City':['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'Birth_year':[1990, 1989, 1992, 1997, 1982],
    'Name':['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steve']
}

df = DataFrame(data) #represents the column organized in DataFrame
print(df)

df_i = DataFrame(data, index=['a', 'b', 'c', 'd', 'e']) #personalizate index
print(df_i)

print('Element:', df_i.values)
print('Index:', df_i.index)
print('Column:', df_i.columns)