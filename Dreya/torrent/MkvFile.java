package dreya.torrent;

import dreya.Config;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import dreya.messenger.Sender;

/**
 *
 * @author smv
 */
public class MkvFile {
    private String filename;

    private int subtitleMaxScore = 0;
    private String subtitleUrl = "";
    
    private int season = 0;
    private int episode = 0;
    
    private String s_season = "";
    private String s_episode = "";
    
    
    public MkvFile(String filename)
    {
        this.filename = filename;
        
        Pattern MY_PATTERN = Pattern.compile("S[0-9].E[0-9].");
        Matcher m = MY_PATTERN.matcher(filename);
        
        if (m.find())
        {
            String seepcode = m.group();
            seepcode = seepcode.toLowerCase();
            seepcode = seepcode.replace("s","");
            
            String[] parts = seepcode.split("e");
            
            this.season = Integer.parseInt(parts[0]);
            this.episode = Integer.parseInt(parts[1]);
        }
    }
    
    public boolean isValidWithoutSrt()
    {
        if (this.filename.length()>3)
        {
            
            if ("mkv".equals(this.filename.substring(this.filename.length() - 3)))
            {
                
                String srtFile = this.getSrtFileName();
                
                File f = new File(Config.showsFolder+srtFile);
                return !(f.exists() && !f.isDirectory());
            }
        }
        
        return false;
    }
    
    private String getSrtFileName()
    {
        return this.filename.substring(0,this.filename.length()-3)+"srt";
    }
    
    public void checkSubtitle(String content, String href)
    {
        
        String filename = this.filename.toLowerCase();
        content = content.toLowerCase();
        
        String s_ep = this.episode+"";        
        String d_ep = this.episode+"";
        if (this.episode<10)
        {
            d_ep = "0"+this.episode;
        }
        this.s_episode = d_ep;
        String s_se = this.season+"";        
        String d_se = this.season+"";
        if (this.season<10)
        {
            d_se = "0"+this.season;
        }
        this.s_season = d_se;
        
        if (content.contains("magyar"))
        {
            content = content.replace("[", " ");
            content = content.replace("]", " ");
            content = content.replace("(", " ");
            content = content.replace(")", " ");            
            content = content.replace(".", " ");
            content = content.replace(",", " ");
            content = content.replace("-", " ");
            
            while (!content.equals(content.replace("  "," ")))
            {
                content = content.replace("  ", " ");    
            }
            
           
            if (content.contains(" "+s_se+"x"+d_ep+" "))
            {
                int score = 0;
                String[] parts = content.split(" ");
                 
                for (String part: parts)
                {
                    if (filename.contains(part))
                    {
                         score++;
                    }
                }
                
                if (score>this.subtitleMaxScore)
                {
                    this.subtitleMaxScore = score;
                    this.subtitleUrl = href;
                }
            }
            
            
            
           
        }
    }
    
    public void download()
    {
        boolean hasSeries = false;
        
        if (this.subtitleMaxScore>0)
        {
            try
            {
                
                List<Series> seriesList = Config.seriesList;
              
                for (Series series : seriesList)
                {
                    if (this.filename.toLowerCase().contains(series.getSubtitleText().toLowerCase()))
                    {
                        
                        Sender.send("", series.getName()+" "+this.s_season+"x"+this.s_episode+" magyar felirat letöltve!");
                        hasSeries = true;
                    }
                }
                
                if (!hasSeries)
                {
                    Sender.send("", this.getSrtFileName()+" magyar felirat letöltve!");
                }
                
                System.setProperty("http.agent", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"); 

                URL website = new URL("http://feliratok.info"+this.subtitleUrl);
                ReadableByteChannel rbc = Channels.newChannel(website.openStream());
                FileOutputStream fos = new FileOutputStream(Config.showsFolder+this.getSrtFileName());
                fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);                        
            }
            catch (IOException ex) {
                System.out.println("[error] "+ex.getMessage());
            }
        }
    }
    
}
