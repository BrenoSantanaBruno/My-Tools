package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func is_valid_ipv4(ip string) bool {
	parts := strings.Split(ip, ".")
	if len(parts) != 4 {
		return false
	}
	for _, part := range parts {
		var number int
		_, err := fmt.Sscanf(part, "%d", &number)
		if err != nil || number < 0 || number > 255 {
			return false
		}
	}
	return true
}

func get_ip() string {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("Digite o IP: ")
		ip, _ := reader.ReadString('\n')
		ip = strings.TrimSpace(ip)
		if is_valid_ipv4(ip) {
			return ip
		}
		fmt.Println("IP inválido. Tente novamente.")
	}
}

func get_service() (string, string) {
	services := map[string]string{
		"FTP":    "21",
		"SSH":    "22",
		"Telnet": "23",
		"SMTP":   "25",
		"DNS":    "53",
		"HTTP":   "80",
		"POP3":   "110",
		"IMAP":   "143",
		"HTTPS":  "443",
	}

	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Println("Escolha um serviço dos seguintes:")
		for service := range services {
			fmt.Println(service)
		}
		chosen_service, _ := reader.ReadString('\n')
		chosen_service = strings.TrimSpace(chosen_service)
		if port, ok := services[chosen_service]; ok {
			return chosen_service, port
		}
		fmt.Println("Serviço inválido. Tente novamente.")
	}
}

func main() {

	fmt.Println("Tock Tock Services Protocols")
	fmt.Println("============================")
	fmt.Println("DevStorm - Breno Santana/2023")
	fmt.Println("============================")

	service, port := get_service()
	fmt.Printf("Interagindo com o: %s\n", service)

	ip := get_ip()

	conn, err := net.Dial("tcp", ip+":"+port)
	if err != nil {
		fmt.Println("Erro na conexão:", err)
		return
	}
	defer conn.Close()

	buffer := make([]byte, 1024)
	conn.Read(buffer)
	fmt.Println("Banner recebido:", string(buffer))

	fmt.Printf("Enviando dados para %s Server - usuário\n", service)
	conn.Write([]byte("USER teste\r\n"))
	conn.Read(buffer)
	fmt.Println("Banner recebido:", string(buffer))

	fmt.Printf("Enviando dados para %s Server - senha\n", service)
	conn.Write([]byte("PASS teste\r\n"))
	conn.Read(buffer)
	fmt.Println("Banner recebido:", string(buffer))
}
