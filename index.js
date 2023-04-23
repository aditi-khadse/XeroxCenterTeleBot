const path = require("path");
const express = require("express");
const multer = require("multer");
const mongoose = require("mongoose");

const app = express();
const PORT = 8000;

// const upload = multer({ dest: 'uploads/' });
//Ye uploads folder ko direct kar dega

// Server both the files
app.use(express.static("views")); //Ye karna reh gaya tha
app.use(express.static("images"));

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    return cb(null, "./uploads");
  },
  filename: function (req, file, cb) {
    return cb(null, `${Date.now()}-${file.originalname}`);
  },
});

const upload = multer({ storage });

mongoose
  .connect(
    "mongodb+srv://TelegramXeroxCenter:EC7KO1SYmJR9Q8DW@cluster0.ga4tmpi.mongodb.net/test",
    { useNewUrlParser: true, useUnifiedTopology: true }
  )
  .then(() => {
    console.log("Connected to database");
  })
  .catch((err) => {
    console.log(err, " not connected");
  });

app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  return res.sendFile(path.resolve("../OnTips/views/index.html"));
});

app.post("/upload", upload.single("pdfUploaded"), (req, res) => {
  console.log(req.body);
  console.log(req.file);

  return res.redirect("/");
});

app.set("views", path.resolve("../OnTips/views"));

app.use(express.json());

app.get("/", (req, res) => {
  return res.render("index");
});

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});
