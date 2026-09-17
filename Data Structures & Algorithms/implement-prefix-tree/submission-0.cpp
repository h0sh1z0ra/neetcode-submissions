class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord = false;
};

class PrefixTree {
    TrieNode* root;
public:
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        // iterate through every character
        TrieNode* cur = root;

        for (const char& c : word) {
            if (!cur->children.count(c)) 
                cur->children[c] = new TrieNode(); // inserted as a new node
            cur = cur->children[c]; // already exists
        }
        // current is now set to the end of the word
        cur->endOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;

        for (const char& c : word) {
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        // if it reaches the end of the word, it's a word and it'll return true
        return cur->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;

        for (const char& c : prefix) {
            if (!cur->children.count(c))
                return false;
            cur = cur->children[c];
        }
        return true;
    }
};
