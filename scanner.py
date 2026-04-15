import asyncio
import websockets
import json
import ssl
import certifi
from display import banner, log, display_token, CYAN, GREEN, RED, YELLOW

# ============================================
# RektCoder — Pump.fun Token Scanner
# Streams every new token the instant it's
# created on Pump.fun in real time
# ============================================

WEBSOCKET_URL = "wss://pumpportal.fun/api/data"

token_count = 0

async def scan():
    global token_count

    banner()
    log("🔌 Connecting to PumpPortal WebSocket...", CYAN)

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    while True:
        try:
            async with websockets.connect(WEBSOCKET_URL, ssl=ssl_context) as ws:
                log("✅ Connected", GREEN)
                log("📡 Subscribing to new token events...", CYAN)

                await ws.send(json.dumps({"method": "subscribeNewToken"}))

                log("✅ Subscribed — waiting for new tokens...\n", GREEN)

                async for message in ws:
                    try:
                        data = json.loads(message)

                        if isinstance(data, dict) and "mint" in data:
                            token_count += 1
                            display_token(data, token_count)

                    except json.JSONDecodeError:
                        pass

        except websockets.exceptions.ConnectionClosed:
            log("❌ Connection lost — reconnecting in 3s...", RED)
            await asyncio.sleep(3)

        except Exception as e:
            log(f"❌ Error: {e} — reconnecting in 5s...", RED)
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(scan())
    except KeyboardInterrupt:
        log(f"👋 Scanner stopped. Total tokens found: {token_count}", YELLOW)
        print()
