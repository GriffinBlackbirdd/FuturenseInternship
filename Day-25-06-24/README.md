![Banner](https://qqeanlpfsgowrbzukhie.supabase.co/storage/v1/object/public/images/minionsNumpy.webp?t=2024-06-25T09%3A22%3A06.136Z)
# 🥳 Minion Army Adventures with NumPy

Welcome to the world of Gru and his minions! This script uses NumPy to perform various array operations while narrating a fun story about our minion army. Let's dive into the adventures of our minions as they steal the moon, organize parades, and more!

## 🚀 Getting Started

### Initialize the Minion Army
We start by initializing our minion army with specific XP points.

```python
import numpy as n

minionArmy = n.array([1, 2, 3, 4, 5, 6])
print("Our Minion Army: ", minionArmy)
```

### Stealing the Moon 🌕
Our minions successfully steal the moon and get rewarded with extra XP points.

```python
updatedXPs = minionArmy + 100
print("Our minion army: ", updatedXPs)
```

### Parade Formation 🎉
We arrange our minions into rows and columns for a parade.

```python
cadetMinions = n.array([[101, 102, 103], [104, 105, 106]])
print("The parade formation: ", cadetMinions, sep = "\n")
```

### Dealing with Traitors 😱
We identify and separate traitor minions.

```python
traitorMinions = cadetMinions[0, :]
print("Traitor Minions: ", traitorMinions)
```

### Assimilating XP Points
Loyal minions assimilate the XP points from traitors.

```python
loyalMinions = n.array([104, 105, 106])
traitorMinions = n.array([101, 102, 103])
newMinionArmy = loyalMinions + traitorMinions 
print("Our new minions army: ", newMinionArmy)
```

## 🛠️ Hands-On Practice

### Array Operations and Broadcasting
Perform element-wise operations using broadcasting.

```python
array3D = n.array([[[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
array2D = n.array([[1, 2, 3, 3.5], [5, 4, 6, 6.5], [7, 8, 9, 9.5]])
multiBroadcasting = array3D * array2D
print("Final Output: ", multiBroadcasting, sep = '\n')
```

### Indexing and Slicing
Extract specific elements from arrays.

```python
array3Dg = n.array([[[ 1,  2], [ 3,  4], [ 5,  6]], [[ 7,  8], [ 9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]], [[19, 20], [21, 22], [23, 24]]])
extractedElements = array3Dg[::2, ::2, :]
print("Extracted Elements: ", extractedElements, sep = '\n')
```

### Array Manipulation
Reshape and roll arrays.

```python
array2Dn = n.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]])
reshapedArray2Dn = array2Dn.reshape(2, 2, 6)
flattenedArray2Dn = reshapedArray2Dn.reshape(4, 6)
print("Flattened Array n and it's shape: ", flattenedArray2Dn, flattenedArray2Dn.shape, sep = "\n")
```

## 📚 Additional Functions

### Element-wise Operations
Perform addition, subtraction, multiplication, and division using broadcasting.

```python
def mainOperations(c, d):
    try:
        addition = c + d
        subtraction = c - d
        multiplication = c * d
        division = c / d
    except ValueError as e:
        print("Broadcasting not possible:", e)
```

### Replace with Mean
Replace specified values with the mean of neighboring elements.

```python
def replaceWithMean(p, x):
    rows, cols = p.shape
    mask = (p == x)
    paddedP = n.pad(p, pad_width=1, mode='constant', constant_values=0)
    sumNeighbors = (paddedP[1:-1, :-2] + paddedP[1:-1, 2:] + paddedP[:-2, 1:-1] + paddedP[2:, 1:-1])
    count = ((paddedP[1:-1, :-2] != 0).astype(int) + (paddedP[1:-1, 2:] != 0).astype(int) + (paddedP[:-2, 1:-1] != 0).astype(int) + (paddedP[2:, 1:-1] != 0).astype(int))
    meanNeighbors = n.divide(sumNeighbors, count, where=count != 0)
    result = p.copy()
    result[mask] = meanNeighbors[mask]
    return result
```
Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).
