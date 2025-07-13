# Rust Embedded Template

This project provides a minimal template for starting a `#![no_std]` Rust embedded application. It is designed to be a
starting point for bare-metal or embedded development without the Rust standard library.

## Directory and Files Structures

├── cpp_src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Optional C/C++ source files (if needed)  
├── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Rust source files  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── main.rs&nbsp;&nbsp;&nbsp;&nbsp;# Main entry point with custom _start function and panic handler  
├── Cargo.toml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Project configuration and dependencies  
├── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# This file  
└── LICENSE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# MIT License file  

## Features

- Basic project structure for Rust embedded applications
- `#![no_std]` and `#![no_main]` setup
- Minimal panic handler
- Ready for further embedded development
- Optional C/C++ source files support

This template implements a memory allocator using the low-stack allocation strategy, which is suitable for embedded systems 
to prevent stack overflow issues, because the stack is allocated at the beginning of the RAM and grows downwards; if the
stack grows too large, it will reach the lowe RAM address, and if try to write bellow that address, it will cause an 
application panic and trigger the *HardFault_Handler*.

This estragy is implemented in the linker script [linker_low_stack.ld](./linker_low_stack.ld) and in the 
[startup_stm32g431.rs](./src/startup_stm32g431.rs) file.  

## Usage

To use this template, follow these steps:

### Use Cargo Generate

This is the recommended way to create a new project based on this template. It allows you to quickly scaffold a new Rust
embedded project with the necessary files and structure.

1. **Install `cargo-generate`:**
   If you haven't already, install `cargo-generate`:
   ```bash
   cargo install cargo-generate
   ```
2. **Generate a new project:**
   ````bash
   cargo generate --git https://github.com/BolivarTech/rust-embedded-template.git --name myproject

   ````

### Clone Git Repository

If you prefer to clone the repository directly, you can do so. This method is useful if you want to explore the code or
make modifications before starting your own project.

1. **Clone the repository:**
   ```
   git clone https://github.com/BolivarTech/rust-embedded-template.git
   cd rust-embedded-template
   ```

2. **Build the project:**
   ```
   cargo build
   ```

   > **Note:** Running `cargo test` is not supported in `#![no_std]` projects.

3. **Flash or run on your target hardware**  
   (Refer to your hardware or emulator documentation for details.)

## Documentation

For more detailed information on how to set up and use this template, refer to the [How-to Guide](doc/howto_detailed_setup.md).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.