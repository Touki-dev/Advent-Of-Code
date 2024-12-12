import puppeteer from 'puppeteer';
import { writeFile } from 'fs/promises';
import { mkdir } from 'fs/promises';
import session from './session-value.json' assert { type: 'json' };

const n = 10;

async function createFile(folderPath, name, n, data) {
  try {
    folderPath = folderPath + n;
    await mkdir(folderPath);

    filePath = folderPath + name;

    await writeFile(filePath, result, 'utf8');
    console.log(`Fichier créé avec succès : ${filePath}`);
  } catch (err) {
    console.error('Erreur lors de la création du fichier :', err);
  }
}

await (async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });
  const page = await browser.newPage();
  
  // Create example
  await page.goto('https://adventofcode.com/2024/day/' + n);

  const example = await page.evaluate(() => document.querySelector('pre code').textContent);
  await createFile('/Users/macdegaspard/Desktop/Python/Advent Of Code/2024/Day', '/example.txt', n, example)
  
  const cookie = {
    "domain":".adventofcode.com",
    "expirationDate":1767462807.710037,
    "hostOnly":false,
    "httpOnly":true,
    "name":"session",
    "path":"/",
    "sameSite":"unspecified",
    "secure":true,
    "session":false,
    "storeId":"0",
    "value":session.value
  }

  await page.setCookie(cookie);
  
  await page.goto('https://adventofcode.com/2024/day' + n + '/input');
  const input = await page.evaluate(() => document.querySelector('pre').textContent);
  console.log(input)
  // await browser.close();
})();