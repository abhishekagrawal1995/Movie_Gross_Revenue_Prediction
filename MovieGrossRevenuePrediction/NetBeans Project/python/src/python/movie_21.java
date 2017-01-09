/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package python;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author geekdon
 */
public class movie_21 extends javax.swing.JFrame {

    /**
     * Creates new form movie_21
     */
    
    ArrayList <String> features = new ArrayList <String> ();
    HashMap <String,ArrayList <Integer> > combination = new HashMap <String, ArrayList <Integer> > ();
    ArrayList<String> genre;
    Set<Integer> required = new HashSet<Integer>();
    String title;
    @SuppressWarnings("empty-statement")
    void initialsefeatures()
    {
        
        features.add("Budget");
        features.add("Opening weekend");
        features.add("Screens");
        
        features.add("MetaScore");
        features.add("Popularity");
        features.add("Imdb_Rating");
        features.add("Tomato Meter");
        features.add("Tomato Rating");
        
        features.add("User Meter");
        features.add("User Rating");
        
        features.add("User Reviews");
        /// 	combination = {'Mystery': [0, 1, 4, 10], 'Romance': [0, 1, 10], 
        //'Sport': [0, 1, 3, 4, 6, 7], 'Sci-Fi': [1], 'Family': [0, 1, 4, 7, 10], 'Horror': [1, 10], 'Thriller': [0, 1], 'Crime': [0, 1], 'Drama': [0, 1, 4], 'Fantasy': [0, 1, 2, 4, 9], 'Animation': [0, 1], 'Music': [0, 1, 6, 10], 'Adventure': [0, 1], 'Action': [1, 4], 'Comedy': [0, 1], 'Documentary': [4, 7, 9, 10], 'Biography': [0, 1, 3, 4, 6, 7], 'History': [1, 4, 7]}
        
        
        combination. put("Action", new ArrayList<Integer>() {{add(1);add(4);}});
        combination. put("Adventure", new ArrayList<Integer>() {{add(0);add(1);}});
        combination. put("Horror", new ArrayList<Integer>() {{add(1);add(10);}});
        combination. put("Romance", new ArrayList<Integer>() {{add(0);add(1);add(10);}});
        combination. put("Sport", new ArrayList<Integer>() {{add(0);add(1);add(3);add(4);add(6);add(7);}});
        combination. put("Mystery", new ArrayList<Integer>() {{add(0);add(1);add(4);add(10);}});
        combination. put("Sci-Fi", new ArrayList<Integer>() {{add(1);}});
        combination. put("Family", new ArrayList<Integer>() {{add(0);add(1);add(4);add(7);add(10);}});
        combination. put("Thriller", new ArrayList<Integer>() {{add(0);add(1);}});
        combination. put("Crime", new ArrayList<Integer>() {{add(0);add(1);}});
        combination. put("Drama", new ArrayList<Integer>() {{add(0);add(1);add(4);}});
        combination. put("Fantasy", new ArrayList<Integer>() {{add(0);add(1);add(2);add(4);add(9);}});
        combination. put("Animation", new ArrayList<Integer>() {{add(0);add(1);}});
        combination. put("Comedy", new ArrayList<Integer>() {{add(0);add(1);}});
        combination. put("Music", new ArrayList<Integer>() {{add(0);add(1);add(6);add(10);}});
        combination. put("Documentary", new ArrayList<Integer>() {{add(4);add(7);add(9);add(10);}});
        combination. put("History", new ArrayList<Integer>() {{add(1);add(4);add(7);}});
        combination. put("Biography", new ArrayList<Integer>() {{add(0);add(1);add(3);add(4);add(6);add(7);}});
        
        for(String i:genre){
            ArrayList<Integer> com = combination.get(i);
            for(int j:com){
               required.add(j);
            }
        }
        
        required.add(2);
        required.add(1);
        required.add(7);
        System.out.println(required);
        if(required.contains(0)){
            jTextField1.setEditable(true);
            jTextField1.setText("Enter in ($)");
            jLabel3.setText("Budget **");
       }
        else{
            jTextField1.setText("Nil");
           jTextField1.setEditable(false);
        }
        if(required.contains(1)){
            jTextField2.setEditable(true);
            jTextField2.setText("Enter in ($)");
            jLabel4.setText("Opening Weekend **");
       }
        else{
            jTextField2.setText("Nil");
           jTextField2.setEditable(false);
        }
        if(required.contains(2)){
            jTextField3.setEditable(true);
            jTextField3.setText("Enter...");
            jLabel5.setText("Screens **");
       }
        else{
            jTextField3.setText("Nil");
           jTextField3.setEditable(false);
        }
        if(required.contains(3)){
            jTextField4.setEditable(true);
            jTextField4.setText("Enter...");
            jLabel6.setText("MetaScore **");
       }
        else{
            jTextField4.setText("Nil");
           jTextField4.setEditable(false);
        }
        if(required.contains(4)){
            jTextField10.setEditable(true);
            jTextField10.setText("Enter...");
            jLabel12.setText("Imdb_Popularity **");
       }
        else{
            jTextField10.setText("Nil");
           jTextField10.setEditable(false);
        }
         if(required.contains(5)){
            jTextField7.setEditable(true);
            jTextField7.setText("Enter...");
            jLabel9.setText("Imdb_Rating **");
       }
         else{
             jTextField7.setText("Nil");
           jTextField7.setEditable(false);
         }
          if(required.contains(6)){
            jTextField5.setEditable(true);
            jTextField5.setText("Enter...");
            jLabel7.setText("Tomato Meter **");
       }
          else{
              jTextField5.setText("Nil");
           jTextField5.setEditable(false);
          }
       if(required.contains(7)){
            jTextField6.setEditable(true);
            jTextField6.setText("Enter...");
            jLabel8.setText("Tomato Rating **");
       }
       else{
           jTextField6.setText("Nil");
           jTextField6.setEditable(false);
       }
       
        if(required.contains(8)){
            jTextField8.setEditable(true);
            jTextField8.setText("Enter...");
            jLabel10.setText("User Meter **");
       }
        else{
            jTextField8.setText("Nil");
           jTextField8.setEditable(false);
        }
        
         if(required.contains(9)){
            jTextField9.setEditable(true);
            jTextField9.setText("Enter...");
            jLabel11.setText("User Rating **");
       }
         else{
             jTextField9.setText("Nil");
           jTextField9.setEditable(false);
         }
          if(required.contains(10)){
            jTextField11.setEditable(true);
            jTextField11.setText("Enter...");
            jLabel13.setText("Tomato_Popularity **");
       }
          else{
           jTextField11.setText("Nil");
              jTextField11.setEditable(false);
          }
    }
    
    public movie_21(String title, ArrayList <String> genre) {
        initComponents();
        this.genre = genre;
        this.title = title;
        initialsefeatures();
        this.jTextArea1.setText(title);
        this.setVisible(true);
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        jTextField1 = new javax.swing.JTextField();
        jTextField2 = new javax.swing.JTextField();
        jTextField3 = new javax.swing.JTextField();
        jTextField4 = new javax.swing.JTextField();
        jTextField5 = new javax.swing.JTextField();
        jTextField6 = new javax.swing.JTextField();
        jTextField7 = new javax.swing.JTextField();
        jTextField8 = new javax.swing.JTextField();
        jTextField9 = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jTextField10 = new javax.swing.JTextField();
        jTextField11 = new javax.swing.JTextField();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        jLabel17 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        jLabel1 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel1.setLayout(null);

        jLabel2.setFont(new java.awt.Font("Comic Sans MS", 1, 18)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(223, 15, 15));
        jLabel2.setText("Movie Title:");
        jPanel1.add(jLabel2);
        jLabel2.setBounds(170, 10, 130, 70);

        jTextArea1.setColumns(20);
        jTextArea1.setRows(5);
        jScrollPane1.setViewportView(jTextArea1);

        jPanel1.add(jScrollPane1);
        jScrollPane1.setBounds(320, 20, 262, 50);

        jTextField1.setText("jTextField1");
        jTextField1.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jTextField1MouseClicked(evt);
            }
        });
        jTextField1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextField1ActionPerformed(evt);
            }
        });
        jPanel1.add(jTextField1);
        jTextField1.setBounds(190, 220, 86, 28);

        jTextField2.setText("jTextField2");
        jTextField2.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jTextField2MouseClicked(evt);
            }
        });
        jTextField2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextField2ActionPerformed(evt);
            }
        });
        jPanel1.add(jTextField2);
        jTextField2.setBounds(190, 260, 86, 28);

        jTextField3.setText("jTextField3");
        jTextField3.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jTextField3MouseClicked(evt);
            }
        });
        jPanel1.add(jTextField3);
        jTextField3.setBounds(190, 300, 86, 28);

        jTextField4.setText("jTextField4");
        jPanel1.add(jTextField4);
        jTextField4.setBounds(440, 120, 86, 28);

        jTextField5.setText("jTextField5");
        jPanel1.add(jTextField5);
        jTextField5.setBounds(440, 160, 86, 28);

        jTextField6.setText("jTextField6");
        jPanel1.add(jTextField6);
        jTextField6.setBounds(440, 200, 86, 28);

        jTextField7.setText("jTextField7");
        jPanel1.add(jTextField7);
        jTextField7.setBounds(420, 330, 86, 28);

        jTextField8.setText("jTextField8");
        jPanel1.add(jTextField8);
        jTextField8.setBounds(420, 370, 86, 28);

        jTextField9.setText("jTextField9");
        jPanel1.add(jTextField9);
        jTextField9.setBounds(420, 410, 86, 28);

        jLabel5.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(237, 39, 39));
        jLabel5.setText("Screens(Integer)");
        jPanel1.add(jLabel5);
        jLabel5.setBounds(10, 300, 180, 21);

        jLabel4.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(219, 23, 23));
        jLabel4.setText("Open Weekend($)");
        jPanel1.add(jLabel4);
        jLabel4.setBounds(10, 260, 180, 21);

        jLabel3.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(222, 17, 17));
        jLabel3.setText("Budget($)");
        jPanel1.add(jLabel3);
        jLabel3.setBounds(10, 210, 170, 40);

        jLabel6.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel6.setForeground(new java.awt.Color(226, 16, 16));
        jLabel6.setText("MetaScore");
        jPanel1.add(jLabel6);
        jLabel6.setBounds(330, 130, 91, 21);

        jLabel7.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel7.setForeground(new java.awt.Color(230, 17, 17));
        jLabel7.setText("Tomato Meter");
        jPanel1.add(jLabel7);
        jLabel7.setBounds(310, 170, 119, 21);

        jLabel8.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel8.setForeground(new java.awt.Color(238, 42, 42));
        jLabel8.setText("Tomato Rating");
        jPanel1.add(jLabel8);
        jLabel8.setBounds(310, 200, 124, 21);

        jLabel9.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel9.setForeground(new java.awt.Color(237, 10, 10));
        jLabel9.setText("IMDB Rating");
        jPanel1.add(jLabel9);
        jLabel9.setBounds(290, 330, 107, 21);

        jLabel10.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel10.setForeground(new java.awt.Color(231, 20, 20));
        jLabel10.setText("User Meter");
        jPanel1.add(jLabel10);
        jLabel10.setBounds(290, 370, 93, 21);

        jLabel11.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel11.setForeground(new java.awt.Color(219, 32, 32));
        jLabel11.setText("User Rating");
        jPanel1.add(jLabel11);
        jLabel11.setBounds(290, 410, 98, 21);

        jTextField10.setText("jTextField10");
        jPanel1.add(jTextField10);
        jTextField10.setBounds(710, 230, 94, 28);

        jTextField11.setText("jTextField11");
        jPanel1.add(jTextField11);
        jTextField11.setBounds(720, 280, 94, 28);

        jLabel12.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel12.setForeground(new java.awt.Color(240, 15, 15));
        jLabel12.setText("IMDB_Popularity");
        jPanel1.add(jLabel12);
        jLabel12.setBounds(550, 240, 144, 21);

        jLabel13.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel13.setForeground(new java.awt.Color(220, 19, 19));
        jLabel13.setText("Tomato_Popularity");
        jPanel1.add(jLabel13);
        jLabel13.setBounds(550, 280, 161, 21);

        jLabel15.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel15.setForeground(new java.awt.Color(95, 229, 29));
        jLabel15.setText("Critic View");
        jPanel1.add(jLabel15);
        jLabel15.setBounds(310, 90, 130, 30);

        jLabel16.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel16.setForeground(new java.awt.Color(61, 234, 17));
        jLabel16.setText("User View");
        jPanel1.add(jLabel16);
        jLabel16.setBounds(320, 300, 110, 30);

        jLabel14.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel14.setForeground(new java.awt.Color(122, 217, 32));
        jLabel14.setText("Basic Features");
        jPanel1.add(jLabel14);
        jLabel14.setBounds(20, 180, 150, 30);

        jLabel17.setFont(new java.awt.Font("Ubuntu", 3, 18)); // NOI18N
        jLabel17.setForeground(new java.awt.Color(106, 233, 27));
        jLabel17.setText("Popularity");
        jPanel1.add(jLabel17);
        jLabel17.setBounds(570, 200, 110, 40);

        jButton1.setFont(new java.awt.Font("Comic Sans MS", 1, 36)); // NOI18N
        jButton1.setText("Estimate");
        jButton1.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                jButton1MouseReleased(evt);
            }
        });
        jPanel1.add(jButton1);
        jButton1.setBounds(570, 350, 190, 90);

        jLabel1.setIcon(new javax.swing.ImageIcon("/home/geekdon/Downloads/rsz_movies-tad.jpg")); // NOI18N
        jLabel1.setText("T");
        jPanel1.add(jLabel1);
        jLabel1.setBounds(0, 0, 1213, 576);

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 835, 577));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1MouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jButton1MouseReleased
        // TODO add your handling code here:
        // TODO add your handling code here:
        String fin = "",temp;
        /// Budget
        temp = jTextField1.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        
        temp = jTextField2.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField3.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField4.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField10.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField7.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField5.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField6.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField8.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField9.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        fin = fin + ",";
        
        temp = jTextField11.getText().toString();
        if (!temp.equals("Nil")) {
            fin = fin + temp;
        } else {
            fin = fin + "0";
        }
        
        String gen = "";
        for (String i:genre) {
            gen = gen + i + ",";
        }
        int si = gen.length();
        gen = gen.substring(0,si-1);
       // System.out.println(gen);
       // System.out.println(fin);
        this.setVisible(false);
        try {      
            Movie_Output1 obj = new Movie_Output1(this.title,gen,fin);
        } catch (IOException ex) {
            Logger.getLogger(movie_2.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_jButton1MouseReleased

    private void jTextField1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextField1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jTextField1ActionPerformed

    private void jTextField1MouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jTextField1MouseClicked
        // TODO add your handling code here:
        jTextField1.setText("");
    }//GEN-LAST:event_jTextField1MouseClicked

    private void jTextField2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextField2ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jTextField2ActionPerformed

    private void jTextField2MouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jTextField2MouseClicked
        // TODO add your handling code here:
        jTextField2.setText("");
    }//GEN-LAST:event_jTextField2MouseClicked

    private void jTextField3MouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jTextField3MouseClicked
        // TODO add your handling code here:
         jTextField3.setText("");
    }//GEN-LAST:event_jTextField3MouseClicked

    private void jTextField4MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField4.setText("");
    }                                        
private void jTextField5MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField5.setText("");
    }                                        
private void jTextField6MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField6.setText("");
    }                                        
private void jTextField7MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField7.setText("");
    }                                        
private void jTextField8MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField8.setText("");
    }                                        

   private void jTextField9MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField9.setText("");
    }                                        
private void jTextField10MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField10.setText("");
    }                                        

private void jTextField11MouseClicked(java.awt.event.MouseEvent evt) {                                         
        // TODO add your handling code here:
         jTextField11.setText("");
    }                                        

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel16;
    private javax.swing.JLabel jLabel17;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextArea1;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextField jTextField10;
    private javax.swing.JTextField jTextField11;
    private javax.swing.JTextField jTextField2;
    private javax.swing.JTextField jTextField3;
    private javax.swing.JTextField jTextField4;
    private javax.swing.JTextField jTextField5;
    private javax.swing.JTextField jTextField6;
    private javax.swing.JTextField jTextField7;
    private javax.swing.JTextField jTextField8;
    private javax.swing.JTextField jTextField9;
    // End of variables declaration//GEN-END:variables
}
