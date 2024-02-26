import json
import os

from pydantic import ValidationError
from schemas.input_schema import InputModel
from schemas.output_schema import OutputModel


def load_input_data(input_data_path):
    """Load and return the input data from JSON file."""
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, "..", input_data_path)
    with open(schema_path, "r") as file:
        input_data = json.load(file)
    return input_data


def validate_data(data, data_type):
    """
    Validate the provided data using Pydantic models.

    Args:
        data: The data to validate.
        data_type: The type of data to validate, either 'input' or 'output'.

    Raises:
        ValueError: If the data_type is invalid.
        ValidationError: If the data fails validation.
    """
    try:
        if data_type == "input":
            InputModel(**data)
        elif data_type == "output":
            OutputModel(**data)
        else:
            raise ValueError("Invalid data_type. Must be 'input' or 'output'.")
    except ValidationError as e:
        print(f"Pydantic validation error: {e}")
        raise


def find_enum(value, my_enum):
    """
    Find and return the enum member with the specified value.

    Args:
        value: The value to search for.
        MyEnum: The enum class to search in.

    Returns:
        The enum member with the specified value.

    Raises:
        ValueError: If no enum member with the specified value is found.
    """
    for member in my_enum.__members__.values():
        if member.value == value:
            return member
    raise ValueError(f"No enum member with value '{value}'")
