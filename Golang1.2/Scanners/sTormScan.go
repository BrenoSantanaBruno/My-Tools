package main

import (
	"flag"
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	host := flag.String("host", "localhost", "host a ser verificado")
	sleepTime := flag.Int("sleep", 10, "tempo de atraso entre as verificações de portas, em segundos")

	flag.Parse()

	file, err := os.Create("portas_abertas.txt")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Não foi possível criar o arquivo: %v\n", err)
		os.Exit(1)
	}
	defer file.Close()

	for i := 1; i <= 1024; i++ {
		address := fmt.Sprintf("%s:%d", *host, i)
		conn, err := net.DialTimeout("tcp", address, 60*time.Second)

		if err != nil {
			fmt.Printf("A porta %d está fechada no host %s\n", i, *host)
		} else {
			conn.Close()
			fmt.Printf("A porta %d está aberta no host %s\n", i, *host)
			fmt.Fprintf(file, "A porta %d está aberta no host %s\n", i, *host)
		}

		time.Sleep(time.Duration(*sleepTime) * time.Second) // Dorme pelo tempo especificado.
	}
}
