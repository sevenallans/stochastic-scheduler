"""
Stochastic Schedule Simulator
Author: Allan Kipruto
Description: A Monte Carlo simulation comparing rigid time-blocking against 
             event-driven scheduling under varying cognitive fatigue and shock probabilities.
"""

import numpy as np
import pandas as pd

class WeeklySimulation:
    def __init__(self, target_hours=10, liquid_hours=15):
        self.target_hours = target_hours
        self.liquid_hours = liquid_hours
        
    def generate_shocks(self, iterations=1000):
        """
        Generates a matrix of random environmental and cognitive shocks.
        0 = Normal flow, 1 = External Disruption, 2 = Cognitive Fatigue
        """
        # 70% normal, 15% external disruption, 15% fatigue
        probabilities = [0.70, 0.15, 0.15] 
        # Generate shocks for every available liquid hour across all iterations
        return np.random.choice([0, 1, 2], size=(iterations, self.liquid_hours), p=probabilities)

    def run_rigid_calendar(self, shock_matrix):
        """Simulates Path A: Static scheduling with no defenses."""
        completions = []
        for week in shock_matrix:
            hours_completed = 0
            for hour in week:
                if hour == 0:  # Normal flow
                    hours_completed += 1
                elif hour == 1: # Distraction destroys the block
                    continue
                elif hour == 2: # Fatigue halves productivity
                    hours_completed += 0.5
            
            # Did we hit the 10-hour target?
            completions.append(1 if hours_completed >= self.target_hours else 0)
        
        return completions

    def run_event_driven(self, shock_matrix):
        """Simulates Path C: Defenses active (ignores minor shocks)."""
        completions = []
        for week in shock_matrix:
            hours_completed = 0
            fatigue_debt = 0  # Tracks cognitive exhaustion
            
            for hour in week:
                if fatigue_debt > 0:
                    # Defense 1: Mandatory recovery block if fatigued (Stop-Loss)
                    fatigue_debt -= 1
                    continue
                    
                if hour == 0:  # Normal flow
                    hours_completed += 1
                elif hour == 1: 
                    # Defense 2: Air-gapping absorbs the external shock
                    # The system blocks the distraction, preserving the hour
                    hours_completed += 1
                elif hour == 2: 
                    # Defense 3: Fatigue hits. Halt work before negative returns.
                    fatigue_debt = 1  # Force 1 hour of recovery next
                    hours_completed += 0.5
            
            # Did we hit the 10-hour target?
            completions.append(1 if hours_completed >= self.target_hours else 0)
            
        return completions

if __name__ == "__main__":
    print("Initializing Monte Carlo Engine...")
    sim = WeeklySimulation()
    shocks = sim.generate_shocks()
    
    rigid_results = sim.run_rigid_calendar(shocks)
    event_results = sim.run_event_driven(shocks)
    
    rigid_success = np.mean(rigid_results) * 100
    event_success = np.mean(event_results) * 100
    
    print(f"Rigid Calendar Success Rate: {rigid_success:.2f}%")
    print(f"Event-Driven (Defended) Success Rate: {event_success:.2f}%")