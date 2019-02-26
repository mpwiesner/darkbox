import numpy as np

def abs_area(x):
   """
   Calculate the sum of the numbers

   Then it outputs it to you

   Parameters
   ------------
   x: ndarray
      The signal for which to compute energy

   Returns
   --------
   energy : float
        The sum of squares 
   """

   return np.sum(np.abs(x))

