# pylint: disable=missing-module-docstring

class Result():
    '''Class for managing the result assertion'''

    def __init__(self) -> None:
        self.search1_count = 0
        self.search2_count = 0
        self.search3_count = 0

    def get_search1_average(self, number_of_iterations):
        '''Return search 1 average compare actions'''
        return self.search1_count/number_of_iterations

    def get_search2_average(self, number_of_iterations):
        '''Return search 2 average compare actions'''
        return self.search2_count/number_of_iterations

    def get_search3_average(self, number_of_iterations):
        '''Return search 3 average compare actions'''
        return self.search3_count/number_of_iterations
