---
layout: default
title: Projects
---

This page details the projects I completed during my undergraduate degree.
Please select any of the images to review project material.

## **GOCPI: A Scalable Energy System Modelling Tool (2019)**

I am developing an open-source energy modelling tool for users to design their own energy systems. The model intends to inform policy and investment in sustainable technology. The model is built using Python, Excel, GNU Mathprog and IBM Watson Machine Learning services.

[![GOCPI Project](/assets/images/GOCPI.jpg)]({{ site.url }}/p4p.html)


## **Prototype Wind Turbine (2018)**

I lead a four person team tasked to designed, built, and tested a wind turbine to operate at 140 rpm. Blade profile design was simulated using MATLAB and Xfoil to optimise profile aerodynamics. Optimal profiles were modelled in Dassault Systemes Solidworks and laser cut from sheets of Perspex. 

Blade profile aerodynamics were optimised through the maximisation of the power coefficient ($$C_p = \frac{P_E}{P_T}$$) The equations related to blade profile design are displayed below.

**Equations:**

Variable                          | Equation                                                                              
:---------------------------------:|:-------------------------------------------------------------------------------------:
Rotor Radius                       | $$R=\sqrt{\frac{2P_s}{C_p \eta \rho \pi V_{u}^{3}}}$$                                 
Tip Speed Ratio                    | $$\lambda_r = \frac{\Omega_r}{V_u}$$                                                  
Local Wind Angle                   | $$\Phi = \frac{2}{3}tan^{-1}(\frac{1}{\lambda_r})$$                                   
Chord Length with Wake Rotation    | $$c = \frac{8 \pi r}{B C_L}(1 - \Phi)$$                                               
Blade Setting Angle                | $$ \beta = \frac{180}{\pi}(cos (\Phi) - \alpha)$$                                     
Normal Co-efficient                | $$C_n = C_L cos(\Phi) + C_D sin(\Phi)$$                                               
Tangential Co-efficient            | $$C_t = C_L sin(\Phi) - C_D cos(\Phi)$$                                             
Factor                             | $$ F = \frac{2}{\pi}cos^{-1}(e^{-f}) \text{ where } f = \frac{B(R-r)}{2rsin{\Phi}}$$  
Blade Solidarity                   | $$ \sigma^{'} = \frac{Bc}{2 \pi r}$$                                                    
Axial Induction Factor             | $$a = \frac{\sigma^{'} C_n}{4Fsin^{2}(\Phi)+\sigma^{'}C_n}$$                          
Tangential Load                    | $$\frac{1}{2}\rho \frac{V_{u}^{2}}{sin^{2}(\Phi)}$$                                   
Incremental Torque                 | $$\Delta Q_{i,i+1} = \int_{r_{i + 1}}^{r_{i}}P_Trdr$$                                 
Extracted Power                    | $$P_E = Q \Sigma$$                                                                    
Power Available                    | $$\frac{1}{2}\rho \pi R^2 V_{u}^{3}$$                                                 
Power Co-efficient                 | $$C_P = \frac{P_E}{P_T}$$                                                             

**Click the image below to review the report**

[![Wind Turbine Project](/assets/images/Turbine.jpg)]({{ site.url }}/downloads/turbine.pdf)

## **Transhipment Project (2018)**

I led a team of three in designing and building a series of models to inform transhipment operations. This project is modelled either using optimisation, conceptual and simulation models. The optimisation model is a linear optimisation model, written in AMPL, to model fruit produce flows from producers to packhouses to markets. The model minimises packaging and transportation costs across 10 different demand forecasts. The conceptual and simulation models are alternatives to this optimisation model.

$$F$$

[![Wind Turbine Project](/assets/images/Tranship.jpg)]({{ site.url }}/downloads/tranship.pdf)

## **Chulalongkorn International Business Case Competition (2019) - Sea Limited

[![Wind Turbine Project](/assets/images/Turbine.jpg)]({{ site.url }}/downloads/turbine.pdf)

## **CFA Research Challenge - Comvita (2018)

[![Wind Turbine Project](/assets/images/Turbine.jpg)]({{ site.url }}/downloads/turbine.pdf)

## 
