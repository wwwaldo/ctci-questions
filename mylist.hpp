#ifndef _MY_LIST
#define _MY_LIST

#include <iostream>
#include <string>

// Moved member functions to inside header because of weird templating rules.
template <class T>
class ListNode{
	public:
		ListNode *next;
		T value;

		ListNode(T v){
			value = v;
			next = nullptr;
		}

		void append(T value){
			auto t = new ListNode(value);
			
			auto curr = this;
			while (curr->next != nullptr){
				curr = curr->next;
			}
			curr->next = t;
			return;
		}

		void traverse(){
			auto curr = this;
			while (curr->next != nullptr){
				std::cout << curr->value << std::endl;
				curr = curr->next;
			}
			std::cout << curr->value << std::endl;

		}

};

#endif
