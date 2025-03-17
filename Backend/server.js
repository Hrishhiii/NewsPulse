// require("dotenv").config();
// const express = require("express");
// const mongoose = require("mongoose");
// const cors = require("cors");

// const app = express();
// const PORT = process.env.PORT || 5000;

// // Middleware
// app.use(cors());
// app.use(express.json());

// // MongoDB Connection
// mongoose
//   .connect(process.env.MONGO_URI, {
//     useNewUrlParser: true,
//     useUnifiedTopology: true,
//   })
//   .then(() => console.log("MongoDB Connected"))
//   .catch((err) => console.error("MongoDB connection error:", err));

// // Define News Schema & Model
// const newsSchema = new mongoose.Schema({
//   headline: String,
//   author: String,
//   published_date: String,
//   summary: String,
//   content: String,
//   image_url: String,
//   source_link: String,
// });

// const News = mongoose.model("articles", newsSchema);

// // API Route to Fetch All News
// app.get("/news", async (req, res) => {
//   try {
//     const newsData = await News.find();
//     res.json(newsData);
//   } catch (error) {
//     res.status(500).json({ message: "Error fetching news", error });
//   }
// });

// // Start Server
// app.listen(PORT, () => console.log(`Server running on port ${PORT}`));


require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const cron = require("node-cron");
const { exec } = require("child_process");

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose
  .connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB Connected"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Define News Schema & Model
const newsSchema = new mongoose.Schema({
  headline: String,
  author: String,
  published_date: String,
  summary: String,
  content: String,
  image_url: String,
  source_link: String,
});

const News = mongoose.model("articles", newsSchema);

// API Route to Fetch All News
app.get("/news", async (req, res) => {
  try {
    const newsData = await News.find();
    res.json(newsData);
  } catch (error) {
    res.status(500).json({ message: "Error fetching news", error });
  }
});

const runPythonScraper = async () => {
  try {
    // Delete all previous articles before scraping**
    await News.deleteMany({});
    console.log("Deleted old news articles.");

    // Run the web scraper
    exec("python Web_Scraper.py", (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Python script: ${error.message}`);
        return;
      }
      if (stderr) {
        console.error(`Python script stderr: ${stderr}`);
        return;
      }
      console.log(`Python script output:\n${stdout}`);
    });
  } catch (err) {
    console.error("Error deleting old articles:", err);
  }
}


cron.schedule("0 */3 * * *", async () => {
  console.log("Running Python web scraper...");
  runPythonScraper();
});

runPythonScraper();
// Start Server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

