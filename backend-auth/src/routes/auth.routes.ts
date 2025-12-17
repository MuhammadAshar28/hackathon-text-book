import { Router } from "express";
import { auth } from "../auth";
import { prisma } from "../db";

const router = Router();

/**
 * SIGNUP
 */
router.post("/signup", async (req, res) => {
  const { name, email, password, softwareLevel, languages, hardwareLevel } = req.body;

  try {
    // Better Auth signup
    // The signInEmail/signUpEmail functions return a user object if successful.
    // However, since we want to attach extra data, we do it in steps.
    const result = await auth.api.signUpEmail({
      body: {
        name,
        email,
        password
      }
    });

    if (!result?.user) {
      throw new Error("User creation failed");
    }

    // Save background to Neon linked to the new user
    // The user record is created by Better Auth (via Prisma Adapter) in the 'user' table.
    // We just need to add the background record.
    await prisma.background.create({
      data: {
        userId: result.user.id,
        softwareLevel,
        languages,
        hardwareLevel
      }
    });

    res.json({ success: true, user: result.user });

  } catch (error: any) {
    console.error("Signup error:", error);
    res.status(400).json({ error: error.message || "Signup failed" });
  }
});

/**
 * SIGNIN
 */
router.post("/signin", async (req, res) => {
  const { email, password } = req.body;

  try {
    const session = await auth.api.signInEmail({
      body: { email, password }
    });
    res.json(session);
  } catch (error: any) {
    res.status(401).json({ error: error.message || "Invalid credentials" });
  }
});

export default router;
