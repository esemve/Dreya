package dreya.torrent;

import dreya.Config;
import dreya.Database;
import dreya.messenger.Sender;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author smv
 */
public class Series implements java.io.Serializable  {
    
    private String name = "";
    private String torrentTitle = "";
    private String subtitleText = ""; 
    private String notIn = "";
    
    public int episode = 0;
    public int season = 0;
    
    public Series(String name, String torrentTitle, String subtitleText, String notIn)
    {
        this.name = name;
        this.torrentTitle = torrentTitle;
        this.subtitleText = subtitleText;
        this.notIn = notIn;  
        
        this.episode = Integer.parseInt(Database.get(this.name+".episode", "0"));
        this.season = Integer.parseInt(Database.get(this.name+".season", "0"));
    }
    
    public String getName()
    {
        return this.name;
    }
    
    public String getSubtitleText()
    {
        return this.subtitleText;
    }
    
    
    public String getTorrentTitle()
    {
        return this.torrentTitle;
    }
    
    public void check(String title, String url)
    {
        title = title.toLowerCase();
        
        
        if ((title.contains(this.torrentTitle)) & (title.contains("720p")))
        {
            if (("".equals(this.notIn)) | (!title.contains(this.notIn)))
            {
                this.download(url);
            }
        }
    }
    
    
    public void download(String url)
    {
        
        String[] urlParts = url.split("/");
        String fileName = urlParts[urlParts.length-1];
        
        System.setProperty("http.agent", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"); 
        
        Pattern MY_PATTERN = Pattern.compile("S[0-9].E[0-9].");
        Matcher m = MY_PATTERN.matcher(fileName);
        
        if (m.find())
        {
            String seepcode = m.group();
            seepcode = seepcode.toLowerCase();
            seepcode = seepcode.replace("s","");
            
            String[] parts = seepcode.split("e");
            
            int testSeason = Integer.parseInt(parts[0]);
            int testEpisode = Integer.parseInt(parts[1]);
            
            if ((testSeason>this.season) | ((testSeason==this.season) & (testEpisode>this.episode))) { 
                try
                {
                    
                    URL website = new URL(url);
                    ReadableByteChannel rbc = Channels.newChannel(website.openStream());
                    FileOutputStream fos = new FileOutputStream(Config.showsTorrentFolder+fileName);
                    fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);        
                    
                    this.episode = testEpisode;
                    this.season = testSeason;
                    
                    
                    Database.save(this.name+".episode", this.episode+"");
                    Database.save(this.name+".season", this.season+"");
                    Database.store();
                          
                    String d_ep = this.episode+"";
                    if (this.episode<10)
                    {
                        d_ep = "0"+this.episode;
                    }
                    String d_se = this.season+"";
                    if (this.season<10)
                    {
                        d_se = "0"+this.season;
                    }
                    
                    
                    Sender.send("", this.getName()+" "+d_se+"x"+d_ep+" rész letöltve!");
                    
                    System.out.println("[info] Letöltve: "+url);
                    
                }
                catch (IOException ex) {
                    System.out.println("[error] "+ex.getMessage());
                }            
            }
            
        }
    }
    
}
