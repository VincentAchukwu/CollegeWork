public class Word{

	public static boolean isFirstLetter(String s, char c){
		return s.charAt(0) == c;
	}

	public static boolean containsLetter(String s, char c){
		return s.indexOf(c) != -1;	//one way of doing it..
	}

	public static boolean containsLetter1(String word, char letter){
		boolean check = false;
		for(int i = 0; i < word.length(); i++){
			if(word.charAt(i) == letter){
				return true;
			}
		}
		return false;
	}

	public static boolean allDone(String word, String guess){
		for(int i = 0; i < word.length(); i++){
			boolean check = Word.containsLetter1(guess, word.charAt(i));
			if (check == false){
				return false;
			}
		}
		return true;
	}

	public static String showLetter(String word, char guess){
		String updated = "";
		for(int i = 0; i < word.length(); i++){
			updated = updated + "_";
		}
		for(int j = 0; j < word.length(); j++){
			if(word.charAt(j) == guess){
				updated = updated.substring(0,j) + guess + updated.substring(j + 1);
			}
		}
		return updated;
	}

	public static String showLetters(String word, String guess){
		String updated = "";
		for(int j = 0; j < word.length(); j++){
			updated = updated + "_";
		}
		// assuming guess.length < word.length ...
		for(int i = 0; i < word.length(); i++){
			for(int j = 0; j < guess.length(); j++){
				if(word.charAt(i) == guess.charAt(j)){
					updated = updated.substring(0,i) + guess.charAt(j) + updated.substring(i + 1);
					}
			}
		}
		return updated;
	}
}
