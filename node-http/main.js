const http = require("http");

const server = new http.Server();

server.on("request", function (req, res) {
	if (req.url === "/echo") {
		res.end("echo");
	} else {
		res.end("404")
	}
})
server.listen(5000);
