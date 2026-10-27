class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // For heap, since it's a min-heap, we'll store negative versions so the biggest (=-biggest = smallest) is last. C++ and Python don't have this issue tho so fuck you
        priority_queue<int> maxHeap;

        for (int stone : stones) maxHeap.push(stone);

        while (maxHeap.size() > 1) {
            int big  = maxHeap.top(); maxHeap.pop();
            int big2 = maxHeap.top(); maxHeap.pop();
            maxHeap.push(big - big2);
        }

        return 0 ? (maxHeap.size() == 1) : maxHeap.top();

    }
};
