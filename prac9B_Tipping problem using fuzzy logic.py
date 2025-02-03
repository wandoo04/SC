# Aim: Solve Tipping problem using fuzzy logic
import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl


quality=ctrl.Antecedent(np.arange(0,11,1),'quality') 
service=ctrl.Antecedent(np.arange(0,11,1),'service') 
tip=ctrl.Consequent(np.arange(0,26,1),'tip')

quality['poor']=fuzz.trimf(quality.universe,[0,0,5]) 
quality['average']=fuzz.trimf(quality.universe,[0,5,10]) 
quality['good']=fuzz.trimf(quality.universe,[5,10,10])

service['poor']=fuzz.trimf(service.universe,[0,0,5]) 
service['average']=fuzz.trimf(service.universe,[0,5,10]) 
service['good']=fuzz.trimf(service.universe,[5,10,10])

tip['less']=fuzz.trimf(tip.universe,[0,0,1]) 
tip['some']=fuzz.trimf(tip.universe,[0,1,50]) 
tip['much']=fuzz.trimf(tip.universe,[1,50,100]) 
rule1=ctrl.Rule(quality['poor']|service['poor'],tip['less']) 
rule2=ctrl.Rule(service['average'],tip['some']) 
rule3=ctrl.Rule(service['good']|quality['good'],tip['much']) 
tipping_ctrl=ctrl.ControlSystem([rule1,rule2,rule3]) 
tipping=ctrl.ControlSystemSimulation(tipping_ctrl) 
tipping.input['quality']= float(input(" : ")) 
tipping.input['service']= float(input(" : ")) 
tipping.compute()
print("Recommended tip:", tipping.output['tip']) 
quality.view()
service.view() 
tip.view()



============================

Enter Quality: 2
Enter Service: 3
Recommended tip: ~2 to 5
