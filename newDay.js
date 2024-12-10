import puppeteer from 'puppeteer';
import { writeFile } from 'fs/promises';
import { mkdir } from 'fs/promises';
const n = 10;

await (async () => {
  // Lance le navigateur en désactivant le mode "headless"
  const browser = await puppeteer.launch({
    headless: false, // Affiche le navigateur
    defaultViewport: null, // Utilise la taille par défaut de la fenêtre
  });
  const page = await browser.newPage();

  // Navigate the page to a URL
  await page.goto('https://adventofcode.com/2024/day/' + n);

  const result = await page.evaluate(() => {
    const example = document.querySelector('pre code')
    return example.textContent;
  });
  console.log(result);

  try {
    const folderPath = '2024/Day '+ n;
    // Créer le dossier s'il n'existe pas
    await mkdir(folderPath);

    const filePath = '2024/Day '+n+'/input.txt';

    await writeFile(filePath, result, 'utf8');
        console.log(`Fichier créé avec succès : ${filePath}`);
    } catch (err) {
        console.error('Erreur lors de la création du fichier :', err);
    }

  await browser.close();
})();