class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return {};

        /*
        vector<int> prefix(n), suffix(n), result(n);

        prefix[0]   = 1;
        suffix[n-1] = 1;

        for (int i = 1; i < n; i++) 
            prefix[i] = prefix[i-1] * nums[i-1];
        
        for (int i = n-2; i >= 0; i--)
            suffix[i] = suffix[i+1] * nums[i+1];

        for (int i = 0; i < n; i++)
            result[i] = prefix[i] * suffix[i];
        
        return result; */

        // [1,0,0,1]
        // [1,1,2,8]
        vector<int> output(n);
        output[0] = 1;

        // First pass, for prefix
        for (int i = 1; i < n; i++) {
            output[i] = output[i-1] * nums[i-1];
        }

        // Second pass, for suffix
        int suffix = 1;
        for (int i = n-1; i >= 0; i--) {
            output[i] *= suffix;
            suffix *= nums[i];
        }

        return output;
    }
};
