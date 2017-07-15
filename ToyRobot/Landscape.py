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

    # This method initializes the size of the landscape (always going from (0,0) to (x,y))
    # Input:
    #     (x,y): initial horitzontal and vertical sizes of the landscape
    def __init__(self, (x, y)):
        self.dim_x = x
        self.dim_y = y

    # This method modifies the shape of the landscape (always going from (0,0) to (x,y))
    # Input:
    #     (x,y): new horitzontal and vertical sizes of the landscape
    def reshape(self, (x, y)):
        self.dim_x = x
        self.dim_y = y

    # This method returns the current shape of the landscape
    def get_shape(self):
        return self.dim_x, self.dim_y
