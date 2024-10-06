using System;

class Program
{
    static void Main(string[] args)
    {
        double A = 0, B = 0, C = 0;
        if (args.Length == 3){
            if (!double.TryParse(args[0], out A)){
                Console.WriteLine("Некорректный коэффициент A.");
                return;
            }
            if (!double.TryParse(args[1], out B)){
                Console.WriteLine("Некорректный коэффициент B.");
                return;
            }
            if (!double.TryParse(args[2], out C)){
                Console.WriteLine("Некорректный коэффициент C.");
                return;
            }
        }
        else{
            A = InputCoefficient("A");
            B = InputCoefficient("B");
            C = InputCoefficient("C");
        }

        SolveBiquadraticEquation(A, B, C);
    }
    static double InputCoefficient(string name){
        double coefficient;
        while (true){
            Console.Write($"Введите коэффициент {name}: ");
            if (double.TryParse(Console.ReadLine(), out coefficient)){
                return coefficient;
            }
            else{
                Console.WriteLine("Некорректное значение, попробуйте снова.");
            }
        }
    }

    static void SolveBiquadraticEquation(double A, double B, double C){
        if (A == 0){
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Это не биквадратное уравнение (A не может быть равно 0).");
            Console.ResetColor();
            return;
        }
        double D = B * B - 4 * A * C;

        if (D < 0){
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Корней нет.");
        }
        else{
            double sqrtD = Math.Sqrt(D);
            double z1 = (-B + sqrtD) / (2 * A);
            double z2 = (-B - sqrtD) / (2 * A);
            Console.ForegroundColor = ConsoleColor.Green;
            if (z1 >= 0){
                if (z1 != 0){
                    double x3 = Math.Sqrt(z1);
                    double x4 = -Math.Sqrt(z1);
                    Console.WriteLine($"Корни уравнения: x1 = {x3}, x2 = {x4}");
                }
                else{
                    double x3 = Math.Sqrt(z1);
                    Console.WriteLine($"Корни уравнения: x1 = {x3}");
                }
            }

            if (z2 >= 0 && z2!=z1){
                if (z2 != 0) {
                    double x3 = Math.Sqrt(z2);
                    double x4 = -Math.Sqrt(z2);
                    Console.WriteLine($"Корни уравнения: x3 = {x3}, x4 = {x4}");
                }
                else{
                    double x3 = Math.Sqrt(z2);
                    Console.WriteLine($"Корни уравнения: x3 = {x3}");
                }
            }
            if (z1 < 0 && z2 < 0){
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Действительных корней нет.");
            }
        }
        Console.ResetColor();
    }
}
