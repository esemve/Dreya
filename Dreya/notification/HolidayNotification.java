package dreya.notification;

import dreya.Config;
import dreya.messenger.Messenger;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

/**
 *
 * @author smv
 */
public class HolidayNotification {
    
    public HolidayNotification()
    {
        
    }

    public void check() {
        Calendar now = Calendar.getInstance();
        
        Date datum = new GregorianCalendar(Calendar.YEAR, Calendar.MONTH-1, Calendar.DAY_OF_MONTH+1).getTime();
        int todayOfYear = Integer.parseInt(new SimpleDateFormat("D").format(datum));
        
        
        for (Holiday holiday: Config.events)
        {
            int checkDay = Integer.parseInt(holiday.day);
            int checkMonth = Integer.parseInt(holiday.month);
            
            datum = new GregorianCalendar(Calendar.YEAR, checkMonth-1, checkDay).getTime();
            int checkDayOfYear = Integer.parseInt((new SimpleDateFormat("D").format(datum)));

            if (checkDayOfYear==todayOfYear)
            {
                Messenger.sendMessage("", "Ma van "+holiday.name+"!");
                continue;                
            }
            
            if (checkDayOfYear==todayOfYear+3)
            {
                Messenger.sendMessage("", "3 nap múlva "+holiday.name+"!");
                continue;                
            }
            
            if (checkDayOfYear==todayOfYear+7)
            {
                Messenger.sendMessage("", "Egy hét múlva "+holiday.name+"!");
                continue;                
            }            
            
            if (checkDayOfYear==todayOfYear+14)
            {
                Messenger.sendMessage("", "Két hét múlva "+holiday.name+"!");
                continue;                
            }                        
            
            if (checkDayOfYear==todayOfYear+31)
            {
                Messenger.sendMessage("", "31 nap múlva "+holiday.name+"!");
                continue;                
            }            
            
        }
    }
    
    
}
