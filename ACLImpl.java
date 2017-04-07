
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner; 

public class ACLImpl{
    public static void main(String[] args) throws IOException,NullPointerException {
        FileInputStream fstream = new FileInputStream("/Users/Keerthana/Desktop/infile.txt");
        DataInputStream in = new DataInputStream(fstream);
        BufferedReader br = new BufferedReader(new InputStreamReader(in));

        String strLine;
        int arraySize = 6;
        String array[][] = new String[arraySize][];
        int index = 0;
        while ((strLine = br.readLine()) != null) {
   
            if (index >= arraySize - 1) {
                System.out.println("Error : Increase array size !");
                break;
            }
            array[index] = strLine.split("\t");
            index++;
   
        }

        printAll(array);
        readSecond(array);

 }

 static void printAll(String array[][]) {
 	System.out.println("\n---------------Access Control List-------------\n");
    for (int i = 0; i < array.length; i++) {
    if (array[i] != null) {
    for (int j = 0; j < array[i].length; j++) {
        System.out.print(array[i][j] + " ");
    }
    System.out.println(" ");
   }
  }

 }

 static void readSecond(String array[][]) throws FileNotFoundException,NullPointerException {
 	FileInputStream filestream = new FileInputStream("/Users/Keerthana/Desktop/infile2.txt");
    DataInputStream infil = new DataInputStream(filestream);
    BufferedReader brnew = new BufferedReader(new InputStreamReader(infil));
    int secSize = 6;
    String secondarray[][] = new String[secSize][];
    try {
        String x;
        int secondindex = 0;
        while ( (x = brnew.readLine()) != null ) {
            // Printing out each line in the file
            System.out.println(x);
            secondarray[secondindex] = x.split("\t");
            secondindex++;
        }
       // System.out.println("testing new loop");
        String srcaddr[] = new String[10];
        int k = 0;
        for (int i = 0; i < secondarray.length; i++) {
    		if (secondarray[i] != null) {
   				for (int j = 0; j < secondarray[i].length; j++) {
   					if (j == 0 ) {
   							srcaddr[k] = secondarray[i][j];
   							k++;
   							//System.out.print(secondarray[i][j] + " ");
      						//System.out.println("\n");

   					}
      				
    			}
    			//System.out.println("\n");
   			}
  		}
  		// mask array 
  		String mask[] = new String[10];
  		String addr[] = new String[10];

  		  		int ke = 0,ae = 0;
  		for (int i = 0; i < array.length; i++) {
   			 if (array[i] != null) {
    			for (int j = 0; j < array[i].length; j++) {
    				if (j == 3 ) {
   							addr[ae] = array[i][j];
   							
   							System.out.println("Address in ACL : ");
   							System.out.print(addr[ae] + " ");
   							ae++;
      						//System.out.println("\n");
      					}
        			if (j == 4 ) {
   							mask[ke] = array[i][j];
   							
   							System.out.println("\nMask: ");
   							System.out.print(mask[ke] + " ");
   							ke++;
      						//System.out.println("\n");
      					}
      				}
      				System.out.println("\n");
      			}
      		}
      		


      		// mask operation 
      
  		// src address array  

  		System.out.println("Src Addresses: ");
  				for (int i = 0, u = 0; i <= array.length ; u++,i++){
  					System.out.print(srcaddr[u] + " ");
  					if ((srcaddr[u] != null) && (srcaddr[u].equals(array[i][3]))){
  						System.out.print(array[i][2] + "\n");
  					}
  					else if ((srcaddr[u] != null) && (array[i][3].contains(srcaddr[i].subSequence(0, srcaddr[i].length() - 2))) && (array[i][4].equals("0.0.0.255"))){
  						System.out.print(array[i][2] + "\n");

  					
  				}
  				//else{
  				//	System.out.print( " Allow \n");
  				//}
  			}	
    }
    catch (IOException e) {
        e.printStackTrace();
    }
 }
}