import pandas as pd
import pandas as pd
import difflib
from pandas import ExcelWriter
from pandas import ExcelFile
import xlrd
diff=difflib.Differ()
df = pd.read_excel('Skills_Data.xlsx',sheet='sheet1') #SPMS Data extraction

SRL=df['SRL']
BAND=df['Band']
Education=df['EDUCATION_DETAILS']
Off_shore=df['OFFSHORESUMMARY']
On_site=df['ONSITESUMMARY']
Project=df['PROJECTNAME']
Proj_Desc=df['PROJECTDESCRIPTION']
Start_Date=df['DURATIONFROM']
End_Date=df['DURATIONTODATE']
Primary_skills=df['PRIMARY_SKILLTYPE']+df['PRIMARY_SKILLCATL1']+df['PRIMARY_SKILLCATL1']+df['PRIMARY_SKILLCATL2']+df['PRIMARY_SKILLCATL3']+df['PRIMARY_SKILLCATL4']
Secondary_skills=df['SECONDARY1_SKILLTYPE']+df['SECONDARY1_SKILLCATL1']+df['SECONDARY1_SKILLCATL2']+df['SECONDARY1_SKILLCATL3']+df['SECONDARY1_SKILLCATL4']
Secondary_skills2=df['SECONDARY2_SKILLTYPE']+df['SECONDARY2_SKILLCATL1']+df['SECONDARY2_SKILLCATL2']+df['SECONDARY2_SKILLCATL3']+df['SECONDARY2_SKILLCATL4']
Secondary_skills3=df['SECONDARY3_SKILLTYPE']+df['SECONDARY3_SKILLCATL1']+df['SECONDARY3_SKILLCATL2']+df['SECONDARY3_SKILLCATL3']+df['SECONDARY3_SKILLCATL4']
Hands_on_Exp=df['HANDS_ON_EXPERIENCE']



df1 = pd.read_excel('IJP_Data.xls', sheet='sheet1')  #IJP Data extraction

IJP_name=df1['IJP Name']
Req_ID=df1['Request Id']
IBU=df1['IBU']
cluster=df1['Cluster']
BU=df1['Business Unit']
Release_Date=df1['Release Date']
Close_Date=df1['To be Closed by']
Band=df1['Band']
Location=df1['Location']
Skill=df1['Skill']

arr=('U1','U2','U3','U4','P1','P2')




def Band_search():
    Req_Band = input('Band Value:')

    for i in range(0, len(Band)):
        print(df.iloc[i].where(df['Band'] == Req_Band))

def Education():
    Req_Education = input('Mention the qualification')
    if Req_Education == 'MSc':
        for i in range(0, len(Education)):
            print((df.iloc[i]).where(Education == 'Bachelor of Science,Masters in ComputerApplication'))
    elif Req_Education == 'BE':
        for i in range(0, len(Education)):
            print((df.iloc[i]).where(Education == 'Bachelor of Engineering'))
    elif Req_Education == 'Btech':
        for i in range(0, len(Education)):
            print((df.iloc[i]).where(Education == 'Bachelor of Technology,DIPLOMA - PRE GRAD.'))

def Skill():
    count=0
    Req_skill = input('Mention the skills required')

    for i in range(df.columns.get_loc('PRIMARY_SKILLCATL1'), df.columns.get_loc('PRIMARY_SKILLCATL4')):

        for j in range(0, len(Primary_skills)):
            if df[df.columns[i]].iloc[j] == Req_skill:
                print(df[df.columns[i]].iloc[j])
                count+=1


    if count==0:
        Query=input('No result found.,Search in Secondary skills?-yes/no')
        if Query=='yes':
                   for i in range(df.columns.get_loc('SECONDARY1_SKILLCATL1'), df.columns.get_loc('SECONDARY3_SKILLCATL4')):

                      for j in range(0, len(Secondary_skills )):
                         if df[df.columns[i]].iloc[j] == Req_skill:
                                print(df[df.columns[i]].iloc[j])

        elif Query=='no':
                    Query2=input('Would you like to search with some other skills.Specify them.')

                    if Query2=='no':
                        print('Thank You')
                    else:
                        Data_Retrival()
        else:
                    print('Not a valid one')


def Loc_details():
  Req_loc=input('Location:')
  for data in range(0,len(Location)):
    for i in range(0, len(Location.iloc[data])):

      for j in range(0, len(Location.iloc[data])):
          if (Location.iloc[data])[i:j + 1] == Req_loc:
              print(Location.iloc[data])






def Data_Retrival():
 Entry = input('What would be the search criteria:')
 Search_val = Entry.split()
 Search_Columns = df.columns
 IJP_Columns = df1.columns
 for value in Search_val:

    for column in Search_Columns:

        if value==column:

            if column ==df.columns[1]:
                Band_search()
            if column== df.columns[2]:
                Education()
            for i in range(0, len(value)):

                for j in range(0, len(value)):
                    if value[i:j + 1] == 'skill':
                        Skill()


    if value=='location' or value=='loc':

                Loc_details();


Data_Retrival()
