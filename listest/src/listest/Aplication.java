package listest;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Aplication {

	public static void main(String[] args) {
		// list for names
		List<String> list = new ArrayList<>();
		
		//add
		list.add("monster"); //0
		list.add("purple"); //1
		list.add("antonio"); //5
		list.add("ramos"); //6
		list.add(2, "master"); //2
		list.add(3, "goku"); //3
		list.add(4, "vegeta"); //4
		//remove
		list.remove("antonio");
		list.remove("ramos");
		//remove using index
		list.remove(3);
		
		// print size
		System.out.println(list.size());
		
		// print one by one name using for each
		for(String nomes : list) {
			System.out.println(list);
		}
		
		// remove vegeta using predicate lambda
		list.removeIf(nomes -> nomes.charAt(0) == 'v'); // start index 0 and scroll untill last index for remove name start v in the list
		// print size list again
		System.out.println("---------------------------------");
		System.out.println(list.size());
		// print again list for confirm delete the vegeta
		for(String nomes : list) {
			System.out.println(list);
		}
		
		// found mauluzinha and most index, and to try found one name what dont exist in list
		System.out.println("---------------------------------");
		System.out.println("index of master | " + list.indexOf("master"));
		System.out.println("index of goku | " + list.indexOf("goku"));
		System.out.println("---------------------------------");
		
		// list for print all names start later M
		List<String> listResult = list.stream().filter(nomes -> nomes.charAt(0) == 'm').collect(Collectors.toList());
		for(String nomes : listResult) {
			System.out.println(nomes);
		}
		System.out.println(listResult.size());
		System.out.println("---------------------------------");
		
		// command for first later iniciate is P
		String name = list.stream().filter(nomes -> nomes.charAt(0) == 'p').findFirst().orElse("name not found");
		System.out.println(name);
	}

}
