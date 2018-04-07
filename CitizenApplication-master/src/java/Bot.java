/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Rohit
 */
@WebServlet(urlPatterns = {"/Bot"})
public class Bot extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
       
        response.setContentType("text/plain;charset=UTF-8");
        
        System.out.println("level -> "+request.getParameter("level"));
        String input= request.getParameter("level");
        int level=Integer.parseInt(input);
        
        try (PrintWriter out = response.getWriter()) 
        {
            String query,sql;
            
            Connection conn = null;
            
            String url = "jdbc:mysql://localhost/";
            String dbName = "citizen";
            String driver = "com.mysql.jdbc.Driver";
            String userName = "root"; 
            String password = "root";
            
            Class.forName(driver);
            
            System.out.println("*****test*****");
            
            conn = DriverManager.getConnection(url+dbName,userName,password);		
            Statement st;
            st = conn.createStatement();
        
            System.out.println("Level -> "+level);
            
            
            switch(level)
            {
                
                case 1:
                    query=request.getParameter("location");
                    if(!query.equals(""))
                    {
                        out.print("1");
                        out.print("*");
                        try 
                        {
                            sql = ("SELECT name FROM politician WHERE constituency='"+query+"'");
                            ResultSet rs;
                            rs = st.executeQuery(sql);
                            sql="";
                            while(rs.next()) 
                            { 
                               out.print(rs.getString("name"));
                               out.print("<br>");
                            }
                        }
                        catch(Exception e)
                        {
                            System.out.println(e);
                        }
                        out.close();
                    }
                    else
                    {
                        out.print("-1");
                        out.print("*");
                    }
                    break;
                
                case 2:
                    query=request.getParameter("name");
                    if(!query.equals(""))
                    {
                        out.print("1");
                        out.print("*");
                        try 
                        {
                            sql = ("SELECT DISTINCT rating, positive_comment, negative_comment, category_name FROM politician INNER JOIN (comments INNER JOIN category) WHERE politician.p_id= comments.p_id AND category.c_id=comments.c_id AND politician.name='"+query+"'");
                            ResultSet rs;
                            
                            rs = st.executeQuery(sql);
                            int a=0;
                            
                            while(rs.next())
                            {
                                if(a==0)
                                {
                                    out.print("Rating: ");
                                    out.print(rs.getString("rating"));
                                    out.print("*");
                                    a++;
                                }
                                if(!(rs.getString("positive_comment").equals("")))
                                {
                                    out.print("<b>Positive Comments- "+rs.getString("category_name")+"</b>");
                                    out.print("<br>");
                                    out.print(rs.getString("positive_comment"));
                                    out.print("<br>");
                                    out.print("------------");
                                    out.print("<br>");
                                }
                                if(!(rs.getString("negative_comment").equals("")))
                                {
                                out.print("<br>");
                                out.print("<b>Negative Comments- "+rs.getString("category_name")+"</b>");
                                out.print("<br>");
                                out.print(rs.getString("negative_comment"));
                                out.print("<br>");
                                out.print("------------");
                                out.print("<br>");
                                }
                                
                            }
                            out.close();
                        }
                        
                        catch(Exception e)
                        {
                            out.print("-1");
                            out.print("*");
                        }
                    }
                    else
                    {
                        out.print("-1");
                        out.print("*");
                    }
                    break;
                case 3:
                    query="GET CATEGORIES";
                    if(!query.equals(""))
                    {
                        out.print("1");
                        out.print("*");
                        try 
                        {
                            sql = ("SELECT * FROM category");
                            ResultSet rs;
                            
                            rs = st.executeQuery(sql);
                            int a=0;
                            
                            while(rs.next())
                            {
                                if(!(rs.getString("category_name").equals("")))
                                {
                                    out.print("<b>"+rs.getString("category_name")+"</b>");
                                    out.print("<br>");
                                }
                                
                            }
                            out.close();
                        }
                        
                        catch(Exception e)
                        {
                            out.print("-1");
                            out.print("*");
                        }
                    }
                    else
                    {
                        out.print("-1");
                        out.print("*");
                    }
                    break;
                    
                case 7:
                    String positiveComment = request.getParameter("positiveComment");
                    String negativeComment = request.getParameter("negativeComment");
                    System.out.println(positiveComment);
                    String pName = request.getParameter("pName");
                    String category = request.getParameter("category");
                    float rating = Float.parseFloat(request.getParameter("rating"));
                    int pId;
                    int cId;
                    int sqlResp;
                    ResultSet rs;                            

                    try{
                        sql = ("SELECT * FROM politician WHERE name='"+pName+"'");
                        System.out.println(sql);
                        rs = st.executeQuery(sql);
                        rs.next();
                        System.out.println("foo");
                        pId = rs.getInt("p_id");
//                        pId = 2;
                        System.out.println("foo");
                        sql = ("SELECT * FROM category WHERE category_name='"+category+"'");
                        System.out.println("fooo");    
                        rs = st.executeQuery(sql);
                        System.out.println("fooooo");
                        rs.next();
                        cId = rs.getInt("c_id");
                        System.out.println("foooooooo");
                        if(rating != 0)
                        {
                            out.print("1");
                            out.print("*");
                            try 
                            {
                                System.out.println(pId);
                                System.out.println(cId);
                                System.out.println(positiveComment);
                                System.out.println(negativeComment);
                                sql = ("INSERT INTO comments VALUES("+pId+",'"+positiveComment+"','"+negativeComment+"',"+cId+")");
                                System.out.println(sql);
                                st.execute(sql);

                                // Update the rating

                                // Success
                                out.print("1");
                                out.print("*");
                                out.close();
                            }

                            catch(Exception e)
                            {
                                out.print("-1");
                                out.print("*");
                            }
                        }
                        else
                        {
                            out.print("-1");
                            out.print("*");
                        }
                    }
                    catch(Exception e){
                        out.print("-1");
                        e.printStackTrace();
                        out.print("*");
                    }
                   
                    
                        
                    break;
                    
                default:
                          
            }
            
                
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
