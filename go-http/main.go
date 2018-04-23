package main

import (
	"net/http"
	"runtime"
)

func ServerEcho(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte{'e', 'c', 'h', 'o'})
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	mux := http.NewServeMux()
	mux.Handle("/echo", http.HandlerFunc(ServerEcho))
	http.ListenAndServe(":5000", mux)
}
