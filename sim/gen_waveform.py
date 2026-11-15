#!/usr/bin/env python3
"""Generate a waveform image from counter_tb.vcd using matplotlib."""
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Parse VCD file
vcd_path = 'sim/counter_tb.vcd'
signals = {}
time_vals = []
current_time = 0
scope = ''
var_map = {}  # id -> (name, width)

with open(vcd_path, 'r') as f:
    in_defs = True
    for line in f:
        line = line.strip()
        if line.startswith('$var'):
            parts = line.split()
            # $var wire WIDTH ID NAME $end
            width = int(parts[2])
            vid = parts[3]
            name = parts[4]
            var_map[vid] = (name, width)
            signals[name] = []
        elif line.startswith('$enddefinitions'):
            in_defs = False
        elif not in_defs:
            if line.startswith('#'):
                current_time = int(line[1:])
            elif line.startswith('b'):
                # Binary value: bVALUE ID
                parts = line.split()
                val_str = parts[0][1:]
                vid = parts[1]
                if vid in var_map:
                    name, width = var_map[vid]
                    # Replace x/z with 0 for plotting
                    clean_str = val_str.replace('x', '0').replace('X', '0').replace('z', '0').replace('Z', '0')
                    val = int(clean_str, 2) if clean_str else 0
                    signals[name].append((current_time, val))
            elif len(line) >= 2 and line[0] in '01xzXZ':
                val = 1 if line[0] == '1' else 0
                vid = line[1:]
                if vid in var_map:
                    name, width = var_map[vid]
                    signals[name].append((current_time, val))

# Create step functions for each signal
def make_steps(sig_data, end_time):
    if not sig_data:
        return [0, end_time], [0, 0]
    times = [0]
    vals = [sig_data[0][1] if sig_data[0][0] == 0 else 0]
    for t, v in sig_data:
        times.append(t)
        vals.append(vals[-1])
        times.append(t)
        vals.append(v)
    times.append(end_time)
    vals.append(vals[-1])
    return times, vals

end_time = 5000  # ns

# Plot
fig, axes = plt.subplots(4, 1, figsize=(16, 8), sharex=True, 
                          gridspec_kw={'height_ratios': [1, 1, 1, 2]})
fig.suptitle('counter8 — Simulation Waveform (10 MHz, 8-bit up counter)', fontsize=14, fontweight='bold')

signal_names = ['clk', 'rst', 'en', 'count']
colors = ['#2196F3', '#F44336', '#4CAF50', '#FF9800']

for i, (name, color) in enumerate(zip(signal_names, colors)):
    ax = axes[i]
    if name in signals:
        t, v = make_steps(signals[name], end_time)
        t_ns = [x/1000 for x in t]  # Convert ps to ns
        
        if name == 'count':
            # For count, show as step plot with values
            ax.step([x for x in t_ns], v, where='post', color=color, linewidth=1.5)
            ax.fill_between(t_ns, v, step='post', alpha=0.15, color=color)
            ax.set_ylabel(name, fontsize=11, fontweight='bold')
            ax.set_ylim(-5, 270)
            ax.set_yticks([0, 50, 100, 150, 200, 255])
        else:
            ax.step(t_ns, v, where='post', color=color, linewidth=2)
            ax.fill_between(t_ns, v, step='post', alpha=0.2, color=color)
            ax.set_ylabel(name, fontsize=11, fontweight='bold')
            ax.set_ylim(-0.2, 1.4)
            ax.set_yticks([0, 1])
    
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

axes[-1].set_xlabel('Time (ns)', fontsize=11)
axes[-1].set_xlim(0, end_time/1000)

# Add phase annotations
phases = [
    (0, 200, 'RST', '#FFCDD2'),
    (200, 2200, 'COUNT', '#C8E6C9'),
    (2200, 2700, 'HOLD', '#FFF9C4'),
    (2700, 3700, 'COUNT', '#C8E6C9'),
    (3700, 3900, 'RST', '#FFCDD2'),
    (3900, 4900, 'COUNT', '#C8E6C9'),
]

for start, end, label, fcolor in phases:
    axes[0].axvspan(start, end, alpha=0.15, color=fcolor)
    axes[0].text((start+end)/2, 1.25, label, ha='center', fontsize=8, fontstyle='italic')

plt.tight_layout()
plt.savefig('docs/waveform.png', dpi=150, bbox_inches='tight')
print(f"Saved waveform image to docs/waveform.png")
