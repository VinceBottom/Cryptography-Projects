import pandas as pd
import msoffcrypto
import openpyxl
import os
import io
import xlrd
##
os.chdir("Directory")
##edit based on newly saved census
df1_name = "DataSet1.xlsx"
df2_name = "DataSet2.xlsx"
df3_name = "DataSet3.xlsx"
df4_name = "DataSet4.xlsx"
df5_name = "DataSet5.xlsx"
##assumes same passkey for every dataset, otherwise
##can set up multiple to apply in for-loop by count and if/else statements
passkey = input("Please enter password: ")
##
filelist = [df1_name, df2_name, df3_name, df4_name, df5_name]
##
count = 0
for x in filelist:
	decrypted = io.BytesIO()
	with open(x, "rb") as f:
    		file = msoffcrypto.OfficeFile(f)
    		file.load_key(password=passkey)  # Use password
    		file.decrypt(decrypted)
	if count == 0:
		df1 = pd.read_excel(decrypted, engine='openpyxl')
	if count == 1:
		df2 = pd.read_excel(decrypted, engine='openpyxl')
	if count == 2:
		df3 = pd.read_excel(decrypted, engine='openpyxl')
	if count == 3:
		df4 = pd.read_excel(decrypted, engine='openpyxl')
	if count == 4:
		df5 = pd.read_excel(decrypted, engine='openpyxl')
