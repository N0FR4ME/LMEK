# Contributing to LMEK

Thank you for your interest in contributing to LMEK! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/LMEK.git
   cd LMEK
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests to ensure everything works:
   ```bash
   python -m unittest discover tests
   ```

4. Commit your changes with clear commit messages:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

5. Push to your fork and submit a pull request

## Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting a PR
- Aim for good test coverage

## Adding New Features

When adding new features, please:

1. Add unit tests in the `tests/` directory
2. Add examples in the `examples/` directory
3. Update the README.md and QUICKSTART.md with usage examples
4. Update the CLI if applicable

## Reporting Bugs

When reporting bugs, please include:

- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version and operating system
- Relevant error messages or stack traces

## Feature Requests

Feature requests are welcome! Please:

- Check if the feature has already been requested
- Provide a clear description of the feature
- Explain the use case and why it would be valuable
- If possible, provide examples of how it would be used

## Pull Request Guidelines

- Keep pull requests focused on a single feature or bugfix
- Include tests for new functionality
- Update documentation as needed
- Ensure all tests pass
- Write clear commit messages
- Reference any related issues

## Questions?

If you have questions, please open an issue on GitHub.

Thank you for contributing to LMEK!
