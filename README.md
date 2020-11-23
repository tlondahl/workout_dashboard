# Workou Dashboard
## Introduction
One of my musts in life is to exercise. I know that it gives me energy and makes me feel good. A couple of years ago I started focusing on Olympic Weightlifting, i.e. Snatch and Clean & Jerk. I have been working on my lifts for quite some time but I have no clue on wether I'm good, bad or just plain average, neither do I have a clear view over my progression. I have triad saving my results in spreadsheets, training apps, notes, you name it. Hence, I decided to build a dashboard to visualize my progress.

### Data and Packages
To build this dashboard i used the Dash and Plotly. The data used was mainly based on my own personal records (PR) it was combines with various other data sources to get good reference points. The code and all the datasets can be found [here](https://github.com/tlondahl/workout_dashboard/blob/main/lifting_app.py).

## Results
For those who are not as familiar with Olympic Weightlifting it circles around two main lifts, the "Snatch" (from the ground to over head in one move) and the "Clean and Jerk" (from ground to "front rack" and then from that position to over head). How much you can lift in these two exercises is what matters. It is these two numbers (i.e. your PR's) that you can stare yourself blind at. Hence it was important to me that it was these two lifts that were in focus and the first thing you saw wen entering the dashboard. Furthermore to get a better understanding on howe good you are I used the standards at www.strengthlevel.com/strength-standards as indicators ranging from Beginner to Elite. I visualized everything by plotting it as a gauge with the standards as the background from red (beginner) to green (elite), my goal as a red line and my current PR as the bar with the actual value (in kg) within the gauge and the delta from my last PR below.

![The Snatch and Clean & Jerk Gauges](https://github.com/tlondahl/workout_dashboard/blob/main/snatch_cj_gauge.png)

Even though Olympic Weightlifting only consists of two lifts there are a lot of accessory lifts you need to practice in order to fine-tune you technique and strength in each part of the lift. If you are weak in any of the accessory exercises it can often be an indicator on where it is in your lift that you fail and where you need to improve in order to improve your PR in either snatch or clean & jerk. However, as with everything else in life, it is hard to know where you are without references. Hence, I found a table originating from the Soviet Union, and if it is one thing that is true it is that Russians/Soviets know how to lift heavy weights. Anyhow, I combined this data with my own data, and plotted the results in a bullet graph with the Soviet Standards as a background indicators were dark grey = below were you ought to be, light grey = where you're supposed to be, and even lighter grey/blue means that you can lift more than what you need to (in relation to your PR).  Then of course my own result made out the bar.

![Bullet Gauges of the Accessory Lifts](https://github.com/tlondahl/workout_dashboard/blob/main/accessory_lifts_bullets.png)

## Future Development
I have a few ideas on how to improve the Dashboard.
Ability to update a new PR in the dashboard
Filtering what exercises to show
I would like to expand it to show other type of training results such as Crossfit benchmark workouts.

![Overview of a part of the Dashboard](https://github.com/tlondahl/workout_dashboard/blob/main/overview.png)
