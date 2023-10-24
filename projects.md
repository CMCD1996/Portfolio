---
layout: default
title: Projects
---

![Finance/Economics](assets/images/projects/finance-economics.png)

### **3D Modelling of US Market Yields**

**Introduction**

Modelling yield curves help gauge investor sentiment to risk. Interest rates on bonds with shorter maturities are usually lower than longer maturities as investors assume less risk in the short term. However, macroeconomic and geopolitical uncertainty can reverse this sentiment and invert the yield curve, an unusual but reliable predictor of an impending recession.

The United States of America Department of the Treasury issues securities (bills, notes, and bonds) at various constant maturities to finance US Federal operations. These are some of the safest investments available to investors, given their backing by both faith and credit of the US Government. Treasury securities are highly liquid, traded in primary and secondary markets, proxying for investor sentiment daily.

Yield curves are typically modelled at a point in time to gauge investor sentiment on a given day. By extension, modelling yield curves over time informs how investor sentiment changes throughout economic cycles. Hypothetically, sharp changes or dislocations in three-dimensional space ((x,y,z) = (maturities, time, yields)) would show the extent to which market news was unexpected, quantifiable by measurement of stress or strain on the modelled surface.

The Federal Reserve of Bank of St Louis publishes daily market yields on US Treasury securities across constant maturities, quoted on an investment basis, via their online economic research platform [FRED](https://fred.stlouisfed.org).

**Analysis**

I prepared, modeled, and visualised yield curves as follows:

1. Downloaded market yields for 3-month, 6-month, 1-year, 2-year, -year, and 10-year US Treasury securities up until 24th August 2023 from [FRED](https://fred.stlouisfed.org). Maturity, date, and market yield correspond to x, y, and z cartesian coordinates in the model, respectively.
2. Market yields are not reported every day. I removed missing values, reducing the data to a subset constrained by a user-specified number of observations. I isolated 30 observations between February 1st 2020, to April 1st 2020 (COVID), and 30, 100, and 365 latest observations to August 24th 2023. These are modelled in outcomes.
3. The set of US Treasury securities is discrete, given a few maturities. I used interpolation, a form of numerical analysis, to estimate market yields between each maturity. Numerical analysis is a branch of mathematics that solves continuous problems using numeric approximation. I fitted a polynomial of general form $$AX^3 + BX^2 + CX + D$$ as the dynamism of market pricing renders exact solutions impossible.
4. Visualised estimated market yields (z), observations (y), and maturities (x) as point clouds (see outcomes). A point cloud is a discrete set of points in three-dimensional space with points referenced by cartesian coordinates (x,y,z). Integrated heatmaps show how market yields change for each maturity. Sharp colour gradients highlight risk expectations between maturities at a point in time, and changing risk expectation for a specific maturity over time, on and between yield curves, respectively.

**Outcomes**

I model yield curves over the start of COVID and for 30, 100, & 365 days up to to August 24th 2023.

| ![](assets/images/projects/yc-covid.png) | ![](assets/images/projects/yc-t-30-24-aug-23.png) |
| **Figure 1:** 30 observations between February 1st 2020 to April 1st 2020 (COVID) | **Figure 2:** 30 observations to Aug 24th 2023 |
| ![](assets/images/projects/yc-t-100-24-aug-23.png) | ![](assets/images/projects/yc-t-365-24-aug-23.png) |
| **Figure 3:** 100 observations to Aug 24th 2023 | **Figure 4:** 365 observations to Aug 24th 2023 |

Figure 1 best highlights evolving investor sentiment, given the visceral anxieties associated with the pandemic. US Treasury securities with longer-term maturities had higher yields with perceived higher risk in the short term than shorter-term maturities at the start of February. The world came to terms with the full extent of COVID around early March. The point cloud shows yields across all maturities plummeting, leading to a subtle inversion of the yield curve. I caveat interpolating yield curves led to negative market yield estimates at the low end of maturities, inferring hypothetical negative yielding US Treasury securities.

![Web Development](assets/images/projects/web-development.png)

### **Portfolio Website**

I developed this website using a combination of simple yet intuitive technologies. It is a simple, static blog-aware website using [Jeklyll](https://jekyllrb.com/docs/); a set of [Ruby](https://www.ruby-lang.org/en/) programs distributed via gems by package manager [RubyGems](https://rubygems.org).

RubyGems is the preferred package installer for Ruby, equivalent to PIP being the package manager for installing Python packages from the [Python Package Index (PyPI)](https://pypi.org). A GemFile lists the exact set of Ruby programs required to build the website with specified versions and constraints to avoid dependency issues. [Bundler](https://bundler.io) manages both development and staging phases in the software development cycle with executable terminal commands.

I host the development server locally when building new versions of the website. Markdown files describe content, link to assets e.g., images, documents etc., and reference HTML & CSS templates. New builds leverage the latest versions of [Markdown](https://www.markdownguide.org), [Liquid](https://shopify.github.io/liquid/), [HTML](https://en.wikipedia.org/wiki/HTML), and [CSS](https://en.wikipedia.org/wiki/CSS) files stored locally to generate deployment-ready websites. I leverage [Git](https://git-scm.com) and [GitHub](https://github.com) for distributed version control and software development, respectively.

I deploy new builds to a production server using [GitHub pages](https://pages.github.com); a service hosted directly from a GitHub repository. Furthemore, I connect this website to a registered domain and implement basic cybersecurity measures to mitigate [DDoS](<https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/#:~:text=A%20distributed%20denial%2Dof%2Dservice%20(DDoS)%20attack%20is,a%20flood%20of%20Internet%20traffic.>) risk using [Cloudflare](https://www.cloudflare.com).

![Cuisine](assets/images/food.png)

### **Cooking**

I spent the 2020/2021 summer practising my cooking skills, preparing the following meals.

|![Roast Leg of Lamb in a Red Wine Jus](/assets/images/projects/food/leg-o-lamb.jpg)|![Slow Cooked Lamb Shanks in a Red Wine Jus](/assets/images/projects/food/lamb-shanks.jpg)|
|![Roast Pork](/assets/images/projects/food/roast-pork.jpg)|![Pork Spare Ribs with Homemade Ribs Sauce](/assets/images/projects/food/spare-ribs.jpg)|
|![Roast Chicken](/assets/images/projects/food/roast-chicken.jpg)|![Creamy Yellow Chicken Curry](/assets/images/projects/food/chicken-curry.jpg)|
|![Chicken Enchiladas with Homemade Enchilada Sauce](/assets/images/projects/food/enchiladas.jpg)|![Oven Baked Salmon](/assets/images/projects/food/salmon.jpg)|
|![Potato and Leek Soup](/assets/images/projects/food/potato-leek-soup.jpg)|![Lemon Chilli Salmon Spaghetti](/assets/images/projects/food/lcss.jpg)|
|![Spaghetti Bolognese with Homemade Bolognese Sauce](/assets/images/projects/food/bolognese.jpg)|![Creamy Chicken, Bacon and Mushroom Carbonara](/assets/images/projects/food/carbonara.jpg)|
|![Singapore Noodles](/assets/images/projects/food/singapore-noodles.jpg)|![Chicken Drumsticks with Homemade Southern Spice and Pasta Salad](/assets/images/projects/food/chicken-ds.jpg)|
|![Tom Yum Kung](/assets/images/projects/food/tom-yum-kung.jpg)|![Homemade Margherita Pizza](/assets/images/projects/food/pizza-hm.jpg)|
|![Chicken and Mushroom Risotto](/assets/images/projects/food/risotto.jpg)|![Chicken Seafood Paella](/assets/images/projects/food/paella.jpg)|
