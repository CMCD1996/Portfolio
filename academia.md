---
layout: default
title: Academia
driveId: 1rW4om3FqDZl6quL-0PVW-l-c71CBFPBF/preview
---

I completed a range of assignments and research projects during University. This pages explains major projects and access to my assignments.

Please click any of the graphics to review project material and reports.

## **Finance (Honours): Long-Short Hedge Portfolios & Deep Neural Networks**

[![Project Outline](/assets/images/finance-honours.png)]({{ site.url }}/downloads/cmcd398-research-essay.pdf)

### **Theory & Hypotheses**

Machine learning models optimise a loss function by iteratively fine tuning model parameters to minimise the difference between actual observations & predicted outcomes. Portfolio managers seek to maximise excess returns while diversifying idiosyncratic risk by using trading strategies e.g., Trading long-short equity hedge portfolios.

I reconfigured a neural network to directly use a hedge portfolio loss function to maximise excess returns of one month lead long-short hedge portfolios.

Analysis tested the reconfigured model's ability to generate statistically and economically significant results, outperform standard configurations, and align with a portfolio manager's mandate. Hypothetically,

1. It is possible to reconfigure a neural network from maximisation problems given: **Argmax $$f(x)$$ = Argmin $$-f(x)$$**.
2. A hedge portfolio loss function will not outperform standard minimisation functions given the fundamental theory behind these models.

### **Data**

I used a global factor dataset published by [Jensen et al. (2021)](https://github.com/bkelly-lab/ReplicationCrisis) using [CRSP](https://crsp.org) and [Compustat](https://www.spglobal.com/marketintelligence/en/?product=compustat-research-insight) by S&P Global. The dataset is comprised of individual firm-year observations across countries with a 1-month holding period factor for each characteristic e.g., book-to-market ratio. A factor represents a characteristic's contribution to a portfolio's excess returns to if included in a long-short zero net investment strategy calculated by:

1. Sorting stocks into terciles for each characteristic for each country and month;
2. Defining factors by high-tercile returns minus low-tercile returns to align with a zero cost investment strategy, calculating each factors' alpha using an Ordinary least squares (OLS) regression on a constant and region's market return;
3. Clustering factors by signing factors and equally weighting returns of a factors within a specific cluster.

### **Model Architecture**

An input, ouput, and multiple hidden layers contribute to standard deep neutral network topography (left). I configured a deep neutral network with an input layer, output layer, three dense hidden layers, & one dropout hidden layer to mitigate overfitting (right) using Google's open-source machine learning platform [Tensorflow](https://www.tensorflow.org/).

| ![](assets/images/academia/neural-network.png) | ![](assets/images/academia/nn-configuration.png) |

### **Loss Function**

The hedge loss function is a non-convex function, weighted proportionally to one month lead excess returns, using a monotonically non-increasing ranking function. Note: I use $$\|\|$$ to represent rather than a single bar in expression given limitations in markdown syntax.

Firstly, I define a standard monotonical ranking function as:

$$R(y_{i,t})$$

Secondly, I mathematically express long (L) and short (S) portfolios where L is set of long positions, S is a set of short positions, $$y_{i,t}$$ is the excess return for a given asset (i) in a month (t) with u and v lower and upper bounds on excess returns, respectively.

$$L=\{ y_{i,t} \| R(y_{i,t})\leq u\}$$

$$S = \{ y_{i,t} \| R(y_{i,t})\geq v\}$$

$$0 < u \leq \|y\|$$

$$0 < v \leq \|y\|$$

$$u < v$$

Next, I define a hedge portfolio:

$$H_{t} = \frac{1}{\|L\|}\sum_{i\epsilon L} y_{(i,t)} - \frac{1}{\|S\|}\sum_{i\epsilon S} y_{(i,t)}$$

There are permutations to ranking functions & hedge portfolios. I use a monotonical non-increasing ranking function proportionally weighted to one month lead excess returns as follows:

$$R(\hat{y})= W$$

$$W:=\frac{\hat{y}}{\vec{\textbf{1}} \hat{y}}$$

$$\hat{y}=X^{T} \hat{\theta}$$

$$f_{\hat{\theta}}(X) = (\frac{X^{T} \hat{\theta}}{\vec{\textbf{1}}X^{T} \hat{\theta}})^\top X^{T} \hat{\theta}$$

W is a vector of weights, $$\hat{y}$$ is a vector of predicted outcomes, $$\hat{\theta}$$ is a matrix of estimate parameters in the neural network, and X is the global factor dataset.

Stochastic gradient descent is one of the most common optimisation techniques applied to machine learning algorithmns. It is an iterative technique to train models. The algorithmn works as follows:

1. Determines the partial derivatives your objective function with respect to each feature.
2. Selects a random combination of parameters in feature space as an starting point.
3. Updates partial derivative functions using aforementioned paraemeters.
4. Calculates step size for each feature: **step size = gradient x learning rate**
5. Calculates new parameters by: **new = old - step size**
6. Repeats until locates a global or local minima in feature space.

Finally, I express the monotonical non-increasing ranking function's partial derivative. Tensorflow will calculate this function using Keras Backend as the module has the ability to automatically differentiate novel functions:

$$\frac{\partial f_{\hat{\theta}}(X)}{\partial \hat{\theta}} = \frac{\partial ((\frac{X^{T} \hat{\theta}}{\vec{\textbf{1}}X^{T} \hat{\theta}})^\top X^{T} \hat{\theta})}{\partial \hat{\theta}}$$

$$\frac{\partial (f_{\hat{\theta}}(X))}{\partial \hat{\theta}} = \frac{1}{(\hat{\theta}^\top X \vec{1})} X X^\top \hat{\theta} +\frac{1}{\vec{1}X^\top \hat{\theta}} XX^\top \hat{\theta} -\frac{1}{(\hat{\theta}^\top X \vec{1})^{2}} \hat{\theta}^\top XX^\top \hat{\theta} X \vec{1}$$

I compare the monotonic hedge portfolio function to two mean squared error loss functions;Tensorflow's inbuilt function and a custom mean square error loss function. The purpose to compare performance of hedge portfolio function and validate tensorflow's Keras Backend module in programming custom objective functions.

In summary:

| Expression                    | Function                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                               | **Mean Squared Error**                                                                                                                                                                                                                                                                     |
| --                            | --                                                                                                                                                                                                                                                                                         |
| Loss Function                 | $$f_{\hat{\theta}}(y, X)= \frac{\vec{1}}{\vec{1}^{T}\vec{1}} (\textbf{y} - X^{T}\hat{\theta})^{\circ 2}$$                                                                                                                                                                                  |
| Objective                     | $$\text{argmin}_{\hat{\theta}}: (f_{\hat{\theta}}(y, X))$$                                                                                                                                                                                                                                 |
| Partial Differential Equation | $$\frac{\partial f_{\hat{\theta}}(y, X)}{ \partial \hat{\theta}} = \frac{\vec{1}}{\vec{1}^{T}\vec{1}} (-2(\textbf{y}-X^{T} \hat{\theta})^{\circ 1})$$                                                                                                                                      |
| --                            | --                                                                                                                                                                                                                                                                                         |
|                               | **Hedge Portfolio**                                                                                                                                                                                                                                                                        |
| ----------------------------- | --------                                                                                                                                                                                                                                                                                   |
| Loss Function                 | $$f_{\hat{\theta}}(X)= (\frac{X^{T} \hat{\theta}}{\vec{\textbf{1}}X^{T} \hat{\theta}})^\top X^{T} \hat{\theta}$$                                                                                                                                                                           |
| Objective                     | $$\text{argmax}_{\hat{\theta}}:(f_{\hat{\theta}}(X))$$                                                                                                                                                                                                                                     |
| Partial Differential Equation | $$\frac{\partial (f_{\hat{\theta}}(X))}{\partial \hat{\theta}}  = \frac{1}{(\hat{\theta}^\top X \vec{1})} X X^\top \hat{\theta} +\frac{1}{\vec{1}X^\top \hat{\theta}} XX^\top \hat{\theta} -\frac{1}{(\hat{\theta}^\top X \vec{1})^{2}} \hat{\theta}^\top XX^\top \hat{\theta} X \vec{1}$$ |

### **Programming**

TBC

### **Outcomes**

TBC

### **Resources**

- [Tensorflow](https://www.tensorflow.org/)
- [Google Cloud Platform](https://cloud.google.com)
- [Neptune.ai](https://neptune.ai)
- [Classes and Modules]({{ site.url }}/downloads/cmcd398-finance-honours-code-listing.pdf)
- [Code Repository](https://github.com/CMCD1996/finance-honours)

## **Engineering (Honours) Dissertation: Global Optimisation Carbon Pricing Initiative (GOCPI)- A Scalable Energy Systems Modelling Tool**

My research project explored developing an open-source energy modelling tool for users to design their own energy systems. The model intends to inform policy and investment in sustainable technology. The model is built using Python, Excel, GNU Mathprog and IBM Watson Machine Learning services.

[![Project Outline](/assets/images/engineering-honours.png)]({{ site.url }}/downloads/gocpi.pdf)

### GOCPI Information, References and Required Software

- [OseMOSYS](http://www.osemosys.org/)
- [TIMES (Reference)](https://iea-etsap.org/index.php/etsap-tools/model-generators/times)
- [IBM Academic Initiative](https://www.ibm.com/academic/home)
- [IBM ILOG CPLEX Optimizer](https://www.ibm.com/analytics/cplex-optimizer)
- [IBM Cloud](https://www.ibm.com/cloud)
- [IBM Watson Machine Learning](https://www.ibm.com/cloud/machine-learning)
- [GNU Linear Programming Kit](https://www.gnu.org/software/glpk/)
- [GOCPI GitHub Repository](https://github.com/CMCD1996/GOCPI)
- [OseMOSY GitHub Repository](https://github.com/OSeMOSYS/OSeMOSYS)

## **Prototype Wind Turbine**

I lead a four person team tasked to designed, built, and tested a wind turbine to operate at 140 rpm. Blade profile design was simulated using MATLAB and Xfoil to optimise profile aerodynamics. Optimal profiles were modelled in Dassault Systemes Solidworks and laser cut from sheets of Perspex.

Blade profile aerodynamics were optimised through the maximisation of the power coefficient ($$C_p = \frac{P_E}{P_T}$$) The equations related to blade profile design are displayed below.

Equations:

|            Variable             |                                       Equation                                       |
| :-----------------------------: | :----------------------------------------------------------------------------------: |
|          Rotor Radius           |                $$R=\sqrt{\frac{2P_s}{C_p \eta \rho \pi V_{u}^{3}}}$$                 |
|         Tip Speed Ratio         |                         $$\lambda_r = \frac{\Omega_r}{V_u}$$                         |
|        Local Wind Angle         |                 $$\Phi = \frac{2}{3}tan^{-1}(\frac{1}{\lambda_r})$$                  |
| Chord Length with Wake Rotation |                       $$c = \frac{8 \pi r}{B C_L}(1 - \Phi)$$                        |
|       Blade Setting Angle       |                  $$ \beta = \frac{180}{\pi}(cos (\Phi) - \alpha)$$                   |
|       Normal Co-efficient       |                       $$C_n = C_L cos(\Phi) + C_D sin(\Phi)$$                        |
|     Tangential Co-efficient     |                       $$C_t = C_L sin(\Phi) - C_D cos(\Phi)$$                        |
|             Factor              | $$ F = \frac{2}{\pi}cos^{-1}(e^{-f}) \text{ where } f = \frac{B(R-r)}{2rsin{\Phi}}$$ |
|        Blade Solidarity         |                         $$ \sigma^{'} = \frac{Bc}{2 \pi r}$$                         |
|     Axial Induction Factor      |             $$a = \frac{\sigma^{'} C_n}{4Fsin^{2}(\Phi)+\sigma^{'}C_n}$$             |
|         Tangential Load         |                 $$\frac{1}{2}\rho \frac{V_{u}^{2}}{sin^{2}(\Phi)}$$                  |
|       Incremental Torque        |                $$\Delta Q_{i,i+1} = \int_{r_{i + 1}}^{r_{i}}P_Trdr$$                 |
|         Extracted Power         |                                  $$P_E = Q \Sigma$$                                  |
|         Power Available         |                        $$\frac{1}{2}\rho \pi R^2 V_{u}^{3}$$                         |
|       Power Co-efficient        |                              $$C_P = \frac{P_E}{P_T}$$                               |

[![Wind Turbine Project](/assets/images/wind-turbine.png)]({{ site.url }}/downloads/turbine.pdf)

## **Transhipment Project**

I led a team of three designing and building a series of models to inform transhipment operations. This project is modelled either using optimisation, conceptual and simulation models. The optimisation model is a linear optimisation model, written in AMPL, to model fruit produce flows from producers to packhouses to markets. The model minimises packaging and transportation costs across 10 different demand forecasts. The conceptual and simulation models are alternatives to this optimisation model. The objective function driving the optimisation model follows.

$$ \sum\_{i} \sum\_{j} \sum\_{p} C\_{(i,j)} F\_{(i,j,p)} + \sum\_{m} \sum\_{h} N PC\_{m} B\_{(m,h)} $$

Where C is the cost to transport product between an origin (i) & destination (j) packhouse, F (Flow) is the number of product units to ship between origin and destination in a period (p), N is number of periods, PC is packing cost for a packing machine (m), and B is the build costs for a pack machine in a packhouse (h).

[![Transhipment Project](/assets/images/transhipment.png)]({{ site.url }}/downloads/tranship.pdf)

## **Chulalongkorn International Business Case Competition (2019)**

I represented the University of Auckland Case Programme, competing against 20 teams worldwide to develop and present strategies for Line Mobile and Sea Thailand at the Chulalongkorn International Business Case Competition (CIBCC) in Koh Samui, Thailand. Our team presented our analysis on Sea Limited, placing 3rd in the competition.

[![CIBCC Competition](/assets/images/cibcc.png)]({{ site.url }}/downloads/cibcc.pdf)

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

[![Programming Assignments](/assets/images/programming.png)]({{ site.url }}/downloads/code.pdf)

## **Design**

I completed several design projects. One was to design, model and render a household item in PTC Creo. I chose a Gillette fusion proglide razor. The second was an interface (team of five) to create user-defined catapult designs and three dimensional Solidworks models from user designs (Individually). The user interface includes animations programmed in VBA and API's to manipulate the 3D model.

[![Design Project](/assets/images/design.png)]({{ site.url }}/downloads/design.pdf)

## **Optimisation**

I completed several assignments to develop skills to solve optimisation skills. I covered dynamic programming, heuristics, decision making under uncertainty and set partitioning. Some examples follow.

The use of dynamic programming to evaluate whether to reject an applicant or hire the applicant and stop interviewing:

$$\hat{V}_{N} = \int_{0}^{\hat{V}_{N+1}} \hat{V}_{N+1} f(r)dr + \int_{\hat{V}_{N+1}}^{\infty} rf(r)dr$$

The calculation of expected profit from a manufacturing process. Mean hitting times are calculated by considering the probability the product will reach a different state from another state on another process iteration. One transition probability matrix and five separate states were considered (unfinished, poor, good, scrap and average):

$$M_{ij} = 1 + \sum_{k=1}^{n} P_{ik} \times M_{kj} \text{ where } i \neq j$$

[![Optimisation Assignments](/assets/images/optimisation.png)]({{ site.url }}/downloads/optimisation.pdf)

## **Corporate Governance**

I completed several assignments addressing corporate governance-related theories and applications.

[![Corporate Governance](/assets/images/academia/corporate-governance.png)]({{ site.url }}/downloads/cmcd398-corporate-governance.pdf)

## **Literature Review & Proposals**

My literature review informs the subsequent research proposal, grounded in prior research, exploring applications of data science to private equity.
The intention is to inform investment due diligence.
However, the required time to implement the proposal exceeds the time allocated to the BCOM(Honours) research essay given the proposal's complexity.

[![Literature Reviews & Proposals](/assets/images/lit-review.png)]({{ site.url }}/downloads/cmcd398-lit-review-research-proposal.pdf)

## **Machine Learning & Corporate Culture**

I implemented Stanford's Core Natural Language Processing Algorithm to ascertain measures for corporate culture across NZX/ASX listed companies.
This assignment replicates the methodology implemented by Li et al. (2021), accessible on [Github](https://github.com/MS20190155/Measuring-Corporate-Culture-Using-Machine-Learning).

[![Machine Learning & Corporate Culture](/assets/images/ML-CC.png)]({{ site.url }}/downloads/cmcd398-ml-corporate-culture.pdf)

## **Technical Analysis**

I conducted various forms of technical analysis to inform empirical assignments. Methods include Fama-MacBeth regressions, co-integration testing and Bollinger Band trading strategies.

[![Technical Analysis](/assets/images/academia/technical-analysis.png)]({{ site.url }}/downloads/cmcd398-technical-analysis.pdf)

$$
$$
