-------------------------------
-- RXA_Domopalooza_ML_in_SQL --
-- Created:           012019 --
-- Author:          JPrantner--
-------------------------------

-- Because of the way Redshift is coded in Domo the querey is broken into seperate steps --
-- The step names are indicated below --


-- Step1--
select * from "domopalooza_econ" 
 where Month > 'January 01, 2010'

--Step2--
select month
 from step1
  group by month
  order by random()
  limit 80

--Step3--
select t1.month
 ,ln(t1."unemployment") as "unemployment"
 ,ln(t1."consumer sentiment") as "consumer sentiment"
 from 
  step1 t1 inner join  step2 t2 on t1."month"=t2."month"

--Step4--
SELECT
 ((N * Sxy) - (Sx * Sy)) / ((N * Sxx) - (Sx * Sx)) AS SPEND_ELASTICITY
  FROM ( SELECT SUM(unemployment) AS Sx, 
       SUM("consumer sentiment") AS Sy, SUM(unemployment * unemployment) AS Sxx, 
       SUM(unemployment * "consumer sentiment") AS Sxy, SUM("consumer sentiment" * "consumer sentiment") AS Syy, COUNT(*) AS N FROM step3 ) sums;

-- Output File --
Select * from step4	   
	   