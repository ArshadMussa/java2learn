package pt.c03java.s03excecao.s01basico;

import java.util.Scanner;

public class App05bExcecaoDivisaoZero
{
    public static void main(String args[])
    {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite o numerador: ");
        String xs = teclado.nextLine();
        
        System.out.print("Digite o denominador: ");
        String ys = teclado.nextLine();
        
        teclado.close();

        imprime(xs, ys);
    }
    
	public static void imprime(String xs, String ys) {
		int divisao = divide(xs, ys);
		System.out.println("Resultado da divisao: " + divisao);
	}
	
    // movendo o parseInt para o terceiro nível
	 public static int divide(String xs, String ys)
    {
        int x = Integer.parseInt(xs),
            y = Integer.parseInt(ys);
        
        int divisao;

        divisao = x / y;
            
        return divisao;
    }
}
