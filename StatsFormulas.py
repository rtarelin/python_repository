from __future__ import division

cpop = 300000 #cpop = control population
tpop = 300000 #tpop = treatment population
cs = 69000 #cs = control success
ts = 72000 #ts = treatment success
totpop = cpop + tpop #totpop =total population

csuc = cs/cpop #control success rate
tsuc = ts/tpop
lift = (ts/tpop)/(cs/cpop)-1 #%lift
c_std_err = sqrt((csuc*(1-csuc))/cpop) #control standard error
t_std_err = sqrt((tsuc*(1-tsuc))/cpop) #treatment standard error
std_err_lift = sqrt((c_std_err**2*csuc**2 + t_std_err**2 *tsuc**2)/csuc**4) #standard error %lift
l_conf = lift-std_err_lift *1.96 #lower confidence
u_conf = lift+std_err_lift *1.96 #upper confidence
t_val = (tsuc-csuc)/sqrt(c_std_err**2 + t_std_err**2)
def stat_sig(float):
    if t_val >= 1.96:
        return 'True'
    else: 
        return 'False' #t-test
    
print(cpop/tpop) #ratio of control to treatment, should be close to 1 for equal bucketing
print('Total Population: ' + str(totpop))
print('Control Success: ' + str(csuc*100))
print('% Lift: ' + str(lift*100))
print('Control Standard Error: ' + str(c_std_err))
print('Treatment Standard Error: ' +str(t_std_err))
print('Standard Error Lift: ' + str(std_err_lift*100))
print('Lower Confidence: ' + str(l_conf*100))
print('Upper COnfidence: ' + str(u_conf*100))
print('T-Score: ' + stat_sig(t_val) +' ' + str(t_val))


