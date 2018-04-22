const http = require('http');

var svr = new http.Server(5000, (req) => {
    req.response.write('echo');
});

svr.run();