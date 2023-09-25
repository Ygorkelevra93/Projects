# Default panel

## Scope
The team requested a panel so that they could monitor the performance of charges made, customer goals and quickly obtain information about their customer portfolios,
from a macro level of information such as default KPIs, debt aging, to the detailed information of pointing out when the last charge was made and by which user.

## Project scheme:
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/9194444b-6249-43a0-b9ad-3c911e400002)


## Feature 1 - Automatic billing

### Bases Used:
- accounts receivable as ACR
- Customers as CRM
- Billing_groups as BG

## Accounts receivable table.
Every day in the morning and at break time, a Python routine will read the report generated from the ACR system and carry out the following treatment:
It will bring CRM billing email information and information about which billing group that customer belongs to in BG.
And we save it in a shared location.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/c5ad68a0-fcce-4f3b-87b3-336c5a2461b8)


This treated database will be used to feed another spreadsheet that we leave for the team to access and select the customers they want to charge.
* Project could also be handled automatically, without the team coming in to take the shot. But it was a team choice,
to track which customers are being charged.

### The spreadsheet
The billing spreadsheet has 3 macros:
1 - The first to be updated with the current information processed.
2 - The second to select the customers to be charged
3 - To trigger emails and register them in a tab that will later be read by QLIK SENSE.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/5b580315-91ab-42c9-8c11-0af29a80e7ef)

 
 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Feature 2 - Dashboard

The dashboard will bring together the main information to help manage customers.
It was built with information from the CRM, ACR databases and billing history brought from the billing routine above.
As a point of greater complexity here we have the treatment of the ACR fact table, in addition to adding calculated aging columns,
regions, supervisors of each client, a procedure was created here to store the bases, so that we can monitor
how the billing position was on any selected date.
(Routines executed in different extractors in the area, which read this ACR and concatenate one under the other)

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/4e1519c7-1294-49f7-9d9f-1a11acaa4f74)


### Dashboard:
Above we have the KPIs with default indicators and active matrix counters.

### Charts :
Top left corner, line graph containing the evolution of default considering all dates;
Top right corner, bar graph representing the amount in each sales channel, and which
If selected, it enables drilling down for the subchannel;
Bottom left corner, stacked bar graph with the evolution of the amount in each period and separated by aging;
Bottom right corner, identical to the one above, but this shows the separation by location.

And everyone has the option to export to Excel
