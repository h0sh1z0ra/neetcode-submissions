class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> bracketSet{{')','('}, 
                                             {']','['},
                                             {'}','{'}
                                            };
        stack<char> stack;

        for (char& bracket : s) {
            if (bracketSet.count(bracket)) {
                if (!stack.empty() && stack.top() == bracketSet[bracket])
                    stack.pop();
                else
                    return false;
            } else {
                stack.push(bracket);
            }
        }

        return stack.empty();
    }
};
