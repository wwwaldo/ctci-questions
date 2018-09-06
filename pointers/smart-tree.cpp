#include <iostream>
#include <memory>
#include <string>

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>


class BNode{

	public:
		int data;
		std::shared_ptr<BNode> left;
		std::shared_ptr<BNode> right;

		BNode(int newdata){
			data = newdata;
			return;
		}

		friend std::ostream& operator<<(std::ostream& os, const BNode& node){
			os << node.data;
			return os; // it's still a monad!
		}

};

// A binary tree implemented with shared pointers.
class SmartTree{
	public:

		std::unique_ptr<BNode> root;

		SmartTree(){
			return;
		}

		int insert(int value){
			// todo
			return 0;
		}

		int remove(int value){
			// todo
			return 0;
		}

		friend std::ostream& operator<<(std::ostream& os, const SmartTree& tree){
			std::stringstream buffer;
			
			auto root = *tree.root;

			if (root.left) buffer << root.left;
			buffer << root.data;
			if (root.right) buffer << root.right;

			os << buffer.str();
			return os;
		}

};


/** Unit tests **/
BOOST_AUTO_TEST_CASE( test_initialization ){
	auto node = BNode(0);
	BOOST_CHECK(!(node.left || node.right));
}

BOOST_AUTO_TEST_CASE( test_print ){
	auto node = BNode(0);
	
	std::stringstream buffer;
	buffer << node;

	BOOST_CHECK( buffer.str() == "0" );

}

BOOST_AUTO_TEST_CASE( test_tree_inorder_print ){
	auto tree = SmartTree();
	std::unique_ptr<BNode> rp(new BNode(0));
	rp->left = std::make_shared<BNode>(1);
	rp->right = std::make_shared<BNode>(2);

	tree.root = std::move(rp);
	
	std::stringstream buffer;
	buffer << tree;
	
	BOOST_CHECK( buffer.str() == "102" );

}

BOOST_AUTO_TEST_CASE( test_insertion ){
	auto tree = SmartTree();
	tree.insert(0);

	std::stringstream buffer;
	buffer << tree;



}


