#!/usr/bin/env node
// Renders the Little Lilies document sources to A4 PDFs in public/docs.
//
// The sources are plain HTML using doc-styles.css and @page A4. They are
// rendered through headless Chrome, which is the only engine here that honours
// print-color-adjust and mm page boxes faithfully.
//
//   node scripts/render-docs.mjs
//
// Documents still carrying .gate markers render with their dashed UNCONFIRMED
// bands intact — that is deliberate. Nothing is published to parents until the
// school has signed the figures off and the markers are removed.

import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { mkdir, access } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, resolve, join } from 'node:path';

const exec = promisify(execFile);
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const outDir = join(root, 'public', 'docs');

const CHROME_CANDIDATES = [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
];

const DOCS = [
  ['prospectus-source.html',    'little-lilies-prospectus.pdf'],
  ['doc-enrolment-source.html', 'enrolment-form.pdf'],
  ['doc-consent-source.html',   'medical-consent-form.pdf'],
  ['doc-fees-source.html',      'fee-sheet.pdf'],
  ['doc-handbook-source.html',  'parent-handbook.pdf'],
];

async function findChrome() {
  for (const p of CHROME_CANDIDATES) {
    try { await access(p); return p; } catch { /* keep looking */ }
  }
  throw new Error('No Chrome/Chromium/Edge binary found. Install one, or add its path to CHROME_CANDIDATES.');
}

const chrome = await findChrome();
await mkdir(outDir, { recursive: true });

for (const [src, out] of DOCS) {
  const target = join(outDir, out);
  await exec(chrome, [
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--virtual-time-budget=10000',   // let webfonts land before the snapshot
    `--print-to-pdf=${target}`,
    `file://${join(root, src)}`,
  ]);
  console.log(`  ${src.padEnd(28)} -> public/docs/${out}`);
}

console.log(`\n${DOCS.length} documents rendered.`);
