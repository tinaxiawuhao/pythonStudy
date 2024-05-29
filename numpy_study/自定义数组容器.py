import numpy as np

# class DiagonalArray:
#      def __init__(self, N, value):
#          self._N = N
#          self._i = value
#      def __repr__(self):
#          return f"{self.__class__.__name__}(N={self._N}, value={self._i})"
#      def __array__(self, dtype=None):
#          return self._i * np.eye(self._N, dtype=dtype)
     
# arr = DiagonalArray(5, 1)
# print(arr)
# print(np.asarray(arr))
# print(np.multiply(arr, 2))

from numbers import Number
import numpy.lib.mixins

HANDLED_FUNCTIONS = {}
class DiagonalArray(numpy.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, N, value):
         self._N = N
         self._i = value
    def __repr__(self):
         return f"{self.__class__.__name__}(N={self._N}, value={self._i})"
    def __array__(self, dtype=None):
         return self._i * np.eye(self._N, dtype=dtype)
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
         if method == '__call__':
             N = None
             scalars = []
             for input in inputs:
                 if isinstance(input, Number):
                     scalars.append(input)
                 elif isinstance(input, self.__class__):
                     scalars.append(input._i)
                     if N is not None:
                         if N != self._N:
                             raise TypeError("inconsistent sizes")
                     else:
                         N = self._N
                 else:
                     return NotImplemented
             return self.__class__(N, ufunc(*scalars, **kwargs))
         else:
             return NotImplemented
    def __array_function__(self, func, types, args, kwargs):
        if func not in HANDLED_FUNCTIONS:
            return NotImplemented
        # Note: this allows subclasses that don't override
        # __array_function__ to handle DiagonalArray objects.
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented
        return HANDLED_FUNCTIONS[func](*args, **kwargs)
    
arr = DiagonalArray(5, 1)
print(np.multiply(arr, 3))
print(np.add(arr, 3))
print(np.sin(arr))
print(arr + 3)
