using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedList
{
    public class mergeSort
    {
        public void msort(int[] arr, int l , int r)
        {
            if (l < r)
            {
                int m = l + (r - l) / 2;
                msort(arr, l, m);
                msort(arr, m + 1, r);
                merge(arr, l, r, m);
            }
        }

        void merge(int[] arr, int l, int r, int m)
        {
            int n1 = m - l + 1;
            int n2 = r - m;
            int[] larr = new int[n1];
            int[] rarr = new int[n2];

            for (int i = 0; i < n1; ++i)
            {
                larr[i] = arr[l + i];
            }
            for (int i = 0; i < n2; ++i)
            {
                rarr[i] = arr[m + 1 + i];
            }
            int p = 0, q = 0, k = l;
            while (p < n1 && q < n2)
            {
                if (larr[p] >= rarr[q])
                {
                    arr[k] = rarr[q];
                    q++;
                }
                else
                {
                    arr[k] = larr[p];
                    p++;
                }
                k++;
            }

            while (p < n1)
            {
                arr[k] = larr[p];
                p++;
                k++;
            }
            while (q < n2)
            {
                arr[k] = rarr[q];
                q++;
                k++;
            }


        }
        public void printArray(int[] arr)
        {
            for(int i = 0; i < arr.Length; ++i)
            {
                Console.Write($"{arr[i]} ");
            }
            Console.WriteLine();

        }
    }
}
