# Stochastic Schedule Simulator

**Author:** Allan Kipruto

## Overview
A Monte Carlo simulation built in Python to mathematically evaluate time-management strategies in high-variance, stochastic environments. This project tests the resilience of a Rigid Calendar (static time-blocking) versus an Event-Driven Protocol (dynamic execution with cognitive defenses).

## The Experiment
The engine runs 1,000 simulated iterations of a standard work week under constrained liquidity (12 available hours for a 10-hour target output). It introduces randomized environmental shocks:
* **External Disruptions:** Urgent, unexpected tasks that destroy planned time blocks.
* **Internal Friction:** Cognitive fatigue and energy depletion resulting from extended deep work.

## Key Findings
Under stress-tested constraints (12 liquid hours):
* **Rigid Calendar Success Rate:** ~87.7%
* **Event-Driven Success Rate:** ~93.2%

**Conclusion:** When time liquidity dries up, rigid scheduling systems break. Event-driven systems that utilize cognitive stop-losses and active defense mechanisms preserve core execution and yield a mathematically higher probability of success.

## How to Run
```cmd
python stochastic_scheduler.py