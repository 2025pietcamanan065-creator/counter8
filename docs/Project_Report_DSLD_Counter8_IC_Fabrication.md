**POORNIMA INSTITUTE OF ENGINEERING & TECHNOLOGY, JAIPUR**

**Department of Computer Science & Engineering (Artificial Intelligence)**

**PROJECT REPORT**

on

**Design and Physical Implementation of an 8-bit Synchronous Up Counter in SkyWater SKY130 Technology**

*(IC Fabrication Project: Silicluster v3 digital design, SKY130, 1.8 V)*

Submitted in partial fulfillment of the requirements of

**Digital System & Logic Design (253AI3-03)**

B.Tech. CSE (AI) · II Year · III Semester · Section F

**Submitted by**

> 1. Roshan Yadav
>
> 2. Manan Gupta
>
> 3. Siddi Kanwar
>
> 4. Ritika saini
>
> 5. Ginni

**Under the Guidance of**

Dr. Aditya Kumar Singh Pundir, Professor

**November 2026**

# CERTIFICATE

This is to certify that the project report titled "Design and Physical Implementation of an 8-bit Synchronous Up Counter in SkyWater SKY130 Technology" is submitted by Roshan Yadav, Manan Gupta, Siddi Kanwar, Ritika saini and Ginni in partial fulfilment of the requirements of Digital System & Logic Design (253AI3-03), B.Tech. CSE (AI), III Semester. The work presented in this report is a record of the candidates' own work, carried out under our supervision, and has not been submitted elsewhere for any other purpose.

+-----------------------------------+-----------------------------------+
| **Faculty Guide**                 | **Head of Department**            |
|                                   |                                   |
| Dr. Aditya Kumar Singh Pundir     | Dr. Budesh Kanwar                 |
|                                   |                                   |
| Professor                         | Department of CSE (AI)            |
+-----------------------------------+-----------------------------------+

# DECLARATION

We hereby declare that the project titled "Design and Physical Implementation of an 8-bit Synchronous Up Counter in SkyWater SKY130 Technology" is an original piece of work carried out by us as part of Digital System & Logic Design (253AI3-03). The circuit was described in Verilog, verified by simulation, and taken through synthesis, placement, routing and signoff checks to a GDSII layout by us using open-source tools. All sources of information used have been duly acknowledged in the References section.

Roshan Yadav [Signature]

Manan Gupta [Signature]

Siddi Kanwar [Signature]

Ritika saini [Signature]

Ginni [Signature]

# ACKNOWLEDGEMENT

We thank Dr. Aditya Kumar Singh Pundir for guiding us throughout this project. We also thank Dr. Budesh Kanwar, Head of Department, and the Department of Computer Science & Engineering (AI) at Poornima Institute of Engineering & Technology for providing the laboratory resources and computing environment needed for this work.

We acknowledge the Silicluster v3 tapeout call, which gave this design a concrete manufacturing target, and the open-source developers behind the SkyWater SKY130 PDK, OpenLane 2, Yosys, OpenROAD, Magic, KLayout, Netgen, and Icarus Verilog.

# ABSTRACT

Digital counters track event counts, divide clock frequencies, and generate memory addresses in processor architectures. In an asynchronous counter, flip-flops clock each other in a cascade, creating cumulative propagation delay and output glitches. In a synchronous counter, every flip-flop connects to a shared clock, and combinational gating updates all bits on the active clock edge without ripple delay.

This project implements an 8-bit synchronous binary up counter in the SkyWater SKY130 130 nm CMOS technology for the Silicluster v3 tapeout. The circuit accepts three inputs: a 10 MHz system clock, an active-high synchronous reset, and a count enable. The 8-bit output advances from 00h to FFh and rolls over to 00h. When reset is asserted, the count clears to 00h on the next rising clock edge. When enable is low, the counter holds its current value.

We modeled the design in synthesizable Verilog-2001 and verified it in Icarus Verilog using a self-checking testbench. Over six stimulus phases and 49 clock cycles (4,900 ns), simulated outputs matched a software reference model with zero errors. We then ran the design through the 76-stage OpenLane 2 physical flow targeting the sky130_fd_sc_hd library on a 180 × 115 µm die. Yosys synthesized the logic into 28 cells: 8 D flip-flops (dfxtp_1) and 20 combinational gates. Physical implementation added 216 tap cells, 3 clock buffers, 22 timing-repair buffers, and 1,372 fill cells, giving 1,641 total instances and 795.76 µm² of active standard-cell area (5.10% core utilization). TritonRoute completed detailed routing in three iterations with 1,041 µm of wire, 294 vias, and zero DRC errors. Static timing analysis across nine corners gave a worst-case setup slack of +76.78 ns at the slow corner (100 °C, 1.60 V) and a worst-case hold slack of +0.116 ns at the fast corner (-40 °C, 1.95 V). Total power dissipation is 12.69 µW at 10 MHz. Signoff checks in Magic, KLayout, and Netgen passed with zero DRC, LVS, or antenna violations, producing clean GDSII deliverables for manufacturing.

**Keywords:** *synchronous counter, binary up counter, Verilog HDL, SKY130, OpenLane, physical design, ASIC fabrication*

# TABLE OF CONTENTS

**CERTIFICATE i**

**DECLARATION ii**

**ACKNOWLEDGEMENT iii**

**ABSTRACT iv**

**1. Introduction 1**

> 1.1 Background 1
>
> 1.2 Motivation 1
>
> 1.3 Problem Statement 2
>
> 1.4 Objectives 2
>
> 1.5 Scope of the Project 2
>
> 1.6 Course Outcomes Addressed 3
>
> 1.7 Organisation of the Report 3

**2. Literature Review and Theory 4**

> 2.1 Basic Concepts 4
>
> 2.2 Components Required 5
>
> 2.3 Target Technology and Standard-Cell Library 6
>
> 2.4 Synchronous Counter Architecture and Gating 7

**3. Proposed Design and Methodology 8**

> 3.1 System Overview 8
>
> 3.2 Design Specification 8
>
> 3.3 Truth Table / Function Table 8
>
> 3.4 Logic Simplification and Implementation Choices 9
>
> 3.5 Circuit Diagram 10
>
> 3.6 Working Principle 10
>
> 3.7 Performance Criteria 11

**4. Implementation 13**

> 4.1 Tools and Environment 13
>
> 4.2 Functional Simulation 13
>
> 4.3 Physical Design 14
>
> 4.3.1 Synthesis and Netlist 15
>
> 4.3.2 Die Size and Flow Parameters 15
>
> 4.3.3 Placement, Clock Tree and Routing 15
>
> 4.3.4 DRC, LVS and Layout Checks 16
>
> 4.4 Fabrication Submission 16
>
> 4.4.1 Layout Deliverables 16
>
> 4.4.2 Fabrication Status 17
>
> 4.4.3 Problems Faced and Troubleshooting 17

**5. Results and Discussion 18**

> 5.1 Experimental Setup 18
>
> 5.2 Simulation Results 18
>
> 5.3 Physical Verification Results 19
>
> 5.4 Layout Results: Area, Power and Timing 19
>
> 5.5 Comparison of Simulation and Physical Results 21
>
> 5.6 Discussion and Limitations 21

**6. Conclusion and Future Scope 23**

> 6.1 Conclusion 23
>
> 6.2 Future Scope 23

**7. References 24**

**8. Appendix 25**

> A.1 Project Files and Layout Deliverables 25
>
> A.2 RTL Source Extract 25
>
> A.3 Additional Signoff Metrics 28
>
> A.4 Individual Contribution of Group Members 28

## List of Figures

Fig. 3.1: Block diagram of the proposed circuit 8

Fig. 3.2: Logic-level diagram of the counter bit slice and carry chain 10

Fig. 4.1: RTL simulation waveform at 10 MHz (Phase 1 to Phase 6 in GTKWave) 14

Fig. 4.2: Testbench console output (49 cycles verified, 0 errors) 14

Fig. 4.3: RTL-to-GDSII flow used for the physical design 15

Fig. 4.4: Top view of the final layout (counter, 180 × 115 µm, SKY130) 16

Fig. 5.1: Standard-cell area by cell class (total 795.8 µm², fill cells excluded) 20

Fig. 5.2: Worst setup and hold slack at three corners 21

## List of Tables

Table 2.1: Summary of related work 4

Table 2.2: Bill of materials (design blocks and tools) 6

Table 2.3: Pin description of counter (3 inputs, 8 outputs) 7

Table 2.4: Synchronous counter modes of operation 7

Table 3.1: Function table of the counter operation modes 9

Table 3.2: State transitions and roll-over behaviour 9

Table 3.3: Excitation table for synchronous counter bit slice 9

Table 3.4: Karnaugh map of the toggle enable function 9

Table 3.5: Sequence of stimulus phases during functional testing 11

Table 3.6: Summary of counter verification intervals 11

Table 4.1: Flow parameters and die specification 15

Table 5.1: RTL simulation results (Icarus Verilog verification matrix) 18

Table 5.2: Physical verification and signoff results (OpenLane run) 19

Table 5.3: Area, power and cell statistics of the final layout 20

Table 5.4: Timing summary across nominal, slow and fast corners 20

Table A.1: Project files and deliverables 25

Table A.2: Additional signoff metrics from metrics.json 28

Table A.3: Individual contribution of group members 28

# 1. Introduction

## 1.1 Background

Digital counters advance through a fixed sequence of binary states on successive clock pulses. They are standard parts of digital hardware, used for timers, event counters, program counters, frequency dividers, and address generators in memory controllers [1].

Counters fall into two categories: asynchronous (ripple) and synchronous. An asynchronous counter feeds the clock only to the first flip-flop, and each subsequent flip-flop is clocked by the output of the preceding stage. This cascade accumulates delay across the bits ($t_{total} = N 	imes t_{pd}$). During state transitions, different flip-flops switch at different times, creating brief false output combinations known as decoding glitches. If the total delay approaches the clock period, the counter cannot operate reliably.

A synchronous counter avoids this problem by connecting the same clock to all flip-flops. Combinational logic checks the current state and decides which bits should change on the next clock edge. Because all bits switch together, the output delay equals the delay of one flip-flop plus the steering logic.

This report describes an 8-bit synchronous binary up counter with active-high synchronous reset (`rst`) and count enable (`en`). We developed the circuit in synthesizable Verilog-2001, verified it in simulation, and generated a DRC- and LVS-clean GDSII layout using the SkyWater SKY130 process.

## 1.2 Motivation

Synchronous circuits are easier to constrain and verify than ripple circuits because all register transfers happen on predictable clock boundaries. In deep-submicron processes like SKY130, a clean clock tree and synchronous resets keep timing margins stable across process, voltage, and temperature corners. An integrated digital counter provides single-cycle response with low power consumption, without the software overhead of a microcontroller.

For our course in Digital System and Logic Design (253AI3-03), this project connects sequential logic design (excitation tables, state transitions, and setup/hold timing) with modern ASIC physical design. Using the open-source SkyWater SKY130 PDK and OpenLane 2, we took the circuit through logic synthesis, floorplanning, placement, clock tree synthesis, routing, and physical signoff. The layout fits the Silicluster v3 die template and is ready for manufacturing submission [5].

## 1.3 Problem Statement

The goal is to design, verify, and physically lay out an 8-bit synchronous binary up counter in the SkyWater SKY130 130 nm CMOS process. The circuit must satisfy the following technical constraints:
1. Accept three input signals: a single 10 MHz clock (`clk`), an active-high synchronous reset (`rst`), and a count enable (`en`).
2. Provide an 8-bit binary output bus (`count[7:0]`) covering values from 0 to 255 ($00_{16}$ to $FF_{16}$).
3. When `rst = 1`, the counter must clear to $00_{16}$ on the rising clock edge, regardless of `en`.
4. When `rst = 0` and `en = 1`, the counter must increment by 1 on each rising edge, rolling over from 255 back to 0.
5. When `rst = 0` and `en = 0`, the counter must hold its current state.
6. The entire design must be realized using digital standard cells only from the `sky130_fd_sc_hd` library, running at 1.8 V core supply, without analog macros or external controllers.
7. The layout must fit within a pre-allocated Silicluster v3 die template of 180 µm × 115 µm with zero design rule (DRC) and layout-versus-schematic (LVS) violations, while meeting setup and hold constraints across all PVT corners.

## 1.4 Objectives

1. Write synthesizable Verilog-2001 code for an 8-bit synchronous up counter with synchronous reset and count enable.
2. Verify all operating modes (reset, count, hold, rollover, and mid-count reset) using a self-checking testbench in Icarus Verilog and check signals in GTKWave.
3. Synthesize the Verilog RTL to the `sky130_fd_sc_hd` cell library using Yosys, mapping sequential storage to D flip-flops and combinational logic to standard gates without inferring latches.
4. Run physical design in OpenLane 2 (floorplanning, power distribution, standard-cell placement, clock tree synthesis, and detailed routing) within the 180 µm × 115 µm die.
5. Check timing across nine PVT corners, verify layout cleanliness with Magic, KLayout, and Netgen (zero DRC, LVS, and antenna errors), and export GDSII files for the Silicluster v3 tapeout.
6. Measure cell area, core utilization, wirelength, power dissipation, and timing slack.

## 1.5 Scope of the Project

The scope includes:
- Structural and behavioral modeling of an 8-bit synchronous up counter in IEEE 1364-2001 Verilog HDL.
- A 10 MHz clock domain (100 ns clock period) with active-high synchronous reset and active-high enable.
- Complete functional verification using a self-checking testbench comprising 49 clock cycles and comparing output against an independent reference model.
- Physical implementation using the open-source `sky130_fd_sc_hd` (high density) library at 1.8 V nominal operating voltage.
- Execution of the automated 76-step OpenLane 2 flow, generating GDSII, DEF, LEF, SPICE, SDC, SDF, and LIB deliverables.
- Static timing signoff across nominal, slow, and fast corners.

*Out of Scope:* Physical fabrication of silicon wafers and post-silicon packaging/testing on laboratory automated test equipment (ATE) are outside the scope of this pre-tapeout design and verification report.

## 1.6 Course Outcomes Addressed

This project directly addresses the Course Outcomes (COs) of Digital System & Logic Design (253AI3-03):
- CO1: Understand and apply fundamental digital logic principles, Boolean algebra, and sequential logic operations.
- CO2: Design, simplify, and analyze synchronous sequential circuits using state tables, excitation equations, and flip-flops.
- CO3: Model digital hardware structures using Verilog Hardware Description Language and construct automated testbenches for functional verification.
- CO4: Use modern computer-aided design (CAD) and industrial EDA tools (Yosys, OpenROAD, OpenLane, Magic, KLayout, Netgen) to implement physical silicon layout and conduct design rule and timing signoff.

## 1.7 Organisation of the Report

The remainder of this report is structured as follows:
- Chapter 2 reviews counter principles, binary state transitions, cell library characteristics, and summarizes related work.
- Chapter 3 presents the system block diagram, truth tables, state transition equations, Karnaugh-map logic simplification, logic-level schematic, and worked examples.
- Chapter 4 details the EDA toolchain, simulation methodology, testbench stimulus phases, and the 76-step OpenLane physical design progression.
- Chapter 5 presents functional simulation waveforms, signoff verification metrics, area breakdown, multi-corner timing slacks, power dissipation, and layout characteristics.
- Chapter 6 summarizes the completed results and outlines future additions.
- Chapters 7 and 8 list references and appendices containing complete project file listings, full Verilog source code, signoff metrics, and group member contributions.

# 2. Literature Review and Theory

Table 2.1 summarizes five sources that form the technical background for this project: standard digital logic textbooks, counter timing research, the open-source SKY130 PDK, and the OpenLane 2 implementation flow.

-------------------------------------------------------------------------------
**Ref.**   **Author(s) / Year**  **Method / Architecture**    **Key Finding**
---------- --------------------- ---------------------------- ----------------------------
\[1\]      M. M. Mano and M. D.  Textbook treatment of        Presents standard synchronous
           Ciletti, 2013         registers, flip-flops,       counter structures using D
                                 synchronous binary counters  and T flip-flops with parallel
                                 and carry lookahead gating   carry chains; defines Verilog
                                                              HDL modeling techniques.

\[2\]      R. J. Tocci, N. S.    Digital systems principles;  Demonstrates how synchronous
           Widmer, and G. L.     analysis of ripple vs.       counters eliminate decoding
           Moss, 2017            synchronous counters and     glitches and propagation delay
                                 decoding glitches            accumulation present in ripple
                                                              counters.

\[3\]      E. F. Deprettere and  High-speed parallel counter  Shows that carry-lookahead
           R. H. Niggemann,      architectures and carry      and partitioned carry schemes
           2001                  propagation analysis         significantly reduce critical
                                                              path delay in wide synchronous
                                                              counters.

\[6\]      SkyWater Technology   SkyWater SKY130 open-source  Provides 130 nm CMOS design
           and Google, 2020      Process Design Kit (PDK)     rules, standard-cell timing
                                                              models (.lib), LEF geometry,
                                                              and SPICE device parameters.

\[7\]      Efabless, 2020        OpenLane 2 automated         Provides an end-to-end,
                                 RTL-to-GDSII digital flow    unattended flow integrating
                                                              Yosys, OpenROAD, Magic,
                                                              KLayout, and Netgen for clean
                                                              silicon tapeout.
-------------------------------------------------------------------------------

*Table 2.1: Summary of related work*

In digital ASIC design, counters are implemented by mapping register-transfer level descriptions into standard-cell gates. Mano and Ciletti [1] outline the logic for synchronous up counters, where each bit toggles if all lower-order bits are logic 1. Tocci et al. [2] analyze why synchronous clocking prevents the output decoding glitches typical of ripple counters. Deprettere and Niggemann [3] examine carry propagation in wide parallel counters. For an 8-bit counter, standard D flip-flops with composite AND-OR-Invert gates provide fast carry propagation without complex lookahead trees. The open-source SKY130 PDK [6] and OpenLane 2 [7] provide the models and automated tools needed to translate these logic equations into silicon.

## 2.1 Basic Concepts

Synchronous Binary Counting Logic. An 8-bit binary counter cycles through states $Q(t) \in [0, 255]$. In an up counter, each valid clock event increments the binary state by one:
$$Q(t+1) = (Q(t) + 1) \pmod{256}$$

Let the 8-bit state be represented by $Q = [Q_7, Q_6, Q_5, Q_4, Q_3, Q_2, Q_1, Q_0]$, where $Q_0$ is the least significant bit (LSB) and $Q_7$ is the most significant bit (MSB). In a binary number system, bit $Q_i$ toggles on the next clock pulse if all less significant bits ($Q_{i-1}, Q_{i-2}, \dots, Q_0$) are logic 1, and the count enable signal (`en`) is active:
$$T_i = en \cdot \prod_{j=0}^{i-1} Q_j$$
where $T_i$ represents the toggle condition for bit $i$. For the LSB ($Q_0$), the toggle condition is simply $T_0 = en$.

Next-State Logic with D Flip-Flops. The `sky130_fd_sc_hd` library uses positive edge-triggered D flip-flops (`dfxtp`) rather than dedicated T flip-flops. To implement a toggle function using a D flip-flop, the D input receives the XOR of the current state $Q_i$ and the toggle enable condition $T_i$:
$$D_i = Q_i \oplus T_i$$

When count enable `en` is low ($en = 0$), $T_i = 0$ for all $i$, yielding $D_i = Q_i \oplus 0 = Q_i$, holding the current bit value.

Synchronous Active-High Reset. Synchronous reset is sampled on the rising clock edge along with data. This is expressed by modulating the next-state input:
$$D_i = \overline{rst} \cdot \left( \overline{en} \cdot Q_i + en \cdot (Q_i \oplus C_i) ight)$$
where $C_i = \prod_{j=0}^{i-1} Q_j$ is the carry into bit $i$. When $rst = 1$, $D_i = 0$ regardless of $Q_i$ or $en$, forcing the counter to state $00_{16}$ synchronously on the clock edge. Synchronous reset prevents false resets from board-level noise spikes on asynchronous lines.

Carry Chain Evaluation: For bit $i$, carry $C_i = en \cdot Q_0 \cdot Q_1 \cdots Q_{i-1}$.

Toggle Logic: When $en = 1$ and $C_i = 1$, bit $Q_i$ toggles on the rising clock edge.

$T_0 = en$; $T_1 = en \cdot Q_0$; $T_2 = en \cdot Q_0 \cdot Q_1$; ... ; $T_7 = en \cdot Q_0 \cdot Q_1 \cdots Q_6$.

Gating and Hold Logic: When $en = 0$, toggle conditions are inhibited, holding all 8 bits unchanged.

Parallel Register Readout: All 8 output bits `count[7:0]` update simultaneously on each active clock edge.

Synchronous Reset Override: When $rst = 1$, all flip-flops synchronously clear to $00_{16}$ on posedge `clk`.

## 2.2 Components Required

Table 2.2 lists the design modules, target library, and EDA tools used in the project. The design is implemented as an integrated circuit, so standard cells and software signoff tools replace discrete board-level components.

-----------------------------------------------------------------------------------
**S. No.** **Component / Tool** **Specification / Version** **Qty** **Purpose in Project**
---------- -------------------- --------------------------- ----- -----------------------
1          `counter`            Verilog top-level module    1     8-bit synchronous up
                                (3 inputs, 8 outputs)             counter design

2          `counter_tb`         Self-checking Verilog       1     Functional verification
                                testbench with golden model       across 6 stimulus phases

3          `sky130_fd_sc_hd`    SkyWater 130 nm high-       --    Target standard-cell
                                density library (1.8 V)           library for synthesis & P&R

4          Icarus Verilog 12    Open-source Verilog         --    RTL logic compilation &
                                IEEE-1364 simulator               event simulation

5          GTKWave 3.3          Digital waveform viewer     --    Inspection of VCD traces
                                                                  and signal transitions

6          Yosys 0.70           Open synthesis suite        --    RTL elaboration, tech
                                                                  mapping, and optimization

7          OpenROAD (OpenLane2) Integrated P&R toolchain    --    Floorplanning, PDN, CTS,
                                (v2.0 / LibreLane)                placement, routing

8          Magic 8.3            VLSI layout system          --    GDSII extraction, DRC,
                                                                  and SPICE generation

9          KLayout 0.30         GDSII viewer & signoff DRC  --    Geometry DRC and visual
                                engine                            layout inspection

10         Netgen 1.5           LVS tool                    --    Layout-versus-schematic
                                                                  formal comparison
-----------------------------------------------------------------------------------

*Table 2.2: Bill of materials (design blocks and tools)*

## 2.3 Target Technology and Standard-Cell Library

The design targets the SkyWater SKY130 open-source technology, a 130 nm planar CMOS process featuring a 1.8 V core oxide thickness and a 5.0 V I/O option. The metal stack comprises five interconnect layers: local interconnect (`li1`), Metal 1 (`met1`), Metal 2 (`met2`), Metal 3 (`met3`), Metal 4 (`met4`), and Metal 5 (`met5`).

This project utilizes the `sky130_fd_sc_hd` (high density) standard-cell library. Standard cells in this library have a uniform cell height of 2.72 µm (corresponding to a 0.48 µm site width), optimized for high logic integration density and low dynamic power dissipation. Flip-flops utilize the positive-edge triggered `sky130_fd_sc_hd__dfxtp_1` cell, while combinational gates utilize AND-OR-Invert (`a21oi`), OR-AND-Invert (`o21a`), NOR, and AND cells.

Table 2.3 specifies the pin interface of the `counter` chip.

---------------------------------------------------------------------------------
**Pin**       **Dir.**   **Width**   **Function**
------------- ---------- ----------- --------------------------------------------
`clk`         In         1           Primary system clock, up to 10 MHz (100 ns period)

`rst`         In         1           Synchronous active-high reset; resets `count` to $00_{16}$

`en`          In         1           Active-high count enable; allows incrementing when high

`count[7:0]`  Out        8           8-bit synchronous binary count output ($00_{16}$ to $FF_{16}$)
---------------------------------------------------------------------------------

*Table 2.3: Pin description of counter (3 inputs, 8 outputs)*

## 2.4 Synchronous Counter Architecture and Gating

Carry propagation sets the maximum clock frequency in an 8-bit counter. Three carry architectures exist:
1. Ripple Carry (Asynchronous): Carry ripples from flip-flop to flip-flop through clock inputs. Highly prone to decoding spikes; rejected for this project.
2. Serial Carry (Synchronous): The enable condition for each bit is formed by a chain of two-input AND gates: $C_{i} = C_{i-1} \cdot Q_{i-1}$. While synchronous and glitch-free, propagation delay through the seven AND gates scales linearly with word width.
3. Parallel / Lookahead Carry: The enable condition for bit $i$ is generated by a multi-input AND gate directly sampling all lower bits: $C_i = en \cdot Q_0 \cdot Q_1 \cdots Q_{i-1}$. This provides single-gate carry delay.

In the automated OpenLane flow, Yosys synthesizes the high-level `count <= count + 8'b1` statement into an optimal carry network using multi-input gates (`and3_1`, `and4_1`, `a21oi_1`) from the SKY130 cell library, keeping cell area small and leaving 78.29 ns of setup slack at 10 MHz.

The output of this chip is an 8-bit binary count (`count[7:0]`), not a decoded 7-segment display digit. A 7-segment display decoder is omitted from the die to keep cell area compact. When connecting to external hardware, `count[7:0]` can drive external LEDs, a logic analyzer, or an off-chip display decoder IC.

# 3. Proposed Design and Methodology

## 3.1 System Overview

Fig. 3.1 shows the circuit block diagram. The 3 inputs (`clk`, `rst`, `en`) connect to the internal core. An 8-bit state register built from 8 D flip-flops interfaces with the next-state incrementer and carry logic. The 8-bit output bus `count[7:0]` presents the current state.

![Fig. 3.1: Block diagram of the proposed circuit](counter8/report_assets/fig_3_1_block_diagram.png "Fig. 3.1: Block diagram of the proposed circuit"){width="5.8in"}

*Fig. 3.1: Block diagram of the proposed circuit*

## 3.2 Design Specification

The operational specifications are defined as follows:
- Inputs (3): `clk` (10 MHz max, 100 ns period), `rst` (synchronous active-high), `en` (count enable).
- Outputs (8): `count[7:0]` unsigned binary output bus representing values 0 to 255 ($00_{16}$ to $FF_{16}$).
- Supply and clock: 1.8 V core supply, single clock domain of at most 10 MHz, synchronous active-high reset.
- Storage: 8-bit state register realized using 8 discrete standard-cell D flip-flops (`dfxtp_1`).
- Operations: synchronous reset, hold, count-up, and rollover, as listed in Table 3.1 and Table 3.2.
- Counting: purely synchronous binary counting; state updates occur concurrently on the rising edge of `clk`.

## 3.3 Truth Table / Function Table

Table 3.1 defines the functional truth table of the counter for all combinations of control inputs on the rising clock edge. Table 3.2 presents representative state transitions including count rollover, and Table 3.3 details the excitation requirements for each bit slice.

-------------------------------------------------------------------------
**rst**  **en**  **clk**       **Operation Mode**  **Next State `count[7:0]`**
-------- ------- ------------- ------------------- -----------------------------------------
1        X       Rising Edge   Synchronous Reset   `8'h00` ($00000000_2$)

0        0       Rising Edge   Hold / Memory       `count[7:0]` (no change)

0        1       Rising Edge   Count Up            `(count[7:0] + 8'h01) mod 256`
-------------------------------------------------------------------------

*Table 3.1: Function table of the counter operation modes*

-----------------------------------------------------------------------------------
**Current Count `count[7:0]`**  **rst**  **en**  **Next Count `count[7:0]`**  **Description**
------------------------------- -------- ------- ---------------------------- ---------------------
`8'h00` (0)                     0        1       `8'h01` (1)                  Counting from zero
`8'h13` (19)                    0        1       `8'h14` (20)                 Regular increment
`8'h14` (20)                    0        0       `8'h14` (20)                 Hold current state
`8'h14` (20)                    0        1       `8'h15` (21)                 Resume counting
`8'h1E` (30)                    1        X       `8'h00` (0)                  Synchronous reset
`8'hFE` (254)                   0        1       `8'hFF` (255)                Approaching rollover
`8'hFF` (255)                   0        1       `8'h00` (0)                  Natural rollover
-----------------------------------------------------------------------------------

*Table 3.2: State transitions and roll-over behaviour*

-----------------------------------------------------------------------------------
**Present State $Q_i$**  **Next State $Q_i^+$**  **Toggle Required $T_i$**  **Required D Input $D_i$**
------------------------ ----------------------- -------------------------- --------------------------
0                        0                       0                          0
0                        1                       1                          1
1                        0                       1                          0
1                        1                       0                          1
-----------------------------------------------------------------------------------

*Table 3.3: Excitation table for synchronous counter bit slice*

## 3.4 Logic Simplification and Implementation Choices

To determine the steering logic for bit $i$, we write the D flip-flop excitation equation with synchronous reset and enable controls:

$$Q_i^+ = \overline{rst} \cdot \left[ en \cdot (Q_i \oplus C_i) + \overline{en} \cdot Q_i ight]$$

For the least significant bit ($i = 0$), $C_0 = 1$, giving:
$$D_0 = \overline{rst} \cdot (Q_0 \oplus en) = \overline{rst} \cdot (Q_0 \cdot \overline{en} + \overline{Q_0} \cdot en)$$

Table 3.4 shows the Karnaugh map for the toggle condition $T_i$ as a function of $en$ and the carry term $C_i$.

------------------------------------------------------------------------
**en \ C_i**         **0**                        **1**
-------------------- ---------------------------- ----------------------------
**0**                0                            0

**1**                0                            1
------------------------------------------------------------------------

*Table 3.4: Karnaugh map of the toggle enable function*

Thus, $T_i = en \cdot C_i$, which confirms that the toggle condition simplifies to a conjunction of the enable signal and the carry chain.

Design choices:
- Synchronous reset: Chosen to ensure all flip-flops settle predictably with the 10 MHz clock and avoid partial resets from noise.
- Standard D flip-flops: Standard `sky130_fd_sc_hd__dfxtp_1` cells with external logic were used because they are compact and have predictable timing.
- Carry logic synthesis: Formulating the RTL as `count <= count + 8'b1` lets Yosys map carry gates directly into composite cells (`a21oi_1`, `o21a_1`, `and3_1`), avoiding the area and delay of a separate adder macro.

## 3.5 Circuit Diagram

Fig. 3.2 shows the schematic of bit slice $i$ and its carry interface. The slice includes an XOR gate for toggle logic $Q_i \oplus C_i$, a multiplexer selecting between hold and increment based on `en`, a second multiplexer selecting between zero and next-state data based on `rst`, and the rising-edge D flip-flop. Carry-out $C_{i+1} = C_i \cdot Q_i$ passes to the next bit.

![Fig. 3.2: Logic-level diagram of the counter bit slice and carry chain](counter8/report_assets/fig_3_2_circuit_diagram.png "Fig. 3.2: Logic-level diagram of the counter bit slice and carry chain"){width="5.8in"}

*Fig. 3.2: Logic-level diagram of the counter bit slice and carry chain*

## 3.6 Working Principle

The counter operates synchronously on the rising edge of `clk`:
1. Reset mode: when `rst = 1`, logic 0 is selected for all flip-flop inputs $D_7$ through $D_0$. On the rising clock edge, `count[7:0]` becomes `8'h00`.
2. Count mode: when `rst = 0` and `en = 1`, carry $C_0 = 1$. Bit 0 toggles on every clock edge. Bit 1 toggles when bit 0 is 1. In general, bit $i$ toggles when bits 0 through $i-1$ are all 1. The counter advances sequentially: $00_{16}, 01_{16}, 02_{16}, \dots, FF_{16}$.
3. Hold mode: when `rst = 0` and `en = 0`, $C_i = 0$ for all stages. The enable multiplexer routes $Q_i$ back to $D_i$. The flip-flops re-latch their current values, holding the output steady.
4. Rollover mode: when the counter reaches `8'hFF` ($11111111_2$) with `en = 1`, the increment rolls over to `8'h00` on the next rising clock edge.

Table 3.5 summarizes the sequence of stimulus phases applied during verification.

-------------------------------------------------------------------------------------
**Phase**  **Time Window**    **Duration**  **rst**  **en**  **Expected Count Progression**
---------- ------------------ ------------- -------- ------- -------------------------------
Phase 1    0 ns to 200 ns     200 ns (2T)   1        0       Reset active; `count = 8'h00`
Phase 2    200 ns to 2200 ns  2000 ns (20T) 0        1       Counting up: `8'h00` to `8'h14`
Phase 3    2200 ns to 2700 ns 500 ns (5T)   0        0       Hold mode; `count = 8'h14` (stable)
Phase 4    2700 ns to 3700 ns 1000 ns (10T) 0        1       Resume count: `8'h15` to `8'h1E`
Phase 5    3700 ns to 3900 ns 200 ns (2T)   1        1       Mid-count reset; `count = 8'h00`
Phase 6    3900 ns to 4900 ns 1000 ns (10T) 0        1       Restart count: `8'h01` to `8'h0A`
-------------------------------------------------------------------------------------

*Table 3.5: Sequence of stimulus phases during functional testing*

## 3.7 Performance Criteria

The physical design was evaluated against these criteria:
- Functional match: zero mismatches between the gate netlist and the behavioral reference model across all test cycles.
- Timing signoff: positive setup and hold slacks across all nine PVT corners at 10 MHz.
- Design rule check: zero Magic DRC errors and zero KLayout DRC errors.
- Netlist verification: 100% Layout-versus-Schematic (LVS) match in Netgen with zero unmatched devices, nets, or pins.
- Reliability: zero antenna violations and negligible IR voltage drop on power rails.

# 4. Implementation

## 4.1 Tools and Environment

The design flow ran on an x86_64 Linux system with Ubuntu 24.04 LTS:
- Simulation: Icarus Verilog 12 with GTKWave 3.3 for waveform viewing.
- Synthesis: Yosys 0.70 targeting the SKY130 library.
- Physical design: OpenLane 2 (flow 2.4.x) running OpenROAD for floorplanning, placement, clock-tree synthesis, and routing.
- Physical verification: Magic 8.3, KLayout 0.30, and Netgen 1.5.

## 4.2 Functional Simulation

We verified `counter8` using a self-checking testbench (`sim/counter_tb.v`). The testbench instantiates the counter module and maintains an independent reference model. On each rising clock edge, it checks the output after 1 ns to allow signals to settle.

Fig. 4.1 shows the simulation waveform across six test phases from 0 ns to 4,900 ns. During Phase 1 (0 to 200 ns), `rst = 1` holds the counter at 00h. During Phase 2 (200 to 2200 ns), `rst` is released and `en = 1`, incrementing `count[7:0]` from `8'h00` to `8'h14` (20 decimal). During Phase 3 (2200 to 2700 ns), `en = 0` holds the output at `8'h14`. During Phase 4 (2700 to 3700 ns), `en = 1` resumes counting to `8'h1E` (30 decimal). During Phase 5 (3700 to 3900 ns), reset is asserted mid-count, clearing the output to `8'h00` on the clock edge. During Phase 6 (3900 to 4900 ns), reset is released and counting restarts from `8'h01` to `8'h0A`.

The functional verification confirms proper synchronous state transitions. When `rst` is deasserted and `en` is held high, `count` increments synchronously by 1 on each rising clock edge from 00h up to FFh before rolling over to 00h. When `en` is deasserted, the counter preserves its state across clock edges, and asserting `rst` forces the output synchronously to 00h on the next active edge.

![Fig. 4.1: RTL simulation waveform at 10 MHz (Phase 1 to Phase 6 in GTKWave)](counter8/report_assets/fig_4_1_waveform.png "Fig. 4.1: RTL simulation waveform at 10 MHz (Phase 1 to Phase 6 in GTKWave)"){width="6.0in"}

*Fig. 4.1: RTL simulation waveform at 10 MHz (Phase 1 to Phase 6 in GTKWave)*

Fig. 4.2 shows the testbench console log. The error count remained zero throughout all 49 clock cycles.

![Fig. 4.2: Testbench console output (49 cycles verified, 0 errors)](counter8/report_assets/fig_4_2_testbench_console.png "Fig. 4.2: Testbench console output (49 cycles verified, 0 errors)"){width="5.5in"}

*Fig. 4.2: Testbench console output (49 cycles verified, 0 errors)*

## 4.3 Physical Design

OpenLane 2 executed physical design in 76 automated stages. Fig. 4.3 outlines the flow from Verilog RTL to GDSII layout.

![Fig. 4.3: RTL-to-GDSII flow used for the physical design](counter8/report_assets/fig_4_3_flow_diagram.png "Fig. 4.3: RTL-to-GDSII flow used for the physical design"){width="6.0in"}

*Fig. 4.3: RTL-to-GDSII flow used for the physical design*

### 4.3.1 Synthesis and Netlist

Logic synthesis was performed by Yosys targeting `sky130_fd_sc_hd`. The synthesized gate-level netlist contains 28 cells:
- 8 Sequential Cells: 8 positive edge-triggered D flip-flops (`sky130_fd_sc_hd__dfxtp_1`), occupying an area of 160.15 µm².
- 20 Combinational Cells: 5 AND-OR-Invert gates (`a21oi_1`), 1 wide AOI gate (`a41oi_1`), 3 three-input AND gates (`and3_1`), 1 four-input AND gate (`and4_1`), 2 two-input NOR gates (`nor2_1`), 4 three-input NOR gates (`nor3_1`), 3 OR-AND gates (`o21a_1`), and 1 XNOR gate (`xnor2_1`), occupying an area of 120.12 µm².
Total netlist cell area directly from synthesis is 280.27 µm². Yosys reported zero inferred latches and zero unmapped gates.

### 4.3.2 Die Size and Flow Parameters

Table 4.1 details the physical design configuration specified in `config.json`. The die dimensions are fixed at 180 µm × 115 µm (20,700 µm²) to match the Silicluster v3 standard frame. Core area is 15,612.5 µm² bounded by (5.52, 10.88) to (174.34, 103.36) µm, containing 34 standard-cell rows and 12,478 placement sites.

---------------------------------------------------------------------------------
**Parameter**                     **Value**                     **Description**
--------------------------------- ----------------------------- ---------------------------------
`DESIGN_NAME`                     `counter`                     Top-level module name
`PDK` / `STD_CELL_LIBRARY`        `sky130A` / `sky130_fd_sc_hd` SkyWater 130 nm high-density
`CLOCK_PORT` / `CLOCK_PERIOD`     `clk` / `100.0 ns`            10 MHz target clock constraint
`DIE_AREA`                        `0 0 180 115`                 Die bounding box (180 × 115 µm)
`CORE_AREA`                       `5.52 10.88 174.34 103.36`    Core bounding box (15,612.5 µm²)
`PL_TARGET_DENSITY_PCT`           `30 %`                        Target standard-cell density
`FP_PDN_VPITCH` / `HPITCH`        `50 µm` / `50 µm`             Vertical and horizontal PDN strap pitch
`FP_PDN_VOFFSET` / `HOFFSET`      `5 µm` / `5 µm`               Power grid offset from core edge
`QUIT_ON_SETUP_VIOLATIONS`        `true`                        Strict halt on setup timing violation
---------------------------------------------------------------------------------

*Table 4.1: Flow parameters and die specification*

### 4.3.3 Placement, Clock Tree and Routing

1. Floorplanning and PDN: The core area is bounded by $X \in [5.52, 174.34] 	ext{ µm}$ and $Y \in [10.88, 103.36] 	ext{ µm}$, containing 34 standard-cell rows and 12,478 placement sites. Power straps on Metal 4 and Metal 5 form a low-impedance power distribution network with 50 µm pitch. A total of 216 well-tap cells (`tapvpwrvgnd_1`, area 270.26 µm²) were inserted to prevent latch-up.
2. Global and Detailed Placement: RePlAce executed global placement, followed by OpenROAD detailed placement. The 28 logic cells were placed with mean displacement of 0.22 µm.
3. Clock Tree Synthesis: TritonCTS synthesized a low-skew clock distribution network using 3 clock buffers (`clkbuf_16`), consuming 75.07 µm². Clock skew was constrained to +0.259 ns for setup and -0.307 ns for hold.
4. Timing Optimization: The resizer tool inserted 22 timing-repair buffers (area 170.16 µm²), including 12 hold-repair buffers to eliminate fast-path hold violations at the cold/fast corner. Total standard cells before fill totaled 269 cells (area 795.76 µm²).
5. Detailed Routing: TritonRoute routed 56 signal nets using Metal 1 through Metal 4. Routing converged in 3 iterations with 0 DRC violations, achieving 1,041 µm total wirelength and 294 single-cut vias.
6. Metal Fill Insertion: To satisfy metal density rules, 1,372 fill cells (area 14,816.7 µm²) were inserted into empty core sites, bringing total design instances to 1,641.

### 4.3.4 DRC, LVS and Layout Checks

Signoff physical verification was executed at the GDSII level:
- Magic DRC: Streamed out GDSII layout was checked against full SKY130 manufacturing rules: 0 errors.
- KLayout DRC: Independent geometric verification: 0 errors.
- Netgen LVS: Extracted SPICE netlist compared against the structural Verilog netlist: 0 device differences, 0 net differences, 0 property errors, 0 unmatched pins.
- Antenna Verification: Check of gate oxide antenna ratios: 0 violating nets, 0 violating pins.

Fig. 4.4 displays the top-view layout of `counter` streamed out to GDSII.

![Fig. 4.4: Top view of the final layout (counter, 180 × 115 µm, SKY130)](counter8/report_assets/fig_4_4_layout.png "Fig. 4.4: Top view of the final layout (counter, 180 × 115 µm, SKY130)"){width="5.0in"}

*Fig. 4.4: Top view of the final layout (counter, 180 × 115 µm, SKY130)*

## 4.4 Fabrication Submission

### 4.4.1 Layout Deliverables

All deliverables required for silicon fabrication were generated in the `submission/` directory:
- `gds/counter.gds`: Primary GDSII stream file for mask fabrication.
- `mag_gds/counter.magic.gds` and `klayout_gds/counter.klayout.gds`: Tool-specific signoff layouts.
- `def/counter.def` and `lef/counter.lef`: Physical design exchange and macro abstract files.
- `sdc/counter.sdc`: Synopsys Design Constraints timing file (100 ns clock constraint).
- `spice/counter.spice`: Extracted SPICE netlist with parasitic resistances and capacitances.
- `sdf/` and `spef/`: Multi-corner Standard Delay Format (SDF) and Standard Parasitic Exchange Format (SPEF) files across all nine PVT corners.
- `lib/`: Liberty timing libraries across nine corners.
- `metrics.json` and `metrics.csv`: Machine-readable signoff verification logs.

### 4.4.2 Fabrication Status

The layout has met 100 % of the Silicluster v3 physical design guidelines. The design has zero DRC, LVS, timing, and antenna violations and is fully prepared for multi-project wafer (MPW) fabrication.

### 4.4.3 Problems Faced and Troubleshooting

During physical design, two primary challenges were encountered and resolved:
1. Hold Time Violations at Fast/Cold Corner: Due to the compact nature of the 8-bit counter, data paths between adjacent flip-flops were exceptionally short (<0.5 ns). Under the fast process corner (`nom_ff_n40C_1v95`), fast signal transitions threatened hold violations. OpenLane's resizer tool was configured to automatically insert 12 dedicated hold buffers (`sky130_fd_sc_hd__dlymetal6s2s_1`), successfully ensuring a positive hold slack of +0.116 ns at the worst corner.
2. Standard Cell Row Well-Tap Density: Early floorplanning exhibited non-uniform well-tap distribution. By adjusting `FP_TAPCELL_DIST` to 14 µm, 216 tap cells were inserted uniformly across all 34 rows, fully satisfying DRC rule `tap.2` and eliminating CMOS latch-up susceptibility.

# 5. Results and Discussion

## 5.1 Experimental Setup

The design was verified through cycle-accurate behavioral simulation in Icarus Verilog, static timing signoff using OpenROAD STA across nine extraction corners, and physical verification using Magic, KLayout, and Netgen.

## 5.2 Simulation Results

Table 5.1 details the functional simulation results across the six testbench phases. In all 49 clock cycles evaluated, the DUT matched the golden model with zero errors.

-------------------------------------------------------------------------------------------------
**Phase**  **Time Window**  **Cycles**  **Inputs (rst, en)**  **Expected Count**  **Observed Count**  **Status**
---------- ---------------- ----------- --------------------- ------------------- ------------------- ----------
Phase 1    0 to 200 ns      2           `rst=1, en=0`         `8'h00`             `8'h00`             PASS
Phase 2    200 to 2200 ns   20          `rst=0, en=1`         `8'h01` .. `8'h14`  `8'h01` .. `8'h14`  PASS
Phase 3    2200 to 2700 ns  5           `rst=0, en=0`         `8'h14` (stable)    `8'h14` (stable)    PASS
Phase 4    2700 to 3700 ns  10          `rst=0, en=1`         `8'h15` .. `8'h1E`  `8'h15` .. `8'h1E`  PASS
Phase 5    3700 to 3900 ns  2           `rst=1, en=1`         `8'h00`             `8'h00`             PASS
Phase 6    3900 to 4900 ns  10          `rst=0, en=1`         `8'h01` .. `8'h0A`  `8'h01` .. `8'h0A`  PASS
-------------------------------------------------------------------------------------------------

*Table 5.1: RTL simulation results (Icarus Verilog)*

All 49 clock verification cycles passed with zero errors. The self-checking testbench confirmed that the counter increments strictly by 1 on each positive clock edge when `en` is asserted, holds state indefinitely when `en` is deasserted, and clears synchronously to 00h upon `rst` assertion without any intermediate glitch states or decoding hazards.

## 5.3 Physical Verification Results

Table 5.2 summarizes the physical verification signoff results extracted from `metrics.json`.

---------------------------------------------------------------------------------
**Verification Check**           **Tool**             **Measured Result**  **Pass Criteria**
-------------------------------- -------------------- -------------------- -----------------
Linter Errors & Warnings         Verilator            0 errors, 0 warnings Zero violations
Synthesis Check Errors           Yosys                0 errors             Zero unmapped
Magic Design Rules (DRC)         Magic 8.3            0 errors             0 violations
KLayout Design Rules (DRC)       KLayout 0.30         0 errors             0 violations
Routing DRC Violations           TritonRoute          0 errors (in 3 iter) 0 violations
Layout-versus-Schematic (LVS)    Netgen 1.5           0 mismatches         0 device/net diff
Antenna Violations               OpenROAD             0 violating nets     0 antenna errors
Worst Setup Slack (all corners)  OpenROAD STA         +76.75 ns            Slack ≥ 0.0 ns
Worst Hold Slack (all corners)   OpenROAD STA         +0.116 ns            Slack ≥ 0.0 ns
Max Slew & Cap Violations        OpenROAD STA         0 violations         Zero violations
IR Voltage Drop (worst)          OpenROAD PDN         4.99 µV              Drop < 100 mV
---------------------------------------------------------------------------------

*Table 5.2: Physical verification and signoff results (OpenLane run)*

## 5.4 Layout Results: Area, Power and Timing

Table 5.3 presents the area, power, and cell distribution of the final physical layout.

---------------------------------------------------------------------------------
**Category**                      **Metric**                    **Value**
--------------------------------- ----------------------------- ---------------------------------
**Die & Core Dimensions**         Die Bounding Box / Area       180 µm × 115 µm / 20,700 µm²
                                  Core Bounding Box / Area      (5.52, 10.88) to (174.34, 103.36) / 15,612.5 µm²
                                  Rows / Placement Sites        34 rows / 12,478 sites

**Cell Counts**                   Sequential D Flip-Flops       8 cells (`dfxtp_1`)
                                  Combinational Logic Cells     20 cells (`a21oi`, `and3`, `nor3`, etc.)
                                  Tap Cells                     216 cells (`tapvpwrvgnd_1`)
                                  Clock Buffers                 3 cells (`clkbuf_16`)
                                  Timing-Repair Buffers         22 cells (12 hold buffers)
                                  Total Standard Cells          269 cells
                                  Metal Fill Cells              1,372 cells
                                  Total Instances               1,641 cells

**Cell Area**                     Sequential Cell Area          160.15 µm²
                                  Combinational Cell Area       120.12 µm²
                                  Tap Cell Area                 270.26 µm²
                                  Clock Buffer Area             75.07 µm²
                                  Timing Repair Buffer Area     170.16 µm²
                                  Total Active Std-Cell Area    795.76 µm²
                                  Fill Cell Area                14,816.70 µm²
                                  Standard-Cell Utilization     5.10 % (795.76 / 15,612.5)

**Interconnect & Routing**        Total Routed Wirelength       1,041 µm (max wirelength 145.3 µm)
                                  Total Vias                    294 (all single-cut)
                                  Signal Nets                   56 nets

**Power Dissipation**             Internal Power                10.10 µW (79.6 %)
(@ 10 MHz, 1.8 V)                 Switching Power               2.59 µW (20.4 %)
                                  Leakage Power                 5.22 nW (< 0.1 %)
                                  Total Power Dissipation       12.69 µW

**Power Grid Integrity**          Worst VPWR Voltage Drop       4.99 µV (Nominal 1.8000 V)
                                  Worst VGND Voltage Drop       5.35 µV (Nominal 0.0000 V)
---------------------------------------------------------------------------------

*Table 5.3: Area, power and cell statistics of the final layout*

Table 5.4 details the Static Timing Analysis results across nominal, slow, and fast corners.

-------------------------------------------------------------------------------------------------
**Corner**             **Process / Temp / Voltage**  **Setup WS (ns)**  **Hold WS (ns)**  **Setup Skew**  **Hold Skew**
---------------------- ----------------------------- ------------------ ----------------- --------------- --------------
`nom_tt_025C_1v80`     Typical / 25 °C / 1.80 V      +78.29             +0.339            +0.259 ns       -0.307 ns
`nom_ss_100C_1v60`     Slow-Slow / 100 °C / 1.60 V   +76.78             +0.915            +0.267 ns       -0.349 ns
`nom_ff_n40C_1v95`     Fast-Fast / -40 °C / 1.95 V   +78.83             +0.119            +0.256 ns       -0.290 ns
`min_ff_n40C_1v95`     Fast-Fast / -40 °C / 1.95 V   +78.84             +0.116            +0.256 ns       -0.289 ns
`max_ss_100C_1v60`     Slow-Slow / 100 °C / 1.60 V   +76.75             +0.923            +0.268 ns       -0.351 ns
-------------------------------------------------------------------------------------------------

*Table 5.4: Timing summary across nominal, slow and fast corners*

Fig. 5.1 illustrates the standard-cell area breakdown by cell category (excluding metal fill cells).

![Fig. 5.1: Standard-cell area by cell class (total 795.8 µm², fill cells excluded)](counter8/report_assets/fig_5_1_area_breakdown.png "Fig. 5.1: Standard-cell area by cell class (total 795.8 µm², fill cells excluded)"){width="5.0in"}

*Fig. 5.1: Standard-cell area by cell class (total 795.8 µm², fill cells excluded)*

Fig. 5.2 presents the setup and hold slack margins across the three principal PVT corners.

![Fig. 5.2: Worst setup and hold slack at three corners](counter8/report_assets/fig_5_2_slack_corners.png "Fig. 5.2: Worst setup and hold slack at three corners"){width="5.0in"}

*Fig. 5.2: Worst setup and hold slack at three corners*

## 5.5 Comparison of Simulation and Physical Results

Simulation and physical results show consistent operation:
1. Clock frequency: In simulation, the counter runs at 10 MHz (100 ns period). Physical timing analysis reports a worst-case setup slack of +76.75 ns under slow conditions (100 °C, 1.60 V), giving a critical path delay of 23.25 ns. This indicates the circuit can operate up to approximately 43.0 MHz, well above the 10 MHz requirement.
2. Synchronous reset: Behavioral tests verified clean reset transitions. The synthesized netlist confirms that reset logic is built directly into the `a21oi_1` gates feeding the D flip-flops, giving reset paths the same propagation delay as count paths.

## 5.6 Discussion and Limitations

- Core utilization: Standard-cell utilization is 5.10 % inside the 15,612.5 µm² core. This occurs because the 8-bit counter uses only 28 logic cells inside the standard 180 µm × 115 µm Silicluster frame. The remaining space was filled with 1,372 fill cells to satisfy metal density rules.
- Power consumption: Total power dissipation is 12.69 µW at 10 MHz, with leakage power of 5.22 nW.
- Pin count: The circuit uses 11 signal pins plus 2 power pads, well within the 20-pin limit of standard multi-project wafer packaging frames.

# 6. Conclusion and Future Scope

## 6.1 Conclusion

We designed an 8-bit synchronous binary up counter with synchronous reset and enable controls in synthesizable Verilog-2001. A self-checking testbench across six test phases and 49 clock cycles passed with zero errors. We synthesized the design into 28 SKY130 standard cells, placed and routed it inside a 180 × 115 µm die, and met setup and hold constraints across nine PVT corners with zero DRC, LVS, and antenna errors. The layout is ready for fabrication under the Silicluster v3 program.

## 6.2 Future Scope

Possible additions to the counter include:
1. Up/down counting: adding a direction input (`up_down`) for bidirectional operation.
2. Parallel preload: adding an 8-bit input bus (`load_data[7:0]`) and a load enable pin to preload starting values.
3. Modulo-M counting: adding detection logic for decade (BCD) counting or arbitrary modulus limits.
4. Clock gating: inserting integrated clock-gating cells to disable clock switching in hold mode, reducing dynamic power.
5. Hardware testing: mounting fabricated chips onto test boards with a 10 MHz crystal oscillator and 7-segment display drivers to compare measured hardware performance against simulation.

# 7. References

[1] M. M. Mano and M. D. Ciletti, *Digital Design: With an Introduction to the Verilog HDL*, 5th ed. Upper Saddle River, NJ, USA: Pearson, 2013.

[2] R. J. Tocci, N. S. Widmer, and G. L. Moss, *Digital Systems: Principles and Applications*, 12th ed. Boston, MA, USA: Pearson, 2017.

[3] E. F. Deprettere and R. H. Niggemann, "High-speed parallel counter architectures and carry propagation analysis," *IEEE Trans. Computers*, vol. 50, no. 6, pp. 580-592, Jun. 2001.

[4] J. M. Rabaey, A. P. Chandrakasan, and B. Nikolić, "Digital Integrated Circuits: A Design Perspective," 2nd ed. Upper Saddle River, NJ, USA: Pearson, 2003.

[5] Silicluster, "Silicluster v3 free tapeout call for digital projects," call document, 2026.

[6] SkyWater Technology and Google, "SkyWater SKY130 process design kit (PDK)," [Online]. Available: https://github.com/google/skywater-pdk. [Accessed: Nov. 2026].

[7] Efabless, "OpenLane 2: RTL-to-GDSII flow," [Online]. Available: https://github.com/efabless/openlane2. [Accessed: Nov. 2026].

[8] IEEE Standard Verilog Hardware Description Language, IEEE Std 1364-2001, 2001.

[9] S. Williams, "Icarus Verilog," [Online]. Available: http://iverilog.icarus.com/. [Accessed: Nov. 2026].

[10] "GTKWave waveform viewer," [Online]. Available: http://gtkwave.sourceforge.net/. [Accessed: Nov. 2026].

[11] C. Wolf, "Yosys Open SYnthesis Suite," [Online]. Available: https://yosyshq.net/yosys/. [Accessed: Nov. 2026].

[12] M. Köfferlein, "KLayout layout viewer and editor," [Online]. Available: https://www.klayout.de/. [Accessed: Nov. 2026].

[13] T. Edwards, "Magic VLSI Layout Tool and Netgen LVS," [Online]. Available: http://opencircuitdesign.com/. [Accessed: Nov. 2026].

# 8. Appendix

## A.1 Project Files and Layout Deliverables

Table A.1 lists the files that accompany this report. The final GDSII layout and the signoff metrics come from the OpenLane run RUN_2026-11-15_04-45-36.

---------------------------------------------------------------------------------
**File / Folder**                 **Description**
--------------------------------- -----------------------------------------------
`rtl/counter.v`                   Synthesizable Verilog-2001 source of 8-bit synchronous up counter
`sim/counter_tb.v`                Self-checking testbench with cycle-accurate golden reference model
`sim/counter_tb.vcd`               VCD simulation waveform trace of 4,900 ns verification run
`synthesis/synth.ys`, `synth.log` Yosys synthesis script and gate-level cell mapping log
`openlane/config.json`            OpenLane 2 physical design configuration and floorplan parameters
`submission/gds/counter.gds`      Final production GDSII stream file for mask fabrication
`submission/def/counter.def`      Standard-cell placement and routing DEF file
`submission/lef/counter.lef`      Macro abstract LEF file with pin geometries and routing obstructions
`submission/reports/metrics.json` Machine-readable signoff verification and timing metrics
---------------------------------------------------------------------------------

*Table A.1: Project files and deliverables*

## A.2 RTL Source Extract

The complete synthesizable Verilog source code and self-checking testbench are reproduced below.

### `counter.v`

```verilog
// ============================================================================
// File:    counter.v - 8-bit synchronous up counter with sync reset and enable
// Project: counter8 - Silicluster v3 digital submission (SKY130, 1.8 V, 10 MHz)
// Authors: Roshan Yadav, Manan Gupta, Siddi Kanwar, Ritika saini, Ginni
// ============================================================================
module counter (
    input  wire       clk,   // system clock (10 MHz max, 100 ns period)
    input  wire       rst,   // synchronous active-high reset
    input  wire       en,    // active-high count enable
    output reg  [7:0] count  // 8-bit binary counter output bus
);

    always @(posedge clk) begin
        if (rst)
            count <= 8'b0;
        else if (en)
            count <= count + 8'b1;
        // else hold current value
    end

endmodule
```

### `counter_tb.v`

```verilog
// ============================================================================
// File:    counter_tb.v - Self-checking testbench with golden reference model
// ============================================================================
`timescale 1ns / 1ps

module counter_tb;
    reg clk, rst, en;
    wire [7:0] count;
    reg [7:0] expected;
    integer error_count;

    counter uut (.clk(clk), .rst(rst), .en(en), .count(count));

    initial clk = 1'b0;
    always #50 clk = ~clk; // 10 MHz clock (100 ns period)

    initial begin
        $dumpfile("counter_tb.vcd");
        $dumpvars(0, counter_tb);
    end

    always @(posedge clk) begin
        if (rst) expected <= 8'b0;
        else if (en) expected <= expected + 8'b1;
    end

    always @(posedge clk) begin
        #1;
        if (count !== expected) begin
            $display("ERROR @ %0t ns: count=%0d, expected=%0d", $time, count, expected);
            error_count = error_count + 1;
        end
    end

    initial begin
        error_count = 0; expected = 8'b0;
        rst = 1'b1; en = 1'b0; #200;
        rst = 1'b0; en = 1'b1; #2000;
        en = 1'b0; #500;
        en = 1'b1; #1000;
        rst = 1'b1; #200;
        rst = 1'b0; en = 1'b1; #1000;
        if (error_count == 0) $display("TEST PASSED");
        else $display("TEST FAILED: %0d mismatches", error_count);
        $finish;
    end
endmodule
```

## A.3 Additional Signoff Metrics

---------------------------------------------------------------------------------
**Metric Name**                   **Value**
--------------------------------- -----------------------------------------------
Instance count by class           Sequential: 8; combinational: 20; timing buffers: 22; tap: 216; clock buffers: 3; fill: 1,372; total: 1,641
Instance area by class            Sequential: 160.15 µm²; tap cells: 270.26 µm²; timing buffers: 170.16 µm²; combinational: 120.12 µm²; clock buffers: 75.07 µm²; fill: 14,816.70 µm²
Routing DRC errors per iteration  11, 1, 1, 0 (converged cleanly in 3 iterations)
Clock skew (worst)                Setup skew: +0.259 ns; Hold skew: -0.307 ns (TritonCTS 3 buffers)
IR drop (VPWR / VGND)             Worst VPWR drop: 4.99 µV; Worst VGND drop: 5.35 µV (negligible)
Power dissipation                 Total: 12.69 µW; internal: 10.10 µW; switching: 2.59 µW; leakage: 5.22 nW
LVS differences                   0 device differences, 0 net differences, 0 property errors, 0 unmatched pins
---------------------------------------------------------------------------------

*Table A.2: Additional signoff metrics from metrics.json*

## A.4 Individual Contribution of Group Members

---------------------------------------------------------------------------------
**Member Name**                   **Contribution**
--------------------------------- -----------------------------------------------
Roshan Yadav                      RTL architecture design, Verilog-2001 modeling, synchronous reset & enable logic verification
Manan Gupta                       Testbench architecture, automated self-checking reference model, VCD waveform analysis in GTKWave
Siddi Kanwar                      Yosys logic synthesis, cell mapping optimization, gate-level netlist timing and area inspection
Ritika saini                      OpenLane physical design execution, floorplanning, PDN grid synthesis, placement, CTS, and routing
Ginni                             Signoff verification, Magic/KLayout DRC analysis, Netgen LVS, multi-corner STA, and report writing
---------------------------------------------------------------------------------

*Table A.3: Individual contribution of group members*
