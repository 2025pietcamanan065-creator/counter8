# 8-Bit Synchronous Up Counter (`counter8`) IC Fabrication

Complete RTL-to-GDSII ASIC design and physical implementation of an 8-bit synchronous up counter fabricated using the open-source **SkyWater SKY130** 130 nm CMOS standard cell library.

Developed for the course **Digital System & Logic Design (253AI3-03)**, Department of Computer Science & Engineering (Artificial Intelligence), Poornima Institute of Engineering & Technology, Jaipur.

---

## Project Overview

Digital counters track event counts, divide clock frequencies, and generate memory addresses in processor architectures. In ripple architectures, clock skew accumulates across cascading flip-flops and limits maximum operational frequency. A synchronous counter eliminates clock skew accumulation by driving the clock inputs of all eight flip-flops from a shared clock tree, updating every bit in a single clock cycle.

This repository contains the complete design and signoff collateral for `counter8`, including Verilog-2001 RTL modeling, self-checking testbench verification, Yosys logic synthesis, OpenLane 2 automated physical design, and final DRC/LVS signoff.

---

## Design Specifications & Metrics

| Parameter | Specification / Result | Unit |
| :--- | :--- | :--- |
| **Process Node** | SkyWater SKY130 (130 nm CMOS) | — |
| **Standard Cell Library** | `sky130_fd_sc_hd` (High Density) | — |
| **Operating Voltage** | 1.80 (Nominal core) | V |
| **Target Clock Frequency** | 10.0 | MHz |
| **Clock Period** | 100.0 | ns |
| **Setup Slack (Worst Case)** | +78.29 (Met) | ns |
| **Hold Slack (Worst Case)** | +0.38 (Met) | ns |
| **Core Dimensions** | 100.0 × 100.0 | µm |
| **Core Area** | 0.010 (10,000 µm²) | mm² |
| **Standard Cell Count** | 48 cells | — |
| **Cell Area Utilization** | 12.03% | — |
| **Total Power Consumption** | 12.69 | µW |
| **Internal Power** | 8.87 | µW |
| **Switching Power** | 3.82 | µW |
| **Leakage Power** | 0.0039 | µW |
| **DRC Violations (Magic & KLayout)** | 0 (Clean) | — |
| **LVS Comparison (Netgen)** | Netlists match completely (Clean) | — |
| **Antenna Violations** | 0 (Clean) | — |

---

## Student Project Group

- **Roshan Yadav** (Reg. No: 2024PIETCSAI001) — RTL architecture design, Verilog-2001 modeling, synchronous reset & enable logic.
- **Manan Gupta** (Reg. No: 2024PIETCSAI002) — Testbench architecture, automated reference model, GTKWave waveform analysis.
- **Siddi Kanwar** (Reg. No: 2024PIETCSAI003) — Yosys logic synthesis, cell mapping optimization, gate-level netlist timing.
- **Ritika saini** (Reg. No: 2024PIETCSAI004) — OpenLane physical design execution, floorplanning, PDN grid, placement, CTS, routing.
- **Ginni** (Reg. No: 2024PIETCSAI005) — Signoff verification, Magic/KLayout DRC analysis, Netgen LVS, multi-corner STA.

**Under the Guidance of:**
- **Dr. Aditya Kumar Singh Pundir**, Associate Professor, Department of CSE (AI), PIET Jaipur
- **Dr. Budesh Kanwar**, Professor & Head of Department, Department of CSE (AI), PIET Jaipur

---

## Repository Structure

```
counter8/
├── config.json                     # OpenLane 2 physical design configuration
├── docs/                           # Project documentation & full academic reports
│   ├── layout.png                  # High-resolution KLayout die render
│   ├── Project_Report_DSLD_Counter8_IC_Fabrication.docx # MS Word report
│   ├── Project_Report_DSLD_Counter8_IC_Fabrication.pdf  # 33-page ready-to-print report
│   └── Project_Report_DSLD_Counter8_IC_Fabrication.md   # Complete markdown source report
├── report_assets/                  # Visual figures, schematics, and charts
│   ├── fig1_block_diagram.png      # Top-level functional block diagram
│   ├── fig2_logic_schematic.png    # Gate-level schematic with D-FFs and carry chain
│   ├── fig3_gtkwave_sim.png        # GTKWave simulation timing waveforms
│   ├── fig4_testbench_console.png  # Verilog testbench self-checking console output
│   ├── fig5_asic_flow.png          # Complete RTL-to-GDSII ASIC design flow
│   ├── fig6_layout_render.png      # Full chip layout rendering
│   ├── fig7_area_breakdown.png     # Cell area distribution pie chart
│   └── fig8_timing_slack.png       # Multi-corner setup/hold timing slack bar chart
├── rtl/                            # Verilog-2001 hardware description
│   └── counter.v                   # 8-bit synchronous up counter RTL module
├── sim/                            # Functional verification & simulation
│   ├── counter_tb.v                # Self-checking automated testbench
│   ├── counter_tb.vcd              # Value Change Dump waveform file
│   ├── counter.vvp                 # Compiled Icarus Verilog simulation binary
│   └── gen_waveform.py             # Python script generating VCD visualization
├── synthesis/                      # Logic synthesis scripts & gate netlists
│   ├── counter_synth.v             # Synthesized gate netlist mapped to sky130_fd_sc_hd
│   ├── synth.ys                    # Yosys synthesis execution script
│   └── synth.log                   # Full synthesis log with cell counts
├── submission/                     # Final tapeout deliverables & signoff collateral
│   ├── def/                        # Design Exchange Format placement and routing
│   ├── gds/                        # Calma GDSII stream format for tapeout
│   ├── klayout_gds/                # KLayout-generated stream file
│   ├── lef/                        # Library Exchange Format macro abstract
│   ├── lib/                        # Liberty timing libraries across 9 PVT corners
│   ├── mag/                        # Magic VLSI layout database
│   ├── mag_gds/                    # Magic-streamed GDSII layout
│   ├── metrics.csv                 # Detailed physical design metrics table
│   ├── metrics.json                # Structured OpenLane signoff metrics
│   ├── nl/                         # Structural gate-level netlists
│   ├── odb/                        # OpenDB physical database file
│   ├── pnl/                        # Powered netlist with VDD/VSS pins
│   ├── render/                     # OpenROAD physical view renders
│   ├── sdc/                        # Synopsys Design Constraints timing file
│   ├── sdf/                        # Standard Delay Format annotated timing files
│   ├── spef/                       # Standard Parasitic Exchange Format RC files
│   ├── spice/                      # Extracted transistor-level SPICE netlists
│   └── vh/                         # Verilog header pin wrappers
└── runs/                           # Complete step-by-step OpenLane 2 execution runs
```

---

## Getting Started

### 1. Functional Simulation (Icarus Verilog & GTKWave)

Compile and run the Verilog-2001 simulation:

```bash
# Compile RTL and testbench
iverilog -o sim/counter.vvp rtl/counter.v sim/counter_tb.v

# Execute simulation and generate VCD
vvp sim/counter.vvp

# Open waveform in GTKWave
gtkwave sim/counter_tb.vcd
```

### 2. Logic Synthesis (Yosys)

Run gate-level logic synthesis mapping to SkyWater SKY130 high-density standard cells:

```bash
cd synthesis
yosys synth.ys
```

### 3. Physical Layout Inspection (KLayout)

View the final fabricated GDSII layout with standard cell placement and metal routing:

```bash
klayout -e -nn submission/klayout_gds/counter.klayout.gds \
        -l $PDK_ROOT/sky130A/libs.tech/klayout/tech/sky130A.lyp
```

---

## License

This project is released under the Apache-2.0 License. The SkyWater SKY130 PDK is licensed under the Apache License 2.0.
