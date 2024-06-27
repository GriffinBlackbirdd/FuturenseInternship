
![Banner](https://qqeanlpfsgowrbzukhie.supabase.co/storage/v1/object/public/images/pandas.webp?t=2024-06-27T09%3A23%3A17.432Z)
# Pandas Data Manipulation Example

This repository contains a simple example of how to use the pandas library for data manipulation in Python. The code demonstrates creating pandas Series from lists and dictionaries, reading data from a CSV file, and performing various data operations such as grouping, filtering, and sorting.

## Overview of Pandas

Pandas is a powerful and flexible open-source data analysis and manipulation library for Python. It provides data structures and functions needed to manipulate structured data seamlessly. The primary data structures in pandas are `Series` and `DataFrame`.

- **Series**: A one-dimensional labeled array capable of holding any data type.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types.

Pandas is widely used in data science, machine learning, and data analysis due to its ease of use and integration with other libraries.

## Code Explanation

### Importing Pandas

```python
import pandas as p
```

### Creating a Series from a List

```python
data = [1214, 21435, 23144, 424124]
s = p.Series(data, index=["Amogh", "Arreyan", "Hemanth", "Surya"])
print("Series from list:")
print(s)
```

### Creating a Series from a Dictionary

```python
dict_data = {"Apple": 100, "Banana": 200, "Cherry": 300}
s_from_dict = p.Series(dict_data)
print("Series from dictionary:")
print(s_from_dict)
```

### Reading Data from a CSV File

```python
data = p.read_csv("data.csv")
data.info()
data.describe()
```

### Data Manipulation

#### Adding a New Column

```python
data['Pulse_Diff'] = data['Maxpulse'] - data['Pulse']
```

#### Grouping Data

```python
avg_calories = data.groupby('Duration')['Calories'].mean().reset_index()
```

#### Filtering Data

```python
high_calories = data[data['Calories'] > 400]
```

#### Sorting Data

```python
sorted_data = data.sort_values(by='Date')
```

### Displaying the Result

```python
avg_calories
```

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).