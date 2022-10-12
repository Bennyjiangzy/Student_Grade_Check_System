var express = require("express"),
app = express(),
bodyparser = require("body-parser"),
mongoose = require("mongoose");
var MongoClient = require('mongodb').MongoClient;

const uri = "mongodb://mongodb:27017";


const get ={ grades: async () =>{
  const client = await new MongoClient(uri);
  
  try{
    const database = client.db("test")
    const grades = database.collection("grade")
    let allgrades = await grades.find().toArray()
    return allgrades
  }
  catch{
    console.log(err)
  }

}}
app.use(bodyparser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", function (req, res) {
    res.render("index",{ allgrades: null })
})

app.get("/getgrades", async function (req, res) {   
    let test=await get.grades()
    console.log(test)

    res.render("index", { allgrades: test })    
    }
)

app.listen(3000, () => console.log("listening on http://localhost:3000"))
