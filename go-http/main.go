package main

import (
	"net/http"
)

func ServerEcho(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte{'e', 'c', 'h', 'o'})
}

func main() {
	mux := http.NewServeMux()
	mux.Handle("/echo", http.HandlerFunc(ServerEcho))
	http.ListenAndServe(":5000", mux)
}