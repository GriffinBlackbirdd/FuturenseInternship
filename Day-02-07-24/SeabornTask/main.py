'''
I have a picked up a dataset about transformers and LSTM from https://github.com/mwaskom/seaborn-data/tree/master, the dataset is labelled as 'glue.csv'
@author: Arreyan Hamid
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
FOLDER_PATH = "E:\\futurense\\FuturenseInternship\\Day-02-07-24\\SeabornTask"
dataPath = os.path.join(FOLDER_PATH, "transformers.csv")
data = pd.read_csv(dataPath)

print(data.head(10))

# MAKING A DISTPLOT
# This plot helps in understanding the overall distribution and central tendency of the Score values.
plt.figure(figsize=(10, 6))
sns.histplot(data['Score'], kde=True)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# MAKING A BOX PLOT
# This plot helps in comparing the distribution of scores across different tasks.
plt.figure(figsize=(10, 6))
sns.boxplot(x='Task', y='Score', data=data)
plt.title('Scores by Task')
plt.xlabel('Task')
plt.ylabel('Score')
plt.show()

# MAKING A BAR PLOT
# This plot helps in identifying which models perform better on average.
plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y='Score', data=data)
plt.title('Average Score by Model')
plt.xlabel('Model')
plt.ylabel('Average Score')
plt.xticks(rotation=90)
plt.show()

# MAKING A POINT PLOT
# This plot helps in visualizing how scores have changed over time for different tasks.
plt.figure(figsize=(10, 6))
sns.pointplot(x='Year', y='Score', hue='Task', data=data)
plt.title('Score Trend Over Years by Task')
plt.xlabel('Year')
plt.ylabel('Score')
plt.show()

# MAKING A HEATMAP
# This plot helps in understanding the relationships between different numerical variables in the dataset.
plt.figure(figsize=(10, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# MAKING A PAIR PLOT
# THis visualizes the relationships between pairs of numerical variables.
numeric_data = data[['Year', 'Score']]
sns.pairplot(numeric_data)
plt.show()
