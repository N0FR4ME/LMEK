#!/usr/bin/env python3
"""
LMEK Calculator CLI

Command-line interface for Linear Mathematic Analysis and Electrical Circuits Calculator.
"""

import argparse
import sys
import numpy as np
from lmek import MatrixCalculator, FunctionPlotter, CircuitAnalyzer


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="LMEK - Linear Mathematic Analysis and Electrical Circuits Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Calculate RREF of a matrix
  python -m lmek.cli matrix rref "[[2,1,-1,8],[-3,-1,2,-11],[-2,1,2,-3]]"
  
  # Plot a function
  python -m lmek.cli plot function "x**2" -5 5
  
  # Calculate Ohm's law
  python -m lmek.cli circuit ohms --voltage 12 --resistance 4
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Matrix operations
    matrix_parser = subparsers.add_parser('matrix', help='Matrix operations')
    matrix_subparsers = matrix_parser.add_subparsers(dest='operation')
    
    rref_parser = matrix_subparsers.add_parser('rref', help='Calculate RREF')
    rref_parser.add_argument('matrix', help='Matrix as string representation')
    
    det_parser = matrix_subparsers.add_parser('det', help='Calculate determinant')
    det_parser.add_argument('matrix', help='Matrix as string representation')
    
    inv_parser = matrix_subparsers.add_parser('inv', help='Calculate inverse')
    inv_parser.add_argument('matrix', help='Matrix as string representation')
    
    eigen_parser = matrix_subparsers.add_parser('eigen', help='Calculate eigenvalues')
    eigen_parser.add_argument('matrix', help='Matrix as string representation')
    
    # Plotting
    plot_parser = subparsers.add_parser('plot', help='Plotting functions')
    plot_subparsers = plot_parser.add_subparsers(dest='plot_type')
    
    func_parser = plot_subparsers.add_parser('function', help='Plot a function')
    func_parser.add_argument('expression', help='Mathematical expression (e.g., "sin(x)")')
    func_parser.add_argument('start', type=float, help='Start of interval')
    func_parser.add_argument('end', type=float, help='End of interval')
    func_parser.add_argument('--save', help='Save plot to file')
    
    # Circuit analysis
    circuit_parser = subparsers.add_parser('circuit', help='Circuit analysis')
    circuit_subparsers = circuit_parser.add_subparsers(dest='circuit_op')
    
    ohms_parser = circuit_subparsers.add_parser('ohms', help="Ohm's law calculation")
    ohms_parser.add_argument('--voltage', type=float, help='Voltage (V)')
    ohms_parser.add_argument('--current', type=float, help='Current (A)')
    ohms_parser.add_argument('--resistance', type=float, help='Resistance (Ω)')
    
    power_parser = circuit_subparsers.add_parser('power', help='Power calculation')
    power_parser.add_argument('--voltage', type=float, help='Voltage (V)')
    power_parser.add_argument('--current', type=float, help='Current (A)')
    power_parser.add_argument('--resistance', type=float, help='Resistance (Ω)')
    power_parser.add_argument('--power', type=float, help='Power (W)')
    
    series_parser = circuit_subparsers.add_parser('series', help='Series resistance')
    series_parser.add_argument('resistances', nargs='+', type=float, help='Resistance values')
    
    parallel_parser = circuit_subparsers.add_parser('parallel', help='Parallel resistance')
    parallel_parser.add_argument('resistances', nargs='+', type=float, help='Resistance values')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Handle commands
    if args.command == 'matrix':
        handle_matrix_command(args)
    elif args.command == 'plot':
        handle_plot_command(args)
    elif args.command == 'circuit':
        handle_circuit_command(args)
    else:
        parser.print_help()
        return 1
    
    return 0


def handle_matrix_command(args):
    """Handle matrix operations."""
    calc = MatrixCalculator()
    
    # Parse matrix string
    try:
        matrix = eval(args.matrix)
        matrix = np.array(matrix, dtype=float)
    except Exception as e:
        print(f"Error parsing matrix: {e}", file=sys.stderr)
        return 1
    
    if args.operation == 'rref':
        result = calc.rref(matrix)
        print("RREF:")
        print(result)
    elif args.operation == 'det':
        result = calc.determinant(matrix)
        print(f"Determinant: {result}")
    elif args.operation == 'inv':
        try:
            result = calc.inverse(matrix)
            print("Inverse:")
            print(result)
        except np.linalg.LinAlgError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    elif args.operation == 'eigen':
        result = calc.eigenvalues(matrix)
        print("Eigenvalues:")
        print(result)
    else:
        print("Unknown matrix operation", file=sys.stderr)
        return 1
    
    return 0


def handle_plot_command(args):
    """Handle plotting commands."""
    plotter = FunctionPlotter()
    
    if args.plot_type == 'function':
        try:
            plotter.plot_symbolic(
                args.expression,
                (args.start, args.end),
                save_path=args.save,
                show=(args.save is None)
            )
            if args.save:
                print(f"Plot saved to {args.save}")
        except Exception as e:
            print(f"Error plotting function: {e}", file=sys.stderr)
            return 1
    else:
        print("Unknown plot type", file=sys.stderr)
        return 1
    
    return 0


def handle_circuit_command(args):
    """Handle circuit analysis commands."""
    analyzer = CircuitAnalyzer()
    
    if args.circuit_op == 'ohms':
        try:
            result = analyzer.ohms_law(
                voltage=args.voltage,
                current=args.current,
                resistance=args.resistance
            )
            print("Ohm's Law Results:")
            print(f"  Voltage: {result['voltage']:.4f} V")
            print(f"  Current: {result['current']:.4f} A")
            print(f"  Resistance: {result['resistance']:.4f} Ω")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    elif args.circuit_op == 'power':
        try:
            result = analyzer.power_calculation(
                voltage=args.voltage,
                current=args.current,
                resistance=args.resistance,
                power=args.power
            )
            print("Power Calculation Results:")
            if result['voltage'] is not None:
                print(f"  Voltage: {result['voltage']:.4f} V")
            if result['current'] is not None:
                print(f"  Current: {result['current']:.4f} A")
            if result['resistance'] is not None:
                print(f"  Resistance: {result['resistance']:.4f} Ω")
            if result['power'] is not None:
                print(f"  Power: {result['power']:.4f} W")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    elif args.circuit_op == 'series':
        result = analyzer.series_resistance(*args.resistances)
        print(f"Total series resistance: {result:.4f} Ω")
    elif args.circuit_op == 'parallel':
        try:
            result = analyzer.parallel_resistance(*args.resistances)
            print(f"Total parallel resistance: {result:.4f} Ω")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        print("Unknown circuit operation", file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
