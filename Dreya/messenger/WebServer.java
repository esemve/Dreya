package dreya.messenger;

import org.eclipse.jetty.server.Server;

/**
 *
 * @author smv
 */
public class WebServer implements Runnable
{
  
    public void WebServer()
    {
        
    }
    

    
    public void run()
    {
        try
        {
            Server server = new Server(18080);
            server.setHandler(new Handler());

            server.start();
            server.join();        
        }
        catch (Exception ex)
        {
            System.out.println(ex.getMessage());
        }

        
    }
}