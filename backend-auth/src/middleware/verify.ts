import { auth } from "../auth";

export async function verify(req: any, res: any, next: any) {
  try {
    const session = await auth.api.getSession({
      headers: req.headers
    });
    req.user = session.user;
    next();
  } catch {
    res.status(401).json({ error: "Unauthorized" });
  }
}
