import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
import random
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создать пустой DataFrame для One-Hot представления
one_hot_data = pd.DataFrame()

# Получить уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Для каждого уникального значения создать новый столбец в One-Hot представлении
for value in unique_values:
    # Создать новый столбец с названием, соответствующим уникальному значению
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

# В one_hot_data каждый столбец будет соответствовать одному уникальному значению
one_hot_data.head()
print(one_hot_data)