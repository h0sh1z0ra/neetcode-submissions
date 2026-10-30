class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int res = 0;
        std::priority_queue<int> maxHeap;

        for (int& num : nums) maxHeap.push(num);

        for (int i = 0; i < k; i++) {
            res = maxHeap.top();
            maxHeap.pop();
        }

        return res;
    }
};
