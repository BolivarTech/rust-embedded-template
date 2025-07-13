#![no_std]
#![no_main]
#![cfg_attr(test, no_main)]


mod startup_stm32g431;

use core::panic::PanicInfo;

fn test(mut i: i32, limit: i32) -> i32 {

    i += 1;
    if (limit < 0) || (i < limit) {
        return test(i, limit)
    }
    i
}

#[no_mangle]
pub extern "C" fn main() -> ! {
    static mut I: i32 = 0;

    static Arreglo: [u32;5] = [1,2,3,4,5];

    let _Message = "Hello, World!";

    let r = test(0,30);  // To test Stack Overflow

    unsafe { I = r; }

    loop{
        unsafe {
            // Increment the counter
            I += 1;

            // Check if the counter has reached a certain value
            if I > 10 {
                // Reset the counter
                I = 0;
            }
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
