
import os

# if __name__ == '__main__':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blogs.settings')
#     import django
#     django.setup()
#     from blog import models
#
#     from datetime import date,timedelta,datetime
#     import time
#     from blog import models
#     date_list = []
#     def get_all_dates(date1,date2):
#
#         the_date = date(int(date1.split('-')[0]),int(date1.split('-')[1]),int(date1.split('-')[2]))
#         end_date = date(int(date2.split('-')[0]),int(date2.split('-')[1]),int(date2.split('-')[2]))
#         days = timedelta(days=1)
#         while the_date <= end_date:
#             yield the_date.strftime('%Y-%m-%d')
#             the_date = the_date + days
#             print(the_date)
#     now = datetime.now()
#     nextweek = now + timedelta(days = 7)
#     nextweek_str = nextweek.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
#     now_str = now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
#     print(now_str.split(" ")[0])
#     print(nextweek_str.split(" ")[0])
#
#     for i in get_all_dates(str(now_str) ,str(nextweek_str)):
#         date_list.append(i)
#     print(date_list)
#     from django.db.models import Count
#     for date in date_list:
#         visit_num_list = models.Index_page.objects.filter(visit_time__day=date).annotate(c=Count("visit_num")).values("visit_time__day", "c")
from datetime import date, timedelta, datetime
def get_all_dates(date1,date2):
    the_date = date(int(date1.split('-')[0]),int(date1.split('-')[1]),int(date1.split('-')[2]))
    end_date = date(int(date2.split('-')[0]),int(date2.split('-')[1]),int(date2.split('-')[2]))
    days = timedelta(days=1)
    while the_date <= end_date:
        yield the_date.strftime('%Y-%m-%d')
        the_date = the_date + days