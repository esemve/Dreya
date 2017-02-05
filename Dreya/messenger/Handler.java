package dreya.messenger;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.net.URLDecoder;

import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import dreya.question.TextParser;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.json.JSONException;
import org.json.JSONObject;

/**
 *
 * @author smv
 */
public class Handler extends AbstractHandler
{
    @Override
    public void handle( String target,
                        Request baseRequest,
                        HttpServletRequest request,
                        HttpServletResponse response ) throws IOException,
                                                      ServletException
    {
        
        // Declare response encoding and types
        response.setContentType("text/html; charset=utf-8");

        // Declare response status code
        response.setStatus(HttpServletResponse.SC_OK);
        
        String query = request.getQueryString();
        query = query.replace("payload=", "");
        query = URLDecoder.decode(query, "UTF-8");
        
        JSONObject jo;
        try {
            jo = new JSONObject(query);
            String sender = jo.getString("sender");
            String message = jo.getString("message");
            
            TextParser parse = new TextParser(sender, message);
            String answer = parse.getAnswer();
            response.getWriter().println(answer+"");
            
                    
        } catch (JSONException ex) {
            Logger.getLogger(Handler.class.getName()).log(Level.SEVERE, null, ex);
        }

        
        
        // Write back response
        //response.getWriter().println(text);

        // Inform jetty that this request has now been handled
        baseRequest.setHandled(true);
    }

}