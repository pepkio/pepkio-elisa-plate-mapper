# pepkio-elisa-plate-mapper

Programmatically construct, validate, and quality-check 96-well and 384-well microplate layouts for ELISA assays and bioanalytical workflows via the Pepkio API.

# What It Does

`pepkio-elisa-plate-mapper` provides a Python interface to programmatically design and validate microplate layouts for enzyme-linked immunosorbent assays (ELISA), spectrophotometric protein quantification, and serial dilution series. It checks well classifications, verifies essential blank controls, evaluates perimeter edge-effect vulnerabilities, and computes intra-assay coefficient of variation (%CV) across replicate groups.

# Features

- **Typed Pydantic Models**: Programmatically define plate layouts using `ElisaPlateMapperInput` and `WellInput` models.
- **Assay Quality Control Checks**: Automatically detect missing blank controls and verify standard curve point counts.
- **Perimeter Edge-Effect Assessment**: Compute perimeter standard fraction to identify standards positioned in outer wells subject to evaporation bias.
- **Replicate Intra-Assay Precision**: Track %CV across replicate groups to evaluate pipetting consistency.
- **CLI & REST API Client**: Access manifest examples, fetch past runs, and validate plate configurations synchronously or asynchronously.

# Installation

```bash
pip install pepkio-elisa-plate-mapper
```

# Quick Example

```python
from pepkio_elisa_plate_mapper import ElisaPlateMapperInput, PepkioClient, WellInput

# Define wells for a microplate layout
wells = [
    WellInput(well="A1", type="standard", label="Std 100 ng/mL", concentration=100.0, od=1.85, group_id="std_1", replicate=1),
    WellInput(well="A2", type="standard", label="Std 100 ng/mL", concentration=100.0, od=1.82, group_id="std_1", replicate=2),
    WellInput(well="H12", type="blank", label="Blank", od=0.04),
    WellInput(well="B1", type="unknown", label="Serum Sample A", od=0.92, group_id="samp_A", replicate=1),
]

input_data = ElisaPlateMapperInput(wells=wells)

# Execute layout validation via the Pepkio API client
with PepkioClient(api_key="YOUR_API_KEY") as client:
    result = client.run(input_data)
    print("Run Status:", result.status)
    print("QC Results:", result.result)
```

# Typical Use Cases

- **Sandwich & Indirect ELISA**: Organize standard curves, antibody dilutions, and unknown serum/plasma samples in duplicate or triplicate.
- **Colorimetric Protein Assays**: Map BSA standard series and cell lysate replicates for BCA, Bradford, or Lowry spectrophotometric assays.
- **Serial Dilutions & Standard Curves**: Plan 8-point or 12-point serial dilution series while avoiding outer row/column thermal gradients.
- **qPCR & RT-qPCR Plate Layouts**: Arrange standard template dilutions and No Template Control (NTC) wells across 96-well or 384-well plates.
- **Cell Viability Screens**: Organize drug candidate serial dilutions and vehicle controls for MTT or Luminescent cell-based assays.

# Scientific Background

Microplate assays rely on consistent spatial arrangement and accurate control wells for reliable quantification. Thermal gradients, differential evaporation along perimeter wells (rows A/H and columns 1/12), and inconsistent pipetting in technical replicates are major sources of intra-assay variance. Structured microplate mapping ensures systematic control placement, early detection of missing blanks, and quantitative monitoring of perimeter exposure and intra-assay precision (%CV) prior to downstream curve fitting.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/elisa-plate-mapper

Web-only features include an interactive drag-and-drop 96-well grid visualization, automatic layout generation, printable bench worksheet protocols, and shareable setup links.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-elisa-plate-mapper

Web Application: https://www.pepkio.com/tools/elisa-plate-mapper

Source code and issue tracking are maintained on [GitHub](https://github.com/pepkio/pepkio-elisa-plate-mapper).

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and provides bioinformatics analysis services (https://www.pepkio.com/cro) for life science research. Explore additional online laboratory calculators and microplate utility tools at https://www.pepkio.com.

# Keywords

* ELISA
* microplate
* plate mapper
* 96-well plate
* 384-well plate
* standard curve
* serial dilution
* well assignment
* intra-assay CV
* edge effect
* optical density
* absorbance
* bioanalysis
* qPCR layout
* BCA assay
* Bradford assay
* antibody dilution
* microplate reader
* quality control
* pipetting layout
* assay validation
* technical replicates
* blank controls
* laboratory calculator
* Python client
* ELISA plate layout generator
* 96 well microplate layout mapper
* standard curve serial dilution planner
* microplate edge effect detector
* intra assay coefficient of variation calculator
* microplate reader sample well validator
* sandwich ELISA layout design tool
* qPCR plate setup generator
* protein assay standard curve mapper
* 384 well plate layout validation
* technical replicate variance calculator
* laboratory information management system plate mapper
* automated microplate quality control Python client
* ELISA plate design web tool
