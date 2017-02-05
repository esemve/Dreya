package dreya;

import dreya.messenger.WebServer;
import dreya.miners.Bkk;
import dreya.torrent.EzRSSParser;
import dreya.torrent.SubtitleDownloader;
import java.util.Calendar;


/**
 *
 * @author smv
 */
public class DreyaWork {
    
    public DreyaWork()
    {
        
        Database.restore();
        Config.init();

        
        try
        {
            WebServer ws = new WebServer();
            Thread t = new Thread(ws);
            t.start();
        }
        catch (Exception ex)
        {
            System.out.println("A WebServer inicializálása nem sikerült!");
        }
                
        
        try
        {
            this.work();
        }
        catch (InterruptedException ex) { }
        
    }
    
    public void work() throws InterruptedException
    {
        
        int counter = 0;
        Bkk bkk = new Bkk();
        EzRSSParser torrentRssParser = new EzRSSParser();
        SubtitleDownloader subtitle = new SubtitleDownloader();
        
        while (true)
        {
            counter++;
            if (counter>1200)
            {
                counter = 0;
            }
            
            Calendar now = Calendar.getInstance();
            int hour = now.get(Calendar.HOUR_OF_DAY);
            int min = now.get(Calendar.MINUTE);
            int sec = now.get(Calendar.SECOND);
            
            //System.out.println(Integer.toString(hour)+":"+Integer.toString(min)+':'+Integer.toString(sec));
            
            if (counter==120)            
            {
                
                torrentRssParser.check();
            }
            
            if (counter==200)
            {
                subtitle.check();                
            }
            
            if (counter==500)
            {
                bkk.run();
            }
            
            Thread.sleep(1000);
            
        }         
    }
    
}
