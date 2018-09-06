#include <iostream>
#include <string>

#include <vector>
#include <deque>

#include <stddef.h> // size_t

// A tree node with some metadata.
class RandTreeNode{
	public:
		int value;
		size_t subtree_size; // number of nodes in this subtree, including self.
		RandTreeNode *left;
		RandTreeNode *right; // left and right children

		// create a new leaf node.
		RandTreeNode(int newvalue){
			value = newvalue;
			subtree_size = 1;
			left = nullptr;
			right = nullptr;
		}

		~RandTreeNode(){ // overload the destructor to manage memory
			delete left; // need to do this because the default destructor on pointers DOES NOT FREE the memory that the pointers point to!! Only frees the memory allocated to store the pointer itself!
			delete right;
		}

		friend std::ostream& operator<<(std::ostream& os, const RandTreeNode& node){
			os << node.value;
			return os; // it's a monad!
		}

		void addLeftChild(int newvalue){
			auto child = new RandTreeNode(newvalue);
			left = child;
			subtree_size++; 
			return;
		}

		void addRightChild(int newvalue){
			auto child = new RandTreeNode(newvalue);
			right = child;
			subtree_size++;
			return;
		}

		void removeLeftChild(){
			left = nullptr; // hurray for memory management 
			subtree_size--;
			return;
		}

		void removeRightChild(){
			right = nullptr;
			subtree_size--;
			return;
		}

		int getValue(){
			return value;
		}
};


// Wrapper class for non-balancing bst. bonus: generalize int vals.
class RandBinTree{
	public:
		RandTreeNode *root;		
		
		// Initialize empty RandBinTree
		RandBinTree(){
			root = nullptr;
			return;		
		}


		~RandBinTree(){
			delete root;
		}

		// doesn't belong to my class --?
		friend std::ostream& operator<<(std::ostream& os, const RandBinTree& tree){
			
			std::deque<RandTreeNode *> queue;
			queue.push_back(tree.root);

			while ( !queue.empty() ){
				auto current = *queue.cbegin();
				queue.pop_back();	
			}

			os << "Placeholder ... todo!" << std::endl;

			return os;
		}

		int insert(int newvalue){
			if (root == nullptr){
				root = new RandTreeNode(newvalue);
			}
			else{
				// Traverse the tree.
				auto current = root;
				while (true){
					RandTreeNode *next = newvalue <= current->value ? current->left : current->right;
					if (next == nullptr){
						if (newvalue <= current->value) current->addLeftChild(newvalue);
						if (newvalue > current->value) current->addRightChild(newvalue);
						break;
					}
					current = next;

				}
			}
			return 0;
		}

		int remove(){
			std::cerr << "Not yet implemented." << std::endl; // writes to std::cerr aren't buffered, which is good!
			return 0;

		}

		
		RandTreeNode *find(){

		}

		RandTreeNode * getRandom(){

		}


};

int func(){

	auto tree = RandBinTree();
	tree.insert(1);
	tree.insert(0);
	tree.insert(2);

	// inspect the tree
	std::cout << tree.root->value;
	std::cout << tree.root->left->value;
	std::cout << tree.root->right->value;

	std::cout << tree.root->subtree_size;
	std::cout << tree.root->left->subtree_size;

	std::cout << tree << std::endl; // where everything goes wrong...

	return 0;
}

int main(int argc, char **argv){

	std::cout << "Hello world" << std::endl;
	func();
}
