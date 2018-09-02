#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE ListTest
#include <boost/test/unit_test.hpp>

#include <iostream>
#include <string>

#include "mylist.hpp"

// A simple linked list implementation.

BOOST_AUTO_TEST_CASE( my_test )
{
	ListNode<int> node(0); // correct calling convention for invoking constructor.
	node.append(1);
	node.append(2);
	
	node.traverse();

	BOOST_CHECK( true );
}
