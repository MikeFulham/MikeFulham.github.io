import random as ran
import pandas as pd
import os

def createNumberPlate():
    """Returns a random number plate (May not be valid)"""
    areaCodes = ['AA ', ' AB ', ' AC ', ' AD ', ' AE ', ' AF ', ' AG ', ' AH ', ' AJ ', ' AK ', ' AL ', ' AM ', ' AN ', ' AO ', ' AP ', ' AR ', ' AS ', ' AT ', ' AU ', ' AV ', ' AW ', ' AX ', ' AY ', ' BA ', ' BY ', ' CA ', ' CB ', ' CC ', ' CD ', ' CE ', ' CF ', ' CG ', ' CH ', ' CJ ', ' CK ', ' CL ', ' CM ', ' CN ', ' CO ', ' CP ', ' CR ', ' CS ', ' CT ', ' CU ', ' CV ', ' CW ', ' CX ', ' CY ', ' DA ', ' DB ', ' DC ', ' DD ', ' DE ', ' DF ', ' DG ', ' DH ', ' DJ ', ' DKDL ', ' DM ', ' DN ', ' DO ', ' DP ', ' DR ', ' DS ', ' DT ', ' DU ', ' DV ', ' DW ', ' DX ', ' DY ', ' EA ', ' EY ', ' FA ', ' FB ', ' FC ', ' FD ', ' FE ', ' FF ', ' FG ', ' FH ', ' FJ ', ' FK ', ' FL ', ' FM ', ' FN ', ' FP ', ' FR ', ' FS ', ' FT ', ' FV ', ' FW ', ' FX ', ' FY ', ' GA ', ' GB ', ' GC ', ' GD ', ' GE ', ' GF ', ' GG ', ' GH ', ' GJ ', ' GK ', ' GL ', ' GM ', ' GN ', ' GO ', ' GP ', ' GR ', ' GS ', ' GT ', ' GU ', ' GV ', ' GW ', ' GX ', ' GY ', ' HA ', ' HB ', ' HC ', ' HD ', ' HE ', ' HF ', ' HG ', ' HH ', ' HJ ', ' HK ', ' HL ', ' HM ', ' HN ', ' HO ', ' HP ', ' HR ', ' HS ', ' HT ', ' HU ', ' HV ', ' HW ', ' HX ', ' HY ', ' KA ', ' KB ', ' KC ', ' KD ', ' KE ', ' KF ', ' KG ', ' KH ', ' KJ ', ' KK ', ' KL ', ' KM ', ' KN ', ' KO ', ' KP ', ' KR ', ' KS ', ' KT ', ' KU ', ' KV ', ' KW ', ' KX ', ' KY ', ' LA ', ' LB ', ' LC ', ' LD ', ' LE ', ' LF ', ' LG ', ' LH ', ' LJ ', ' LK ', ' LL ', ' LM ', ' LN ', ' LO ', ' LP ', ' LR ', ' LS ', ' LT ', ' LU ', ' LV ', ' LW ', ' LX ', ' LY ', ' MA ', ' MY ', ' NA ', ' NB ', ' NC ', ' ND ', ' NE ', ' NG ', ' NH ', ' NJ ', ' NK ', ' NL ', ' NM ', ' NN ', ' NO ', ' NP ', ' NR ', ' NS ', ' NT ', ' NU ', ' NV ', ' NW ', ' NX ', ' NY ', ' OA ', ' OB ', ' OC ', ' OD ', ' OY ', ' PA ', ' PB ', ' PC ', ' PD ', ' PE ', ' PF ', ' PG ', ' PH ', ' PJ ', ' PK ', ' PL ', ' PM ', ' PN ', ' PO ', ' PP ', ' PR ', ' PS ', ' PT ', ' PU ', ' PV ', ' PW ', ' PX ', ' PY ', ' RA ', ' RB ', ' RC ', ' RD ', ' RE ', ' RF ', ' RG ', ' RH ', ' RI ', ' RJ ', ' RK ', ' RL ', ' RM ', ' RN ', ' RO ', ' RP ', ' SA ', ' SB ', ' SC ', ' SD ', ' SE ', ' SF ', ' SG ', ' SH ', ' SJ ', ' SK ', ' SL ', ' SM ', ' SN ', ' SO ', ' SP ', ' SR ', ' SS ', ' ST ', ' SU ', ' SV ', ' SW ', ' SX ', ' SY ', ' VA ', ' VB ', ' VC ', ' VD ', ' VE ', ' VF ', ' VG ', ' VH', 'WA ', ' WB ', ' WC ', ' WD ', ' WE ', ' WF ', ' WG ', ' WH ', ' WJ ', ' WK ', ' WL ', ' WM ', ' WN ', ' WO ', ' WP ', ' WR ', ' WS ', ' WT ', ' WU ', ' WV ', ' WW', 'WX ', ' WY ', ' YA ', ' YB ', ' YC ', ' YD ', ' YE ', ' YF ', ' YG ', ' YH ', ' YJ ', ' YK ', ' YL ', ' YM ', ' YN ', ' YO ', ' YP ', ' YR ', ' YS ', ' YT ', ' YU ', ' YV ', ' YW ', ' YX ', ' YY']
    dates = ["02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67"]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    plate = ran.choice(areaCodes).replace(" ","");
    plate+=ran.choice(dates)
    plate+=" "
    plate+=ran.choice(alphabet)+ran.choice(alphabet)+ran.choice(alphabet)
    return plate




x = list()
for i in range(1000):
    x.append(createNumberPlate())


df = pd.read_csv(os.getcwd() + "\\Training Data.csv")
df["Plates"] = x
df.to_csv(os.getcwd() + "\\Training Data.csv")