// Generate 5 words with at least four syllables that contain the same latin root
//
// Generate definition of one of them, user matches it with the correct word for points
//
//
import fetch from 'node-fetch';

const fetch = require('node-fetch');
const cheerio = require('cheerio');

let randomLetter = String.fromCharCode(Math.random() * (86 - 65 + 1) + 65);

/* Generate random letter to append to link to webscrape */
let rootLetterLink = "https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/" + randomLetter;

fetch(rootLetterLink, function(error, response, html) {
	if (error) {
		console.error('Error: ', error);
		return;
	}

	const $ = cheerio.load(html);
	const table = $(randomLetter);

	const rowCount = document.querySelectorAll('tbody tr').length;
	console.log(rowCount);
});
/* Scrape column for root */


/* Generate definition of root */


/* Generate definition of word */
