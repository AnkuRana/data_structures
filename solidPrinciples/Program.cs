
using solidPrinciples;
using System.Xml;

// open closed relationship principle
//Console.WriteLine("Hello, World!");
//Product apple = new Product("Apple", Color.White, Size.Medium);
//Product oneplus = new Product("OnePlus", Color.Green, Size.Large);
//Product xiomi = new Product("Xiomi", Color.Yellow, Size.Small);
//Product micromax = new Product("MicroMax", Color.Green, Size.Small);

//List<Product> products = new List<Product>() { apple, oneplus, xiomi, micromax };
//oldFilter old = new oldFilter();
//BetterFilter bf = new BetterFilter();

//foreach(var p in old.filterbyColor(products, Color.Green))
//    {
//    Console.WriteLine($"Filter(Old): - {p.name} is Green");
//    }

//foreach (var p in old.filterbySize(products, Size.Small))
//{
//    Console.WriteLine($"Filter(Old): - {p.name} is small");
//}

//foreach (var p in bf.filter(products, new AndSpecification<Product>(new ColorSpecification(Color.Yellow), new SizeSpecification(Size.Small))))
//{
//    Console.WriteLine($"BetterFilter(New): - {p.name} is White");
//}

// Liskove substitution principle
static void Area(Rectangle r)
{
    int area = r.Height * r.Width;
    Console.WriteLine($"Area: {area}");
}

Rectangle rc = new Rectangle(2, 3);
Rectangle sq= new Square();
sq.Width = 3;
Area(rc);
Console.Write("Square:");
Area(sq);
