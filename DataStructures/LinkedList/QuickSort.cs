using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedList
{
    class QuickSort
    {
        public void quickSort(int[] arr, int low, int high)
        {
            if (low < high)
            {
                int pi = partition(arr, low, high);
                quickSort(arr, low, pi-1);
                quickSort(arr, pi+1, high);

            }
            
        }

        int partition(int[] arr, int low, int high)
        {
            int i = low - 1;
            int pivot = arr[high];
            for (int j = low; j < high; j++)
            {
                if (pivot >= arr[j])
                {
                    i++;
                    new HelperClass().swap(arr, i, j);
                }
            }
            new HelperClass().swap(arr, i + 1, high);

            return i+1;
        }
        
        
    }
}
