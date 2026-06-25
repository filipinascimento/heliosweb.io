#!/usr/bin/env node
import { createServer } from 'node:http';
import { createReadStream, existsSync, mkdirSync } from 'node:fs';
import { readFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('../../helios-web-next/node_modules/playwright');
const { PNG } = require('../../helios-web-next/node_modules/pngjs');

const DOCS_SITE = path.resolve(fileURLToPath(new URL('..', import.meta.url)));
const SITE_DIR = path.join(DOCS_SITE, 'site');
const OUTPUT_DIR = path.join(DOCS_SITE, 'output', 'playwright');
const TARGETS = [
  { id: 'basic-rendering', path: '/examples/helios-web/basic/', bodyName: 'helios_web_basic_rendering' },
  { id: 'loading-building', path: '/examples/helios-web/attributes-mappers/', bodyName: 'helios_web_loading_building' },
  { id: 'mappers-legends', path: '/examples/helios-web/attributes-mappers/', bodyName: 'helios_web_mappers_legends' },
  { id: 'selection-hover-labels', path: '/examples/helios-web/interaction-labels/', bodyName: 'helios_web_selection_labels' },
  { id: 'layouts', path: '/examples/helios-web/layouts-filters/', bodyName: 'helios_web_layouts' },
  { id: 'filters', path: '/examples/helios-web/layouts-filters/', bodyName: 'helios_web_filters' },
  { id: 'advanced-filter', path: '/examples/helios-web/advanced-apis/', bodyName: 'helios_web_advanced_filter' },
  { id: 'persistence-save-restore', path: '/examples/helios-web/persistence-export/', bodyName: 'helios_web_persistence' },
  { id: 'exporter-figure-output', path: '/examples/helios-web/persistence-export/', bodyName: 'helios_web_exporter' },
  { id: 'mobile-touch', path: '/examples/helios-web/mobile-custom/', bodyName: 'helios_web_mobile_touch' },
  { id: 'custom-behavior', path: '/examples/helios-web/mobile-custom/', bodyName: 'helios_web_custom_behavior' },
];

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.map': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.wasm': 'application/wasm',
};

function resolveRequestPath(url) {
  const parsed = new URL(url, 'http://127.0.0.1');
  let pathname = decodeURIComponent(parsed.pathname);
  if (pathname.endsWith('/')) pathname += 'index.html';
  const candidate = path.normalize(path.join(SITE_DIR, pathname));
  if (!candidate.startsWith(SITE_DIR)) return null;
  if (existsSync(candidate)) return candidate;
  const asDirectoryIndex = path.join(candidate, 'index.html');
  return existsSync(asDirectoryIndex) ? asDirectoryIndex : null;
}

function createStaticServer() {
  return createServer((request, response) => {
    const filePath = resolveRequestPath(request.url ?? '/');
    if (!filePath) {
      response.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
      response.end('not found');
      return;
    }
    const contentType = MIME_TYPES[path.extname(filePath)] ?? 'application/octet-stream';
    response.writeHead(200, { 'content-type': contentType });
    createReadStream(filePath).pipe(response);
  });
}

function listen(server) {
  return new Promise((resolve) => {
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      resolve(`http://127.0.0.1:${address.port}`);
    });
  });
}

function closeServer(server) {
  return new Promise((resolve, reject) => {
    server.close((error) => (error ? reject(error) : resolve()));
  });
}

async function assertNonBlankPng(filePath, label) {
  const png = PNG.sync.read(await readFile(filePath));
  const corner = [
    png.data[0],
    png.data[1],
    png.data[2],
  ];
  let visiblePixels = 0;
  let variedPixels = 0;
  for (let offset = 0; offset < png.data.length; offset += 4) {
    const alpha = png.data[offset + 3];
    if (alpha > 8) visiblePixels += 1;
    const delta = Math.abs(png.data[offset] - corner[0])
      + Math.abs(png.data[offset + 1] - corner[1])
      + Math.abs(png.data[offset + 2] - corner[2]);
    if (alpha > 8 && delta > 30) variedPixels += 1;
  }
  if (visiblePixels < 1000 || variedPixels < 80) {
    throw new Error(`${label} screenshot appears blank: ${visiblePixels} visible pixels, ${variedPixels} varied pixels`);
  }
}

async function main() {
  if (!existsSync(path.join(SITE_DIR, 'index.html'))) {
    throw new Error('Build docs-site first with `python3 scripts/build_docs.py`.');
  }
  mkdirSync(OUTPUT_DIR, { recursive: true });

  const server = createStaticServer();
  const baseUrl = await listen(server);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
  const failures = [];
  page.on('pageerror', (error) => failures.push(error.message));
  page.on('console', (message) => {
    if (message.type() !== 'error') return;
    const text = message.text();
    if (text.startsWith('Failed to load resource:')) return;
    failures.push(text);
  });

  try {
    for (const target of TARGETS) {
      const url = `${baseUrl}${target.path}`;
      console.log(`checking ${target.id}`);
      const response = await page.goto(url, { waitUntil: 'domcontentloaded' });
      if (!response?.ok()) {
        throw new Error(`Failed to load ${target.path}: HTTP ${response?.status() ?? 'unknown'}`);
      }
      await page.locator('.mkdocs-sidecode-page-data').waitFor({ state: 'attached', timeout: 30000 });
      const exampleIdsByBodyName = await page.$eval('.mkdocs-sidecode-page-data', (node) => {
        const rawText = node.tagName === 'TEMPLATE'
          ? node.content.textContent
          : node.textContent;
        const text = rawText?.trim();
        if (!text) throw new Error('Sidecode page data is empty.');
        const payload = JSON.parse(text);
        return Object.fromEntries((payload.examples || []).map((example) => [example.bodyName, example.id]));
      });
      const exampleId = exampleIdsByBodyName[target.bodyName];
      if (!exampleId) {
        throw new Error(`Could not find sidecode example bodyName "${target.bodyName}" on ${target.path}.`);
      }
      const stageSelector = `[data-sidecode-example="${exampleId}"] [data-role="render"]`;
      const stage = page.locator(stageSelector).first();
      await stage.waitFor({ state: 'visible', timeout: 45000 });
      await page.evaluate((selector) => {
        document.querySelector(selector)?.scrollIntoView({ block: 'center' });
      }, stageSelector);
      const canvas = stage.locator('canvas').first();
      await canvas.waitFor({ state: 'visible', timeout: 45000 });
      await page.waitForTimeout(900);
      const screenshot = path.join(OUTPUT_DIR, `${target.id}.png`);
      const bounds = await canvas.boundingBox();
      if (!bounds) {
        throw new Error(`Could not resolve canvas bounds for ${target.id}.`);
      }
      await page.screenshot({ path: screenshot, clip: bounds });
      await assertNonBlankPng(screenshot, target.id);
      console.log(`validated ${target.id}`);
    }

    if (failures.length) {
      throw new Error(`Browser console/page errors:\n${failures.join('\n')}`);
    }
  } finally {
    await browser.close();
    await closeServer(server);
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
