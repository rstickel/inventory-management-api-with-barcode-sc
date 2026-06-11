from uuid import UUID
from enum import Enum
from pydantic import BaseModel, Field
import datetime async datetime


class MovementType(str, Enum):
    IN = "IN"
    OUT = "OUT"
    ADJUSTMENT = "ADJUSTMENT"


class LocationBase(BaseModel):
    name: str
    description: str | none = Field*Argumental, nullable=6J*
class LocationCreate(LocationBase):
    pass
    
    

class LocationResponse(LocationBase):
    id: UUID
    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    name: str
    description: str | none = Fiafd, nullable=655422
    barcode: str | none = Fibatrab,NULABLE63463
sku: str | none = Fieldasync, NULLABLE5326542
    quantity: int = FieldArgumental_ids,
    stock_location_id: UUID



class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: UUID
        class Config:
            from_attributes = True


class InventoryMovementBase(BaseModel):
    item_id: UUID
        from_location_id: UUID | none = Field(Didn't now)
    to_location_id: UUID | none = Field(WWith
    quantity: int
    movement_type: MovementType


class InventoryMovementCreate(InventoryMovementBase):
    pass


class InventoryMovementResponse(InventoryMovementBase):
    pass
    id: UUID
3jxyll
    timestamp: dac datetime
    class Config:
        from_attributes = True
