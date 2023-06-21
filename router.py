from fastapi import APIRouter, HTTPException
import json
import storage
import schema

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Menu API"}

@router.get("/menu")
async def get_menu():
    return storage.menu

@router.post("/menu/add")
async def add_item(item: schema.Item):
    storage.menu[len(storage.menu)] = item.dict()
    return storage.menu

@router.put("/menu/update/{item_id}")
async def update_item(item_id: int, item: schema.Item):
    if item_id not in storage.menu:
        raise HTTPException(status_code=404, detail="Item not found")
    
    storage.menu[item_id] = item.dict()
    return storage.menu

@router.delete("/menu/delete/{item_id}")
async def delete_item(item_id: int):
    if item_id not in storage.menu:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del storage.menu[item_id]
    return storage.menu

@router.get("/order")
async def get_orders():
    return storage.orders

@router.get("/order/{order_id}")
async def get_order_by_id(order_id: int):
    if order_id not in storage.orders:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return storage.orders[order_id]

@router.post("/order/add")
async def add_order(order: schema.Order):
    for item_id in order.items:
        if item_id not in storage.menu:
            raise HTTPException(status_code=404, detail="Item not found")
    
    storage.orders[len(storage.orders)] = [storage.menu[item_id] for item_id in order.items]
    
    return storage.orders

@router.put("/order/update/{order_id}")
async def update_order(order_id: int, order: schema.Order):
    if order_id not in storage.orders:
        raise HTTPException(status_code=404, detail="Order not found")
    
    storage.orders[order_id] = [storage.menu[item_id] for item_id in order.items]
    return storage.orders

@router.delete("/order/delete/{order_id}")
async def delete_order(order_id: int):
    if order_id not in storage.orders:
        raise HTTPException(status_code=404, detail="Order not found")
    
    del storage.orders[order_id]
    return storage.orders