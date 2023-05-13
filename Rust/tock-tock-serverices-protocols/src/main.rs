use std::io::{self, Read, Write};
use std::net::TcpStream;
use std::str;

fn is_valid_ipv4(ip: &str) -> bool {
    let parts: Vec<&str> = ip.split('.').collect();
    if parts.len() != 4 {
        return false;
    }
    for part in parts {
        if let Ok(number) = part.parse::<u8>() {
            if number < 0 || number > 255 {
                return false;
            }
        } else {
            return false;
        }
    }
    true
}

fn get_ip() -> String {
    let stdin = io::stdin();
    loop {
        print!("Digite o IP: ");
        io::stdout().flush().unwrap();
        let mut ip = String::new();
        stdin.read_line(&mut ip).unwrap();
        let ip = ip.trim();
        if is_valid_ipv4(ip) {
            return ip.to_string();
        }
        println!("IP inválido. Tente novamente.");
    }
}

fn get_service() -> (&'static str, &'static str) {
    let services = [
        ("FTP", "21"),
        ("SSH", "22"),
        ("Telnet", "23"),
        ("SMTP", "25"),
        ("DNS", "53"),
        ("HTTP", "80"),
        ("POP3", "110"),
        ("IMAP", "143"),
        ("HTTPS", "443"),
    ];
    let stdin = io::stdin();
    loop {
        println!("Escolha um serviço dos seguintes:");
        for &(service, _) in &services {
            println!("{}", service);
        }
        let mut chosen_service = String::new();
        stdin.read_line(&mut chosen_service).unwrap();
        let chosen_service = chosen_service.trim();
        if let Some(&(service, port)) = services
            .iter()
            .find(|&(service, _)| *service == chosen_service)
        {
            return (service, port);
        } else {
        }
        println!("Serviço inválido. Tente novamente.");
    }
}

fn main() -> io::Result<()> {
    println!("Tock Tock Services Protocols");
    println!("============================");
    println!("DevStorm - Breno Santana/2023");
    println!("============================");

    let (service, port) = get_service();
    println!("Interagindo com o: {}", service);

    let ip = get_ip();

    let mut stream = TcpStream::connect(format!("{}:{}", ip, port))?;

    let mut buffer = [0; 1024];
    stream.read(&mut buffer)?;
    println!(
        "Banner recebido: {}",
        str::from_utf8(&buffer)
            .unwrap()
            .trim_end_matches(char::from(0))
    );

    println!("Enviando dados para {} Server - usuário", service);
    stream.write_all(b"USER teste\r\n")?;
    stream.read(&mut buffer)?;
    println!(
        "Banner recebido: {}",
        str::from_utf8(&buffer)
            .unwrap()
            .trim_end_matches(char::from(0))
    );

    println!("Enviando dados para {} Server - senha", service);
    stream.write_all(b"PASS teste\r\n")?;
    stream.read(&mut buffer)?;
    println!(
        "Banner recebido: {}",
        str::from_utf8(&buffer)
            .unwrap()
            .trim_end_matches(char::from(0))
    );

    Ok(())
}
