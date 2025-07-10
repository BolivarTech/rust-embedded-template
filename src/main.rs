#![no_std]
#![cfg_attr(test, no_main)]
#![no_main]

mod startup_stm32g431;

use core::panic::PanicInfo;

#[no_mangle]
pub extern "C" fn main() -> ! {

    loop{
    }
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {

    loop {
    }
}
