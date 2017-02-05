package dreya.torrent;

import java.io.IOException;
import java.util.ArrayList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import dreya.Config;
import java.io.File;

/**
 *
 * @author smv
 */
public class SubtitleDownloader {
    
    
    public void check()
    {
        ArrayList<MkvFile> files = this.loadFiles();
        this.checkFeliratokInfo(files);        
    }
    
    
    private ArrayList<MkvFile> loadFiles()
    {
        ArrayList<MkvFile> files = new ArrayList<MkvFile>(); 
        
        File folder = new File(Config.showsFolder);
        File[] listOfFiles = folder.listFiles();

        for (File listOfFile : listOfFiles) {
            if (listOfFile.isFile()) {
                
                MkvFile newFile = new MkvFile(listOfFile.getName());
                if (newFile.isValidWithoutSrt())
                {
                    files.add(newFile);
                }
            } 
        }        
        
        
        return files;
        
    }

    private void checkFeliratokInfo(ArrayList<MkvFile> files)
    {
        try
        {
            Document doc = Jsoup.connect("http://www.feliratok.info/").get();
            Elements rows = doc.getElementsByAttributeValue("id", "vilagit");
            
            
            rows.forEach((Element row) -> {
                try
                {
                    Elements links = row.getElementsByTag("a");

                    String srtHref = links.get(1).attr("href");
                    String rowContent = row.text();
                    
                    files.forEach((file) -> {
                        file.checkSubtitle(rowContent,srtHref);
                    });                    
                    
                }
                catch (Exception ex) {
                    System.out.println("[error] "+ex.getMessage());
                }
            });
            
            files.forEach((file) -> {
                file.download();
            });                  
        }
        catch (IOException ex)
        {
            System.out.println("[error] "+ex.getMessage());
        }
        
    }
}
