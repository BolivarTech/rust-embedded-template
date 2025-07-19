#![no_std]
#![no_main]

use core::panic::PanicInfo;
use core::ffi;
//use rtt_target::{debug_rtt_init_print, debug_rprintln};



//use panic_halt as _; // Use panic_halt crate for minimal panic handler

const LED_GREEN: u32 = 0;

extern "C" {
    fn c_main_init();
    fn HAL_Delay(delay: ffi::c_uint);
    fn BSP_LED_Toggle(led: ffi::c_uint) -> ffi::c_int;
}


/// Entry point of the program.
///
/// Runs a loop that calls the recursive test function and checks the stack guard.
/// If the stack guard is corrupted, the loop breaks.
#[no_mangle]
extern "C" fn main() -> ! {
    unsafe {
        c_main_init();
    }
//    debug_rtt_init_print!(); // nop in --release
    loop{
        unsafe {
            _ = BSP_LED_Toggle(LED_GREEN);
//            debug_rprintln!("LED toggled"); // not present in --release
            HAL_Delay(500); // Delay 500 milliseconds
        }
    }
}

/// Panic handler for the program.
///
/// Loops forever on panic.
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
    }
}