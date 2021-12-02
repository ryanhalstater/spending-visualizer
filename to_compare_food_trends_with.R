library('fpp')
library(ggplot2)
library('pracma')
library(readxl) 
library(AER)
library(sqldf)


df <- read.csv('tableau_friendly_results.csv')
colnames(df)
ne <- sqldf("select Year, Food from df where Region = 'northeast'")
s <- sqldf("select Year, Food from df where Region = 'south'")
w <- sqldf("select Year, Food from df where Region = 'west'")
mw <- sqldf("select Year, Food from df where Region = 'midwest'")

ne_lm = lm( Food ~ Year, data = ne)
s_lm = lm( Food ~ Year, data = s)
w_lm = lm( Food ~ Year, data = w)
mw_lm = lm( Food ~ Year, data = mw)

ne_se <- sqrt(sum(ne_lm$residuals^2)/ne_lm$df.residual)
s_se <- sqrt(sum(s_lm$residuals^2)/s_lm$df.residual)
w_se <- sqrt(sum(w_lm$residuals^2)/w_lm$df.residual)
mw_se <- sqrt(sum(mw_lm$residuals^2)/mw_lm$df.residual)
#coeftest(ne_lm, vcov. = vcovHC, type = "const")

ne_b <- ne_lm$coefficients[2]
s_b <- s_lm$coefficients[2]
w_b <- w_lm$coefficients[2]
mw_b <- mw_lm$coefficients[2]

dof <- length(mw$Year) - 2

#can now compare slope parameters 
t_val <- (w_b - s_b)/s_se
  
pt(t_val, dof, lower.tail = FALSE)

