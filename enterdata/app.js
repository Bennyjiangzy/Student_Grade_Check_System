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

app.post('/redirect', function (req, res) {
    console.log(req.body)
    res.redirect('/login')
  })

app.post('/get', function (req, res) {
    console.log(req.body)
    res.redirect('/grades')
  })

app.get("/grades", (req, res) => {
    res.sendFile(path.join(__dirname,"public/views/base.html"))
})

app.listen(8091, () => console.log("listening on http:localhost:8091"))

module.exports = app;