Title: US Hurricanes
Date: 2017-08-18
Modified: 2017-08-18 2314
Authors: Vincent La
Slug: hurricane
Summary: An analysis of severe weather patterns in the United States

<style type="text/css">
    .panel {
        width: 50%; height: 100%;
    }
</style>

<div style="margin: 2em auto; width: 100%; height: 600px;">
    <div class="panel" style="float: left;">
        <div style="width: 100%; height: 100%;
            background: url('images/Andrew_23_aug_1992_1231Z.jpg');
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;"></div>
    </div>
    <div class="panel" style="float: right;">
        <div style="height: 50%;
            background: url('images/New_Orleans_Survivor_Flyover.jpg');
            background-position: center right;
            background-repeat: no-repeat;
            background-size: cover;">
        </div><div style="height: 50%;
            background: url('images/Support_during_Hurricane_Harvey_(TX)_(50).jpg');
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;">
        </div>
    </div>
</div>

## Motivation

This project analyzes severe weather events, focusing on the United States. Some goals of this project are:

 * Revealing changing trends and patterns in weather events
 * Analyzing the severity, frequency, and impact of severe weather
 * Clarifying the connection between climate change and severe weather
 
## Technology

I'm not too crazy on using the "right" software, and am more concerned with informing the public and answering
the questions above. Currently I've heavily used:

 * Python: mainly to process and load data
 * R: dplyr, ggplot2, leaflet
 * PostgreSQL + PostGIS