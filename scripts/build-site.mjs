import { cp, mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const output = path.join(root, "dist");
const loungePattern = /^lounge-0[1-9]-[a-z0-9-]+$/;

await rm(output, { recursive: true, force: true });
await cp(path.join(root, "interface"), output, { recursive: true });

const entries = await readdir(root, { withFileTypes: true });
for (const entry of entries) {
  if (!entry.isDirectory() || !loungePattern.test(entry.name)) continue;

  const source = path.join(root, entry.name, "README.md");
  const destinationDirectory = path.join(output, entry.name);
  const guide = await readFile(source, "utf8");
  await mkdir(destinationDirectory, { recursive: true });
  await writeFile(path.join(destinationDirectory, "README.md"), guide, "utf8");
}