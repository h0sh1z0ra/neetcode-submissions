class MinStack {
public:
    MinStack() {}
    
    void push(int val) {
        theStack.push(val);
       
        val = std::min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        theStack.pop();
        minStack.pop();
    }
    
    int top() {
        return theStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }

private:
    std::stack<int> theStack;
    std::stack<int> minStack;
};
