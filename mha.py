importcsv
importplotly.graph_objectsasgo
#-----------------------------------------------------------------------------------------
#CalculatingtheMonthlySum
#-----------------------------------------------------------------------------------------
monthly_sum={}
forrowincsv.reader(open('mha.csv')):
key=(row[1])
if(row[4].isnumeric()):
if(keyinmonthly_sum):
monthly_sum[key]= monthly_sum[key]+float(row[4])
else:
monthly_sum[key]=float(row[4])

print("================\nPrintingtheMonthlySum\n================\n")
formon,new_car_totalinmonthly_sum.items():
print(mon,int(new_car_total))
#-----------------------------------------------------------------------------------------
#Calculatingwheretheoldsalesismax
#-----------------------------------------------------------------------------------------
old_sales_max={}
max_val=0
corrs_yr=""
corrs_month=""
forrowincsv.reader(open('mha.csv')):
if(row[5].isnumeric()):
if(int(row[5])>max_val):
max_val=int(row[5])
corrs_yr=row[0]
corrs_month=row[1]

print("\n\n\n================\nPrintingYear,MonthforwhichsalesisMax:",corrs_yr,"-",
corrs_month,",andthevalueis", max_val,"\n==================\n")
#-----------------------------------------------------------------------------------------
#CalculatingYearlySummary
#-----------------------------------------------------------------------------------------
yearly_sum_old={}
yearly_sum_new={}
forrowincsv.reader(open('mha.csv')):
key=(row[0])
if(row[4].isnumeric()):
if(keyinyearly_sum_old):
yearly_sum_old[key]= yearly_sum_old[key]+float(row[4])
yearly_sum_new[key]= yearly_sum_new[key]+float(row[4])
else:
yearly_sum_old[key]=float(row[4])
yearly_sum_new[key]=float(row[5])

#-----------------------------------------------------------------------------------------
#GeneratingGraph1-YearvsSales
#-----------------------------------------------------------------------------------------
x_axis=[]
y_axis_1=[]
y_axis_2=[]
fory,tinsorted(yearly_sum_old.items()):
x_axis.append(y)
y_axis_1.append(t)
fory,tinsorted(yearly_sum_old.items()):
y_axis_2.append(t)
fig=go.Figure(data=[
go.Bar(name='Oldcarsales',x=x_axis,y=y_axis_1),
go.Bar(name='Newcarsales',x=x_axis,y=y_axis_2)
])
fig.update_layout(barmode='group')
fig.show()
#-----------------------------------------------------------------------------------------
#CalculatingMonthlySummaryfor2019
#-----------------------------------------------------------------------------------------
monthly_sum_old={}
monthly_sum_new={}
forrowincsv.reader(open('mha.csv')):
key=(row[1])
if(row[4].isnumeric()):
if(row[0]=='2019'):
if(keyinmonthly_sum_old):
monthly_sum_old[key]= monthly_sum_old[key]+float(row[4])
monthly_sum_new[key]= monthly_sum_new[key]+float(row[4])
else:
monthly_sum_old[key]=float(row[4])
monthly_sum_new[key]=float(row[5])
#-----------------------------------------------------------------------------------------
#GeneratingGraph2-MonthvsSalesfor2019
#-----------------------------------------------------------------------------------------
x_axis=[]
y_axis_1=[]
y_axis_2=[]

fory,tinsorted(monthly_sum_old.items()):
x_axis.append(y)
y_axis_1.append(t)
fory,tinsorted(monthly_sum_old.items()):
y_axis_2.append(t)
fig=go.Figure(data=[
go.Bar(name='Oldcarsalesin2019',x=x_axis,y=y_axis_1),
go.Bar(name='Newcarsalesin2019',x=x_axis,y=y_axis_2)
])
fig.update_layout(barmode='group')
fig.show()