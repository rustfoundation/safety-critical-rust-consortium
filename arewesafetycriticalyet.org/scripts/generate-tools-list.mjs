import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import YAML from 'yaml';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const siteRoot = path.resolve(__dirname, '..');

const inputPath = path.resolve(
  siteRoot,
  '..',
  'subcommittee',
  'tooling',
  'tool-list',
  'available-tools.yaml',
);

const outputDir = path.resolve(siteRoot, 'src', 'generated');
const outputPath = path.resolve(outputDir, 'toolsList.ts');

function assertHas(obj, key) {
  if (obj == null || typeof obj !== 'object' || !(key in obj)) {
    throw new Error(`Expected tools list to contain key: ${key}`);
  }
}

const yamlText = await fs.readFile(inputPath, 'utf8');
const data = YAML.parse(yamlText);

assertHas(data, 'metadata');
assertHas(data, 'tools');
assertHas(data, 'open-topics');

await fs.mkdir(outputDir, {recursive: true});

const output = `/*
 * This file is auto-generated.
 * Source: ${path.relative(siteRoot, inputPath)}
 * Script: scripts/generate-tools-list.mjs
 */

const toolsList = ${JSON.stringify(data, null, 2)} as const;

export default toolsList;
`;

await fs.writeFile(outputPath, output, 'utf8');

console.log(
  `Generated ${path.relative(siteRoot, outputPath)} from ${path.relative(
    siteRoot,
    inputPath,
  )}`,
);
