package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, `Uso: %s host
`, os.Args[0])
		os.Exit(1)
	}

	host := os.Args[1]

	for i := 1; i <= 65535; i++ {
		address := fmt.Sprintf("%s:%d", host, i)
		conn, err := net.DialTimeout("tcp", address, 60*time.Second)

		if err != nil {
			//fmt.Sprintf("A porta #{i} está fechada ou filtrada.")
			continue
		}

		conn.Close()
		fmt.Printf("A porta %d está aberta no host %s\n", i, host)
	}
}
