var express = require("express"),
app = express(),
bodyparser = require("body-parser"),
mongoose = require("mongoose");
var MongoClient = require('mongodb').MongoClient;

const uri = "mongodb://mongodb:27017/grade";
const client = new MongoClient(uri);
const database = client.db("grade")
const grades = database.collection("grade")

app.use(bodyparser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", function (req, res) {
    res.render("index",{ allgrades: null })
})

app.get("/getgrades", function (req, res) {   
    var allgrades = grades.find()
    console.log(allgrades)

    if ((allgrades.count()) === 0) {
        console.log("No documents found!");
      } else {
        res.render("index", { allgrades: allgrades })
      }        
    }
)

app.listen(3000, () => console.log("listening on http://localhost:3000"))
