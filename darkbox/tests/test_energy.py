from darkbox import energy

from numpy.testing import assert_equal

def test_square():
   y = energy.abs_area([1,2,3,5,6])
   assert_equal(y,17)