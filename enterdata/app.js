const express = require('express')
const path = require('path');

const app = express()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/login", (req, res) => {
    res.sendFile(path.join(__dirname,"public/views/login.html"))
})

app.get("/register", (req, res) => {
    res.sendFile(path.join(__dirname,"public/views/register.html"))
})

app.get("/grades", (req, res) => {
    res.sendFile(path.join(__dirname,"public/views/base.html"))
})

app.listen(8091, () => console.log("listening on port http://localhost:8091"))

module.exports = app;