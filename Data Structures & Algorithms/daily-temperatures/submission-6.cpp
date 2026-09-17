class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        std::stack<pair<int, int>> tempStack; // store (index, temp)
        vector<int> result(n, 0);

        for (int i = 0; i < n; i++) {
            // if greater than the top element in the stack
            // while loop resolves multiple days
            while (!tempStack.empty() && temperatures[i] > tempStack.top().second) {
                auto [prevIdx, temp] = tempStack.top(); tempStack.pop();
                result[prevIdx] = i - prevIdx;
            }

            // if not in stack
            tempStack.push({i, temperatures[i]});
        }
        return result;
    }
};
