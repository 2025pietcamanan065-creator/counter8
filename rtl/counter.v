// ============================================================================
// File:    counter.v
// Project: counter8 — Silicluster v3 digital submission
// Author:  Deepak
// Date:    2026-11-15
//
// Description:
//   8-bit synchronous up counter with active-high reset and count enable.
//   - rst=1 : count <= 0          (synchronous reset)
//   - en=1  : count <= count + 1  (count up)
//   - else  : count <= count      (hold)
//
// Technology: SKY130 (sky130_fd_sc_hd), 1.8 V, max 10 MHz clock
// ============================================================================

module counter (
    input  wire       clk,   // system clock (10 MHz max)
    input  wire       rst,   // synchronous active-high reset
    input  wire       en,    // count enable
    output reg  [7:0] count  // 8-bit counter output
);

    always @(posedge clk) begin
        if (rst)
            count <= 8'b0;
        else if (en)
            count <= count + 8'b1;
        // else: hold current value (implicit)
    end

endmodule
