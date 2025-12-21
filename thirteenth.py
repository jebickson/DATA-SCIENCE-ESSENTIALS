import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display first 10 rows
print(df.head(10))

# Overall statistics
print("Overall statistics:")
print(df.describe())

# Group by species and calculate mean
species_mean = df.groupby('species').mean()
print("\nMean of features for each species:")
print(species_mean)

# Group by species and calculate median
species_median = df.groupby('species').median()
print("\nMedian of features for each species:")
print(species_median)

# Multiple aggregations: mean, std, min, max
species_stats = df.groupby('species').agg(['mean', 'std', 'min', 'max'])
print("\nDetailed statistics for each species:")
print(species_stats)

# Plot mean petal length by species
species_mean['petal length (cm)'].plot(kind='bar')
plt.title('Mean Petal Length by Species')
plt.ylabel('Petal Length (cm)')
plt.show()

