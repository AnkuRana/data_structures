using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedList
{
    class BubbleSort
    {
        static int count=0;
        public void bubblesort(int[] arrt)
        {
            bool flag = false;
            for (int i = 0; i < arrt.Length; i++)
            {
                for (int j = 0; j < arrt.Length - 1; j++)
                {
                    if (arrt[j] > arrt[j + 1])
                    {
                        flag = true;
                        // swap numbers in  array at following indicies
                        new HelperClass().swap(arrt, j, j + 1);
                    }
                    if (!flag)
                    {
                        Console.WriteLine($"There is no more comparison left. Count: {count}");
                        return;
                    }

                }
                count++;
            }
        }
    }
}
