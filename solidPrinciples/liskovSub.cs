using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace solidPrinciples
{
    //The Liskov Substitution Principle (LSP) states,
    //"you should be able to use any derived class instead of a parent class and have it behave in the same manner without modification."
    //It ensures that a derived class does not affect the behavior of the parent class; in other words,
    //a derived class must be substitutable for its base class.

    //This principle is just an extension of the Open Closed Principle,
    //and we must ensure that newly derived classes extend the base classes without changing their behavior.
    //I will explain this with a real-world example that violates LSP.

    //A father is a doctor, whereas his son wants to become a cricketer.
    //So here, the son can't replace his father even though they belong to the same family hierarchy.
    public class Rectangle
    {
        public virtual int Height { get; set; }
        public virtual int Width { get; set; }
        public Rectangle() { }
        public Rectangle(int h, int w) { 
            Height= h;
            Width= w;
        }
    }
    public class Square : Rectangle
    {
        public override int Height{
            set
            {
                base.Height = base.Width = value;
            }
        }
        public  override int Width
        {
            set
            {
                base.Width = base.Height = value;
            }
        }
    }
}
