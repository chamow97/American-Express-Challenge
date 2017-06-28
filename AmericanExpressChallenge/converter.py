import csv,sys,os
project_dir="/AmericanExpressChallenge/";
sys.path.append(project_dir)

os.environ['DJANGO_SETTING_MODULE'] = 'settings'
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AmericanExpressChallenge.settings")
django.setup()
from credit_card.models import credit_card_details
data=csv.reader(open('a.csv'), delimiter=',')
for row in data:
	if row[0] != 'ID':
		ccd = credit_card_details()
		ccd.user_id = row[0]
		ccd.name = row[1]
		ccd.limit_bal = row[2]
		ccd.sex = row[3]
		ccd.education = row[4]
		ccd.marriage = row[5]
		ccd.age = row[6]
		ccd.pay_0 = row[7]
		ccd.pay_2 = row[8]
		ccd.pay_3 = row[9]
		ccd.pay_4 = row[10]
		ccd.pay_5 = row[11]
		ccd.pay_6 = row[12]
		ccd.bill_amt_1 = row[13]
		ccd.bill_amt_2 = row[14]
		ccd.bill_amt_3 = row[15]
		ccd.bill_amt_4 = row[16]
		ccd.bill_amt_5 = row[17]
		ccd.bill_amt_6 = row[18]
		ccd.save()