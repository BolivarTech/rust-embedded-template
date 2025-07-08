# Rust Embedded Detailed Setup

## Install Rust Toolchain

For installation instructions, see [Rust Toolchain Install Guide](https://www.rust-lang.org/tools/install).

## Install Cargo Utils

  ```bash
  rustup target install <TARGET>  # Example: rustup target install thumbv7em-none-eabihf
  cargo install cargo-binutils cargo-generate
  rustup component add llvm-tools-preview
  ```
## Read ELF file content

To read the content of an ELF file, you can use the `cargo readobj` command or `cargo objdump` command. These commands will help you inspect the ELF file's headers and sections.

```bash
cargo readobj -- -h <ELF_FILE>
cargo readobj -- -S <ELF_FILE>
```

```bash
cargo objdump -- -h <ELF_FILE>
```

## ELF (Executable and Linkable Format) File Structure

ELF File  
  ├─ ELF header&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Contains Metadata about the file)  
  ├─ Program Header (Provide information about the segments that need to be  
  │&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;loaded into memory for the program run correctly)  
  ├─ Sections  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .text&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Executable code)  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .data&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Initialized data)  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .bss&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Uninitialized data)  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .rodata&nbsp;&nbsp;&nbsp;(Read-Only data)  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .symtab&nbsp;&nbsp;(Symbol table)  
  │&nbsp;&nbsp;&nbsp;&nbsp;├─ .debug&nbsp;&nbsp;&nbsp;&nbsp;(Debugging information for debuggers like GDB)  
  │&nbsp;&nbsp;&nbsp;&nbsp;└─ .strtab&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(String table)  
  └─ Section header table (Describe sections within the file)  

## Setup Cargo Environment:

At the project's root, create file and directory structure as follows:

```bash
mkdir -p .cargo && touch .cargo/config.toml
```

In the file create this template.

```toml
[build]
target = "thumbv7em-none-eabihf" # Specify the target architecture

[target.thumbv7em-none-eabihf]
#linker = "arm-none-eabi-ld"  # Uncomment if you want to use a custom linker
rustflags = [
    "-C", "link-arg=-Tlinker.ld",  # Linker script
    "-C", "link-arg=-Map=output.map", # Map file for debugging
    "-C", "link-arg=-L./lib", # Additional library path
]
```
This will set the target architecture and specify the linker script and additional flags for the build process.

## Create Linker Script

On the projec's root level create the file: *linker.ld*  
**Note:** this can be any name but must be the same in the *config.toml*

The linker script defines the memory layout of the target device. Here is a basic example for an ARM Cortex-M target:
[linker.ld](../linker.ld)  

