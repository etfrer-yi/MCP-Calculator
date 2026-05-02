from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exp: float) -> float:
    """Raises base to the power of exp."""
    return base ** exp

@mcp.tool()
def sqrt(n: float) -> float:
    """Returns the square root of n."""
    if n < 0:
        raise ValueError("Cannot take sqrt of a negative number")
    return math.sqrt(n)

@mcp.tool()
def sin(x: float) -> float:
    """Sine of x (in radians)."""
    return math.sin(x)

@mcp.tool()
def cos(x: float) -> float:
    """Cosine of x (in radians)."""
    return math.cos(x)

@mcp.tool()
def tan(x: float) -> float:
    """Tangent of x (in radians)."""
    return math.tan(x)

@mcp.tool()
def asin(x: float) -> float:
    """Arcsine of x, returns radians."""
    return math.asin(x)

@mcp.tool()
def acos(x: float) -> float:
    """Arccosine of x, returns radians."""
    return math.acos(x)

@mcp.tool()
def atan(x: float) -> float:
    """Arctangent of x, returns radians."""
    return math.atan(x)

@mcp.tool()
def log(x: float, base: float = math.e) -> float:
    """Logarithm of x with given base (default: natural log)."""
    return math.log(x, base)

@mcp.tool()
def log10(x: float) -> float:
    """Base-10 logarithm of x."""
    return math.log10(x)

@mcp.tool()
def exp(x: float) -> float:
    """e raised to the power of x."""
    return math.exp(x)

@mcp.tool()
def factorial(n: int) -> int:
    """Factorial of non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    return math.factorial(n)

@mcp.tool()
def degrees(x: float) -> float:
    """Converts radians to degrees."""
    return math.degrees(x)

@mcp.tool()
def radians(x: float) -> float:
    """Converts degrees to radians."""
    return math.radians(x)

@mcp.tool()
def pi() -> float:
    """Returns the value of pi."""
    return math.pi

@mcp.tool()
def euler() -> float:
    """Returns Euler's number (e)."""
    return math.e

@mcp.tool()
def abs_val(x: float) -> float:
    """Absolute value of x."""
    return abs(x)

@mcp.tool()
def ceil(x: float) -> int:
    """Ceiling of x."""
    return math.ceil(x)

@mcp.tool()
def floor(x: float) -> int:
    """Floor of x."""
    return math.floor(x)

@mcp.tool()
def mod(a: float, b: float) -> float:
    """Remainder of a divided by b."""
    return a % b

if __name__ == "__main__":
    mcp.run(transport="stdio")
