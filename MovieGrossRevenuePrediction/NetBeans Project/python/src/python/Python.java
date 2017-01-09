/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package python;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author geekdon
 */
public class Python {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) throws IOException, InterruptedException {
        MovieGross g = new MovieGross();
        g.run();
        /*
        String filename = "regression_v9_multi_wls_gui";
       // filename = "hello";
        String name = "/home/geekdon/Desktop/MovieData/code/"+filename+".py";
        String cmd = "python "+name;
        System.out.println(cmd);
        ProcessBuilder pb = new ProcessBuilder("/home/geekdon/miniconda2/bin/python",name);
        
        Process p = pb.start();
       
        BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
         String s = null;
        
         while ((s = in.readLine()) != null) {
                System.out.println(s);
            }
        
         
        */
    }
    
}
