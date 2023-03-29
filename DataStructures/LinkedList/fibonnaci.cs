using System;

public class fibonnaci
{
    public void fib_series(int n) { 
        string name = "Amit Rana";
        Console.WriteLine($"hello {name}.");
          
        var fibon= new List<int>();

        for (int i = 0; i < n; i++)
        {
            fibon.Add(fib(i));
        }

        foreach (var num in fibon)
        {
            Console.WriteLine(num);
        }

    }
    int fib(int n)
    {
        if (n <= 1)
        {
            return n;
        }
        else
        {
            return fib(n - 1) + fib(n - 2);

        }

    }
}
