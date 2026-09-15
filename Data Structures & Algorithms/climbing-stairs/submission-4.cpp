class Solution {
public:
    int climbStairs(int n) {
        int prevStep = 1;
        int currStep = 1;

        for (int i = 0; i < n; i++) {
            int temp = prevStep;
            prevStep += currStep;
            currStep = temp;
        }
        return currStep;
    }
};
