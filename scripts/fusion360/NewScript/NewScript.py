"""
Hexagon Creation Script for Fusion 360

This script creates a regular hexagon shape in Fusion 360.
"""

import traceback
import math
import adsk.core
import adsk.fusion


def _calculate_hexagon_vertices(
    radius: float,
    center_x: float = 0.0,
    center_y: float = 0.0,
    center_z: float = 0.0
) -> list:
    """
    Calculate the vertices of a regular hexagon.

    Args:
        radius: Radius from center to vertex (circumradius)
        center_x: X coordinate of center
        center_y: Y coordinate of center
        center_z: Z coordinate of center

    Returns:
        List of Point3D objects representing the hexagon vertices
    """
    vertices = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        vertices.append(adsk.core.Point3D.create(x, y, center_z))
    return vertices


def _create_hexagon_sketch(
    component: adsk.fusion.Component,
    vertices: list,
    center_x: float,
    center_y: float,
    center_z: float,
    sketch_name: str
) -> adsk.fusion.Sketch:
    """
    Create a hexagon sketch from vertices.

    Args:
        component: The component to add the sketch to
        vertices: List of Point3D objects for hexagon vertices
        center_x: X coordinate of center
        center_y: Y coordinate of center
        center_z: Z coordinate of center
        sketch_name: Name for the sketch

    Returns:
        The created sketch object
    """
    xy_plane = component.xYConstructionPlane
    sketch = component.sketches.add(xy_plane)
    sketch.name = sketch_name

    lines = sketch.sketchCurves.sketchLines
    for i in range(6):
        start_point = vertices[i]
        end_point = vertices[(i + 1) % 6]
        lines.addByTwoPoints(start_point, end_point)

    sketch.sketchPoints.add(adsk.core.Point3D.create(center_x, center_y, center_z))
    return sketch


def _extrude_sketch_profile(
    component: adsk.fusion.Component,
    sketch: adsk.fusion.Sketch,
    thickness: float
) -> adsk.fusion.ExtrudeFeature:
    """
    Extrude the sketch profile to create a 3D body.

    Args:
        component: The component containing the sketch
        sketch: The sketch to extrude
        thickness: Extrusion thickness in cm

    Returns:
        The created extrude feature
    """
    profile = None
    for prof in sketch.profiles:
        profile = prof
        break

    if not profile:
        raise Exception("Failed to find hexagon profile for extrusion")

    extrudes = component.features.extrudeFeatures
    extrude_input = extrudes.createInput(
        profile,
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    )

    distance = adsk.core.ValueInput.createByReal(thickness)
    extrude_input.setDistanceExtent(False, distance)

    return extrudes.add(extrude_input)


def _apply_edge_fillets(
    component: adsk.fusion.Component,
    body: adsk.fusion.BRepBody,
    fillet_radius: float
) -> None:
    """
    Apply fillets to the vertical edges of a body.

    Args:
        component: The component containing the body
        body: The body to apply fillets to
        fillet_radius: Radius of the fillet in cm
    """
    if fillet_radius <= 0:
        return

    edges_to_fillet = adsk.core.ObjectCollection.create()

    for edge in body.edges:
        geom = edge.geometry
        if hasattr(geom, 'direction'):
            direction = geom.direction
            if abs(direction.x) < 0.01 and abs(direction.y) < 0.01:
                edges_to_fillet.add(edge)

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
    """
    root_comp = design.rootComponent
    occurrence = root_comp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    component = occurrence.component
    component.name = component_name

    vertices = _calculate_hexagon_vertices(radius, center_x, center_y, center_z)

    sketch = _create_hexagon_sketch(
        component,
        vertices,
        center_x,
        center_y,
        center_z,
        f"{component_name}_Sketch"
    )

    extrude_feature = _extrude_sketch_profile(component, sketch, thickness)

    if fillet_radius > 0:
        body = extrude_feature.bodies.item(0)
        _apply_edge_fillets(component, body, fillet_radius)

    return component


def run(_context: str):
    """This function is called by Fusion when the script is run."""
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox('No active Fusion 360 design found. Please open or create a design.')
            return

        hexagon_component = create_hexagon(
            design=design,
            radius=10.0,
            center_x=0.0,
            center_y=0.0,
            center_z=0.0,
            thickness=0.5,
            fillet_radius=0.5,
            component_name="Hexagon"
        )

        app.activeViewport.fit()

        ui.messageBox(
            f'Hexagon created successfully!\n\n'
            f'Component: {hexagon_component.name}\n'
            f'Radius: 10.0 cm\n'
            f'Thickness: 0.5 cm\n'
            f'Edge rounding: 0.5 cm'
        )

    except:  # pylint:disable=bare-except
        if ui:
            ui.messageBox(f'Failed:\n{traceback.format_exc()}')
