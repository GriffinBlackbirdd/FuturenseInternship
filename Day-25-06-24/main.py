import numpy as n

# Let us imagine ourselves as Gru from Despicable Me series, and we have a minion army standed and ready for all of our tasks.
# Let's initialize our minion army, each minion has a specific tag to their name much like how footballers have a jersey numbers, and here each tag of the minions displays there XP points.

minionArmy = n.array([1, 2, 3, 4, 5, 6])
print("Our Minion Army: ", minionArmy)


# Hurry Up! We have to assemble our minion army to steal the moon 🌕
# Some time passes...

# We have stolen the Moon! Yay, let us grant some extra 100 XPs to all our minions.
updatedXPs = minionArmy + 100
print("Our minion army: ", updatedXPs)
print(updatedXPs.shape)

# Now, to celebrate we are also organising a marching parade to honor our great leader Gru - You.
# In order to do that, we will have to arrange our minions into rows and columns.
cadetMinions = n.array([[101, 102, 103], [104, 105, 106]])
print("The parade formation: ", cadetMinions, sep = "\n")
print(cadetMinions.shape)

# Oh no! We just got an insider report, the most esteemed minions who form the first row in our parade, they are traitors! They tried to steal the Moon for themselves and sell it somewhere else for money.
# We must teach them a lesson, let us separate them out firstly.
traitorMinions = cadetMinions[0, :]
print("Traitor Minions: ", traitorMinions)

# We will assimilate the XPs from the traitor minions into our loyal minions.
loyalMinions = n.array([104, 105, 106])
traitorMinions = n.array([101, 102, 103])

newMinionArmy = loyalMinions + traitorMinions 
print("Our new minions army: ", newMinionArmy)

# We have some construction work for our EvilLair, let us assign some minions for the task,
workerMinions = n.array([[1, 2, 3], 
                         [4, 5, 6], 
                         [7, 8, 9]])
rows = n.array([0, 2])
cols = n.array([1, 2])
print("Selected Minions:", workerMinions[rows, cols])

# Reshaping our worker minions.
minions_flat = n.array([1, 2, 3, 4, 5, 6])  
minions_grid = minions_flat.reshape(2, 3)
print("Reshaped Minions:\n", minions_grid)

minions_flat = minions_grid.ravel()
print("Flattened Minions:", minions_flat)

# HANDS ON PRACTICE:
# Array Operations and Broadcasting:
# 1. Given a 3D array a with shape (2, 3, 4) and a 2D array b with shape (3, 4), perform element-wise multiplication between a and b using broadcasting.

array3D = n.array([[[ 1,  2,  3,  4], 
                    [ 5,  6,  7,  8], 
                    [ 9, 10, 11, 12]],
                    
                    [[13, 14, 15, 16], 
                    [17, 18, 19, 20], 
                    [21, 22, 23, 24]]])
print(array3D.shape)

array2D = n.array([[1, 2, 3, 3.5], 
                   [5, 4, 6, 6.5],
                   [7, 8, 9, 9.5]])
print(array2D.shape)

multiBroadcasting = array3D * array2D
print("Final Output: ", multiBroadcasting, sep = '\n')

# 2. Implement a function that takes two 2D arrays c and d with different shapes and performs element-wise operations (addition, subtraction, multiplication, and division) between them using broadcasting. 
# Handle the case where broadcasting is not possible.

def mainOperations(c, d):
    try:
        # addition
        addition = c + d
        print("Addition: ", addition, sep = '\n')
        
        # subtraction
        subtraction = c - d
        print("Subtraction: ", subtraction, sep = '\n')
        
        # multiplication
        multiplication = c * d
        print("Multiplication: ", multiplication, sep = '\n')
        
        # division
        division = c / d
        print("Division: ", division, sep = '\n')
        
    except ValueError as e:
        print("Broadcasting not possible:", e)


# Different shapes but compatible for broadcasting
c = n.array([[1, 2, 3], [4, 5, 6]])
d = n.array([1, 2, 3])

mainOperations(c, d)

# Arrays with incompatible shapes
c = n.array([[1, 2, 3], [4, 5, 6]])
d = n.array([[1, 2], [3, 4]])

mainOperations(c, d)

# 3. Create a 2D array e with shape (5, 3) and a 1D array f with length 5. Compute the outer product of e and f using broadcasting.

array2De = n.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12],
                    [13, 14, 15]])

array1Df = n.array([1, 2, 3, 4, 5])

# Firstly, we will need to reshape array1Df so that it's compatible with array2De
# This changes array1Df from shape (5,) to shape (5, 1)
array1Df_reshaped = array1Df[:, n.newaxis]
print(array1Df_reshaped.shape)

# Computing the outer product using broadcasting
outer_product = array2De * array1Df_reshaped

print("2D Array e: ", array2De, sep = "\n")
print("1D Array f: ", array1Df, sep = "\n")
print("Outer Product: ", outer_product, sep = "\n")

# Indexing and Slicing:
# 1. Given a 3D array g with shape (4, 3, 2), extract every other element along the first and second dimensions, but keep all elements along the third dimension.
array3Dg = n.array([[[ 1,  2], [ 3,  4], [ 5,  6]],
              [[ 7,  8], [ 9, 10], [11, 12]],
              [[13, 14], [15, 16], [17, 18]],
              [[19, 20], [21, 22], [23, 24]]])

# Extracting every other element along the first and second dimensions
# but keeping all elements along the third dimension
extractedElements = array3Dg[::2, ::2, :]
# •	::2 for the first dimension means we take every other element along the first dimension (the layers).
# •	::2 for the second dimension means we take every other element along the second dimension (the rows within each layer).
# •	: for the third dimension means we take all elements along the third dimension (all columns within each row).


print("Original 3D Array g: ", array3Dg, sep = '\n')
print("Extracted Elements: ", extractedElements, sep = '\n')


# 2. Create a function that takes a 2D array h and an array of row indices i and column indices j. The function should return a new array k where k[m, n] is the sum of the elements in h along the diagonal specified by i[m] and j[n].
import numpy as nm

def sumAlongDiagonals(h, i, j):
    rows, cols = h.shape
    k = nm.zeros((len(i), len(j)))
    
    for m, rowStart in enumerate(i):
        for n, colStart in enumerate(j):
            row, col = rowStart, colStart
            diagSum = 0
            while row < rows and col < cols:
                diagSum += h[row, col]
                row += 1
                col += 1
            k[m, n] = diagSum
            
    return k

# Example usage
h = nm.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

i = nm.array([0, 1])
j = nm.array([0, 2])

k = sumAlongDiagonals(h, i, j)

print("2D Array h:\n", h)
print("Row indices i:", i)
print("Column indices j:", j)
print("Resulting Array k:\n", k)

# 3. Implement a function that takes a 2D array l and returns a new array m where each element in m is the product of the corresponding row and column means in l.

def mainFunc(l):
    # Compute the mean of each row and reshape to (rows, 1) for broadcasting
    row_means = n.mean(l, axis=1).reshape(-1, 1)
    
    # Compute the mean of each column
    col_means = n.mean(l, axis=0)
    
    # Use broadcasting to compute the outer product of row and column means
    m = row_means * col_means
    
    return m

# Example usage
l = n.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

m = mainFunc(l)

print("2D Array l: ", l, sep = '\n')
print("Resulting Array m: ", m, sep = '\n')


# Array Manipulation:
# 1. Given a 2D array n with shape (4, 6), reshape it into a 3D array with shape (2, 2, 6) and then flatten it back to a 2D array with shape (4, 6).
array2Dn = n.array([[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24]])

print(array2Dn.shape)

reshapedArray2Dn = array2Dn.reshape(2, 2, 6)
print("Reshaped array n and it's shape: ", reshapedArray2Dn, reshapedArray2Dn.shape, sep = '\n')
flattenedArray2Dn = reshapedArray2Dn.reshape(4, 6)
print("Flattened Array n and it's shape: ", flattenedArray2Dn, flattenedArray2Dn.shape, sep = "\n")

# 2. Implement a function that takes a 2D array o and rolls it along the first axis by a specified number of positions. For example, if the input array is [[1, 2, 3], [4, 5, 6]] and the number of positions is 1, the output should be [[4, 5, 6], [1, 2, 3]].
def rollArray(o, positions):
    rolledArray = n.roll(o, shift=positions, axis=0)
    return rolledArray

o = n.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

positions = 1

rolledO = rollArray(o, positions)

print("Original Array o:\n", o)
print(f"Array o rolled by {positions} positions:\n", rolledO)

# 3. Create a function that takes a 2D array p and replaces all occurrences of a specified value x with the mean of the neighboring elements (horizontally and vertically) in the array.
import numpy as n

def replaceWithMean(p, x):
    rows, cols = p.shape
    mask = (p == x)
    paddedP = n.pad(p, pad_width=1, mode='constant', constant_values=0)
    sumNeighbors = (paddedP[1:-1, :-2] + paddedP[1:-1, 2:] +
                    paddedP[:-2, 1:-1] + paddedP[2:, 1:-1])
    
    count = ((paddedP[1:-1, :-2] != 0).astype(int) + (paddedP[1:-1, 2:] != 0).astype(int) +
             (paddedP[:-2, 1:-1] != 0).astype(int) + (paddedP[2:, 1:-1] != 0).astype(int))
    
    meanNeighbors = n.divide(sumNeighbors, count, where=count != 0)
    result = p.copy()
    result[mask] = meanNeighbors[mask]
    
    return result
p = n.array([[1, 2, 3, 4],
              [5, -1, 7, 8],
              [9, 10, -1, 12],
              [13, 14, 15, 16]])

x = -1

replacedP = replaceWithMean(p, x)

print("Original Array p:\n", p)
print(f"Array p with occurrences of {x} replaced with the mean of neighbors:\n", replacedP)