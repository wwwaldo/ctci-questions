#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>
#include <iostream>
#include <string>

class my_class{
	public:
		int x;
		int y;
		std::string name;
		bool is_valid();
		my_class(std::string s);
};

bool my_class::is_valid()
{
		return true;
}

my_class::my_class(std::string s){
	name = s;
	return;
}

BOOST_AUTO_TEST_CASE( my_test )
{
	my_class test_object("Hello world");
	BOOST_CHECK( test_object.is_valid() );

	std::cout << test_object.name << std::endl;

}
