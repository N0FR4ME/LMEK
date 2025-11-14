"""
Example: Electrical Circuits Analysis

Demonstrates circuit analysis functionality.
"""

from lmek import CircuitAnalyzer
import numpy as np


def main():
    analyzer = CircuitAnalyzer()
    
    print("=" * 60)
    print("LMEK Calculator - Electrical Circuits Examples")
    print("=" * 60)
    
    # Example 1: Ohm's Law
    print("\nExample 1: Ohm's Law")
    print("Given: Voltage = 12V, Resistance = 4Ω")
    result = analyzer.ohms_law(voltage=12, resistance=4)
    print(f"Current: {result['current']} A")
    
    # Example 2: Power Calculation
    print("\n" + "=" * 60)
    print("Example 2: Power Calculation")
    print("Given: Voltage = 12V, Current = 3A")
    result = analyzer.power_calculation(voltage=12, current=3)
    print(f"Power: {result['power']} W")
    print(f"Resistance: {result['resistance']} Ω")
    
    # Example 3: Series Resistance
    print("\n" + "=" * 60)
    print("Example 3: Series Resistance")
    resistances = [10, 20, 30, 40]
    print(f"Resistors: {resistances} Ω")
    total_series = analyzer.series_resistance(*resistances)
    print(f"Total series resistance: {total_series} Ω")
    
    # Example 4: Parallel Resistance
    print("\n" + "=" * 60)
    print("Example 4: Parallel Resistance")
    resistances = [10, 20, 30]
    print(f"Resistors: {resistances} Ω")
    total_parallel = analyzer.parallel_resistance(*resistances)
    print(f"Total parallel resistance: {total_parallel:.4f} Ω")
    
    # Example 5: Voltage Divider
    print("\n" + "=" * 60)
    print("Example 5: Voltage Divider")
    vin = 12
    r1 = 10
    r2 = 20
    print(f"Input voltage: {vin}V")
    print(f"R1 (top): {r1}Ω, R2 (bottom): {r2}Ω")
    vout = analyzer.voltage_divider(vin, r1, r2)
    print(f"Output voltage: {vout:.4f}V")
    
    # Example 6: Current Divider
    print("\n" + "=" * 60)
    print("Example 6: Current Divider")
    itotal = 6
    r1 = 10
    r2 = 20
    print(f"Total current: {itotal}A")
    print(f"R1: {r1}Ω, R2: {r2}Ω")
    i1, i2 = analyzer.current_divider(itotal, r1, r2)
    print(f"Current through R1: {i1:.4f}A")
    print(f"Current through R2: {i2:.4f}A")
    print(f"Verification (I1 + I2): {i1 + i2:.4f}A")
    
    # Example 7: RC Time Constant
    print("\n" + "=" * 60)
    print("Example 7: RC Time Constant")
    R = 1000  # 1kΩ
    C = 100e-6  # 100μF
    print(f"Resistance: {R}Ω")
    print(f"Capacitance: {C*1e6}μF")
    tau = analyzer.rc_time_constant(R, C)
    print(f"Time constant τ: {tau}s")
    
    # Example 8: Capacitor Voltage
    print("\n" + "=" * 60)
    print("Example 8: Capacitor Charging")
    v0 = 0  # Initial voltage
    vf = 12  # Final voltage
    tau = 0.1  # Time constant
    t = 0.1  # Time at which to calculate voltage
    print(f"Initial voltage: {v0}V")
    print(f"Final voltage: {vf}V")
    print(f"Time constant: {tau}s")
    print(f"Time: {t}s")
    v_t = analyzer.capacitor_voltage(v0, vf, t, tau)
    print(f"Voltage at t={t}s: {v_t:.4f}V")
    
    # Example 9: Plot RC Response
    print("\n" + "=" * 60)
    print("Example 9: RC Circuit Response Plot")
    print("Plotting capacitor charging curve...")
    analyzer.plot_rc_response(
        v0=0,
        vf=12,
        tau=0.1,
        title="RC Circuit Charging Response",
        show=False,
        save_path="/tmp/rc_response.png"
    )
    print("Saved to /tmp/rc_response.png")
    
    # Example 10: Impedance calculations
    print("\n" + "=" * 60)
    print("Example 10: AC Circuit Impedance")
    R = 1000  # 1kΩ
    C = 1e-6  # 1μF
    f = 1000  # 1kHz
    print(f"RC Circuit - Resistance: {R}Ω, Capacitance: {C*1e6}μF, Frequency: {f}Hz")
    Z = analyzer.impedance_rc(R, C, f)
    print(f"Impedance: {Z:.4f}")
    print(f"Magnitude: {abs(Z):.4f}Ω")
    print(f"Phase: {np.angle(Z, deg=True):.4f}°")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
