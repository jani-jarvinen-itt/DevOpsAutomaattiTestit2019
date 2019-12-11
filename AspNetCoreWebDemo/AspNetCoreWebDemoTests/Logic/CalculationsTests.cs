using Microsoft.VisualStudio.TestTools.UnitTesting;
using AspNetCoreWebDemo.Logic;
using System;
using System.Collections.Generic;
using System.Text;

namespace AspNetCoreWebDemo.Logic.Tests
{
    [TestClass()]
    public class CalculationsTests
    {
        [TestMethod()]
        public void SumTest()
        {
            Calculations calc = new Calculations();
            int a = 100;
            int b = 200;

            int sum = calc.Sum(a, b);
            int expected = a + b;

            Assert.AreEqual(expected, sum);
        }
    }
}