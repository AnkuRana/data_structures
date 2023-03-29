using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace solidPrinciples
{
    //The Open/closed Principle says, "A software module/class is open for extension and closed for modification."
    //heere "Open for extension" means we must design our module/class so that the new functionality can be added only when
    //new requirements are generated.
    //"Closed for modification" means we have already developed a class, and it has gone through unit testing.
    //We should then not alter it until we find bugs. As it says, a class should be open for extensions; we can use inheritance
    public enum Color
    {
        Green, Yellow, White
    }
    public enum Size
    {
        Small, Medium, Large
    }
    public class Product
    {
        public string name;
        public Color color;
        public Size size;

        public Product(string name, Color color, Size size)
        {
            this.name = name;
            this.color = color;
            this.size = size;
        }

    }
    public class oldFilter
    {
        public IEnumerable<Product> filterbySize(IEnumerable<Product> products, Size size)
        {
            foreach (Product p in products)
            {
                if (p.size == size)
                {
                    yield return p;
                }
            }

        }
        public IEnumerable<Product> filterbyColor(IEnumerable<Product> products, Color color)
        {
            foreach (Product p in products)
            {
                if (p.color == color)
                {
                    yield return p;
                }
            }

        }

    }
    public interface ISpecification<T>
    {
        bool isSatisfied(Product p);
    }
    public interface IFilter<T>
    {
        IEnumerable<T> filter(IEnumerable<T> things, ISpecification<T> spec);
    }

    public class ColorSpecification : ISpecification<Product>
    {
        Color color;
        public ColorSpecification(Color color)
        {
            this.color = color;
        }
        public bool isSatisfied(Product p)
        {
            return color == p.color;
        }
    }
    public class SizeSpecification : ISpecification<Product>
    {
        Size size;
        public SizeSpecification(Size size)
        {
            this.size = size;
        }
        public bool isSatisfied(Product p)
        {
            return size == p.size;
        }

    }
    public class AndSpecification<T> : ISpecification<T>
    {
        ISpecification<T> first, second;
        public AndSpecification(ISpecification<T> spec1, ISpecification<T> spec2)
        {
            this.first = spec1;
            this.second = spec2;
        }

        public bool isSatisfied(Product p)
        {
            return first.isSatisfied(p) && second.isSatisfied(p);

        }

    }

    public class BetterFilter : IFilter<Product> 
    { 
        public IEnumerable<Product> filter(IEnumerable<Product> things, ISpecification<Product> specification)
        {
            foreach (var item in things)
            {
                if (specification.isSatisfied(item))
                {
                    yield return item;
                }

            }

        }
    }
    


}
