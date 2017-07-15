'''
/***********************************************
*    Title: Moving Robot Application           *
*    Author: Guillem Nicolau Alomar Sitjes     *
*    Date: July 15th, 2017                     *
*    Code version: 0.1                         *
*    Availability: Public                      *
***********************************************/
'''


class Landscape:
    dim_x = 0
    dim_y = 0

    def __init__(self, (x, y)):
        self.dim_x = x
        self.dim_y = y

    def reshape(self, x, y):
        self.dim_x = x
        self.dim_y = y

    def get_dims(self):
        return self.dim_x, self.dim_y
