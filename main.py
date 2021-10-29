import threading
import uvicorn

from endpoint.rest import app as rest_app
from endpoint.rpc import app as rpc_app

app = rest_app.create_app()


def app_run():
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8081,
        debug=False,
        reload=True,
    )

if __name__ == "__main__":
    print("Receiver has been started")
    thr = threading.Thread(target=app_run())
    thr.start()
    thr.join()

    thr2 = threading.Thread(target=rpc_app.serve())
    thr2.start()
