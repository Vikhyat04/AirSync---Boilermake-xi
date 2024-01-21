import asyncio
import websockets
import multiprocessing as mp
import pickle

client = None

async def send_message(message, extensionClient):
    lock = mp.Lock()
    with lock:
        #clientInstance = pickle.loads(extensionClient)
        pass
    await clientInstance.send_message(message)

async def new_client_connected(client_socket, path):
    print("New client connected!")
    setClient(client_socket)

async def start_server():
    print("Starting server...")
    await websockets.serve(new_client_connected, "localhost", 12345)

def setClient(client_socket):
    global client
    lock = mp.Lock()
    with lock:
        print(pickle.dumps(client_socket))
        #client[:] = pickle.dumps(client_socket)

def run_server(extensionClient):
    global client
    client = extensionClient
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()