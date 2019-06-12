import java.util.*;
import java.lang.*;
import java.io.*;
public class Square
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int a11=sc.nextInt();
		int b11=sc.nextInt();
		int a21=sc.nextInt();
		int b21=sc.nextInt();
		int a31=sc.nextInt();
		int b31=sc.nextInt();
		int a41=sc.nextInt();
		int b41=sc.nextInt();
		if(a11==a21&&a31==a41&&b11==b41&&b21==b31)
		{
			System.out.println("yes");
		}
		else
		{
			System.out.println("no");
		}
	}
}
