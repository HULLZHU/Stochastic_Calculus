#!/usr/bin/env python
# coding: utf-8

# ### Density Function of Geometric Brownian Motion
# 
# $$X_t = e^{W_t}$$
# 
# Where $W_t$ is a brownian Motion
# 
# $$F_{X_t}(x) = P(X_t \leq x) = P(e^W_t \leq x)$$
# 
# $$=P(W_t \leq lnx)=F_{W_t}(lnx)$$
# 
# $$=\frac{1}{\sqrt{2 \pi t}}\int^{ln x}_{-\infty}e^{\frac{-u^2}{2t}}du$$
# 
# Then we can get $Density$ $Function$ that
# 
# $$p(x) = \frac{d}{dx}F_{X_t}(x)= \begin{cases}   \frac{1}{x\sqrt{2\pi t}}e^{-(lnx)^2/(2t)} &&& x>0\\ \\ 0&&& else  \end{cases}$$

# We can say that $$X_t = e^{W_t}$$ is a log-normal distribution
# 
# Where
# 
# $$E[X_t] = E[e^{W_t}]= e^{\frac{t}{2}} \ \ \ _{Appendix 1}$$
# 
# and
# 
# $$E[X_t ^ 2] = E[e^{2W_t}] = e^{2t}$$
# 
# and 
# 
# $$Var[X_t] = E[X_t^2]-E[X_t]^2 = e^{2t}-e^{t/2}2 = e^{2t} -e^t$$

# ### Appendix
# If $\alpha > 0$, then 
# $$E[e^{\alpha W_t}] = \int e^{\alpha x}\phi_t(x)dx$$
# 
# $$=\frac{1}{\sqrt{2\pi t}}\int e^{-\frac{x^2}{2t}+\alpha x}dx$$
# 
# According to Formula that 
# 
# $$\int e^{-a x^2 + bx}dx = \sqrt{\frac{\pi}{a}}{e^{\frac{b^2}{4a}}},\ \ \ \ a>0$$
# 
# We get
# 
# $$E[e^{\alpha W_t }]=e^{{\alpha^2t}/2}$$
