#!usr/bin/python3.7
# -*- coding: utf-8 -*-

''' 
  SC                    : AUTO UP ID DGN 9 LINK :V
  CREATED BY : DULLAH
  FB                   :  HTTPS://WWW.FACEBOOK.COM/DULAHZ
  GIT                  : HTTPS://GITHUB.COM/DZ-ID
  TELEGRAM   : HTTPS://T.ME/UNIKERS
  
  SEBELUM UP ID MANDI DULU BIAR MANJUR :V
  JGN LUPA UP TIAP HARI GAN BIAR BANGKIT AKUNNYA
  KEMUNGKINAN KALO DATA DI AKUN SAMA DGN DATA DI ID/SIM/KTP BAKALAN BANGKIT
  KALO GAK BANGKIT LUPAKAN AJA AKUNNYA. BIKIN YANG BARU HEHE GITU AJA KOK REPOT :V
  
'''

import os, sys, time, mechanize, requests
from bs4 import BeautifulSoup as parser
from threading import *

class utama:
	def __init__(self):
		self.banner()
	
	def banner(self):
		os.system('clear')
		print('''\033[0;96m
   ___       __       __  __     ____   __
  / _ |__ __/ /____  / / / /__  /  _/__/ / \033[0mCreated By DulLah\033[0;96m
 / __ / // / __/ _ \/ /_/ / _ \_/ // _  /  \033[0m©Copyright-2019\033[0;96m
/_/ |_\_,_/\__/\___/\____/ .__/___/\_,_/   \033[0mT.me/unikers\033[0;96m
  \033[0;91m For Disabled Account\033[0;96m  /_/ \033[0;91mWith 9 Link :v\033[0m''')     #//
		print('\033[0m_'*62)
		self.URL = 'https://m.facebook.com/help/contact/{}'
		self.main()
	
	def main(self):
		self.name = input("\nYour full name as it's listed on the account : ")
		if self.name == '':
			sys.exit('\033[0;91mCan not be empty.\033[0m')
		self.email = input('Email address or mobile phone number : ')
		if self.email == '':
			sys.exit('\033[0;91mCan not be empty.\033[0m')
		print('\033[0;91mFormat day-month-year ex : 2-12-2002\033[0m')
		date = input('Date of birth  : ').split('-')
		self.day = int(date[0])
		self.month = int(date[1])
		self.year = int(date[2])
		year = time.strftime('%Y')
		if self.day > 31 or self.day < 1 or self.month > 12 or self.month < 1 or self.year > int(year) or self.year < 1905:
			sys.exit('\033[0;91mSTUPPID, Format day-month-year.\033[0m')
		self.words = input('Addtional info : ')
		if self.words == '':
			sys.exit('\033[0;91mCan not be empty.\033[0m')
		self.file = input('Your photo ID  : ')
		self.settings()
	
	def settings(self):
		self.br = mechanize.Browser()
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True) 
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
		self.br.addheaders = [('User-Agent', 'Mozilla / 5.0 (Linux; U; Android 2.2) AppleWebKit / 533.1 (KHTML, seperti Gecko) Versi / 4.0 Mobile Safari / 533.1')]
		#//
		self.up01()
		self.up02()
		self.up03()
		self.up04()
		self.up05()
		self.up06()
		self.up07()
		self.up08()
		self.up09()
		#//
		sys.exit('\nFinished.')
		
	def up01(self):
		file = open(self.file,'rb')
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/260749603972907\033[0m]')
		self.br.open(self.URL.format('260749603972907'))
		self.br.select_form(nr=0)
		self.br.form['Field707360896076073'] = self.email
		self.br.form['full_name'] = self.name
		self.br.form.add_file(file, 'image/jpeg', self.file, id='693845437294697')
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up02(self):
		file = open(self.file,'rb')
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/183000765122339\033[0m]')
		self.br.open(self.URL.format('183000765122339'))
		self.br.select_form(nr=0)
		self.br.form['Field678538712279760'] = self.email
		self.br.form.add_file(file, 'image/jpeg', self.file, id='356294444474458')
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up03(self):
		file = open(self.file,'rb')
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/269030579858086\033[0m]')
		self.br.open(self.URL.format('269030579858086'))
		self.br.select_form(nr=0)
		self.br.form['Field273693622723960'] = self.email
		self.br.form['Field260611300702356'] = self.words
		self.br.form.add_file(file, 'image/jpeg', self.file, id='421668857843132')
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up04(self):
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/317389574998690\033[0m]')
		self.br.open(self.URL.format('317389574998690'))
		self.br.select_form(nr=0)
		self.br.form['Field140788082712931'] = self.name
		self.br.form['Field226645094102714[year]'] = [str(self.year)]
		self.br.form['Field226645094102714[month]'] = [str(self.month)]
		self.br.form['Field226645094102714[day]'] = [str(self.day)]
		self.br.form['Field214373345339617'] = self.words
		self.br.form['Field1600842126807382'] = self.email
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up05(self):
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/313733425335072\033[0m]')
		self.br.open(self.URL.format('313733425335072'))
		self.br.select_form(nr=0)
		self.br.form['Field216574035102555'] = self.name
		self.br.form['Field104274806588293'] = self.email
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up06(self):
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/487444654660670\033[0m]')
		self.br.open(self.URL.format('487444654660670'))
		self.br.select_form(nr=0)
		self.br.form['name'] = self.name
		self.br.form['Customer_Email_from_Form__c'] = self.email
		self.br.form['email'] = self.email
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up07(self):
		file = open(self.file,'rb')
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/122145551250439\033[0m]')
		self.br.open(self.URL.format('122145551250439'))
		self.br.select_form(nr=0)
		self.br.form['Field267909233296634'] = self.name
		self.br.form['Field1140757832607422'] = self.email
		self.br.form['Field359383984101112'] = self.words
		self.br.form.add_file(file, 'image/jpeg', self.file, id='299297596810876')
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up08(self):
		file = open('up.jpg','rb')
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/357439354283890\033[0m]')
		self.br.open(self.URL.format('357439354283890'))
		self.br.select_form(nr=0)
		self.br.form['Email'] = self.email
		self.br.form['details'] = "I can't log in to my account"
		self.br.form.add_file(file, 'image/jpeg', self.file, id='266395850093752')
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
	
	def up09(self):
		print('\nUp ID on link [\033[0;92mfacebook.com/help/contact/1553947421490701\033[0m]')
		self.br.open(self.URL.format('1553947421490701'))
		self.br.select_form(nr=0)
		self.br.form['Field140788082712931'] = self.name
		self.br.form['Field280690635355052'] = self.email
		self.br.form['Field214373345339617'] = self.words
		sub = self.br.submit().read()
		if 'Terima kasih telah menghubungi Facebook.' in str(sub) or 'Thanks for contacting Facebook.' in str(sub) or 'log in to Facebook.' in str(sub) or '/business/help?' in str(sub):
			print('  - \033[0;92mSuccess.\033[0m')
		else:
			print('  - \033[0;91mFailed.\033[0m')
		
try:
	utama()
except FileNotFoundError:
	sys.exit('\033[0;91mPhoto ID not found.\033[0m')
except (ValueError,IndexError):
	sys.exit('\033[0;91mSTUPPID, Format day-month-year.\033[0m')
except (ConnectionAbortedError,mechanize.URLError):
	sys.exit('\033[0;91mConnection error.\033[0m')
	