package dreya.notification;

import dreya.Config;
import dreya.Database;
import dreya.messenger.Messenger;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

/**
 *
 * @author smv
 */
public class BkkNotification  implements Runnable {
    
    int lastBkkNews = 0;
    
    public BkkNotification()
    {
        this.lastBkkNews = Integer.parseInt(Database.get("lastBkkAlert", "0"));
    }
    
    public void check()
    {
        try
        {
            int last = 0;
            int counter = 0;
            
            Document doc = Jsoup.connect("https://twitter.com/bkkbudapest").get();
            Elements rows = doc.getElementsByClass("content");
            
            
            for (Element row: rows) {

                int time = Integer.parseInt(row.getElementsByClass("_timestamp").attr("data-time"));
                String tweet = row.getElementsByClass("tweet-text").text();
                
                
                if (time>this.lastBkkNews)
                {
                    boolean interest = false;
                    
                    
                    for (String line: Config.bkk)
                    {
                        if (tweet.toLowerCase().contains(line.toLowerCase()))
                        {
                            interest = true;
                            break;
                        }
                    }

                    if (interest)                    
                    {
                        counter++;
                        if (counter<4)
                        {
                            Messenger.sendMessage("", tweet);
                            if (time>last)
                            {
                                last = time;
                            }
                        }
                    }

                }
            }
            
            if ((last>0) & (last>lastBkkNews))
            {
                this.lastBkkNews = last;
                Database.save("lastBkkAlert", this.lastBkkNews+"");
                Database.store();
            }
        }
        catch (IOException ex)
        {
            System.out.println("[error] "+ex);
        }
    }

    @Override
    public void run() {
        while (true)
        {
            try {
                this.check();    
                Thread.sleep(900000);
            } catch (InterruptedException ex) {
                System.out.println("[error] BKKNotification Thread error: "+ex.getMessage());
            }
        }        
    }
}
    

