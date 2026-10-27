# Computer Evolution and Performance

## A short history

Most computers are **general-purpose** machines, built for no specific application; **special-purpose** machines are tailored to one.

- **Z1** (1938) was the first program-controlled mechanical computer, and **Z3** (Germany, 1941) a fully functional programmable machine.
- **ENIAC** (University of Pennsylvania, 1944) was the first operational general-purpose electronic machine, built with vacuum tubes and programmed by switches and cables.
- **EDVAC** explored the stored program; **EDSAC** (Cambridge, 1949) became the first full-scale, fully operational stored-program computer.
- Harvard's **MARK III and IV** used separate memories for instructions and data, giving the name **Harvard architecture**.
- **UNIVAC I** (1951) was the first general-purpose commercial computer, and the **IBM 701** came in 1952.
- IBM's **360** series (1964); DEC's **PDP-8**, the first minicomputer; Intel's **4004** (1971), the first microprocessor; the first PCs (1977).
- Supercomputers: the **CDC 6600** (1961) and **Cray-1** (1976); later parallel machines were shared-memory or distributed-memory, then networks and grids.

## Architectural styles

Early designers did more per instruction, adding complex instructions and many addressing modes (over 20 on the VAX) to close the **semantic gap**. These are **CISC** machines. Studies then found that assignments, conditional branches and procedure calls make up over 80 percent of executed instructions. Speeding these up while simplifying instructions gave **RISC** machines, which most modern processors follow. Integration grew from SSI, MSI and LSI to VLSI.

## Performance measures

- **Clock rate** f, cycle time T = 1/f.
- **CPI** (cycles per instruction): the average number of clock cycles each instruction takes. For a mix of instructions, CPI = Σ (fraction of instructions of each type × its cycles).
- **CPU time** = instruction count × CPI ÷ clock rate = IC × CPI × T.
- **MIPS** (million instructions per second) = clock rate ÷ (CPI × 10⁶).
- **MFLOPS** counts floating-point operations per second.

None of these alone defines performance consistently: MIPS ignores how much work each instruction does, so a machine with simpler instructions can show high MIPS but run slower.

**Example:** machine A has a 50 ns cycle and CPI 4.0 (200 ns per instruction); machine B a 65 ns cycle and CPI 2.5 (162.5 ns). B is 200 ÷ 162.5 ≈ **1.23 times faster**.

**Example:** a program runs in 50 s on a 500 MHz machine A, so it uses 25 × 10⁹ cycles. If B needs 2.5 times as many cycles and must finish in 20 s, its clock must be 62.5 × 10⁹ ÷ 20 = **3.125 GHz**.

**Speedup** = old execution time ÷ new execution time.

Source: CSC 313-Computer Organization and Architecture.pdf (course material, T. Oguntunde), Unit 1 (historical development, architectural styles, technological development, performance measures and the unit's exercises)
