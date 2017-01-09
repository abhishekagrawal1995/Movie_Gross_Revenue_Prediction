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
public class movie_2 extends javax.swing.JFrame {

    /**
     * Creates new form movie_2
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
        System.out.println(required);
        if(required.contains(0)){
            jTextField1.setEditable(true);
            jTextField1.setText("Enter....");
            jLabel1.setText("Budget **");
       }
        else{
            jTextField1.setText("Nil");
           jTextField1.setEditable(false);
        }
        if(required.contains(1)){
            jTextField2.setEditable(true);
            jTextField2.setText("Enter...");
            jLabel2.setText("Opening Weekend **");
       }
        else{
            jTextField2.setText("Nil");
           jTextField2.setEditable(false);
        }
        if(required.contains(2)){
            jTextField3.setEditable(true);
            jTextField3.setText("Enter...");
            jLabel3.setText("Screens **");
       }
        else{
            jTextField3.setText("Nil");
           jTextField3.setEditable(false);
        }
        if(required.contains(3)){
            jTextField4.setEditable(true);
            jTextField4.setText("Enter...");
            jLabel4.setText("MetaScore **");
       }
        else{
            jTextField4.setText("Nil");
           jTextField4.setEditable(false);
        }
        if(required.contains(4)){
            jTextField7.setEditable(true);
            jTextField7.setText("Enter...");
            jLabel7.setText("Imdb_Popularity **");
       }
        else{
            jTextField7.setText("Nil");
           jTextField7.setEditable(false);
        }
         if(required.contains(5)){
            jTextField9.setEditable(true);
            jTextField9.setText("Enter...");
            jLabel9.setText("Imdb_Rating **");
       }
         else{
             jTextField9.setText("Nil");
           jTextField9.setEditable(false);
         }
          if(required.contains(6)){
            jTextField5.setEditable(true);
            jTextField5.setText("Enter...");
            jLabel5.setText("Tomato Meter **");
       }
          else{
              jTextField5.setText("Nil");
           jTextField5.setEditable(false);
          }
       if(required.contains(7)){
            jTextField6.setEditable(true);
            jTextField6.setText("Enter...");
            jLabel6.setText("Tomato Rating **");
       }
       else{
           jTextField6.setText("Nil");
           jTextField6.setEditable(false);
       }
       
        if(required.contains(8)){
            jTextField10.setEditable(true);
            jTextField10.setText("Enter...");
            jLabel10.setText("User Meter **");
       }
        else{
            jTextField10.setText("Nil");
           jTextField10.setEditable(false);
        }
        
         if(required.contains(9)){
            jTextField11.setEditable(true);
            jTextField11.setText("Enter...");
            jLabel11.setText("User Rating **");
       }
         else{
             jTextField11.setText("Nil");
           jTextField6.setEditable(false);
         }
          if(required.contains(10)){
            jTextField8.setEditable(true);
            jTextField8.setText("Enter...");
            jLabel8.setText("Tomato_Popularity **");
       }
          else{
           jTextField8.setText("Nil");
              jTextField8.setEditable(false);
          }
    }
    
    public movie_2(String title, ArrayList <String> genre) {
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

        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        jLabel1 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jTextField2 = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        jTextField3 = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        jTextField4 = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        jTextField5 = new javax.swing.JTextField();
        jLabel6 = new javax.swing.JLabel();
        jTextField6 = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        jTextField7 = new javax.swing.JTextField();
        jLabel8 = new javax.swing.JLabel();
        jTextField8 = new javax.swing.JTextField();
        jLabel9 = new javax.swing.JLabel();
        jTextField9 = new javax.swing.JTextField();
        jLabel10 = new javax.swing.JLabel();
        jTextField10 = new javax.swing.JTextField();
        jLabel11 = new javax.swing.JLabel();
        jTextField11 = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jLabel14 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel16 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jTextArea1.setColumns(20);
        jTextArea1.setRows(5);
        jScrollPane1.setViewportView(jTextArea1);

        jLabel1.setText("Budget");

        jTextField1.setText("jTextField1");
        jTextField1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextField1ActionPerformed(evt);
            }
        });

        jLabel2.setText("Opening weekend");

        jTextField2.setText("jTextField2");

        jLabel3.setText("Screens");

        jTextField3.setText("jTextField3");

        jLabel4.setText("MetaScore");

        jTextField4.setText("jTextField4");

        jLabel5.setText("Tomato Meter");

        jTextField5.setText("jTextField5");

        jLabel6.setText("Tomato Rating");

        jTextField6.setText("jTextField6");

        jLabel7.setText("Imdb_Popularity");

        jTextField7.setText("jTextField7");

        jLabel8.setText("Tomato_Popularity");

        jTextField8.setText("jTextField8");

        jLabel9.setText("Imdb_Rating");

        jTextField9.setText("jTextField9");

        jLabel10.setText("User Meter");

        jTextField10.setText("jTextField10");

        jLabel11.setText("User Rating");

        jTextField11.setText("jTextField11");

        jButton1.setText("Estimate");
        jButton1.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                jButton1MouseReleased(evt);
            }
        });
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jLabel12.setText("Title of Movie");

        jLabel13.setText("Movie Features");

        jLabel14.setText("Critic View");

        jLabel15.setText("User View");

        jLabel16.setText("Popularity");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(43, 43, 43)
                        .addComponent(jLabel12)
                        .addGap(6, 6, 6)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 320, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel1)
                                    .addComponent(jLabel2)
                                    .addComponent(jLabel3))
                                .addGap(4, 4, 4)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jTextField3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(jLabel6))
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                        .addComponent(jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(jLabel5))
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                        .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(jLabel14)
                                            .addComponent(jLabel4))))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTextField4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jTextField6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jTextField5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addComponent(jLabel13, javax.swing.GroupLayout.Alignment.LEADING))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel9)
                            .addComponent(jLabel10)
                            .addComponent(jLabel11)
                            .addComponent(jLabel15))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jTextField11, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jTextField10, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jTextField9, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel7)
                            .addComponent(jLabel8))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jTextField8, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jTextField7, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addComponent(jLabel16))
                .addGap(37, 37, 37))
            .addGroup(layout.createSequentialGroup()
                .addGap(113, 113, 113)
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 484, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(4, 4, 4)
                .addComponent(jLabel16)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel7)
                            .addComponent(jTextField7, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel8)
                            .addComponent(jTextField8, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel15))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(8, 8, 8)
                                .addComponent(jLabel12))
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel13)
                            .addComponent(jLabel14))))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4)
                    .addComponent(jTextField4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel9)
                    .addComponent(jTextField9, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel5)
                    .addComponent(jTextField5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel10)
                    .addComponent(jTextField10, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(jLabel3)
                        .addComponent(jTextField3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(jLabel6)
                        .addComponent(jTextField6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(jLabel11)
                        .addComponent(jTextField11, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(33, 33, 33)
                .addComponent(jButton1)
                .addContainerGap(23, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jTextField1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextField1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jTextField1ActionPerformed

    private void jButton1MouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jButton1MouseReleased
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
        
        temp = jTextField7.getText().toString();
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
        
        temp = jTextField10.getText().toString();
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
        fin = fin + ",";
        
        temp = jTextField8.getText().toString();
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
            Movie_Output obj = new Movie_Output(this.title,gen,fin);
        } catch (IOException ex) {
            Logger.getLogger(movie_2.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_jButton1MouseReleased

    /**
     * @param args the command line arguments
     */
    /*
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
     /*   try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(movie_2.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(movie_2.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(movie_2.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(movie_2.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
      /*  java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new movie_2().setVisible(true);
            }
        });
    }*/

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
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
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
