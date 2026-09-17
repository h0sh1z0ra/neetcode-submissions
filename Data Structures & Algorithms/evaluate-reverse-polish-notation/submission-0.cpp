class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // edge cases: negative numbers
        unordered_set<string> operators{"+", "-", "*", "/"};
        stack<int> stack;

        for (const string& token : tokens) {
            if (operators.count(token)) {
                int num2 = stack.top(); stack.pop();
                int num1 = stack.top(); stack.pop();

                if (token == "+") stack.push(num1 + num2);
                else if (token == "-") stack.push(num1 - num2);
                else if (token == "*") stack.push(num1 * num2);
                else if (token == "/") stack.push(num1 / num2);

            } else {
                stack.push(stoi(token));
            }
        }
        return stack.top();
    }
};
