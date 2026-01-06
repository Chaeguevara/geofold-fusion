# Fusion 360 Scripts for geofold-fusion

This directory contains Fusion 360 Python scripts for creating geometric shapes and implementing paperfolding algorithms.

## Overview

These scripts are designed to automate the creation of geometric shapes in Fusion 360, which can then be used for paperfolding simulations and 3D printing.

## Scripts

### create_hexagon.py

Creates a regular hexagon (육각형) with optional edge rounding in Fusion 360.

**Features:**
- Creates a 3D extruded hexagon with customizable radius
- **Adjustable radius**: Control the size from center to vertex (circumradius)
- **Edge rounding**: Optional fillets on vertical corners for smooth edges
- **Adjustable thickness**: Control the height of the extruded shape
- Supports custom positioning (X, Y, Z coordinates)
- Includes predefined presets (small, medium, large, with rounded or sharp variants)
- Fully parameterized for easy modification
- Includes configuration class for advanced usage

**Default Parameters:**
- Radius: 10.0 cm (center to vertex distance)
- Thickness: 0.5 cm (extrusion height)
- Edge rounding: 0.5 cm (fillet radius on vertical corners)
- Center position: (0, 0, 0)
- Component name: "Hexagon_Base"

## How to Use in Fusion 360

### Method 1: Run as Script

1. Open Fusion 360
2. Go to **Tools** → **Add-Ins** → **Scripts and Add-Ins**
3. Click the **+** button next to "My Scripts"
4. Navigate to this directory: `scripts/fusion360/`
5. Select `create_hexagon.py`
6. Click **Run**

### Method 2: Add to Scripts Library

1. Copy the script file to your Fusion 360 scripts folder:
   - **Windows**: `%appdata%\Autodesk\Autodesk Fusion 360\API\Scripts\`
   - **macOS**: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/`
   - **Linux**: Not officially supported, but can work with Wine
2. Restart Fusion 360 or refresh the Scripts panel
3. The script will appear in your Scripts list

## Customizing the Hexagon

You can modify the default parameters in the `run()` function:

```python
hexagon_component = create_hexagon(
    design=design,
    radius=15.0,           # 15 cm radius (center to vertex)
    center_x=5.0,          # Offset X position by 5 cm
    center_y=5.0,          # Offset Y position by 5 cm
    center_z=0.0,
    thickness=1.0,         # 1 cm thick extrusion
    fillet_radius=0.8,     # 0.8 cm edge rounding (use 0 for sharp corners)
    component_name="My_Custom_Hexagon"
)
```

**Understanding the radius parameter:**
- `radius`: Distance from the hexagon center to any vertex (circumradius)
- For a regular hexagon, the side length equals the radius
- Increase radius to make a larger hexagon, decrease for smaller

## Using Presets

The script includes six predefined configurations:

**With Rounded Edges:**
- **small**: 5 cm radius, 0.3 cm thickness, 0.3 cm edge rounding
- **medium**: 10 cm radius, 0.5 cm thickness, 0.5 cm edge rounding (default)
- **large**: 20 cm radius, 1.0 cm thickness, 1.0 cm edge rounding

**With Sharp Corners:**
- **small_sharp**: 5 cm radius, 0.3 cm thickness, no edge rounding
- **medium_sharp**: 10 cm radius, 0.5 cm thickness, no edge rounding
- **large_sharp**: 20 cm radius, 1.0 cm thickness, no edge rounding

To use a preset, modify the `run()` function to call `create_hexagon_from_preset()`:

```python
# Create a large hexagon with rounded edges
hexagon_component = create_hexagon_from_preset(
    design=design,
    preset_name='large'
)

# Or create a medium hexagon with sharp corners
hexagon_component = create_hexagon_from_preset(
    design=design,
    preset_name='medium_sharp'
)
```

## Advanced Usage

### Creating Multiple Hexagons

You can create multiple hexagons by calling the function multiple times with different parameters:

```python
# Create a small rounded hexagon at origin
small_hex = create_hexagon(
    design,
    radius=5.0,
    thickness=0.3,
    fillet_radius=0.3,
    component_name="Hexagon_1"
)

# Create a medium sharp hexagon offset to the right
medium_hex = create_hexagon(
    design,
    radius=10.0,
    center_x=15.0,
    thickness=0.5,
    fillet_radius=0.0,  # Sharp corners
    component_name="Hexagon_2"
)

# Create a large thick hexagon offset upward
large_hex = create_hexagon(
    design,
    radius=15.0,
    center_y=20.0,
    thickness=2.0,      # Extra thick for strength
    fillet_radius=1.5,  # Heavy rounding
    component_name="Hexagon_3"
)
```

### Using HexagonConfig Class

For more complex configurations, use the `HexagonConfig` class:

```python
from create_hexagon import HexagonConfig, create_hexagon

# Create custom configuration
my_config = HexagonConfig(
    radius=12.5,
    center_x=10.0,
    center_y=10.0,
    center_z=0.0,
    thickness=0.8,
    fillet_radius=0.6,
    component_name="Custom_Hexagon"
)

# Create hexagon with custom config
hexagon = create_hexagon(design, **my_config.to_dict())
```

### Edge Rounding Examples

```python
# No rounding (sharp corners) - good for precise paperfolding
sharp_hex = create_hexagon(design, radius=10.0, fillet_radius=0.0)

# Light rounding - subtle smoothing
light_hex = create_hexagon(design, radius=10.0, fillet_radius=0.3)

# Medium rounding - balanced appearance
medium_hex = create_hexagon(design, radius=10.0, fillet_radius=0.5)

# Heavy rounding - very smooth corners
heavy_hex = create_hexagon(design, radius=10.0, fillet_radius=1.0)
```

## Mathematical Details

### Regular Hexagon Properties

A regular hexagon has the following properties:
- 6 equal sides
- 6 equal angles (each 120°)
- The circumradius (center to vertex) equals the side length
- Vertices are equally spaced at 60° intervals around the center

### Understanding Radius vs Size

The **radius parameter** controls the overall size of the hexagon:
- **Circumradius**: Distance from center to any vertex
- For a regular hexagon: `side_length = radius`
- **Diameter**: The distance across the hexagon through the center = `2 × radius`
- **Width** (flat-to-flat): Distance between parallel sides = `radius × √3`

**Example sizes:**
- radius = 5 cm → side length = 5 cm, diameter = 10 cm
- radius = 10 cm → side length = 10 cm, diameter = 20 cm
- radius = 20 cm → side length = 20 cm, diameter = 40 cm

### Coordinate Calculation

Each vertex is calculated using polar coordinates:
```
x = center_x + radius × cos(θ)
y = center_y + radius × sin(θ)
```

Where θ = 0°, 60°, 120°, 180°, 240°, 300° for the six vertices.

### Edge Rounding (Fillet) Details

- **Fillet radius**: Determines the smoothness of vertical corners
- Applied to vertical edges (the edges connecting top and bottom faces)
- `fillet_radius = 0`: Sharp corners (no rounding)
- Larger values create smoother, more rounded corners
- Maximum recommended: `fillet_radius ≤ thickness` to avoid geometric conflicts

## Next Steps for Paperfolding

This 3D hexagon serves as the foundation for various paperfolding operations:

1. **Valley and Mountain Folds**: Add fold lines from center to vertices on the top face
2. **Tessellation**: Create repeating hexagon patterns in arrays
3. **Fold Simulation**: Implement fold angles and transformations
4. **Thickness Variations**: Adjust thickness to simulate different paper weights
5. **Export for 3D Printing**: Generate STL files for physical models (File → Export → STL)
6. **Pattern Creation**: Combine multiple hexagons with different parameters

## Troubleshooting

### Script doesn't appear in Fusion 360
- Make sure the file is in the correct Scripts directory
- Check that the file has a `.py` extension
- Try restarting Fusion 360

### Error: "No active Fusion 360 design found"
- Create a new design or open an existing one before running the script
- Make sure you're in the Design workspace (not Drawing or CAM)

### Hexagon appears too small or too large
- Adjust the `radius` parameter to change the size
- Note: Measurements are in centimeters by default
- Use the predefined presets for standard sizes (small, medium, large)
- Remember: radius = distance from center to vertex = side length

### Script runs but nothing appears
- Try running `app.activeViewport.fit()` to zoom to the created geometry
- Check the component browser on the left side of Fusion 360
- The hexagon might be created at a different location than expected
- Very thin hexagons (small thickness) might be hard to see

### Fillet/rounding doesn't appear
- Ensure `fillet_radius` is greater than 0
- Try increasing the fillet radius (e.g., 0.5 or higher)
- Make sure thickness is sufficient (fillet_radius should be ≤ thickness)
- Check that the 3D body was created successfully

### Error during fillet operation
- Reduce the fillet_radius value
- Ensure fillet_radius is not larger than the thickness
- Try using sharp corners (fillet_radius=0) if issues persist

## Contributing

When adding new scripts to this directory:

1. Follow the existing code structure and documentation style
2. Include comprehensive docstrings for all functions
3. Add error handling and user-friendly messages
4. Update this README with usage instructions
5. Test thoroughly in Fusion 360 before committing

## License

MIT License - See project root for details

## References

- [Fusion 360 API Documentation](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A)
- [Fusion 360 Python API Reference](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-7B5A90C8-E94C-48DA-B16B-430729B734DC)
- Regular Hexagon Mathematics: [Wolfram MathWorld](https://mathworld.wolfram.com/RegularHexagon.html)
