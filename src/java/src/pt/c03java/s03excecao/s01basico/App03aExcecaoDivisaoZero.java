package pt.c03java.s03excecao.s01basico;

import java.util.Scanner;

public class App03aExcecaoDivisaoZero
{
    public static void main(String args[])
    {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite o numerador: ");
        String xs = teclado.nextLine();
        
        System.out.print("Digite o denominador: ");
        String ys = teclado.nextLine();
        
        teclado.close();

        int x = Integer.parseInt(xs),
            y = Integer.parseInt(ys);
        
        int divisao = divide(x, y);
        System.out.println("Resultado da divisao: " + divisao);
    }
    
    // erro no módulo
    public static int divide(int x, int y)
    {
        int divisao;

        divisao = x / y;
            
        return divisao;
    }
}
