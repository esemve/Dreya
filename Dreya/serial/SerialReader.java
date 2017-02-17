package dreya.serial;

import java.io.BufferedReader;
import java.io.FileReader;

/**
 *
 * @author smv
 */
public class SerialReader implements Runnable {
    
    
    public static String[] port = new String[2];
    public static FileReader fr;
    public static BufferedReader br;
    public static boolean motion = false;
    public static String temp = "";
    public static String key1 = "0";
    public static String key2 = "0";    
    
    public void run()
    {
        
        int counter = 0;
        SerialReader.port[0] = "/dev/ttyACM0";
        SerialReader.port[1] = "/dev/ttyACM1";
        
        while (true)
        {
        
            String port = SerialReader.port[counter];
            try
            {
                SerialReader.fr.close();
                SerialReader.br.close();
            }
            catch (Exception ex) { }

            try  {
               
                
                SerialReader.fr = new FileReader(port);
                SerialReader.br = new BufferedReader(fr);
                String line;
                
                while (true)
                {
                   line = br.readLine();
                   
                   String inputLine = line;
                   
                    if ("motion".equals(inputLine))
                    {

                        SerialReader.motion = true;
                    }
                    else if ("nomotion".equals(inputLine))
                    {
                        SerialReader.motion = false;
                    } 
                    else
                    {

                        String[] testLine = inputLine.split(" ");    
                        if (null != testLine[0])
                        switch (testLine[0]) {
                            case "temp":
                                SerialReader.temp = testLine[1];
                                break;
                            case "key1":
                                SerialReader.key1 = testLine[1];
                                break;
                            case "key2":
                                SerialReader.key2 = testLine[1];
                                break;
                            default:
                                break;
                        }

                    }
   
                   
                   if ("null".equals(line))
                   {
                       SerialReader.br.close();
                       SerialReader.fr.close();
                       throw new Exception("[SerialReader.1.error] Megszakadt a serial port!");
                   }
                }
                
                
            }
            catch (Exception ex)        
            {
                try
                {
                    SerialReader.br.close();
                    SerialReader.fr.close();                
                }
                catch (Exception ex2) { 
                    System.out.println("[SerialReader.2.error] "+ex2.getMessage());
                }
                System.out.println("[SerialReader.3.error] "+ex.getMessage());
            }
            try
            {
                Thread.sleep(1000);                                   
            }
            catch (Exception ex)
            {
                System.out.println("[error] "+ex.getMessage());
            }
            
            counter++;
            if (counter>=SerialReader.port.length)
            {
                counter = 0;
            }
            
        }
        
    }

}
