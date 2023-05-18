#![allow(unused)]

use std::io;
use rand::Rng;
use std::cmp::Ordering;


fn main(){
//Create a calculator that takes three user inputs (x, y, and operator)
// Createfunction for +, -, *, /, and % (modulus)
//Use if/else or Match for Operator
//Might take a little research!

//Opening Lines
    println!("Breno's Rust Calculator");
    println!("You must select two values (x and y) and an operator (+, -, *, /, %)");

    //Receive a value for x
    println!("Please enter a value for x: ");

    let mut x:String = String::new();
    io::stdin().read_line(&mut x).expect("Failed to read line");
    let x:i32 = x.trim().parse().expect("Please type a number!");
    let float_x:f64 = x as f64;

    //Receive a value for y
    println!("Please enter a value for y: ");

    let mut y:String = String::new();
    io::stdin().read_line(&mut y).expect("Failed to read line");
    let y:i32 = y.trim().parse().expect("Please type a number!");
    let float_y:f64 = y as f64;
// add(x,y);
// subtract(x,y);
// multiply(x,y);
// divide(float_x,float_y);
// module(x, y);


//Receive an operator
    println!("Please enter an operator (+, -, *, /, %): ");
    let mut operator: String = String::new();
    io::stdin().read_line(&mut operator);
    let operator_slice: &str = operator.trim();

    //Match Operator
    match operator_slice{
        "+" => {
            add(x, y);
        }
        "-" => {
            subtract(x, y);
        }
        "*" => {
            multiply(x, y);
        }
        "/" => {
            divide(float_x,float_y);
        }
        "%" => {
            module(x, y);
        }
        &_ => {
            println!("Please enter a valid operator (+, -, *, /, %)");
        }
    }
}



fn add(x:i32 , y:i32)  {
    println!("The result of {} + {} = {}", x, y, x + y);
}
fn subtract(x:i32 , y:i32)  {
    println!("The result of {} - {} = {}", x, y, x - y);
}
fn multiply(x:i32 , y:i32)  {
    println!("The result of {} * {} = {}", x, y, x * y);
}
fn divide(x:f64 , y:f64)  {
    println!("The result of {} / {} = {}", x, y, x / y);
}
fn module(x:i32 , y:i32)  {
    println!("The result of {} % {} = {}", x, y, x % y);
}