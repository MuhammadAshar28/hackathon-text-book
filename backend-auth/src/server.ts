import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import authRoutes from "./routes/auth.routes";

dotenv.config();

const app = express();

app.use(cors({
  origin: process.env.BETTER_AUTH_URL || "http://localhost:3000",
  credentials: true
}));

app.use(express.json());
app.use("/auth", authRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Auth server running on http://localhost:${PORT}`);
});
