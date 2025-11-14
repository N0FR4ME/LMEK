"""
Electrical circuits analysis module for LMEK calculator.

Provides circuit analysis functionality for linear circuits.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt


class CircuitAnalyzer:
    """Analyzer for electrical circuits."""
    
    def __init__(self):
        """Initialize the CircuitAnalyzer."""
        pass
    
    @staticmethod
    def ohms_law(voltage: Optional[float] = None,
                 current: Optional[float] = None,
                 resistance: Optional[float] = None) -> Dict[str, float]:
        """
        Apply Ohm's Law: V = I * R
        
        Args:
            voltage: Voltage in volts (V)
            current: Current in amperes (A)
            resistance: Resistance in ohms (Ω)
            
        Returns:
            Dictionary with all three values
            
        Examples:
            >>> analyzer = CircuitAnalyzer()
            >>> result = analyzer.ohms_law(voltage=12, resistance=4)
            >>> print(result['current'])  # Output: 3.0
        """
        if sum([voltage is not None, current is not None, resistance is not None]) != 2:
            raise ValueError("Exactly two parameters must be provided")
        
        if voltage is None:
            voltage = current * resistance
        elif current is None:
            current = voltage / resistance
        else:  # resistance is None
            resistance = voltage / current
        
        return {
            'voltage': voltage,
            'current': current,
            'resistance': resistance
        }
    
    @staticmethod
    def power_calculation(voltage: Optional[float] = None,
                         current: Optional[float] = None,
                         resistance: Optional[float] = None,
                         power: Optional[float] = None) -> Dict[str, float]:
        """
        Calculate power using various formulas:
        P = V * I
        P = V² / R
        P = I² * R
        
        Args:
            voltage: Voltage in volts (V)
            current: Current in amperes (A)
            resistance: Resistance in ohms (Ω)
            power: Power in watts (W)
            
        Returns:
            Dictionary with all values
        """
        provided = sum([v is not None for v in [voltage, current, resistance, power]])
        if provided < 2:
            raise ValueError("At least two parameters must be provided")
        
        # Calculate missing values
        if power is None:
            if voltage is not None and current is not None:
                power = voltage * current
            elif voltage is not None and resistance is not None:
                power = voltage ** 2 / resistance
            elif current is not None and resistance is not None:
                power = current ** 2 * resistance
        
        if voltage is None:
            if power is not None and current is not None:
                voltage = power / current
            elif power is not None and resistance is not None:
                voltage = np.sqrt(power * resistance)
        
        if current is None:
            if power is not None and voltage is not None:
                current = power / voltage
            elif power is not None and resistance is not None:
                current = np.sqrt(power / resistance)
        
        if resistance is None:
            if voltage is not None and current is not None:
                resistance = voltage / current
            elif power is not None and voltage is not None:
                resistance = voltage ** 2 / power
            elif power is not None and current is not None:
                resistance = power / current ** 2
        
        return {
            'voltage': voltage,
            'current': current,
            'resistance': resistance,
            'power': power
        }
    
    @staticmethod
    def series_resistance(*resistances: float) -> float:
        """
        Calculate total resistance for resistors in series.
        R_total = R1 + R2 + R3 + ...
        
        Args:
            *resistances: Variable number of resistance values
            
        Returns:
            Total resistance
        """
        return sum(resistances)
    
    @staticmethod
    def parallel_resistance(*resistances: float) -> float:
        """
        Calculate total resistance for resistors in parallel.
        1/R_total = 1/R1 + 1/R2 + 1/R3 + ...
        
        Args:
            *resistances: Variable number of resistance values
            
        Returns:
            Total resistance
        """
        if any(r == 0 for r in resistances):
            raise ValueError("Resistance cannot be zero")
        
        return 1 / sum(1/r for r in resistances)
    
    @staticmethod
    def voltage_divider(vin: float, r1: float, r2: float) -> float:
        """
        Calculate output voltage in a voltage divider circuit.
        Vout = Vin * R2 / (R1 + R2)
        
        Args:
            vin: Input voltage
            r1: First resistor (top)
            r2: Second resistor (bottom)
            
        Returns:
            Output voltage
        """
        return vin * r2 / (r1 + r2)
    
    @staticmethod
    def current_divider(itotal: float, r1: float, r2: float) -> Tuple[float, float]:
        """
        Calculate current distribution in parallel resistors.
        
        Args:
            itotal: Total current
            r1: First resistor
            r2: Second resistor
            
        Returns:
            Tuple of (current through r1, current through r2)
        """
        i1 = itotal * r2 / (r1 + r2)
        i2 = itotal * r1 / (r1 + r2)
        return (i1, i2)
    
    @staticmethod
    def rc_time_constant(resistance: float, capacitance: float) -> float:
        """
        Calculate RC time constant.
        τ = R * C
        
        Args:
            resistance: Resistance in ohms
            capacitance: Capacitance in farads
            
        Returns:
            Time constant in seconds
        """
        return resistance * capacitance
    
    @staticmethod
    def rl_time_constant(resistance: float, inductance: float) -> float:
        """
        Calculate RL time constant.
        τ = L / R
        
        Args:
            resistance: Resistance in ohms
            inductance: Inductance in henrys
            
        Returns:
            Time constant in seconds
        """
        return inductance / resistance
    
    @staticmethod
    def capacitor_voltage(v0: float, vf: float, t: float, tau: float) -> float:
        """
        Calculate capacitor voltage during charging/discharging.
        V(t) = Vf + (V0 - Vf) * e^(-t/τ)
        
        Args:
            v0: Initial voltage
            vf: Final voltage
            t: Time
            tau: Time constant
            
        Returns:
            Voltage at time t
        """
        return vf + (v0 - vf) * np.exp(-t / tau)
    
    @staticmethod
    def plot_rc_response(v0: float, vf: float, tau: float, 
                        duration: float = None,
                        num_points: int = 1000,
                        title: str = "RC Circuit Response",
                        show: bool = True,
                        save_path: Optional[str] = None) -> None:
        """
        Plot RC circuit voltage response over time.
        
        Args:
            v0: Initial voltage
            vf: Final voltage
            tau: Time constant
            duration: Duration to plot (default: 5*tau)
            num_points: Number of points to plot
            title: Plot title
            show: Whether to display the plot
            save_path: Optional path to save the figure
        """
        if duration is None:
            duration = 5 * tau
        
        t = np.linspace(0, duration, num_points)
        v = vf + (v0 - vf) * np.exp(-t / tau)
        
        plt.figure(figsize=(10, 6))
        plt.plot(t, v, 'b-', linewidth=2, label='V(t)')
        plt.axhline(y=vf, color='r', linestyle='--', label=f'Final Voltage = {vf}V')
        plt.axhline(y=v0, color='g', linestyle='--', label=f'Initial Voltage = {v0}V')
        plt.axvline(x=tau, color='orange', linestyle='--', label=f'τ = {tau}s')
        
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    @staticmethod
    def impedance_rc(resistance: float, capacitance: float, frequency: float) -> complex:
        """
        Calculate impedance of RC circuit.
        Z = R + 1/(jωC)
        
        Args:
            resistance: Resistance in ohms
            capacitance: Capacitance in farads
            frequency: Frequency in Hz
            
        Returns:
            Complex impedance
        """
        omega = 2 * np.pi * frequency
        z_c = -1j / (omega * capacitance)
        return resistance + z_c
    
    @staticmethod
    def impedance_rl(resistance: float, inductance: float, frequency: float) -> complex:
        """
        Calculate impedance of RL circuit.
        Z = R + jωL
        
        Args:
            resistance: Resistance in ohms
            inductance: Inductance in henrys
            frequency: Frequency in Hz
            
        Returns:
            Complex impedance
        """
        omega = 2 * np.pi * frequency
        z_l = 1j * omega * inductance
        return resistance + z_l
