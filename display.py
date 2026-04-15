from datetime import datetime

# Colors
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
DIM     = "\033[2m"
BRIGHT  = "\033[1m"
RESET   = "\033[0m"

def banner():
    print(f"\n{CYAN}{BRIGHT}")
    print(f"   ██████╗ ███████╗██╗  ██╗████████╗")
    print(f"   ██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝")
    print(f"   ██████╔╝█████╗  █████╔╝    ██║   ")
    print(f"   ██╔══██╗██╔══╝  ██╔═██╗    ██║   ")
    print(f"   ██║  ██║███████╗██║  ██╗   ██║   ")
    print(f"   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ")
    print(f"   {YELLOW}P U M P . F U N  T O K E N  S C A N N E R{RESET}")
    print(f"   {DIM}Real-time new token detection via PumpPortal{RESET}\n")

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

def divider():
    print(f"{DIM}{'─' * 70}{RESET}")

def log(message, color=DIM):
    print(f"{DIM}[{timestamp()}]{RESET} {color}{message}{RESET}")

def display_token(data, count):
    name = data.get("name", "Unknown")
    symbol = data.get("symbol", "???")
    mint = data.get("mint", "")
    bonding_curve = data.get("bondingCurveKey", "")
    creator = data.get("traderPublicKey", "")
    market_cap = data.get("marketCapSol", 0)
    initial_buy = data.get("initialBuy", 0)
    v_sol = data.get("vSolInBondingCurve", 0)
    signature = data.get("signature", "")
    uri = data.get("uri", "")

    divider()
    print(f"\n{GREEN}{BRIGHT}   🟢 NEW TOKEN #{count}{RESET}")
    print(f"   {BRIGHT}Name:{RESET}           {YELLOW}{name}{RESET}")
    print(f"   {BRIGHT}Symbol:{RESET}         {CYAN}${symbol}{RESET}")
    print(f"   {BRIGHT}Mint:{RESET}           {DIM}{mint}{RESET}")
    print(f"   {BRIGHT}Creator:{RESET}        {DIM}{creator}{RESET}")
    if bonding_curve:
        print(f"   {BRIGHT}Bonding Curve:{RESET}  {DIM}{bonding_curve}{RESET}")
    if market_cap:
        print(f"   {BRIGHT}Market Cap:{RESET}     {MAGENTA}{float(market_cap):.2f} SOL{RESET}")
    if initial_buy:
        print(f"   {BRIGHT}Initial Buy:{RESET}    {YELLOW}{float(initial_buy):,.0f} tokens{RESET}")
    if v_sol:
        print(f"   {BRIGHT}Bonding SOL:{RESET}    {GREEN}{float(v_sol):.4f} SOL{RESET}")
    if uri:
        print(f"   {BRIGHT}Metadata:{RESET}      {DIM}{uri}{RESET}")
    if signature:
        print(f"   {BRIGHT}Solscan:{RESET}       {DIM}https://solscan.io/tx/{signature}{RESET}")
    print(f"   {BRIGHT}Pump.fun:{RESET}       {DIM}https://pump.fun/coin/{mint}{RESET}")
    print(f"   {BRIGHT}Time:{RESET}           {BLUE}{timestamp()}{RESET}")
    print()
