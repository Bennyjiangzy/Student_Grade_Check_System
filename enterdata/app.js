const express = require('express')
const path = require('path');
const XMLHttpRequest = require('xhr2');

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
    const url = "http://bk-lb:8080/user"
    var xhr = new XMLHttpRequest();
    // asynchronous requests
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(req.body));
    res.status(200).redirect('/login')
  })

app.post('/get', function (req, res) {

  console.log(req.body)
  const url = "http://bk-lb:8080/usernamepass"
  var xhr = new XMLHttpRequest();
  // asynchronous requests
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      if (xhr.status == 201 || xhr.status == 200){
        console.log("login succeed, redirecting to ordering page");
    
        res.redirect('/grades')
      }
    }
};
  xhr.send(JSON.stringify(req.body));
})


app.post('/savegrade', function (req, res) {

  console.log(req.body)
  dataToSend = {"studentID": req.body.studentID,
                  "name": req.body.name,
                  "grade": Number(req.body.grade)}
  var xhr = new XMLHttpRequest();
  // asynchronous requests
  xhr.open("POST", "http://bk-lb:8090/grade", true);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  // Send the request over the network
  xhr.send(JSON.stringify(dataToSend));
})

app.get("/grades", (req, res) => {
    res.sendFile(path.join(__dirname,"public/views/base.html"))
})

app.listen(8091, () => console.log("listening on http://localhost:8091"))

module.exports = app;