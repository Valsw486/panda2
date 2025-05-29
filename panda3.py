import pandas as pd

# Загрузка CSV-файла в DataFrame

df = pd.read_csv('World-happiness-report-2024 (1).csv')


# Вывод первы х 5 строк данных
print("Первые 5строк данных:")
print(df.head())

print(df.info())

print(df.describe())


