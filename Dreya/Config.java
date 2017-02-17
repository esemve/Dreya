package dreya;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import dreya.torrent.Series;
import java.util.ArrayList;
import java.util.List;
import dreya.notification.Holiday;



/**
 *
 * @author smv
 */
public class Config {
    
    public static String messengerSenderGateway = "";
    public static String showsFolder = "";
    public static String ezRss = "";
    public static String cameraIp = "";
    public static String cameraUserPass = "";
    public static String showsTorrentFolder = "";
    public static List<Series> seriesList = new ArrayList<Series>();
    public static String workDir = "";
    public static String dataDir = "";
    public static ArrayList<String> bkk = new ArrayList<String>();
    public static ArrayList<Holiday> events = new ArrayList<Holiday>();
    
    public static void init()
    {
        
        Config.workDir = System.getProperty("user.dir");
        Config.dataDir = System.getProperty("user.dir")+"/data/";
        
        String configFile = Config.workDir+"/config.xml";
        System.out.println("[info] Config file beolvasása innen: "+configFile);      
             
        try
        {
            File fXmlFile = new File(configFile);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(fXmlFile);
            doc.getDocumentElement().normalize();
            
            Config.messengerSenderGateway = doc.getElementsByTagName("messengerSenderGateway").item(0).getTextContent();
            Config.showsFolder = doc.getElementsByTagName("showsFolder").item(0).getTextContent();
            Config.ezRss = doc.getElementsByTagName("ezRss").item(0).getTextContent();
            Config.showsTorrentFolder = doc.getElementsByTagName("showsTorrentFolder").item(0).getTextContent();
            Config.cameraIp = doc.getElementsByTagName("cameraIp").item(0).getTextContent();
            Config.cameraUserPass = doc.getElementsByTagName("cameraUserPass").item(0).getTextContent();
            
            NodeList nList = doc.getElementsByTagName("series");
            
            for (int temp = 0; temp < nList.getLength(); temp++) {

		Node nNode = nList.item(temp);

		if (nNode.getNodeType() == Node.ELEMENT_NODE) {

			Element eElement = (Element) nNode;

			String name = eElement.getElementsByTagName("name").item(0).getTextContent();
                        String torrentTitle = eElement.getElementsByTagName("torrentTitle").item(0).getTextContent();
                        String subtitleText = eElement.getElementsByTagName("subtitleText").item(0).getTextContent();
                        String notIn = eElement.getElementsByTagName("notIn").item(0).getTextContent();
                        
                        Series series = new Series(name, torrentTitle.toLowerCase(), subtitleText.toLowerCase(), notIn.toLowerCase());
                        Config.seriesList.add(series);
                        
		}      
            }


            NodeList bkkList = doc.getElementsByTagName("line");
            for (int temp = 0; temp < bkkList.getLength(); temp++) {
                Node bkkNode = bkkList.item(temp);
                bkkNode.normalize();
                if (bkkNode.getNodeType() == bkkNode.ELEMENT_NODE) {
                    Element bkkElement = (Element) bkkNode;

                    bkkElement.normalize();
                    if (bkkElement.getTextContent()!=null)
                    {
                        String content = bkkElement.getTextContent();
                        Config.bkk.add(temp, content);
                    }
                }
            }
            
            NodeList eventList = doc.getElementsByTagName("event");
            for (int temp = 0; temp < eventList.getLength(); temp++) {
                Node eventNode = eventList.item(temp);
                eventNode.normalize();
                if (eventNode.getNodeType() == eventNode.ELEMENT_NODE) {
                    Element eventElement = (Element) eventNode;
                    eventElement.normalize();
                    if (eventElement.getTextContent()!=null)
                    {
                        Holiday holiday = new Holiday();
                        holiday.month = eventElement.getAttribute("month");
                        holiday.day = eventElement.getAttribute("day");
                        holiday.name = eventElement.getTextContent();
                        Config.events.add(temp, holiday);
                    }
                }
            }
            
            
            System.out.println("[info] Config file feldolgozva");
            
        }
        catch (Exception ex) { 
            System.out.println("[error] "+ex.getMessage());
        }
    }    
}
