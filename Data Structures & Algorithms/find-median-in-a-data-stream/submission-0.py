class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
    def findMedian(self) -> float:
        self.arr.sort()   # important
        
        n = len(self.arr)
        mid = n // 2
        
        if n % 2 == 0:
            return (self.arr[mid] + self.arr[mid - 1]) / 2
        else:
            return self.arr[mid]