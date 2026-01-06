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
    radius: float = 10.0,
    center_x: float = 0.0,
    center_y: float = 0.0,
    center_z: float = 0.0,
    thickness: float = 0.5,
    fillet_radius: float = 0.0,
    component_name: str = "Hexagon"
) -> adsk.fusion.Component:
    """
    Creates a regular hexagon with optional edge rounding in Fusion 360.

    Args:
        design: The active Fusion 360 design
        radius: Radius from center to vertex (circumradius) in cm (default: 10.0)
        center_x: X coordinate of the hexagon center (default: 0.0)
        center_y: Y coordinate of the hexagon center (default: 0.0)
        center_z: Z coordinate of the hexagon center (default: 0.0)
        thickness: Extrusion thickness in cm (default: 0.5)
        fillet_radius: Radius for edge rounding in cm, 0 for no rounding (default: 0.0)
        component_name: Name of the component to create (default: "Hexagon")

    Returns:
        The created component containing the hexagon body

    Raises:
        Exception: If hexagon creation fails

    Note:
        - For a regular hexagon, side_length = radius (when radius is the circumradius)
        - Set fillet_radius > 0 to round the vertical edges at corners
        - Thickness determines the height of the extruded 3D shape
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
        # The circumradius (center to vertex) is used as the radius parameter
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
        sketch_lines = []

        # Connect all vertices to form the hexagon
        for i in range(6):
            start_point = vertices[i]
            end_point = vertices[(i + 1) % 6]  # Wrap around to first vertex
            line = lines.addByTwoPoints(start_point, end_point)
            sketch_lines.append(line)

        # Add a center point for reference
        sketch.sketchPoints.add(adsk.core.Point3D.create(center_x, center_y, center_z))

        # Find the profile for extrusion
        # The sketch should have one closed profile (the hexagon)
        profile = None
        for prof in sketch.profiles:
            profile = prof
            break

        if not profile:
            raise Exception("Failed to find hexagon profile for extrusion")

        # Create extrusion to make it a 3D body
        extrudes = component.features.extrudeFeatures
        extrude_input = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Set the extrusion distance
        distance = adsk.core.ValueInput.createByReal(thickness)
        extrude_input.setDistanceExtent(False, distance)

        # Create the extrusion
        extrude_feature = extrudes.add(extrude_input)

        # Apply fillets to the vertical edges if fillet_radius > 0
        if fillet_radius > 0:
            # Get the body created by extrusion
            body = extrude_feature.bodies.item(0)

            # Collect the vertical edges (the edges at the corners)
            edges_to_fillet = adsk.core.ObjectCollection.create()

            for edge in body.edges:
                # Vertical edges are perpendicular to the XY plane
                # Check if the edge is vertical (parallel to Z axis)
                geom = edge.geometry
                if hasattr(geom, 'direction'):
                    direction = geom.direction
                    # Check if edge is vertical (direction parallel to Z axis)
                    # An edge is vertical if its direction is close to (0, 0, ±1)
                    if abs(direction.x) < 0.01 and abs(direction.y) < 0.01:
                        edges_to_fillet.add(edge)

            # Apply fillet if we found edges
            if edges_to_fillet.count > 0:
                fillets = component.features.filletFeatures
                fillet_input = fillets.createInput()
                fillet_input.addConstantRadiusEdgeSet(
                    edges_to_fillet,
                    adsk.core.ValueInput.createByReal(fillet_radius),
                    True
                )
                fillet_input.isG2 = False
                fillet_input.isRollingBallCorner = True
                fillets.add(fillet_input)

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
            radius=10.0,         # 10 cm radius (center to vertex)
            center_x=0.0,
            center_y=0.0,
            center_z=0.0,
            thickness=0.5,       # 0.5 cm thickness
            fillet_radius=0.5,   # 0.5 cm edge rounding
            component_name="Hexagon_Base"
        )

        # Fit the view to show the created hexagon
        app.activeViewport.fit()

        ui.messageBox(
            f'Hexagon created successfully!\n\n'
            f'Component: {hexagon_component.name}\n'
            f'Radius: 10.0 cm\n'
            f'Thickness: 0.5 cm\n'
            f'Edge rounding: 0.5 cm\n\n'
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
        radius: float = 10.0,
        center_x: float = 0.0,
        center_y: float = 0.0,
        center_z: float = 0.0,
        thickness: float = 0.5,
        fillet_radius: float = 0.0,
        component_name: str = "Hexagon"
    ):
        """
        Initialize hexagon configuration.

        Args:
            radius: Radius from center to vertex in cm
            center_x: X coordinate of center
            center_y: Y coordinate of center
            center_z: Z coordinate of center
            thickness: Extrusion thickness in cm
            fillet_radius: Edge rounding radius in cm (0 for no rounding)
            component_name: Name for the component
        """
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.thickness = thickness
        self.fillet_radius = fillet_radius
        self.component_name = component_name

    def to_dict(self):
        """Convert configuration to dictionary."""
        return {
            'radius': self.radius,
            'center_x': self.center_x,
            'center_y': self.center_y,
            'center_z': self.center_z,
            'thickness': self.thickness,
            'fillet_radius': self.fillet_radius,
            'component_name': self.component_name
        }

    @classmethod
    def from_dict(cls, config_dict):
        """Create configuration from dictionary."""
        return cls(**config_dict)


# Predefined hexagon configurations for common paperfolding patterns
PRESET_CONFIGS = {
    'small': HexagonConfig(
        radius=5.0,
        thickness=0.3,
        fillet_radius=0.3,
        component_name="Hexagon_Small"
    ),
    'medium': HexagonConfig(
        radius=10.0,
        thickness=0.5,
        fillet_radius=0.5,
        component_name="Hexagon_Medium"
    ),
    'large': HexagonConfig(
        radius=20.0,
        thickness=1.0,
        fillet_radius=1.0,
        component_name="Hexagon_Large"
    ),
    'small_sharp': HexagonConfig(
        radius=5.0,
        thickness=0.3,
        fillet_radius=0.0,
        component_name="Hexagon_Small_Sharp"
    ),
    'medium_sharp': HexagonConfig(
        radius=10.0,
        thickness=0.5,
        fillet_radius=0.0,
        component_name="Hexagon_Medium_Sharp"
    ),
    'large_sharp': HexagonConfig(
        radius=20.0,
        thickness=1.0,
        fillet_radius=0.0,
        component_name="Hexagon_Large_Sharp"
    ),
}


def create_hexagon_from_preset(
    design: adsk.fusion.Design,
    preset_name: str = 'medium'
) -> adsk.fusion.Component:
    """
    Create a hexagon using a predefined configuration.

    Args:
        design: The active Fusion 360 design
        preset_name: Name of the preset. Available options:
            - 'small': 5cm radius with rounded edges
            - 'medium': 10cm radius with rounded edges (default)
            - 'large': 20cm radius with rounded edges
            - 'small_sharp': 5cm radius with sharp corners
            - 'medium_sharp': 10cm radius with sharp corners
            - 'large_sharp': 20cm radius with sharp corners

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
