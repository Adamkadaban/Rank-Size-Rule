#  https://github.com/Adamkadaban
#
#  Adam Hassan
#
#  ~Dedicated to Mr.Schweitzer~
#
#  Version 1.2.0 beta 3/14/19
#

import xlrd,os
def error(a, e):
  if e==0:
    return e
  return 100*abs(a-e)/a
def getAns(arr): #[[City, pop], [city, pop], [city, pop]]
  sArr=sorted(arr, key=lambda x : x[1])
  accepted=0
  experimental=0
  pops=[]
  for i in range(len(sArr)):
    pops.append(sArr[i][1])
  pops=sorted(pops)
  tot=0
  for i in range(len(pops)):
    experimental+=pops[0]/(i+1)
    accepted+=pops[i]
    # tot+=error(pops[0]/(i+1), pops[i])
  tot= error(accepted, experimental)
  return round(tot/len(pops), 3)
#input file
book = xlrd.open_workbook('file.xlsx')
sheet = book.sheet_by_name('ws')

#[0]=city name, [1]=country [2]=state/province [3]=population
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)][1:]

# print(data[1:3])

countries={} #val=[city, pop]  {US:[["Davie", 50k],["Weston", 70k]]}
res={}
for i in range(len(data)):
  if data[i][1] in countries.keys():
    x=countries.get(data[i][1])
    x.append([data[i][0], data[i][3]])
    countries.update({data[i][1]:x})
  else:
    countries[data[i][1]]=[[data[i][0], data[i][3]]]

clist=[] # [[Country, [[City, pop], [city, pop]]]]
for key, val in countries.items():
  clist.append([key, val])
# print(clist)
for i in range(len(clist)):
  # print(clist[i][1])
  res[clist[i][0]]=getAns(clist[i][1])

# print(res)
finalRes=[]
for key, val in res.items():
  finalRes.append([key, val])
# print(finalRes)
finalRes = [x for x in finalRes if x[1]!=0]
for i in range(len(finalRes)):
  finalRes[i][1]=abs(100-finalRes[i][1])
finalRes=sorted(finalRes, key=lambda x : x[1])[::-1]
# print(finalRes)

top=int(input("Enter the number of top countries: \t"))
bot=int(input("Enter the number of bottom countries: \t"))


print("--------Results--------")
print("Top "+str(top)+":")
for i in range(top):
  print(str(i+1)+":\t"+finalRes[i][0])
  print("\t "+str(finalRes[i][1]))
print("\nBottom "+str(bot)+":")
for i in range(bot-1, -1, -1):
  print(str(len(finalRes)-i-1)+": "+finalRes[len(finalRes)-i-1][0])
  print("\t"+str(finalRes[len(finalRes)-i-1][1]))

os.system("pause")

# for i in range(len(finalRes)):
#   if "Palau" in finalRes[i]:
#     print(str(i))
#     print(str(finalRes[i][1]))