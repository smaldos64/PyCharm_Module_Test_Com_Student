import math
import Point

class MyMath_Class:
   @staticmethod
   def calculate_discriminant(a_coefficient, b_coefficient, c_coefficient):
        discriminant = 0

        discriminant = math.pow(b_coefficient, 2) - 4*a_coefficient*c_coefficient

        return discriminant

   def calculate_discriminant_self(self, a_coefficient, b_coefficient, c_coefficient):
       discriminant = 0

       discriminant = math.pow(b_coefficient, 2) - 4 * a_coefficient * c_coefficient

       return discriminant
