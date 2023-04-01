using System;
using CustomLinkedList;
using LinkedList;

namespace Datastructure
{
    class Program { 
        static void Main(String[] args)
        {
            //fibonnaci obj = new fibonnaci();
            //obj.fib_series(20);
            //string temp = "123";
            //int number = Convert.ToInt32(temp);
            //Console.WriteLine(number);

            // Create list
            //linked l1 = new linked();
            //l1.add_node(1);
            //l1.add_node(2);
            //l1.add_node(3);
            //l1.add_node(4);
            //l1.add_node(5);
            //Console.WriteLine("Linked List:");
            //l1.print_list();

            ////using method 1
            //Console.WriteLine("Reverse linked list");
            //l1.reverse();
            //l1.print_list();
            
            ////using method 2
            //Console.WriteLine("Reverse linked list using recurssion method 2");
            //if (l1.head == null)
            //{
            //    Console.WriteLine("Linked list is emnpty");
            //}
            //else
            //{
            //    l1.head = l1.reverse_rec(l1.head);
            //}
            //l1.print_list();

            ////using method 3
            //Console.WriteLine("Reverse linked list uisng method 3");
            //l1.rev_util();
            //l1.print_list();
            mergeSort obj = new mergeSort();
            int[] arr = new int[] { 1, 4, 5, 2, 7, 3, 6, 9, 8,4, 32 ,18, 12, 21,19 ,87,65,100, 99 };
            Console.WriteLine("Before sorting:");
            obj.printArray(arr);
            obj.msort(arr, 0, arr.Length-1);
            Console.WriteLine("After Sorting:");
            obj.printArray(arr);
        }

    }
}
