package dreya.torrent;

import dreya.Config;
import java.net.URL;
import java.util.Iterator;
import java.util.List;
 
import com.sun.syndication.feed.synd.SyndEntry;
import com.sun.syndication.feed.synd.SyndFeed;
import com.sun.syndication.io.FeedException;
import com.sun.syndication.io.SyndFeedInput;
import com.sun.syndication.io.XmlReader;
import java.io.IOException;
import com.sun.syndication.feed.synd.SyndEnclosureImpl;

/**
 *
 * @author smv
 */
public class EzRSSParser implements Runnable {
    
    public EzRSSParser() {        
    }
    
    public void check() 
    {

       System.setProperty("http.agent", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"); 
       try
        {
            String url = Config.ezRss;

            SyndFeed feed = new SyndFeedInput().build(new XmlReader(new URL(url)));
            //System.out.println(feed.getTitle());        

            List entries = feed.getEntries();
            Iterator itEntries = entries.iterator();

            while (itEntries.hasNext()) {
                    SyndEntry entry = (SyndEntry) itEntries.next();
                    String title = entry.getTitle();
                    
                    List enclosures = entry.getEnclosures();
                    
                    Iterator<SyndEnclosureImpl> iterator = enclosures.iterator();

                    while (iterator.hasNext()) {
                        SyndEnclosureImpl item = iterator.next();                      
                        String torrentUrl = item.getUrl();
                        
                        Iterator<Series> slist = Config.seriesList.iterator();
                        while (slist.hasNext()) {
                            Series series = slist.next();
                            series.check(title,torrentUrl);
                        }
                    }                    
            }
        }
        catch (FeedException | IOException | IllegalArgumentException ex) { 
            System.out.println("[error] "+ex.getMessage());
        }
                
    }

    @Override
    public void run() {
        
        while (true)
        {
            try {
                this.check();                
                Thread.sleep(1800000);
            } catch (InterruptedException ex) {
                System.out.println("[error] EzRSSParser Thread error: "+ex.getMessage());
            }
        }
        
        
    }
    
}
