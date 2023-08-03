from pydantic import BaseModel


class InputParam(BaseModel):
    """
    This class is created in order to create regular form of input set.
    """

    UUID: str  # required param.
