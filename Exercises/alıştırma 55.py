
import calendar # burada programa calender modülü dahil edildi.

c=calendar.TextCalendar(calendar.MONDAY) # burada c isminde bir değişken tanımlandı. bu değişkene Textcalender
# fonskiyonu kullanılarak birinci argümana takvimi yani calender ikinci parametreye de o takvimin hangi gün ile
# başladığını MONDAY yazdık.

c.prmonth(2018,7) # yukarıda c değişkeninde tanımlanan takvim kullanılrak, 2018 yılının 7. ayını aldık.

c.pryear(2018) # burada ise 2018 yılının tamamının aldık.