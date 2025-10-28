Feature: Calculator basic usage

  # ADD
  Scenario: Use the add operation
    Given I open the calculator
    When I type 2 + 2
    Then the result is 4

  Scenario Outline: Use the add operation multiple times
    Given I open the calculator
    When I type <op_1> + <op_2>
    Then the result is <res>

    Examples: Add numbers
      | op_1 | op_2 | res |
      | 2    | 2    | 4   |
      | 1    | 0    | 1   |
      | 1    | -1   | 0   |
      | 5    | 3    | 8   |

  # SUBSTRACT
  Scenario: Use the substract operation
    Given I open the calculator
    When I type 10 - 3
    Then the result is 7

  Scenario Outline: Use the substract operation multiple times
    Given I open the calculator
    When I type <op_1> - <op_2>
    Then the result is <res>

    Examples: Substract numbers
      | op_1 | op_2 | res |
      | 10   | 3    | 7   |
      | 5    | 0    | 5   |
      | 3    | 10   | -7  |
      | 0    | 5    | -5  |

  # MULTIPLY
  Scenario: Use the multiply operation
    Given I open the calculator
    When I type 4 * 5
    Then the result is 20

  Scenario Outline: Use the multiply operation multiple times
    Given I open the calculator
    When I type <op_1> * <op_2>
    Then the result is <res>

    Examples: Multiply numbers
      | op_1 | op_2 | res |
      | 4    | 5    | 20  |
      | 7    | 0    | 0   |
      | -3   | 4    | -12 |
      | 3    | 3    | 9   |

  # DIVIDE
  Scenario: Use the divide operation
    Given I open the calculator
    When I type 10 / 2
    Then the result is 5

  Scenario Outline: Use the divide operation multiple times
    Given I open the calculator
    When I type <op_1> / <op_2>
    Then the result is <res>

    Examples: Divide numbers
      | op_1 | op_2 | res  |
      | 10   | 2    | 5    |
      | 10   | 4    | 2.5  |
      | -10  | 2    | -5   |
      | 20   | 5    | 4    |

  # POWER
  Scenario: Use the power operation
    Given I open the calculator
    When I type 2 ^ 3
    Then the result is 8

  Scenario Outline: Use the power operation multiple times
    Given I open the calculator
    When I type <op_1> ^ <op_2>
    Then the result is <res>

    Examples: Power calculations
      | op_1 | op_2 | res |
      | 2    | 3    | 8   |
      | 5    | 0    | 1   |
      | 2    | -1   | 0.5 |
      | 3    | 2    | 9   |

  # SQUARE ROOT
  Scenario: Use the square root operation
    Given I open the calculator
    When I type sqrt(16)
    Then the result is 4

  Scenario Outline: Use the square root operation multiple times
    Given I open the calculator
    When I type sqrt(<op_1>)
    Then the result is <res>

    Examples: Square roots
      | op_1 | res |
      | 16   | 4   |
      | 9    | 3   |
      | 0    | 0   |
      | 4    | 2   |

  # LOG10
  Scenario: Use the logarithm base 10 operation
    Given I open the calculator
    When I type log10(10)
    Then the result is 1

  Scenario Outline: Use the logarithm base 10 operation multiple times
    Given I open the calculator
    When I type log10(<op_1>)
    Then the result is <res>

    Examples: Logarithms base 10
      | op_1 | res |
      | 10   | 1   |
      | 100  | 2   |
      | 1    | 0   |
      | 1000 | 3   |
