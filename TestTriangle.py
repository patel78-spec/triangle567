# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Dhruv Patel
"""

import unittest
from mybrand import my_brand
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Testing Invalid Inputs
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle("2", "10", "10"), 'InvalidInput')

    # Testing Not a Triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(6, 1, 1), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 5, 2), 'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 6, 15), 'NotATriangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(1, 17, 5), 'NotATriangle')

    # testing for equilateral triangles
    def testEquilateralTriangleA(self):
      self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')
    
    def testEquilateralTriangleB(self):
      self.assertNotEqual(classifyTriangle(5, 1, 5), 'Equilateral')

    def testEquilateralTriangleC(self):
      self.assertEqual(classifyTriangle(25, 25, 25), 'Equilateral')

    def testEquilateralTrianglesD(self): 
      self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral','1,1,1 should be equilateral')
        
    # testing for right angle triangles
    def testRightTriangleA(self): 
      self.assertEqual(classifyTriangle(3, 4, 5), 'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
      self.assertEqual(classifyTriangle(5, 3, 4), 'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
      self.assertEqual(classifyTriangle(8, 6, 10), 'Right')

    def testRightTraingleD(self):
      self.assertNotEqual(classifyTriangle(10, 7 , 25), 'Right')

    # testing for Scalene
    def testScaleneTriangleA(self):
      self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testScaleneTriangleB(self):
      self.assertEqual(classifyTriangle(90, 100, 110), 'Scalene')

    def testScaleneTriangleC(self):
      self.assertNotEqual(classifyTriangle(90, 90, 110), 'Scalene')

    def testScaleneTriangleD(self):
      self.assertEqual(classifyTriangle(12, 13, 15), 'Scalene')

     # Testing Isosceles Triangles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 13), 'Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4, 26, 26), 'Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertNotEqual(classifyTriangle(8, 5, 9), 'Isosceles')

    def testIsoscelesTriangleD(self):
        self.assertEqual(classifyTriangle(16, 16, 4), 'Isosceles')
        
    

if __name__ == '__main__':
    my_brand('HW-02a')
    print('-------------------Running unit tests----------------------')
    unittest.main()
    my_brand('HW-02a')
