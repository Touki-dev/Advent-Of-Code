cimport numpy as np
import numpy as np
from libc.math cimport pow

# Accélère hexToBase10
def hexToBase10(char* n):
    cdef dict codeHex = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    cdef int n_base10 = 0
    cdef int i, len_n = len(n)
    for i in range(len_n):
        n_base10 += codeHex[n[i]] * pow(16, len_n - i - 1)
    return n_base10

# Accélère is_point_inside_polygon
def is_point_inside_polygon(int x, int y, np.ndarray polygon):
    cdef int n = polygon.shape[0]
    cdef int i
    cdef double px = x, py = y, x1, y1, x2, y2
    cdef int inside = 0

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside