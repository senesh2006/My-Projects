import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")
my_filepath = "/kaggle/input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
my_data = pd.read_csv(my_filepath)
my_data.head()
# Preprocess for decade & alignment plot
my_data['YEAR'] = pd.to_numeric(my_data['YEAR'], errors='coerce')
my_data = my_data.dropna(subset=['YEAR'])
my_data['DECADE'] = (my_data['YEAR'] // 10) * 10

# Group by decade and alignment
my_data_grouped = my_data.groupby(['DECADE', 'ALIGN']).size().reset_index(name='count')

# Plot
plt.figure(figsize=(12, 7))
sns.barplot(data=my_data_grouped, x='DECADE', y='count', hue='ALIGN')
plt.title('DC Characters Introduced Per Decade by Alignment')
plt.xlabel('Decade')
plt.ylabel('Number of Characters')
plt.xticks(rotation=45)
plt.legend(title='Alignment')
plt.tight_layout()
plt.show()

# Group by decade and gender
gender_decade_data = my_data.groupby(['DECADE', 'SEX']).size().reset_index(name='count')

# Plot
plt.figure(figsize=(12, 7))
sns.lineplot(data=gender_decade_data, x='DECADE', y='count', hue='SEX', marker='o')
plt.title('Gender Representation of DC Characters Over Time')
plt.xlabel('Decade')
plt.ylabel('Number of Characters')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()


