Title: US Census Data Visualization Project
Date: 2017-05-14
Modified: 2017-05-14 2314
Tags: census, data, r, shiny, python
Authors: Vincent La
Slug: census
Summary: Overview of Census Data Visualization Project

<img style="object-fit: cover; display: block; margin-left: auto;
    margin-right: auto;"
    width="100%" height="400px"
    src="http://vincela.com/img/census/us-income.png"></img>

## Motivation
The United States of America is a large country, spanning from coast to coast 
in North America. Inside this country are 300 million people, living in 
a myriad of social environments and cultural influences. Thus, trying to study and quantify
some of the attributes of the American people is a difficult task. Yet for the past 
century, this is what the US Census Bureau has done.

As a result of their efforts, there is a large cache of data about Americans.
This project aims to put that data to good use by displaying the data 
in informative ways. Although this project features lots of beautiful data 
visualizations, statistical analysis is not just about pretty graphs. This 
project also seeks to rearrange and combine Census data with other sources 
of information to create insights that cannot just be gained by staring 
at Census data files in Excel.

## Reports
As a college student, time is always in short supply, so the projects below 
are a rough draft.

***Note:*** Because these apps involve loading tens of thousands of observations 
and mapping them, the server and pages may take a while to load (about 10 seconds
on a good day). I will add a loading bar (as well as making the pages load faster)
when I find the time for it.

### Median Household Income
<a href="http://www.vincela.com:3838/census-income">
    <img style="object-fit: cover; display: block; margin-left: auto;
        margin-right: auto;"
        width="100%" height="400px"
        src="http://vincela.com/img/census/sf-money.png"></img>
</a>
    
Is there geographic clustering of high and low income regions? 
Does higher median household income necessary mean higher spending power?
[Find out more.](http://www.vincela.com:3838/census-income)

### Race and Ethnicity
<a href="http://www.vincela.com:3838/census-race">
    <img style="object-fit: cover; display: block; margin-left: auto;
        margin-right: auto;"
        width="100%" height="400px"
        src="http://vincela.com/img/census/us-blacks.png"></img>
</a>
        
Not as well-polished as the median household income report above. Currently,
this "report" just consists of some maps and a data table.

## GitHub and the Technical Stuff
For a look inside the interals of this project, feel free visit
[https://github.com/vincentlaucsb/Census-2010](https://github.com/vincentlaucsb/Census-2010).

This project's objectives were mostly accomplished using:

* PostgreSQL
    * Did most of the heavy lifting cleaning, querying, and aggregating the data
    * Provided the data backend for the Shiny web-app
* R
    * Created an interactive web interface via **Shiny**
    * Created all of the data visualizations via **Leaflet** and **ggplot2**
    * Also did some data cleaning
* Python
    * A custom library automated the copying of US Census Bureau CSV and TXT files into
      a PostgreSQL database.