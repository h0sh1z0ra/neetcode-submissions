class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        using T = tuple<int, int, int>;
        std::priority_queue<T, vector<T>, greater<>> minHeap;

        // Setting up heap
        for (auto& coord : points) {
            long long dist = coord[0]*coord[0] + coord[1]*coord[1];
            minHeap.push({dist, coord[0], coord[1]});
        }
        vector<vector<int>> result;
        for (int _ = 0; _ < k; _++) {
            vector<int> coords;
            auto [d, c1, c2] = minHeap.top();
            coords.push_back(c1); coords.push_back(c2);
            result.push_back(coords);
            minHeap.pop();
        }

        return result;
    }
};
