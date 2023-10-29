class Algorithms:
    def minimum(arr):
        if len(arr) == 0:
            return None
        min_num = arr[0]
        for num in arr:
            if num < min_num:
                min_num = num
        return min_num

    def maximum(arr):
        if len(arr) == 0:
            return None
        max_num = arr[0]
        for num in arr:
            if num > max_num:
                max_num = num
        return max_num

    def bubble_sort(arr):
        for i in range(len(arr)):
            changed = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    changed = True
            if not changed:
                break
        return arr