// ============================================================================
// File:    counter_tb.v
// Project: counter8 — Silicluster v3 digital submission
// Author:  Deepak
// Date:    2026-11-15
//
// Description:
//   Self-checking testbench for the 8-bit up counter.
//   Stimulus as specified, plus a reference model that tracks expected
//   behaviour and compares every clock cycle.
// ============================================================================

`timescale 1ns / 1ps

module counter_tb;

    // ------------------------------------------------------------------
    // DUT signals
    // ------------------------------------------------------------------
    reg        clk;
    reg        rst;
    reg        en;
    wire [7:0] count;

    // ------------------------------------------------------------------
    // Reference model
    // ------------------------------------------------------------------
    reg [7:0] expected;
    integer   error_count;

    // ------------------------------------------------------------------
    // DUT instantiation
    // ------------------------------------------------------------------
    counter uut (
        .clk   (clk),
        .rst   (rst),
        .en    (en),
        .count (count)
    );

    // ------------------------------------------------------------------
    // Clock generation: 10 MHz -> period 100 ns, toggle every 50 ns
    // ------------------------------------------------------------------
    initial clk = 1'b0;
    always #50 clk = ~clk;

    // ------------------------------------------------------------------
    // Waveform dump
    // ------------------------------------------------------------------
    initial begin
        $dumpfile("counter_tb.vcd");
        $dumpvars(0, counter_tb);
    end

    // ------------------------------------------------------------------
    // Reference model update — mirrors the DUT logic
    // ------------------------------------------------------------------
    always @(posedge clk) begin
        if (rst)
            expected <= 8'b0;
        else if (en)
            expected <= expected + 8'b1;
        // else hold
    end

    // ------------------------------------------------------------------
    // Checker: compare count to expected one delta after the clock edge
    // ------------------------------------------------------------------
    always @(posedge clk) begin
        #1; // wait one time-step for DUT output to settle
        if (count !== expected) begin
            $display("ERROR @ %0t ns: count=%0d, expected=%0d",
                     $time, count, expected);
            error_count = error_count + 1;
        end
    end

    // ------------------------------------------------------------------
    // Stimulus
    // ------------------------------------------------------------------
    initial begin
        // Initialise
        error_count = 0;
        expected    = 8'b0;

        // Phase 1: reset active, enable off — 200 ns (2 clocks)
        rst = 1'b1;
        en  = 1'b0;
        #200;

        // Phase 2: counting — 2000 ns (20 clocks)
        rst = 1'b0;
        en  = 1'b1;
        #2000;

        // Phase 3: hold — 500 ns (5 clocks)
        en = 1'b0;
        #500;

        // Phase 4: resume counting — 1000 ns (10 clocks)
        en = 1'b1;
        #1000;

        // Phase 5: assert reset while counting — 200 ns (2 clocks)
        rst = 1'b1;
        #200;

        // Phase 6: release reset and count again — 1000 ns (10 clocks)
        rst = 1'b0;
        en  = 1'b1;
        #1000;

        // ------------------------------------------------------------------
        // Verdict
        // ------------------------------------------------------------------
        if (error_count == 0)
            $display("TEST PASSED");
        else
            $display("TEST FAILED: %0d mismatches", error_count);

        $finish;
    end

endmodule
