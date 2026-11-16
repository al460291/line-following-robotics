# Experiment log

After seeing the results of the experiments, register in experiment_log.csv, we can conclude that PID had the better performance. The MAE meassure was the variable select for these experiments and it shows that, PID presents and error of 0.1196 and 0.1383, respectly, while the worse one was P, as expected, PI shows a better performance compared to P, in the first experiment was not that big, but, in the second experiment wherre the max speed was increased for 3.0 to 5.0 and the round was increased for 2.5 to 3.0. Also, surprinsgly, in the experiments, there was no loss of the line, not even in the P experiment. 

There is also a clear correlation between speed and the MAE meassure, if the speed increase so due the error.

Surprisingly, none of the controllers lost the line during the experiments, including the P controller. All six experimental runs recorded zero line losses, so we can conclude thatthat all controllers were capable of completing the tested scenarios without losing the target line, although their tracking accuracy differed, of course, again, the increase was not that significant, but this is also because the idea is that the car follows the red line, in these experiments at least.

==================
Aditional Experiment - 100s

The controller achieved a Mean Absolute Error (MAE) of 0.2324, representing a 46.81% increase compared to its previous result at a maximum speed of 5.0 (MAE = 0.1583).

Compared to the initial experiment at a maximum speed of 3.0 (MAE = 0.1266), the tracking error increased by approximately 83.57%.

These findings suggest that the P controller becomes less accurate under higher-speed operating conditions, potentially because proportional control alone does not adequately compensate for rapid changes in tracking error.

Once again the zero lines didn't appear, which is good, I did an experiment with 7 and it did went out of the lines so the max speed should be between 6-6.5 to mantain estability.



