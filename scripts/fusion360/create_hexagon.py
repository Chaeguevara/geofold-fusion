"""
Hexagon Generation Script for Fusion 360

This script creates a regular hexagon in Fusion 360, which serves as the foundation
for paperfolding algorithms and 3D printing workflows.

Author: geofold-fusion project
License: MIT
"""

import adsk.core
import adsk.fusion
import traceback
import math


def create_hexagon(
    design: adsk.fusion.Design,
    side_length: float = 10.0,
    center_x: float = 0.0,
    center_y: float = 0.0,
    center_z: float = 0.0,
    component_name: str = "Hexagon"
) -> adsk.fusion.Component:
    """
    Creates a regular hexagon sketch in Fusion 360.

    Args:
        design: The active Fusion 360 design
        side_length: Length of each side of the hexagon in cm (default: 10.0)
        center_x: X coordinate of the hexagon center (default: 0.0)
        center_y: Y coordinate of the hexagon center (default: 0.0)
        center_z: Z coordinate of the hexagon center (default: 0.0)
        component_name: Name of the component to create (default: "Hexagon")

    Returns:
        The created component containing the hexagon sketch

    Raises:
        Exception: If hexagon creation fails
    """
    try:
        # Get the root component
        root_comp = design.rootComponent

        # Create a new component for the hexagon
        occurrence = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        component = occurrence.component
        component.name = component_name

        # Get the XY plane
        xy_plane = component.xYConstructionPlane

        # Create a new sketch on the XY plane
        sketches = component.sketches
        sketch = sketches.add(xy_plane)
        sketch.name = f"{component_name}_Sketch"

        # Calculate hexagon vertices
        # A regular hexagon has 6 vertices equally spaced around a circle
        # The radius of the circumscribed circle equals the side length
        radius = side_length
        vertices = []

        for i in range(6):
            # Calculate angle for this vertex (starting from 0 degrees, going counterclockwise)
            angle = math.radians(60 * i)

            # Calculate vertex coordinates
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)

            vertices.append(adsk.core.Point3D.create(x, y, center_z))

        # Draw the hexagon using lines
        lines = sketch.sketchCurves.sketchLines

        # Connect all vertices to form the hexagon
        for i in range(6):
            start_point = vertices[i]
            end_point = vertices[(i + 1) % 6]  # Wrap around to first vertex
            lines.addByTwoPoints(start_point, end_point)

        # Add a center point for reference
        sketch.sketchPoints.add(adsk.core.Point3D.create(center_x, center_y, center_z))

        return component

    except Exception as e:
        raise Exception(f"Failed to create hexagon: {str(e)}")


def run(context):
    """
    Main entry point for the Fusion 360 script.

    Args:
        context: The context object provided by Fusion 360
    """
    ui = None
    try:
        # Get the application and user interface
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Get the active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox('No active Fusion 360 design found. Please open or create a design.')
            return

        # Create the hexagon with default parameters
        # You can modify these parameters as needed
        hexagon_component = create_hexagon(
            design=design,
            side_length=10.0,  # 10 cm side length
            center_x=0.0,
            center_y=0.0,
            center_z=0.0,
            component_name="Hexagon_Base"
        )

        # Fit the view to show the created hexagon
        app.activeViewport.fit()

        ui.messageBox(
            f'Hexagon created successfully!\n\n'
            f'Component: {hexagon_component.name}\n'
            f'Side length: 10.0 cm\n'
            f'This hexagon can now be used for paperfolding operations.'
        )

    except Exception as e:
        if ui:
            ui.messageBox(f'Failed:\n{traceback.format_exc()}')


# Configuration for parameterized hexagon creation
class HexagonConfig:
    """
    Configuration class for creating hexagons with different parameters.

    This can be used to create hexagons with custom sizes and positions
    for various paperfolding patterns.
    """

    def __init__(
        self,
        side_length: float = 10.0,
        center_x: float = 0.0,
        center_y: float = 0.0,
        center_z: float = 0.0,
        component_name: str = "Hexagon"
    ):
        """
        Initialize hexagon configuration.

        Args:
            side_length: Length of each side in cm
            center_x: X coordinate of center
            center_y: Y coordinate of center
            center_z: Z coordinate of center
            component_name: Name for the component
        """
        self.side_length = side_length
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.component_name = component_name

    def to_dict(self):
        """Convert configuration to dictionary."""
        return {
            'side_length': self.side_length,
            'center_x': self.center_x,
            'center_y': self.center_y,
            'center_z': self.center_z,
            'component_name': self.component_name
        }

    @classmethod
    def from_dict(cls, config_dict):
        """Create configuration from dictionary."""
        return cls(**config_dict)


# Predefined hexagon configurations for common paperfolding patterns
PRESET_CONFIGS = {
    'small': HexagonConfig(side_length=5.0, component_name="Hexagon_Small"),
    'medium': HexagonConfig(side_length=10.0, component_name="Hexagon_Medium"),
    'large': HexagonConfig(side_length=20.0, component_name="Hexagon_Large"),
}


def create_hexagon_from_preset(
    design: adsk.fusion.Design,
    preset_name: str = 'medium'
) -> adsk.fusion.Component:
    """
    Create a hexagon using a predefined configuration.

    Args:
        design: The active Fusion 360 design
        preset_name: Name of the preset ('small', 'medium', or 'large')

    Returns:
        The created component

    Raises:
        ValueError: If preset_name is not valid
    """
    if preset_name not in PRESET_CONFIGS:
        raise ValueError(
            f"Invalid preset name: {preset_name}. "
            f"Valid options: {', '.join(PRESET_CONFIGS.keys())}"
        )

    config = PRESET_CONFIGS[preset_name]
    return create_hexagon(design, **config.to_dict())
