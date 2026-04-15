# Pump.fun Token Scanner — Real-Time New Token Detection

Stream every new Pump.fun token the instant it's created on Solana. No API key, no paid services, completely free.

Built by [RektCoder](https://www.youtube.com/@RektCoder) — full video walkthrough 👉 [Watch on YouTube](https://youtu.be/s-JHcwBIUNE)

## What It Does

Connects to PumpPortal's free WebSocket and streams every new token creation event on Pump.fun in real time. For each token you get:

- Token name and symbol
- Mint address (contract address)
- Creator wallet address
- Bonding curve address
- Market cap in SOL
- Initial buy amount (how much the creator bought at launch)
- SOL locked in bonding curve
- Metadata URI (IPFS link)
- Pump.fun link
- Solscan transaction link

## Python Version

### Setup

```bash
cd python
pip install websockets certifi
python scanner.py
```

### Files

- `scanner.py` — Main file. Connects to WebSocket, subscribes to new token events, streams tokens.
- `display.py` — Terminal formatting, colors, ASCII banner. Purely cosmetic.

### Mac Users

If you get an SSL certificate error, the code already handles it with `certifi`. Just make sure you ran `pip install certifi`.

## TypeScript Version

### Setup

```bash
cd typescript
npm install
npm start
```

### Files

- `src/scanner.ts` — Main file. Same logic as Python version.
- `src/display.ts` — Terminal formatting and colors.

## How It Works

1. Connect to PumpPortal WebSocket (`wss://pumpportal.fun/api/data`)
2. Send `{"method": "subscribeNewToken"}`
3. Receive real-time token creation events
4. Display token data in terminal
5. Auto-reconnect on disconnect

No API key. No rate limits. No cost.

## Series

This is **Part 1** of a sniper bot series:

- **Part 1** — Token Scanner (this video) ✅
- **Part 2** — Scam Filters (coming soon)
- **Part 3** — Auto-Buy with Jupiter (coming soon)

## Links

- 📺 [YouTube — RektCoder](https://www.youtube.com/@RektCoder)
- 📢 [Telegram Channel](https://t.me/rektcoderchannel)
- 💬 [Telegram Community](https://t.me/rektcodercommunity)
- 💻 [GitHub](https://github.com/hoziertom44-arch)

## Disclaimer

This code is for educational purposes only. Trading memecoins involves significant risk. Never trade with money you can't afford to lose. This is not financial advice.

رَبِّ زِدْنِي عِلْمًا 🤲
