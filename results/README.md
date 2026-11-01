# Experiment log

After running each experiment, append one CSV row to `experiment_log.csv`.
Record only measurements you observed. The in-simulator progress display may provide
track percentage and a timer; do not infer missing values. `line_lost_count` can be
measured manually if needed. Take at least one screenshot per controller you test.

The example scripts use `KP=0.01` and `FORWARD_SPEED=1.0` as starting values, not
verified best settings. Compare multiple runs before drawing conclusions.
