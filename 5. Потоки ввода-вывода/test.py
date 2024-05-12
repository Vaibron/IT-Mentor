import pandas as pd

# Создание DataFrame из словаря
data = {
  'Name': ['John', 'Anna', 'Peter', 'Linda'],
  'Age': [28, 22, 34, 42],
  'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

print(df)