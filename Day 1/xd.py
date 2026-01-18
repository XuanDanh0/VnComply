import asyncio
import time
#TODO Viết hàm async đầu tiên
async def in_chao(name: str,time:int):
    """
    In ra lời chào sau khi đợi {delay} giây
    
    Arguments:
    name : str : Tên người nhận lời chào
    delay : int : Thời gian chờ trước khi in lời chào
    
    
    Example:
        await say_hello("Tuan Anh", 3)
        
    """
    #Your code here
    # Hint: Sử dụng await asyncio.sleep(delay) 
    
    await asyncio.sleep(time)

    print(f"xin chao {name}")
    print(f"da cho {time} giay")

#Test Function
async def test_say_hello():
    print("Bắt đầu test...")
    await in_chao("Tuan Anh", 3)
    await in_chao("Nguyen Van A", 1)
    print("Kết thúc test.")
    
#Chạy hàm test
asyncio.run(test_say_hello())