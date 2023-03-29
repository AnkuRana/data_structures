using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace solidPrinciples
{
    //The Dependency Inversion Principle (DIP) states that high-level modules/classes should not depend on low-level modules/classes.
    //First, both should depend upon abstractions. Secondly, abstractions should not rely upon details.
    //Finally, details should depend upon abstractions
    //High-level modules/classes implement business rules or logic in a system(application).
    //Low-level modules/classes deal with more detailed operations; in other words,
    //they may write information to databases or pass messages to the operating system or services.
    //A high-level module/class that depends on low-level modules/classes or some other class and
    //knows a lot about the other classes it interacts with is said to be tightly coupled.
    //When a class knows explicitly about the design and implementation of another class,
    //it raises the risk that changes to one class will break the other.
    //So we must keep these high-level and low-level modules/classes loosely coupled as much as possible.
    //To do that, we need to make both of them dependent on abstractions instead of knowing each other
    public interface Ilogger
    {
        void logmessage(string message);
    }
    public class FileLogger: Ilogger
    {
        public void logmessage(string message)
        {
            Console.WriteLine(message);
        }
    }
    public class DbLogger: Ilogger
    {
        public void logmessage(string message)
        {
            Console.WriteLine(message);
        }
    }
    public class ExceptionLogger
    {
        //public void logintofile(Exception eMessage)
        // {
        //     //string filename = @"C:\Code\data_structures\solidPrinciples\loggingmessage.txt";
        //     FileLogger obj = new FileLogger();
        //     obj.logmessage(eMessage.ToString());

        // }

        // public void logintodb(Exception eMessage)
        // {
        //     DbLogger dbo = new DbLogger();
        //     dbo.logmessage(eMessage.ToString());
        // }

       Ilogger logger;
        public ExceptionLogger(Ilogger logObj)
        {
            logger = logObj;
        }
        public void logmessage(Exception e)
        {
            logger.logmessage(e.ToString());
        }
    }
    public class Datalogger
    {
        public void exportdata()
        {
            try
            {
            }
            catch(IOException e)
            {
                ExceptionLogger eobj = new ExceptionLogger(new DbLogger());
                eobj.logmessage(e);
            }
            catch (Exception e)
            {
                ExceptionLogger eobj = new ExceptionLogger(new FileLogger());
                eobj.logmessage(e);
            }
        }
    }
   
}
