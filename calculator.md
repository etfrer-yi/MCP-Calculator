# Calculator MCP

A scientific calculator MCP server and CLI client built with FastMCP.

## Setup

```bash
cd calculator-mcp
python3 -m venv .venv
.venv/bin/pip install "mcp[cli]"
```

## Usage

```bash
.venv/bin/python client.py <operation> [args]
```

## Operations

### Binary
| Operation | Args | Example |
|-----------|------|---------|
| `add` | `a b` | `client.py add 10 5` → `15.0` |
| `subtract` | `a b` | `client.py subtract 10 5` → `5.0` |
| `multiply` | `a b` | `client.py multiply 10 5` → `50.0` |
| `divide` | `a b` | `client.py divide 10 5` → `2.0` |
| `power` | `base exp` | `client.py power 2 10` → `1024.0` |
| `mod` | `a b` | `client.py mod 10 3` → `1.0` |
| `log` | `x [base]` | `client.py log 100 10` → `2.0` |

### Unary
| Operation | Arg | Example |
|-----------|-----|---------|
| `sqrt` | `n` | `client.py sqrt 144` → `12.0` |
| `exp` | `x` | `client.py exp 1` → `2.71828...` |
| `log10` | `x` | `client.py log10 1000` → `3.0` |
| `factorial` | `n` | `client.py factorial 7` → `5040` |
| `sin` | `x` (radians) | `client.py sin 1.5708` → `≈1.0` |
| `cos` | `x` (radians) | `client.py cos 0` → `1.0` |
| `tan` | `x` (radians) | `client.py tan 0.7854` → `≈1.0` |
| `asin` | `x` | `client.py asin 1` → `1.5708` |
| `acos` | `x` | `client.py acos 1` → `0.0` |
| `atan` | `x` | `client.py atan 1` → `0.7854` |
| `degrees` | `x` | `client.py degrees 3.14159` → `≈180.0` |
| `radians` | `x` | `client.py radians 180` → `≈3.14159` |
| `abs_val` | `x` | `client.py abs_val -5` → `5.0` |
| `ceil` | `x` | `client.py ceil 4.2` → `5` |
| `floor` | `x` | `client.py floor 4.9` → `4` |

### Constants
| Operation | Result |
|-----------|--------|
| `pi` | `3.141592653589793` |
| `euler` | `2.718281828459045` |

## Help

```bash
.venv/bin/python client.py --help
```
