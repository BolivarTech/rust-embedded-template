#![no_std]
#![no_main]
#![cfg_attr(test, no_main)]


mod startup_stm32g431;

use core::panic::PanicInfo;

#[no_mangle]
pub extern "C" fn main() -> ! {
    let mut i = 0;
    loop{
        // Increment the counter
        i += 1;

        // Check if the counter has reached a certain value
        if i == 10 {
            // Reset the counter
            i = 0;
        }

        // Optionally, you could add a delay here to slow down the loop
        // For example, using a busy-wait loop or a delay function
    }
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {

    loop {
    }
}
