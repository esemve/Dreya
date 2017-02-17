package dreya;

import dreya.notification.BkkNotification;
import dreya.notification.HolidayNotification;
import dreya.messenger.WebServer;
import dreya.serial.SerialReader;
import dreya.torrent.EzRSSParser;
import dreya.torrent.SubtitleDownloader;
import java.util.Calendar;
import dreya.security.Security;
import java.io.File;


/**
 *
 * @author smv
 */
public class DreyaWork {
    
    public DreyaWork()
    {
        
        System.out.println("[info] working directory: "+System.getProperty("user.dir"));
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
            SerialReader sr = new SerialReader();
            Thread serialReaderThread = new Thread(sr);
            serialReaderThread.start();
        }
        catch (Exception ex)
        {
            System.out.println("A soros port olvasó inicializálása nem sikerült!");
        }
        
        

        Security security = new Security();
        Thread securityThread = new Thread(security);
        securityThread.start(); 
        
        BkkNotification bkk = new BkkNotification();
        Thread bkkThread = new Thread(bkk);
        bkkThread.start();
        
        EzRSSParser torrentRssParser = new EzRSSParser();
        Thread torrentRssParserThread = new Thread(torrentRssParser);
        torrentRssParserThread.start();
        
        SubtitleDownloader subtitle = new SubtitleDownloader();
        Thread subtitleThread = new Thread(subtitle);
        subtitleThread.start();
        
        try
        {
            this.work();
        }
        catch (InterruptedException ex) { }
    }
    
    public void work() throws InterruptedException
    {
        HolidayNotification holydayNotification = new HolidayNotification();        
        
        int counter = 0;
        while (true)
        {
            
            counter++;
            
            Calendar now = Calendar.getInstance();
            int hour = now.get(Calendar.HOUR_OF_DAY);
            int min = now.get(Calendar.MINUTE);
            int sec = now.get(Calendar.SECOND);
            
            if ((hour==10) & (min==5) & (sec==0))
            {
                holydayNotification.check();
            }
            
            if ((hour==0) | (hour==1) | (hour==2) | (hour==3))
            {
                File f = new File("noturnoff");
                if(f.exists() && !f.isDirectory()) { 
                        // Ne kapcsoljon ki a rendszer
                }
                else
                {
                    Thread.sleep(1000);
                    System.exit(0);
                }
            }

            Thread.sleep(1000);
            
            if (counter==1200)
            {
                counter = 0;
            }
        }         
    }
    
}
