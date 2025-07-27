This README summarizes the Uber Fares Data Analysis project and provides a clear roadmap for achieving project goals.  The project focuses on uncovering insights into fare patterns, ride behaviors, and pricing influences using PowerBI.


**Project Overview**

This project utilizes data from an Uber Fares dataset to analyze and understand key factors driving ride fares. Through an iterative process of data processing, visualization, and interpretation, this project will answer critical questions about ride dynamics and user behavior. 



Key Stages:

**Data Preparation & Exploration (Python)**

The initial phase involves loading the data into a Pandas DataFrame for efficient analysis and performing comprehensive exploratory data analysis.
This stage includes:

 Data Extraction and Cleaning: Extracting the relevant data from the source and cleaning inconsistencies to ensure data integrity. 

 
 Statistical Analysis: Generating summary statistics (mean, median, standard deviation), calculating quartiles, and identifying potential outliers to gain initial insights into the dataset's properties. 


**Feature Engineering & Data Transformation (Python)**
 The project will then focus on:
   * Creating new analytical features like hour-based categories, day of week classification, and peak/off-peak indicators.  
   * Encoding categorical variables for further analysis.
**Power BI Integration & Visualization:**Importing the cleansed data into Power BI Desktop for interactive exploration. 
      Generating compelling visualizations to demonstrate key findings: 
      * Distribution of fares using histograms and box plots.
      * Time-based analysis of ride patterns (hourly, daily, monthly).
      * Seasonal trends in fare pricing through visualizations.  
      * Geographic distribution of rides presented via maps.


**Dashboard Design & Reporting** 
    * Designing a professional dashboard with interactive filters and drill-downs for deep exploration.
    * Creating visually engaging reports to present key findings.





 **Project Outcomes**
 This project will deliver valuable insights into the complex world of ride pricing and user behavior. It will offer a robust foundation for informed decision-making by providing data-driven recommendations. 



**HERE ARE SOME OF THE RESULTS WITH THEIR LABELS:**


**Load the dataset into a Pandas DataFrame using Python**

<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/da58a493-6802-4574-abeb-a26ef8beeeb6" />


****Perform comprehensive exploratory data analysis (EDA) to understand:**

**•Checking missing values**





<img width="959" height="517" alt="Image" src="https://github.com/user-attachments/assets/3d169145-5d9b-4035-8bee-3270d46b4796" />



**•Shape of the datasets**





<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/1b6f2835-29bc-4315-aaa2-93e8965f8255" />



**•Number of Duplicates rows & datatype of each column**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/17a0212f-ed1d-4306-b8b9-52906ff666a2" />




**•Number of unique values per column**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/78079650-9628-4e2c-b451-5b789cb82729" />




**•Percentage of Missing valuues**


<img width="959" height="422" alt="Image" src="https://github.com/user-attachments/assets/0832179c-6671-4987-a7f3-130594d6faab" />




**•Variable description**



<img width="959" height="504" alt="Image" src="https://github.com/user-attachments/assets/317369ba-7904-458c-b6d1-241f2168f774" />



**•Cleaned data (Removing duplicates)**



**For i used data deduplication or removal of duplicate records methodology.**




<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/cc5a24e9-a0e1-4041-b467-f9e5b519ca6f" />



**•Handling missing values**


<img width="959" height="505" alt="Image" src="https://github.com/user-attachments/assets/92487dbd-92b4-4616-b1a9-cb45cf812096" />




**Generate descriptive statistics including:**


**•MEAN**

<img width="959" height="379" alt="2a mean" src="https://github.com/user-attachments/assets/ca07e8ee-ab07-499d-8115-24a4cefd0d07" />




**•MEDIAN**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/f2deffef-7e18-41d8-a32c-709ae5f88cd6" />




**•MODE**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/fed27ef7-8720-454f-bdf7-ab92ba94baf0" />


**•OUTLIER**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/32c58263-0a09-477c-98a9-aed1ef5e64d5" />


**•QUARTILE_1**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/c37a27b5-5530-4cb0-8ba4-0d535da36fca" />


**•QUARTILE_2**


<img width="959" height="538" alt="Image" src="https://github.com/user-attachments/assets/8e356947-36f1-4124-9eb1-34bc1f4bd58f" />




**•QUARTILE_3**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/7acba4d9-d84a-456c-af5b-3250ccb3ad81" />



**•STANDARD_DEVIATION**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/6085b11b-9472-41f0-b3fa-d2bbb29d3b4e" />




**•visualizations showing fare distribution pattern & key relationships**


 **Box plot OF Fare amounts by feature**




<img width="604" height="499" alt="Image" src="https://github.com/user-attachments/assets/495f8766-350f-4ead-b335-df560b4b16a0" />



    
 **Kernel Density OF Fare amounts**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/02c9b27d-a527-4074-b709-112f03b3c90d" />



 **Scatter Plot OF Fare amounts by feature**


<img width="678" height="495" alt="Image" src="https://github.com/user-attachments/assets/00c19451-8812-47af-bf64-4ec51d84de86" />


 **New Analytical feature**

**1.**


<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/c3f5ae00-b9ed-4f31-8690-00b0ad36b09f" />




**2.**



<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/00004283-9b0d-4935-8318-7dc362015011" />









 **Enhancing datasets**

 

<img width="959" height="405" alt="Image" src="https://github.com/user-attachments/assets/a712a8ef-b9a3-476b-b99a-315fc6f966c6" />


 **Saving enhanced datasets**


 <img width="959" height="371" alt="Image" src="https://github.com/user-attachments/assets/3170f844-cd9d-4a23-921b-526923e54b0f" />



**AS THE OUTPUT, ENHANCED DATASETS WAS CREATED IN MY FILE**



<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/99e9d761-a00a-45bb-a577-cec9dfb847f0" />






**NEXT: PowerBI in Summary**

THIS IS THE MODEL VIEW IN PowerBI



<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/3ea05671-0f9e-4ade-8cb6-701f3e75f9d8" />






 **Some of Dashboard development stages**



<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/7648ad3b-dee0-49ae-8bce-75d4486013a7" />










**FINAL PROJECT DASHBOARD**

**In my visuals , i have used:**

1.card
2.gauge
3. bar chart
4. 5.Area chart
5. 6.Bar chart
6. line chart


HERE IT IS






<img width="959" height="539" alt="Image" src="https://github.com/user-attachments/assets/6dc1e351-b933-41b3-8fdf-777a0ca73c61" />









 

 









