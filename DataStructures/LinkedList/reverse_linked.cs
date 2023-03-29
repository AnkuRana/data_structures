using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomLinkedList
{

    class Node
    {
        internal int data;
        internal Node next;
        public Node(int data) {
            this.data = data;
            this.next = null;
        }

    }
    class linked
    {
        internal Node head;

        internal void add_node(int data)
        {
            Node new_node = new Node(data);
            if (head == null)
            {
                head = new_node;
            }
            else
            {
                new_node.next = head;
                head = new_node;
            }
        }

        internal void print_list()
        { 
            Node temp = head;
            if (head == null)
            {
                Console.WriteLine("Linked list is empty.");
            }
            else
            {
                while( temp != null)
                {
                    Console.Write($"{temp.data} -> ");
                    temp = temp.next;
                }
                Console.WriteLine("null");
            }
        }

        //Method 1
        internal void reverse()
        {
            Node currNode = head;
            Node prev = null, conncted;
            while(currNode != null )
            {
                conncted = currNode.next;
                currNode.next = prev;
                prev = currNode;
                currNode = conncted;
            }
            head = prev;

        }
        //Method 2
        internal Node reverse_rec(Node head_node) {
        
            if (head_node == null || head_node.next == null){
                return head_node;
            }
            Node rest = reverse_rec(head_node.next);
            head_node.next.next = head_node;
            head_node.next = null;

            return rest;
        }

        //method 3
        internal void reverse_util(Node current, Node previous)
        {
            Node temp;
            if (current == null)
            {
                head = previous;
                return;
            }
            temp = current.next;
            current.next = previous;
            previous = current;
            reverse_util(temp, previous);
            
        }

        internal void rev_util()
        {
            Node curr = head, prev = null;
            if (head == null)
            {
                Console.WriteLine("List is Empty.");
            }
            else
            {
                reverse_util(curr, prev);

            }
        }
    }
}
