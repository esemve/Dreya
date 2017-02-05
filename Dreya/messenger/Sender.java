package dreya.messenger;

import dreya.Config;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import org.json.JSONObject;

/**
 *
 * @author smv
 */
public class Sender {
    
    public void Sender()
    {
    }
    
    public static void send(String recipient, String content)
    {
        try
        {
            JSONObject jo = new JSONObject();
            jo.put("recipient", recipient);
            jo.put("message", content);
           
            String data = URLEncoder.encode("payload", "UTF-8") + "=" + URLEncoder.encode(jo.toString(), "UTF-8");

            URL url = new URL(Config.messengerSenderGateway);
            HttpURLConnection http = (HttpURLConnection)url.openConnection();
            http.setRequestMethod("POST"); 

            
            http.setDoOutput(true);
            OutputStreamWriter wr = new OutputStreamWriter(http.getOutputStream());
            wr.write(data);
            wr.flush();        
            wr.close();
            
            int statusCode = http.getResponseCode();     
            http.disconnect();            
        }
        catch (Exception ex) {
            
        }
    }
    
}
