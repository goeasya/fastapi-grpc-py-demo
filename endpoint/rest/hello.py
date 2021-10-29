from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def say_hello():
    """
    :return: say hello
    """
    return {"code": 0, "msg": "success", "success": True, "data": "hello."}
