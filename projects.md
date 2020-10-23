---
layout: default
title: Projects
---

This page explains some of the projects I completed during my undergraduate degree.

Please click any of the images to review project material and reports.

## **GOCPI: A Scalable Energy System Modelling Tool (2019)**

I am developing an open-source energy modelling tool for users to design their own energy systems. The model intends to inform policy and investment in sustainable technology. The model is built using Python, Excel, GNU Mathprog and IBM Watson Machine Learning services.

[![GOCPI Project](/assets/images/GOCPI.jpg)]({{ site.url }}/gocpi.html)


## **Prototype Wind Turbine**

I lead a four person team tasked to designed, built, and tested a wind turbine to operate at 140 rpm. Blade profile design was simulated using MATLAB and Xfoil to optimise profile aerodynamics. Optimal profiles were modelled in Dassault Systemes Solidworks and laser cut from sheets of Perspex. 

Blade profile aerodynamics were optimised through the maximisation of the power coefficient ($$C_p = \frac{P_E}{P_T}$$) The equations related to blade profile design are displayed below.

Equations:

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

[![Wind Turbine Project](/assets/images/Turbine.jpg)]({{ site.url }}/downloads/turbine.pdf)

## **Transhipment Project**

I led a team of three in designing and building a series of models to inform transhipment operations. This project is modelled either using optimisation, conceptual and simulation models. The optimisation model is a linear optimisation model, written in AMPL, to model fruit produce flows from producers to packhouses to markets. The model minimises packaging and transportation costs across 10 different demand forecasts. The conceptual and simulation models are alternatives to this optimisation model. The objective function driving the optimisation model follows.

$$ \text{Min }\sum_{i} \sum_{j} \sum_{p} \text{Cost}_{ij} \times \text{Flow}_{ijp} $$
$$ + \sum_{m} \sum_{h} \text{numperiods} \times \text{packcost}_{m} \times \text{built}_{mh}$$

[![Transhipment Project](/assets/images/Tranship.jpg)]({{ site.url }}/downloads/tranship.pdf)


## **Chulalongkorn International Business Case Competition (2019)**

I represented the University of Auckland Case Programme, competing against 20 teams worldwide to develop and present strategies for Line Mobile and Sea Thailand at the Chulalongkorn International Business Case Competition (CIBCC) in Koh Samui, Thailand. Our team presented our analysis on Sea Limited, placing 3rd in the competition. 

[![CIBCC Competition](/assets/images/CIBCC.jpg)]({{ site.url }}/downloads/cibcc.pdf)


## **Programming** 

I completed several assignments to improve coding skills in Python, C++, MatLab, SQL, VBA, AMPL and Git.
These assignments covered Eigen problems, Finite Differences, Non Linear Equations, Ordinary Differential Equations, Partial Differential Equations (PDE's) and Databases. The following examples include some of 

Application of finite difference approximations to track heat flow. This behaviour is modelled using the following PDE:

$$\frac{\partial^{2}u }{\partial x^{2} } + \frac{\partial^{2}u }{\partial y^{2} } - \alpha \frac{\partial u }{\partial t } = 0 $$

Python function to run the IBM ILOG CPLEX Optimisation locally:

```python
    def run_cplex_local(self, model_file):
        """ This function runs cplex on the local device if the energy system
            is of a small enough complexity
        """
        # Creates the model structure
        model = cp.Cplex()
        # Produces the results stream and log streams
        output = model.set_results_stream(None)
        output = model.set_log_stream(None)
        # Write the energy system model to Cplex
        model.read(model_file)
        # Solve the model using the version of Cplex installed on the local
        # device (IBM ILOG CPLEX Optimisation Studio)
        model.solve()
        # Return the value of the objective function
        objective_value = model.solution.get_objective_value()
        return objective_value
```

[![Programming Assignments](/assets/images/Code.jpg)]({{ site.url }}/downloads/code.pdf)


## **Design** 

I completed several design projects. One was to design, model and render a household item in PTC Creo. I chose a Gillette fusion proglide razor. The second was an interface (team of five) to create user-defined catapult designs and three dimensional Solidworks models from user designs (Individually). The user interface includes animations programmed in VBA and API's to manipulate the 3D model.

[![Design Project](/assets/images/Design.jpg)]({{ site.url }}/downloads/design.pdf)


## **Optimisation**

I completed several assignments to develop skills to solve optimisation skills. I covered dynamic programming, heuristics, decision making under uncertainty and set partitioning. Some examples follow.

The use of dynamic programming to evaluate whether to reject an applicant or hire the applicant and stop interviewing:

$$\hat{V}_{N} = \int_{0}^{\hat{V}_{N+1}} \hat{V}_{N+1} f(r)dr + \int_{\hat{V}_{N+1}}^{\infty} rf(r)dr$$

The calculation of expected profit from a manufacturing process. Mean hitting times are calculated by considering the probability the product will reach a different state from another state on another process iteration. One transition probability matrix and five separate states were considered (unfinished, poor, good, scrap and average):

$$M_{ij} = 1 + \sum_{k=1}^{n} P_{ik} \times M_{kj} \text{ where } i \neq j$$

[![Optimisation Assignments](/assets/images/Optimisation.jpg)]({{ site.url }}/downloads/optimisation.pdf)
