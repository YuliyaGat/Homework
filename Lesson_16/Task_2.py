class Mathematician:

    def square_nums(self, nums_list):
        return list(map(lambda num: num**2, nums_list))

    def remove_positives(self, nums_list1):
        return list(filter(lambda num: num <= 0, nums_list1))

    def filter_leaps(self, dates_list):
        return list(filter(lambda year: year%4==0 and year%100!=0 or year%400==0, dates_list))

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]