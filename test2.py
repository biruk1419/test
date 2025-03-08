import asyncio
import websockets

# A set to store all active connections
clients = set()

# When a new WebSocket connection is established
async def handler(websocket, path):
    clients.add(websocket)
    try:
        # Listen for messages from the client
        async for message in websocket:
            # Broadcast the message to all clients except the sender
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.ConnectionClosed:
        print("A client has disconnected")
    finally:
        # Remove the client from the set when disconnected
        clients.remove(websocket)

# Start the WebSocket server on port 8080
start_server = websockets.serve(handler, "localhost", 8080)

# Start the server and run it indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is running on ws://localhost:8080")
asyncio.get_event_loop().run_forever()
