# How to use

there are XXX_guidewire.xml

if want to use the guidewire, contain the extension and then add <include file="filename.xml"/> at the place that want to use it. a example is in the combine.xml file

to use it : python -m mujoco.viewer -mjcf combine.xml

# Combine pid and guidewire

combine_pid_act.xml in that file:

to use it : python -m mujoco.viewer -mjcf combine_pid_act.xml

## Pid parameter:

kp:

kd

imax: 

​	linear: 1mm 

​	rotate: 

slewmax

## joint parameter

linear motor can be simulated as type="slide" axis="0 1 0" 

rotation motor can be simulated as type="hinge" axis="0 1 0" 

#  Parameters

rotate:  euler="0 0 90"

for use of parameter is at 
length		65cm
tip length 	4cm
diameter	0.035 inch--0.0889

straight
3mm J
135 angled
2.5cm len 3mm radius 

# gudidewire	

https://www.teleflex.com/en/usa/arrowUniversity/vascular/cvc/section9/2.html#:~:text=There%20are%20three%20types%20of%20guidewires%3A%20Solid%20Core,both%20the%20core%20wire%20and%20a%20ribbon%20wire

## types
	solid core 
	mandrel
	ribbon 
## tips
### tips 
	standard 
	reshapable
### shape types
	straight tip
	J(3mm,2mm)
	angled


### tip length
	1cm-7cm

### angled tip degree:
	135

### Tip Hardness
	Floppy			(0.6g)
	Super soft	(1g)
	Soft				(2g)

## tip material
 	shaping ribbon
 	core

## materials
	Nitinol core wire --Polyurethane jacket with tungsten carbide
	Nitinol + stainless steel core  
		Teflon coating
		Teflon or polytetrafluoroethylene (PTFE)
		nickel+Titanium core--Teflon coating
			hydrophilic coating
	
	3cm Platinum coil at distal tip
### diameters
	0.010 – 0.038 inch 
	0.0254-0.09652
	https://radiopaedia.org/articles/guidewires?lang=gb
	most used 0.010 0.014 0.018 0.035



## length
 65cm-300cm

## torque control
1:1(best)
## resistance
kink resistance
## friction




# catheter
## types:
	Angled/Multipurpose 0.35 0.38
## material types:
	polyethylene or nylon, non-braided or braided with 1:1 torque 
	the catheter tip is made from a heat-sensitive material.(https://ifu.cookmedical.com/data/IFU_PDF/T_CE_ANGIO88_REV6.PDF)

