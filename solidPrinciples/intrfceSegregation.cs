using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace solidPrinciples
{
    //The Interface Segregation Principle states "that clients should not be forced to implement interfaces they don't use.
    //Instead of one fat interface, many small interfaces are preferred based on groups of methods, each serving one submodule.".
    
    //public interface IJobs
    //{
    //    void assignTask();
    //    void workOnTask();

    //    void assignBreak();
    //}
    public interface IAssignJob
    {
        void assignTask();
        
    }
    public interface IWorkTask
    {
        void workOnTask();
    }
    public interface IAssignBreak
    {
        void assignBreak();
    }
    public class Programmer: IWorkTask
    {
        //public void assignTask()
        //{
        //    Console.WriteLine("Cannot assign Task.");
        //}
        public void workOnTask()
        {
            Console.WriteLine("Work on Task.");
        }
        //public void assignBreak()
        //{
        //    Console.WriteLine("Cannot assign break.");
        //}
    }
    public class TeamLead : IAssignJob, IWorkTask
    {
        public void assignTask()
        {
            Console.WriteLine("Can Assign task.");
        }
        public void workOnTask()
        {
            Console.WriteLine("Can work on task.");
        }
        //public void assignBreak()
        //{
        //    Console.WriteLine("cannot assign break.");
        //}
    }
    public class Manager: IAssignJob, IAssignBreak
    {
        public void assignTask()
        {
            Console.WriteLine("Can assign task.");
        }
        //public void workOnTask()
        //{
        //    Console.WriteLine("Cannot work on task.");
        //}   
        public void assignBreak()
        {
            Console.WriteLine("Can assign  break.");
        }
    }
}
