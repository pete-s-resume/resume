const express = require("express")
const mongoose = require("mongoose")

const userRoute = require('./route/userRoute')

const app = express();
const uri = "mongodb+srv://poomipas9:suppessx@cluster0.suanhmg.mongodb.net/?retryWrites=true&w=majority"
const connect = async() =>{
    try{
        await mongoose.connect(uri,
        {
            useNewUrlParser:true,
            useUnifiedTopology:true
        })
        console.log("Connected to MongoDB")
    }catch(err){
        console.log("Database  has Problem")
        console.log(err)
    }
} 

connect();

app.use(express.json());
app.use("/user",userRoute);

app.listen(8000, () => {
    console.log("Server is running on port 8000")
})