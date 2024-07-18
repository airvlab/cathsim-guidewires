# 1. How to use

There are XXX_guidewire.xml files

Can be seen as a part. If want to use some guidewire, contain the extension and then add `<include file="filename.xml"/>` at the place that want to use it. a example is in the combine.xml file

To run the combine.xml : python -m mujoco.viewer -mjcf combine.xml

# 2. Combine PID controller and guidewire

combine controller and guidewire.

to use it : python -m mujoco.viewer -mjcf combine_pid_act.xml



We should have 2 Degree of freedom. we need two controller to control the linear and rotate.

That's we need two joint to control the move, and each one have a controller

## 2.1 Joint parameter

 linear motor can be simulated as type="slide" axis="0 1 0" 

rotation motor can be simulated as type="hinge" axis="0 1 0"


## 2.2 Pid controller parameter:

### parameter meaning

|         | Meaning                           | Stable | acurate | react |
| ------- | --------------------------------- | ------ | ------- | ----- |
| Kp      | Proportion                        | down   | up      | up    |
| Ki      | Integral                          | down   | up      | down  |
| Kd      | Differential                      | up     | None    | up    |
| imax    | range the I term force            |        |         |       |
| slewmax | each timestep the max move length |        |         |       |

to get the great parameter, need real train.

### What we need.

max move length

linear:  0.001* 

rotate: 1-360°

# 3. Guidewire

## 3.1 Parameter used

Rotate:  the parent body to rotate the guidewire:  euler="0 0 90"

The parameter used is:
length		.65
tip length 	.04
diameter		0.035 inch--0.000889

Nitinol 

Teflon

torch control 1:1



guidewire model type that will be used

straight
3mm J
135 angled
2.5cm len 3mm radius



[Haptic Interface With Force and Torque Feedback for Robot-Assisted Endovascular Catheterization | IEEE Journals &amp; Magazine | IEEE Xplore](https://ieeexplore.ieee.org/document/10179013)

[[25]]( L. Jones, "Kinesthetic sensing" in Human and Machine Haptics, Cambridge, MA, USA:MIT Press, 2000.), [[26]](L. Jandura et al., "Experiments on human performance in torque discrimination and control" in Time-Varying Systems and Control, New York, NY, USA:ASME, vol. 1, pp. 369-375, 1994.) indicate that human's force resolution is 0.06 N, and the just noticeable difference (JND) for torque is 12.7% at the reference of 60 mN•m. The bandwidth for controlling forces has been estimated to be approximately 2 Hz for forearms, while the bandwidth for force control of fingers is determined to be less than 6 Hz [[25]]( L. Jones, "Kinesthetic sensing" in Human and Machine Haptics, Cambridge, MA, USA:MIT Press, 2000.). The operating force and torque during endovascular catheterization procedures generally will not exceed 3.2 N and 10 mN•m [[27]](H. Rafii-Tari et al., "Assessment of navigation cues with proximal force sensing during endovascular catheterization", Med. Image. Comput. Comput. Assist. Interv., vol. 15, pp. 560-567, Sep. 2012.), [[28]](X. Bao et al., "Multilevel operation strategy of a vascular interventional robot system for surgical safety in teleoperation", IEEE Trans. Robot., vol. 38, no. 4, pp. 2238-2250, Aug. 2022.). [[33]](T. L. Brooks, "Telerobotic response requirements", Proc. IEEE Int. Conf. Syst. Man Cybern., pp. 113-120, 1990.) point out that, in a master-slave system, a low bandwidth (5–10 Hz) could be used from the hand controller to the slave, and a higher bandwidth (20–320 Hz) could be used from the slave to the hand controller.

## 3.2 Guide wire Infor resource

https://www.teleflex.com/en/usa/arrowUniversity/vascular/cvc/section9/2.html#:~:text=There%20are%20three%20types%20of%20guidewires%3A%20Solid%20Core,both%20the%20core%20wire%20and%20a%20ribbon%20wire

## 3.3 Types

solid core
mandrel
ribbon

## 3.4 Tips

### type

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

### tip material

 shaping ribbon
 core

## 3.5 materials

### Core:

Nitinol

Nitinol + stainless steel

nickel+Titanium

### Tip:

Teflon

polytetrafluoroethylene (PTFE)

hydrophilic

Polyurethane jacket with tungsten carbide

3cm Platinum coil

## 3.6 diameters

0.010 – 0.038 inch
0.000254-0.0009652
source : https://radiopaedia.org/articles/guidewires?lang=gb
most used 0.010 0.014 0.018 0.035

## 3.7 length

 65cm-300cm

## 3.8 Torque control

1:1(best)

## 3.9 Resistance

kink resistance

## 3.10friction






# catheter

## types:

    Angled/Multipurpose 0.35 0.38

## material types:

    polyethylene or nylon, non-braided or braided with 1:1 torque
    the catheter tip is made from a heat-sensitive material.(https://ifu.cookmedical.com/data/IFU_PDF/T_CE_ANGIO88_REV6.PDF)
