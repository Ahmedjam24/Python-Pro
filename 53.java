import java.util.*;
import java.lang.*;
import java.io.*;
public class Pangram
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc1=new Scanner(System.in);
		String s1=sc1.nextLine();
		char ch1[]=s1.toCharArray();
		int n1=s1.length();
		int count=0;
		for(int i='a';i<='z';i++)
		{
			for(int j=0;j<n1;j++)
			{
				if(i==ch1[j])
				{
					count++;
					j=n1;
				}
			}
		}
		if(count==26)
		{
			System.out.println("yes");
		}
		else
		{
			System.out.println("no");
		}
	}
}
