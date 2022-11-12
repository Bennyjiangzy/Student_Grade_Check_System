var express = require("express");
var bodyparser = require("body-parser");
var MongoClient = require('mongodb').MongoClient;
const path = require('path');
const XMLHttpRequest = require('xhr2');

const uri = "mongodb://bk-lb:27017";


const app = express()
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyparser.urlencoded({ extended: true }));
app.set("view engine", "ejs");


app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname,"/public/views/login.html"))
 
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


const get = { grades: async () =>{
  const client = await new MongoClient(uri);
  try{
    const database = client.db("test")
    const grades = database.collection("grade")
    const test = {last_updated:-1}
    let allgrades = await grades.find().sort(test).toArray()
    return allgrades
  }
  catch{
    console.log(err)
  }
}}

app.get("/grades", function (req, res) {
  res.render("grade", { allgrades: null })
})

app.get("/getgrades", async function (req, res) {   
  let test=await get.grades()
  console.log(test)
  res.render("grade", { allgrades: test })    
})


app.listen(3000, () => console.log("listening on http://localhost:3000"))
