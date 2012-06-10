#-------------------------------------------------------------------------------
# Name:        Sam Module
# Purpose:     Basic operations on a social accounting matrix
#
# Author:      roberto ferrer
#
# Created:     06/09/2012
# Copyright:   (c) roberto ferrer 2012
# Licence:     GNU General Public Licence
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()


class Sam:
    def __init__(self, year, units):
        self.year = year
        self.units = units

    def setYear(self, year):
        self.year = year

    def setUnits(self, units):
        self.units = units

    def calAn(self):
        ''' Calculate matrix of techinical coefficients An.
        '''

