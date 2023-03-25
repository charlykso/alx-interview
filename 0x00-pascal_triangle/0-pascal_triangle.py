#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n
"""
fac = __import__('factorial').fac

def pascal_triangle(n):
  """
  returns a list of lists of integers
  representing the pascal's triangle of n
  """

  triagle = []
  for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
      row[j] = triagle[i - 1][j - 1] + triagle[i - 1][j]
    triagle.append(row)
  return triagle
