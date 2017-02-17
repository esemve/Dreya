package dreya.torrent;

import java.io.IOException;
import java.util.ArrayList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import dreya.Config;
import java.io.File;
import java.util.List;

/**
 *
 * @author smv
 */
public class SubtitleDownloader implements Runnable {
    
    
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
                    
                    
                    files.forEach((MkvFile file) -> {
                        
                        List<Series> seriesList = Config.seriesList;

                        for (Series series : seriesList)
                        {
                            if (rowContent.toLowerCase().contains(series.getSubtitleText().toLowerCase()))
                            {
                                
                                String[] parts = series.getTorrentTitle().toLowerCase().split(" ");
                                
                                boolean allpartsok = true;
                                
                                for (String part : parts)
                                {
                                    if (!file.getFileName().toLowerCase().contains(part))
                                    {
                                        allpartsok = false;
                                    }                                    
                                }
                                
                                if (allpartsok)
                                {
                                    file.checkSubtitle(rowContent,srtHref);                            
                                }
                            }
                        }                        
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

    @Override
    public void run() {
        while (true)
        {
            try {
                this.check();
                Thread.sleep(1800000);
            } catch (InterruptedException ex) {
                System.out.println("[error] Subtitledownloader Thread error: "+ex.getMessage());
            }
        }
    }
}
