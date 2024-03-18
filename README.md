## Point Database

This repository contains a Python implementation of a data structure called PointDatabase, which efficiently stores a set of data points in two-dimensional space and supports fast retrieval of nearby points based on the ℓ∞-distance metric.

### Motivation

The PointDatabase is designed to address the problem of efficiently retrieving nearby points, such as restaurants in a geographical area, given a query point and a maximum distance. Traditional approaches like linear search are inefficient for large datasets, hence the need for a specialized data structure.

### Problem Statement

Given a list of data points in two-dimensional space and a query point with a maximum distance, the task is to implement the PointDatabase class in Python. This class should provide methods to initialize the database with a list of points and to search for nearby points efficiently.

### Implementation

The `PointDatabase` class has the following methods:

- `__init__(self, pointlist)`: Constructs a PointDatabase object from a list of points. This method runs in O(nlogn) time.
- `searchNearby(self, q, d)`: Searches for points within a distance `d` from the query point `q`. This method runs in O(m + log2n) time, where `m` is the number of points returned.



#### Example Test-case:

```python
pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10), (9,2), (10,5)])

print(pointDbObject.searchNearby((5,5), 1))     # Output: []
print(pointDbObject.searchNearby((4,8), 2))     # Output: [(3,7), (4,9)]
print(pointDbObject.searchNearby((10,2), 1.5))  # Output: [(9,2)]
