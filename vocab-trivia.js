// Generate 5 words with at least four syllables that contain the same latin root
//
// Generate definition of one of them, user matches it with the correct word for points
//
//

let rootlinks = {"https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/A-G" : 7,
		 "https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/H-O" : 8,
	  	 "https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/P-Z" : 11};



/* W and Y are not included */
const randomLetter = (rootlinks) => {
	let index = Math.floor(Math.random() * rootlinks.length);
	rootlinks[index]
}

