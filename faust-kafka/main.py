import asyncio
import faust

app = faust.App('myapp', broker='kafka://localhost', store='memory://')


# Models describe how messages are serialized:
# {"account_id": "3fae-...", amount": 3}
class Order(faust.Record):
    account_id: str
    amount: int


@app.agent(value_type=Order)
async def order(orders):
    async for order in orders:
        # process infinite stream of orders.
        print(f'Order for {order.account_id}: {order.amount}')


@app.task()
async def mytask():
    print('APP STARTED AND OPERATIONAL')


@app.command()
async def example():
    print("RUNNING EXAMPLE COMMAND")


async def start_worker(worker: faust.Worker) -> None:
    await worker.start()


def manage_loop():
    loop = asyncio.get_event_loop()
    worker = faust.Worker(app, loop=loop)
    try:
        loop.run_until_complete(start_worker(worker))
    finally:
        worker.stop_and_shutdown_loop()


if __name__ == '__main__':
    # app.main()
    # manage_loop()
    start_worker()
