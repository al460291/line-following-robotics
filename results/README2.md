Additional Experimental - 7 max speed

The additional experiments at a maximum forward speed of 7.0 revealed more significant performance differences between the P, PD, and PID controllers.

The PID controller achieved the lowest Mean Absolute Error (MAE) of 0.2463, compared to 0.2836 for PD and 0.3348 for P. This represents a 26.43% reduction in tracking error compared to P and a 13.15% reduction compared to PD.

An interesting observation is that the advantage of PID over P increased across the tested speed configurations. At maximum speeds of 3.0, 5.0, and 7.0, PID reduced the MAE relative to P by 5.53%, 12.63%, and 26.43%, respectively.

Furthermore, PID achieved the highest average commanded forward speed (6.261), compared to PD (6.149) and P (5.996), while maintaining the lowest tracking error.

All three controllers recorded zero line losses during the experiments, suggesting that the main difference between them was tracking accuracy rather than line detection failure.

Overall, these results suggest that PID provides a better balance between tracking accuracy and commanded forward speed under the evaluated high-speed conditions.

However, these findings are based on individual experimental runs, and the observation periods differed between some configurations. Additional repeated trials under identical conditions would be necessary to establish statistically reliable conclusions about controller robustness.
