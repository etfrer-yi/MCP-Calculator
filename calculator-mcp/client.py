import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command=".venv/bin/python", args=["server.py"])

USAGE = """
Scientific Calculator CLI
Usage: python client.py <operation> [args...]

Binary operations:
  add <a> <b>          a + b
  subtract <a> <b>     a - b
  multiply <a> <b>     a * b
  divide <a> <b>       a / b
  power <base> <exp>   base ^ exp
  log <x> [base]       log(x) [default: natural log]
  mod <a> <b>          a % b

Unary operations:
  sqrt <n>             √n
  sin <x>              sin(x radians)
  cos <x>              cos(x radians)
  tan <x>              tan(x radians)
  asin <x>             arcsin(x)
  acos <x>             arccos(x)
  atan <x>             arctan(x)
  log10 <x>            log₁₀(x)
  exp <x>              e^x
  factorial <n>        n!
  degrees <x>          radians → degrees
  radians <x>          degrees → radians
  abs_val <x>          |x|
  ceil <x>             ⌈x⌉
  floor <x>            ⌊x⌋

Constants (no args):
  pi                   π
  euler                e
"""

BINARY_OPS = {"add", "subtract", "multiply", "divide", "power", "mod"}
UNARY_OPS  = {"sqrt", "sin", "cos", "tan", "asin", "acos", "atan",
              "log10", "exp", "factorial", "degrees", "radians", "abs_val", "ceil", "floor"}
CONSTANTS  = {"pi", "euler"}

async def run(op: str, args: list[str]):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            if op in CONSTANTS:
                tool_args = {}
            elif op == "log":
                if not args:
                    print("log requires at least one argument: x [base]")
                    sys.exit(1)
                tool_args = {"x": float(args[0])}
                if len(args) > 1:
                    tool_args["base"] = float(args[1])
            elif op in BINARY_OPS:
                if len(args) < 2:
                    print(f"{op} requires two arguments")
                    sys.exit(1)
                keys = {"mod": ("a", "b"), "power": ("base", "exp")}.get(op, ("a", "b"))
                tool_args = {keys[0]: float(args[0]), keys[1]: float(args[1])}
            elif op in UNARY_OPS:
                if not args:
                    print(f"{op} requires one argument")
                    sys.exit(1)
                key = "n" if op in ("sqrt", "factorial") else "x"
                val = int(args[0]) if op == "factorial" else float(args[0])
                tool_args = {key: val}
            else:
                print(f"Unknown operation: {op}")
                print(USAGE)
                sys.exit(1)

            result = await session.call_tool(op, tool_args)
            print(result.content[0].text)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(USAGE)
        sys.exit(0)

    op   = sys.argv[1]
    args = sys.argv[2:]
    asyncio.run(run(op, args))

if __name__ == "__main__":
    main()
