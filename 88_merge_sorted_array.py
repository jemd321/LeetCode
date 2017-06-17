class MergeSortedArray:
    def merge_sorted_array(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

class Test:
    test = MergeSortedArray()
    for x in test.merge_sorted_array([1,2,3,4,5,6,7,0,0,0,0,0], 7, [1,2,3,7,8], 5):
        print(x)
    #
    #print("NEXT")
    #for x in test.merge_sorted_array([1,0], 1, [0], 0):
    #    print(x)
    #print("NEXT")
    #for x in test.merge_sorted_array([0, 0], 0, [0], 0):
    #    print(x)
    #print("NEXT")
    #for x in test.merge_sorted_array([0, 0], 0, [1], 1):
    #    print(x)
    #print("NEXT")
    #for x in test.merge_sorted_array([1,2,3,4,5], 5, [0], 0):
    #    print(x)
    print("NEXT")
    for x in test.merge_sorted_array([1,2,3,4,5,0], 5, [6], 1):
        print(x)