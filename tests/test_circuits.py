"""
Unit tests for LMEK circuit analyzer.
"""

import unittest
import numpy as np
from lmek import CircuitAnalyzer
import os


class TestCircuitAnalyzer(unittest.TestCase):
    """Test cases for CircuitAnalyzer."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = CircuitAnalyzer()
    
    def test_ohms_law_voltage(self):
        """Test Ohm's law - calculate voltage."""
        result = self.analyzer.ohms_law(current=3, resistance=4)
        self.assertAlmostEqual(result['voltage'], 12.0)
    
    def test_ohms_law_current(self):
        """Test Ohm's law - calculate current."""
        result = self.analyzer.ohms_law(voltage=12, resistance=4)
        self.assertAlmostEqual(result['current'], 3.0)
    
    def test_ohms_law_resistance(self):
        """Test Ohm's law - calculate resistance."""
        result = self.analyzer.ohms_law(voltage=12, current=3)
        self.assertAlmostEqual(result['resistance'], 4.0)
    
    def test_power_calculation(self):
        """Test power calculation."""
        result = self.analyzer.power_calculation(voltage=12, current=3)
        self.assertAlmostEqual(result['power'], 36.0)
    
    def test_series_resistance(self):
        """Test series resistance calculation."""
        result = self.analyzer.series_resistance(10, 20, 30)
        self.assertAlmostEqual(result, 60.0)
    
    def test_parallel_resistance(self):
        """Test parallel resistance calculation."""
        result = self.analyzer.parallel_resistance(10, 10)
        self.assertAlmostEqual(result, 5.0)
    
    def test_voltage_divider(self):
        """Test voltage divider."""
        vout = self.analyzer.voltage_divider(12, 10, 20)
        self.assertAlmostEqual(vout, 8.0)
    
    def test_current_divider(self):
        """Test current divider."""
        i1, i2 = self.analyzer.current_divider(6, 10, 20)
        self.assertAlmostEqual(i1 + i2, 6.0)
    
    def test_rc_time_constant(self):
        """Test RC time constant."""
        tau = self.analyzer.rc_time_constant(1000, 100e-6)
        self.assertAlmostEqual(tau, 0.1)
    
    def test_rl_time_constant(self):
        """Test RL time constant."""
        tau = self.analyzer.rl_time_constant(100, 10)
        self.assertAlmostEqual(tau, 0.1)
    
    def test_capacitor_voltage(self):
        """Test capacitor voltage calculation."""
        v = self.analyzer.capacitor_voltage(0, 12, 0.1, 0.1)
        # At t = tau, voltage should be about 63.2% of final
        expected = 12 * (1 - np.exp(-1))
        self.assertAlmostEqual(v, expected)
    
    def test_impedance_rc(self):
        """Test RC impedance calculation."""
        Z = self.analyzer.impedance_rc(1000, 1e-6, 1000)
        # Check that it's a complex number
        self.assertIsInstance(Z, complex)
        # Check that magnitude is reasonable
        self.assertGreater(abs(Z), 0)
    
    def test_impedance_rl(self):
        """Test RL impedance calculation."""
        Z = self.analyzer.impedance_rl(100, 0.01, 1000)
        # Check that it's a complex number
        self.assertIsInstance(Z, complex)
        # Check that magnitude is reasonable
        self.assertGreater(abs(Z), 0)
    
    def test_plot_rc_response(self):
        """Test RC response plotting."""
        save_path = "/tmp/test_rc.png"
        
        if os.path.exists(save_path):
            os.remove(save_path)
        
        self.analyzer.plot_rc_response(
            0, 12, 0.1,
            show=False,
            save_path=save_path
        )
        
        self.assertTrue(os.path.exists(save_path))
        
        if os.path.exists(save_path):
            os.remove(save_path)


if __name__ == '__main__':
    unittest.main()
