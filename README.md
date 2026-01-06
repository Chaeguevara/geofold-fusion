# geofold-fusion

A collection of paperfolding algorithms and scripts for creating geometric shapes in Fusion 360 for 3D printing.

## Overview

**geofold-fusion** implements various paperfolding-related algorithms with the goal of generating 3D-printable models via Fusion 360. This project combines computational geometry, origami mathematics, and additive manufacturing to create physical paperfolding models.

## Project Status

🚀 **In Active Development**

Currently implemented:
- ✅ Hexagon (육각형) generation script for Fusion 360

## Features

- **Geometric Shape Generation**: Automated creation of fundamental shapes (hexagons, polygons)
- **Fusion 360 Integration**: Python scripts compatible with Fusion 360 API
- **Parameterized Design**: Customizable dimensions and configurations
- **3D Print Ready**: Shapes designed for export to STL and 3D printing
- **Paperfolding Algorithms**: Foundation for implementing complex origami patterns

## Quick Start

### Prerequisites

- [Fusion 360](https://www.autodesk.com/products/fusion-360/) installed
- Basic understanding of Python (for script customization)
- Git for version control

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chaeguevara/geofold-fusion.git
   cd geofold-fusion
   ```

2. Navigate to the Fusion 360 scripts directory:
   ```bash
   cd scripts/fusion360
   ```

3. Follow the instructions in [scripts/fusion360/README.md](scripts/fusion360/README.md) to run scripts in Fusion 360

### Running Your First Script

1. Open Fusion 360
2. Go to **Tools** → **Add-Ins** → **Scripts and Add-Ins**
3. Click the **+** button and navigate to `scripts/fusion360/create_hexagon.py`
4. Click **Run**
5. A 3D hexagon with rounded edges will be created in your active design!

## Project Structure

```
geofold-fusion/
├── scripts/              # Fusion 360 and automation scripts
│   └── fusion360/       # Fusion 360 Python scripts
│       ├── create_hexagon.py   # Hexagon generation script
│       └── README.md           # Fusion 360 scripts documentation
├── CLAUDE.md            # AI assistant development guide
├── README.md            # This file
└── .gitignore          # Git ignore patterns
```

## Available Scripts

### Fusion 360 Scripts

Located in `scripts/fusion360/`:

1. **create_hexagon.py** - Creates 3D regular hexagons (육각형) with optional edge rounding
   - **Adjustable radius**: Control hexagon size (circumradius)
   - **Edge rounding**: Optional fillets on vertical corners
   - **Adjustable thickness**: Control extrusion height
   - Configurable position (X, Y, Z)
   - Predefined size presets (small, medium, large, with rounded or sharp variants)
   - See [detailed documentation](scripts/fusion360/README.md)

## Roadmap

Planned features and algorithms:

### Phase 1: Basic Shapes ✅ (In Progress)
- [x] Regular hexagon generation with adjustable radius
- [x] 3D extrusion with configurable thickness
- [x] Edge rounding (fillet) support
- [ ] Regular polygon generation (n-gons)
- [ ] Star polygons
- [ ] Tessellation patterns

### Phase 2: Fold Lines and Patterns
- [ ] Valley and mountain fold line generation
- [ ] Crease pattern implementation
- [ ] Fold angle calculations
- [ ] Miura fold pattern
- [ ] Yoshimura pattern

### Phase 3: 3D Transformations
- [x] 2D to 3D extrusion (completed for hexagons)
- [x] Thickness modeling for paper (basic implementation)
- [ ] Fold simulation with dynamic angles
- [ ] Assembly constraints

### Phase 4: Advanced Paperfolding
- [ ] Origami tessellations
- [ ] Curved creases
- [ ] Rigid origami mechanisms
- [ ] Deployable structures

### Phase 5: Export and Manufacturing
- [ ] STL export optimization
- [ ] Parametric model generation
- [ ] Assembly instructions
- [ ] Cut and fold templates

## Mathematical Foundation

This project is based on several mathematical concepts:

- **Computational Geometry**: Polygon generation, tessellations
- **Origami Mathematics**: Huzita-Hatori axioms, flat-foldability
- **Linear Algebra**: Rotation matrices, transformations
- **Graph Theory**: Crease pattern analysis

## Development

### For Developers

See [CLAUDE.md](CLAUDE.md) for comprehensive development guidelines, including:
- Code style and conventions
- Git workflow
- Testing strategy
- Architecture patterns

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes following the guidelines in CLAUDE.md
4. Test thoroughly in Fusion 360
5. Commit using conventional commit messages: `git commit -m "feat: add new feature"`
6. Push to your fork and create a pull request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/Chaeguevara/geofold-fusion.git
cd geofold-fusion

# Create a feature branch
git checkout -b feature/my-new-feature

# Make changes and test in Fusion 360

# Commit changes
git add .
git commit -m "feat: add new paperfolding algorithm"

# Push to remote
git push -u origin feature/my-new-feature
```

## Usage Examples

### Creating a Standard Hexagon

```python
# In Fusion 360, run create_hexagon.py
# Default creates a 10cm radius hexagon with 0.5cm thickness and rounded edges
```

### Creating a Custom Hexagon

Edit the script's `run()` function:

```python
hexagon_component = create_hexagon(
    design=design,
    radius=15.0,           # 15cm radius
    thickness=1.0,         # 1cm thick
    fillet_radius=0.8,     # 0.8cm edge rounding
    center_x=5.0,
    center_y=5.0,
    component_name="Custom_Hexagon"
)
```

### Using Presets

```python
# Create a large hexagon with rounded edges (20cm radius)
hexagon = create_hexagon_from_preset(design, preset_name='large')

# Create a medium hexagon with sharp corners (10cm radius)
hexagon_sharp = create_hexagon_from_preset(design, preset_name='medium_sharp')
```

### Controlling Edge Rounding

```python
# Sharp corners (no rounding)
sharp = create_hexagon(design, radius=10.0, fillet_radius=0.0)

# Smooth rounded corners
rounded = create_hexagon(design, radius=10.0, fillet_radius=1.0)
```

## Resources

### Paperfolding and Origami
- [Origami Mathematics](https://origami.kosmulski.org/)
- [Erik Demaine's Origami Page](http://erikdemaine.org/curved/)
- [Robert Lang's Origami](https://langorigami.com/)

### Fusion 360
- [Fusion 360 API Documentation](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-A92A4B10-3781-4925-94C6-47DA85A4F65A)
- [Fusion 360 Python API Reference](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-7B5A90C8-E94C-48DA-B16B-430729B734DC)

### Computational Geometry
- [CGAL - Computational Geometry Algorithms Library](https://www.cgal.org/)
- [GeoPandas](https://geopandas.org/) (for Python)

## License

MIT License

Copyright (c) 2026 geofold-fusion

See LICENSE file for full details.

## Acknowledgments

- Inspired by the origami mathematics community
- Built with Fusion 360 API
- Thanks to all contributors and paperfolding enthusiasts

## Contact

- **GitHub**: [Chaeguevara/geofold-fusion](https://github.com/Chaeguevara/geofold-fusion)
- **Issues**: [GitHub Issues](https://github.com/Chaeguevara/geofold-fusion/issues)

## Version History

### v0.1.0 (2026-01-06)
- Initial project setup
- Added hexagon generation script for Fusion 360
- Created project documentation and guidelines

---

**Note**: This project is in active development. Features and API may change as the project evolves.
