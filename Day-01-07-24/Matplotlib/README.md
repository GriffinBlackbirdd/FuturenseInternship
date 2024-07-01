![Banner](https://qqeanlpfsgowrbzukhie.supabase.co/storage/v1/object/public/images/tomAndJerry.webp)
# Matplotlib Visualization Examples

This repository contains a series of examples demonstrating how to use the Matplotlib library for data visualization in Python. The code includes various types of plots such as line plots, scatter plots, bar plots, histograms, pie charts, subplots, box plots, heatmaps, and annotations.

## Overview of Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in data science, machine learning, and data analysis for its flexibility and ease of use. Matplotlib integrates well with other libraries such as NumPy and pandas, making it a powerful tool for data visualization.

## Code Explanation

### Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

### Basic Line Plot

```python
# Example 1: Tom's Chase Speed
time = [1, 2, 3, 4, 5]  # in Seconds
speed = [2, 4, 6, 5, 7]  # in KMs

plt.plot(time, speed, label='Tom')
plt.title("Tom's Chase Speed Over Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Speed")
plt.legend()
plt.show()
```

### Basic Scatter Plot

```python
# Example 2: Jerry's Hiding Spots
hiding_spots = [1, 2, 3, 4, 5]
times_found = [1, 2, 2, 3, 4]

plt.scatter(hiding_spots, times_found, label='Jerry')
plt.title("Jerry's Hiding Spots vs Times Found by Tom")
plt.xlabel("Hiding Spot Number")
plt.ylabel("Times Found")
plt.legend()
plt.show()
```

### Basic Bar Plot

```python
# Example 3: Traps Set by Tom vs Jerry's Escapes
traps = ['Trap 1', 'Trap 2', 'Trap 3', 'Trap 4']
times_set = [5, 3, 4, 2]
times_escaped = [4, 3, 2, 2]

plt.bar(traps, times_set, label='Times Set', alpha=0.6)
plt.bar(traps, times_escaped, label='Times Escaped', alpha=0.6)
plt.title("Tom's Traps vs Jerry's Escapes")
plt.xlabel("Traps")
plt.ylabel("Counts")
plt.legend()
plt.show()
```

### Basic Histogram

```python
# Example 4: Hiding Durations
import numpy as np
durations = np.random.normal(loc=10, scale=2, size=100)  # Durations in minutes

plt.hist(durations, bins=15, alpha=0.7)
plt.title("Histogram of Jerry's Hiding Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()
```

### Basic Pie Chart

```python
# Example 5: Jerry's Hobbies
antics = ['Stealing Cheese', 'Setting Traps', 'Running Away', 'Taunting Tom']
counts = [15, 10, 20, 5]

plt.pie(counts, labels=antics, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Distribution of Jerry's Antics")
plt.show()
```

### Basic Subplots

```python
# Example 6: Tom and Jerry's Energy Levels
time = np.linspace(0, 10, 100)
tom_energy = np.sin(time) + np.random.normal(scale=0.1, size=time.shape)
jerry_energy = np.cos(time) + np.random.normal(scale=0.1, size=time.shape)

plt.subplot(2, 1, 1)
plt.plot(time, tom_energy, label='Tom', color='blue')
plt.title("Tom's Energy Level")
plt.xlabel("Time (minutes)")
plt.ylabel("Energy Level")

plt.subplot(2, 1, 2)
plt.plot(time, jerry_energy, label='Jerry', color='green')
plt.title("Jerry's Energy Level")
plt.xlabel("Time (minutes)")
plt.ylabel("Energy Level")

plt.tight_layout()
plt.show()
```

### Basic Box Plot

```python
# Example 7: Time Spent in Activities
activities = ['Chasing', 'Hiding', 'Eating', 'Sleeping']
tom_times = np.random.rand(10, 4) * 10
jerry_times = np.random.rand(10, 4) * 10

plt.boxplot([tom_times[:, i] for i in range(4)], labels=activities)
plt.title("Box Plot of Time Spent by Tom and Jerry")
plt.xlabel("Activities")
plt.ylabel("Time Spent (minutes)")
plt.show()
```

### Basic Heatmap

```python
# Example 8: Frequency of Hobbies
frequency = np.random.rand(7, 4)
plt.imshow(frequency, cmap='hot', interpolation='nearest')
plt.title("Heatmap of Hobbies Frequency Over a Week")
plt.xlabel("Hobbies")
plt.ylabel("Day of the Week")
plt.colorbar(label='Frequency')
plt.xticks(ticks=range(4), labels=antics)
plt.yticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()
```

### Basic Annotations

```python
# Example 9: Annotations on Tom's Speed
time = np.linspace(0, 10, 100)
tom_speed = np.sin(time) + np.random.normal(scale=0.1, size=time.shape)
escape_time = 5
escape_speed = np.sin(escape_time)

plt.plot(time, tom_speed, label='Tom')
plt.title("Tom's Speed with Escape Annotation")
plt.xlabel("Time (minutes)")
plt.ylabel("Speed")
plt.axvline(escape_time, color='r', linestyle='--', label='Jerry Escapes')
plt.annotate('Jerry Escapes', xy=(escape_time, escape_speed), xytext=(escape_time+1, escape_speed+0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.show()
```

### Customizing Plots

```python
# Example 10: Customizing Tom and Jerry's Chase Paths
time = np.linspace(0, 10, 100)
tom_path = np.sin(time) + np.random.normal(scale=0.1, size=time.shape)
jerry_path = np.cos(time) + np.random.normal(scale=0.1, size=time.shape)

plt.plot(time, tom_path, color='blue', linestyle='--', linewidth=2, marker='o', markerfacecolor='red', label='Tom')
plt.plot(time, jerry_path, color='green', linestyle='-', linewidth=2, marker='x', markerfacecolor='yellow', label='Jerry')
plt.title("Tom and Jerry's Chase Paths")
plt.xlabel("Time (minutes)")
plt.ylabel("Position")
plt.legend()
plt.show()
```

### Saving Figures

```python
# Example 11: Saving Figures
traps = ['Trap 1', 'Trap 2', 'Trap 3', 'Trap 4']
times_set = [5, 3, 4, 2]
plt.bar(traps, times_set, label='Times Set')
plt.title("Tom's Traps")
plt.xlabel("Traps")
plt.ylabel("Counts")
plt.legend()
plt.savefig('toms_traps.png')
plt.show()
```

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).
