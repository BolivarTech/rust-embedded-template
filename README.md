# Rust Embedded Template

This project provides a minimal template for starting a `#![no_std]` Rust embedded application. It is designed to be a starting point for bare-metal or embedded development without the Rust standard library.

## Features

- `#![no_std]` and `#![no_main]` setup
- Custom entry point (`_start`)
- Minimal panic handler
- Ready for further embedded development

## Usage

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

## File Structure

- `src/main.rs` — Main entry point and panic handler
- `Cargo.toml` — Project configuration

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.