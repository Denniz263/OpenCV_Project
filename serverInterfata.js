const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 5000;
const RECORDINGS_DIR = path.join(__dirname, "recordings");
const PUBLIC_DIR = path.join(__dirname, "public");

const mimeTypes = {
    ".html": "text/html",
    ".mp4": "video/mp4",
    ".js": "text/javascript",
    ".css": "text/css",
};

const server = http.createServer((req, res) => {

    // API - get list of recordings
    if (req.url === "/api/recordings") {
        fs.readdir(RECORDINGS_DIR, (err, files) => {
            if (err) files = [];
            const mp4s = files.filter(f => f.endsWith(".mp4")).reverse();
            res.writeHead(200, { "Content-Type": "application/json" });
            res.end(JSON.stringify(mp4s));
        });
        return;
    }

    // Serve video files
    if (req.url.startsWith("/recordings/")) {
        const filename = path.basename(req.url);
        const filepath = path.join(RECORDINGS_DIR, filename);
        fs.stat(filepath, (err, stat) => {
            if (err) {
                res.writeHead(404);
                res.end("Not found");
                return;
            }
            res.writeHead(200, {
                "Content-Type": "video/mp4",
                "Content-Length": stat.size,
            });
            fs.createReadStream(filepath).pipe(res);
        });
        return;
    }

    // Serve static files from public/
    let filePath = path.join(PUBLIC_DIR, req.url === "/" ? "index.html" : req.url);
    fs.readFile(filePath, (err, data) => {
        if (err) {
            res.writeHead(404);
            res.end("Not found");
            return;
        }
        const ext = path.extname(filePath);
        res.writeHead(200, { "Content-Type": mimeTypes[ext] || "text/plain" });
        res.end(data);
    });
});

server.listen(PORT, "0.0.0.0", () => {
    console.log(`Dashboard running at http://localhost:${PORT}`);
});