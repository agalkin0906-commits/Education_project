import pandas as pd
import numpy as np

destinations = ['Склад-П1', 'Склад-П2', 'Склад-П3']
data = []

for dest in destinations:
    for i in range(30):
        base_t = 30 if dest == 'Склад-П1' else 60 if dest == 'Склад-П2' else 45
        varied_time = base_t + np.random.randint(-5, 10)
        delay = np.random.randint(0, 20) if np.random.random() > 0.5 else 0
        data.append([dest, varied_time, delay])

df_input = pd.DataFrame(data, columns=['маршрут', 'час', 'затримка'])
df_input.to_csv('logistic_history.csv', index=False, encoding='utf-8-sig')

print("CSV-файл 'logistic_history.csv' створено. Кількість рядків:", len(df_input))
print(df_input.head(100))
