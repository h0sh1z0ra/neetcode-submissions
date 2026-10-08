// classic problem involving binary tree. we need to reverse the child nodes of each node. intuitively we can go with a BFS and invert the tree on each line. so on each level, we just swap the children.

// so say we have 
//    3
// 2     1
// We start at 3, then this becomes
//    3
// 1     2

// and repeat for each node


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return {};

        std::deque<TreeNode*> q{root};

        while (!q.empty()) {
            for (int i = 0; i < q.size(); i++) {
                TreeNode* node = q.back(); q.pop_back();

                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);

                swap(node->left, node->right);
            }
        }

        return root;

    }
};
