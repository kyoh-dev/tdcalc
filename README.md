# tdcalc

A simple term deposit calculator

# Getting started

1. Install Python >= 3.12
1. Run the following commands to get a virtual environment setup

```python
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.dev.txt
```

# Usage

## Running the calculator

You can run the calculator by executing the package as a module with `python -m tdcalc`:

```shell
$ python -m tdcalc --help
usage: python -m tdcalc [-h] --deposit DEPOSIT --interest-rate INTEREST_RATE --term-months TERM_MONTHS --paid-at {monthly,quarterly,annually,maturity}

Calculate interest on a term deposit

options:
-h, --help            show this help message and exit
--deposit DEPOSIT, -d DEPOSIT
                      Amount of the initial deposit
--interest-rate INTEREST_RATE, -i INTEREST_RATE
                      Interest rate as percentage, e.g. 1.1
--term-months TERM_MONTHS, -t TERM_MONTHS
                      Term of the deposit in months
--paid-at {monthly,quarterly,annually,maturity}, -p {monthly,quarterly,annually,maturity}
                      When the interest will be paid
```

### Concrete example

```shell
python -m tdcalc -d 10000 -i 1.1 -t 36 -p maturity                                                                                                                                                                                                                    [16:45:45]
```

## Running the tests

You can run the tests using `pytest [-vvv] tests` to get a nice output.

# Assumptions

* I was entirely sure what "at maturity" meant in terms of calculating the interest, so I opted for calculating that as
simple interest instead of compound, based on Google searches and the output of the Bendigo Bank calculator
* The input for the term is in months, as that's easier to calculate for months and years, but that's assuming the user
is amenable to this

# Design choices
* Tried to approach this using mostly TDD, but didn't bother testing the `__main__.py` package runner
* Validating inputs early on and logging an error to the terminal instead of raising in the calculation functions,
as it's assumed this is being used as a CLI
* Didn't bother going with a full CLI framework in order to get the functionality working properly within the time limit
