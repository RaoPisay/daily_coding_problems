class Solution {
    public int search(int[] arr, int t) {
        int n = arr.length;
        int minIndex = findMinIndex(arr);
        // minIndex == 0 means the array is already in sorted order
        if (minIndex == 0)
            return binarySearch(arr, t, 0, n - 1);

        //check in the first half if `t` falls in within the, minIndex is always `> 0` at this point
        if (t >= arr[0] && t <= arr[minIndex - 1])
            return binarySearch(arr, t, 0, minIndex - 1);

        //if t doesn't fall within the 0 to midIndex range then check in midIndex to n - 1
        return binarySearch(arr, t, minIndex, n - 1);
    }

    //find min number index, should not return -1 at any cost
    public int findMinIndex(int[] arr) {
        int l = 0, r = arr.length - 1;

        while (l < r) {
            int mid = (l + r) >>> 1;
            
            if (arr[mid] > arr[r]) {
                // since mid > right most element then min will be at the right
                l = mid + 1;
            } else {
                // The minimum is either mid or to the left of mid
                r = mid;
            }
        }
        return l; //when l == r it means we found the smallest number
    }

    //1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    //regular binary search logic
    public int binarySearch(int[] arr, int t, int l, int r) {
        int mid = -1;

        while (l <= r) {
            mid = (l + r) >>> 1; // short cut of [((r - l) / 2) + l]
            if (arr[mid] == t)
                return mid;
            if (arr[mid] < t)
                l = mid + 1;
            else
                r = mid - 1;
        }

        return -1;
    }

}
