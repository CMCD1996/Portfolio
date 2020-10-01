---
layout: default
title: Projects
---

This page details the projects I completed during my undergraduate degree.
Please select any of the images to review project material.

## Design and build a prototype wind turbine (2018)

I lead a four person team tasked to designed, built, and tested a wind turbine to operate at 140 rpm. Blade profile design was simulated using MATLAB and Xfoil to optimise profile aerodynamics. Optimal profiles were modelled in Dassault Systemes Solidworks and laser cut from sheets of Perspex. 

Blade profile aerodynamics were optimised through the maximisation of the power coefficient ($$C_p = \frac{P_E}{P_T}$$) The equations related to blade profile design are displayed below.

**Equations:**
Rotor Radius | $$R=\sqrt{\frac{2P_s}{C_p \eta \rho \pi V_{u}^{3}}}$$
Tip Speed Ratio | $$\lambda_r = \frac{\Omega_r}{V_u}$$
Local Wind Angle | $$\Phi = \frac{2}{3}tan^{-1}(\frac{1}{\lambda_r})$$
Chord Length with Wake Rotation | $$c = \frac{8 \pi r}{B C_L}(1 - \Phi)$$
Blade Setting Angle | $$ \beta = \frac{180}{\pi}(cos (\Phi) - \alpha)$$
Normal Co-efficient | $$C_n = C_L cos(\Phi) + C_D sin(\Phi)$$
Tangential Co-efficient | $$C_t = C_L sin(\Phi) - C_D cos(\Phi)$$
Factor | $$ F = \frac{2}{\pi}cos^{-1}(e^{-f}) \text{ where } f = \frac{B(R-r)}{2rsin{\Phi}}$$
Blade Solidarity: $$sigma^{'} = \frac{Bc}{2 \pi r}$$
Axial Induction Factor | $$a = \frac{\sigma^{'} C_n}{4Fsin^{2}(\Phi)+\sigma^{'}C_n}$$
Tangential Load | $$\frac{1}{2}\rho \frac{V_{u}^{2}}{sin^{2}(\Phi)}$$
Incremental Torque | $$\Delta Q_{i,i+1} = \int_{r_{i + 1}}^{r_{i}}P_Trdr$$
Extracted Power | $$P_E = Q \Sigma$$
Power Available | $$\frac{1}{2}\rho \pi R^2 V_{u}^{3}$$
Power Co-efficient | $$C_P = \frac{P_E}{P_T}$$

**Click the image below to review the report**

[![Wind Turbine Project](/assets/images/Turbine.jpg)]({{ site.url }}/downloads/turbine.pdf)

## 

## Project 3

## 
