class QuickSort:

    def quick_sort(self, __list__):

        if len(__list__) < 2:
            return __list__

        else:
            pivot = __list__.pop()
            greater_than_pivot = []
            less_than_pivot = []

            for item in __list__:

                if item > pivot:
                    greater_than_pivot.append(item)

                else:
                    less_than_pivot.append(item)

            return self.quick_sort(less_than_pivot) + [pivot] + self.quick_sort(greater_than_pivot)


try:
    quickSort = QuickSort()
    numbers = list(
        map(int, input('Please enter the list of number:\n').split()))
    numbers = quickSort.quick_sort(numbers)
    print(numbers)

except Exception as error:
    print(error)
