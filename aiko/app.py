import asyncio
from aiko import App

loop = asyncio.get_event_loop()

app = App(loop)

def echo(ctx, next_call):
    return "echo"

app.use(echo)

if __name__ == "__main__":
    app.run()