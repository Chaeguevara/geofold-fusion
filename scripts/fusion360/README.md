# Fusion 360 Scripts for geofold-fusion

This directory contains Fusion 360 Python scripts for creating geometric shapes and implementing paperfolding algorithms.

## Overview

These scripts are designed to automate the creation of geometric shapes in Fusion 360, which can then be used for paperfolding simulations and 3D printing.

## Scripts

### create_hexagon.py

Creates a regular hexagon (육각형) in Fusion 360.

**Features:**
- Creates a regular hexagon with customizable side length
- Supports custom positioning (X, Y, Z coordinates)
- Includes predefined presets (small, medium, large)
- Fully parameterized for easy modification
- Includes configuration class for advanced usage

**Default Parameters:**
- Side length: 10.0 cm
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
    side_length=15.0,      # Change side length to 15 cm
    center_x=5.0,          # Offset X position by 5 cm
    center_y=5.0,          # Offset Y position by 5 cm
    center_z=0.0,
    component_name="My_Custom_Hexagon"
)
```

## Using Presets

The script includes three predefined configurations:

- **small**: 5 cm side length
- **medium**: 10 cm side length (default)
- **large**: 20 cm side length

To use a preset, modify the `run()` function to call `create_hexagon_from_preset()`:

```python
hexagon_component = create_hexagon_from_preset(
    design=design,
    preset_name='large'
)
```

## Advanced Usage

### Creating Multiple Hexagons

You can create multiple hexagons by calling the function multiple times with different parameters:

```python
# Create a small hexagon at origin
small_hex = create_hexagon(design, side_length=5.0, component_name="Hexagon_1")

# Create a medium hexagon offset to the right
medium_hex = create_hexagon(design, side_length=10.0, center_x=15.0, component_name="Hexagon_2")

# Create a large hexagon offset upward
large_hex = create_hexagon(design, side_length=15.0, center_y=20.0, component_name="Hexagon_3")
```

### Using HexagonConfig Class

For more complex configurations, use the `HexagonConfig` class:

```python
from create_hexagon import HexagonConfig, create_hexagon

# Create custom configuration
my_config = HexagonConfig(
    side_length=12.5,
    center_x=10.0,
    center_y=10.0,
    center_z=0.0,
    component_name="Custom_Hexagon"
)

# Create hexagon with custom config
hexagon = create_hexagon(design, **my_config.to_dict())
```

## Mathematical Details

### Regular Hexagon Properties

A regular hexagon has the following properties:
- 6 equal sides
- 6 equal angles (each 120°)
- The radius of the circumscribed circle equals the side length
- Vertices are equally spaced at 60° intervals around the center

### Coordinate Calculation

Each vertex is calculated using polar coordinates:
```
x = center_x + radius × cos(θ)
y = center_y + radius × sin(θ)
```

Where θ = 0°, 60°, 120°, 180°, 240°, 300° for the six vertices.

## Next Steps for Paperfolding

This hexagon serves as the foundation for various paperfolding operations:

1. **Valley and Mountain Folds**: Add fold lines from center to vertices
2. **Tessellation**: Create repeating hexagon patterns
3. **3D Extrusion**: Convert the 2D hexagon into a 3D shape
4. **Fold Simulation**: Implement fold angles and transformations
5. **Export for 3D Printing**: Generate STL files for physical models

## Troubleshooting

### Script doesn't appear in Fusion 360
- Make sure the file is in the correct Scripts directory
- Check that the file has a `.py` extension
- Try restarting Fusion 360

### Error: "No active Fusion 360 design found"
- Create a new design or open an existing one before running the script
- Make sure you're in the Design workspace (not Drawing or CAM)

### Hexagon appears too small or too large
- Adjust the `side_length` parameter
- Note: Measurements are in centimeters by default
- Use the predefined presets for standard sizes

### Script runs but nothing appears
- Try running `app.activeViewport.fit()` to zoom to the created geometry
- Check the component browser on the left side of Fusion 360
- The hexagon might be created at a different location than expected

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
