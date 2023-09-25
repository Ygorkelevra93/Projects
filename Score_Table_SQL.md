# ScoreTable - SQL 

##  Project scope:
The system that the company uses for credit analysis and order approval has a diagnostic screen for each customer with information and scores.
In total, more points of information relevant to the process.
The requester would like a report to be extracted from the bank that provided the information in table format, as the original system did not have this report in its standard version.

## Tools used: 
### SQL Server + QLIKSENSE


### Diagnostic screen with the requested information in table format: (+3000 customers)

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/e1da57f6-813c-4e95-a1d0-cf294f121294)


The difficult point here was, as the company policy is complex, many of the parameters like policies, ratings, and metrics themselves were added
on demand to the tables of the third party system, then studies and validations on the relationship were carried out.
And when it was necessary to extract the information from the scores of each metric and this information was repeated many times for each client, according to all the metrics.



 ![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/018dafa1-479a-4927-afe1-70e42f90ee61)

The solution was to use a "Min" and "Case" aggregation function so that each time that
metric text was found, it would bring in the score value and name that as a new column.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/825c9f30-d1e1-4b3c-8208-ffe314656b6a)


From there, we added some validations that the user also requested and a column to put the date, so that an evolutionary analysis of that behavior could even be carried out.
The end result is a table where the requester can filter and compare behavior VS default, limit value granted, value of bonds paid.


![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/a1978320-ce38-4f6e-a128-42647b81b450)


