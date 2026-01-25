import sys
import os

# This line allows us to reference directories outside of the current directory.
sys.path.insert(0, os.path.abspath('..'))

# This line is the actual reference to the load_iris_data() function from the fethch_data.py file.
from data.fetch_data import load_iris_data
import matplotlib.pyplot as plt
import seaborn as sns

df, target_name = load_iris_data()

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal length',
    y='petal length',
    hue=target_name,
    style=target_name,
    s=90
)

plt.title('Iris Species: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Iris Species')
plt.grid(True)
plt.savefig('plots/sepal_length_v_petal_length.png', dpi=150)
plt.close()