public class Person {
	private String last;
	private String first;
	private String middle;


	public Person(String last, String first, String middle) {
		this.last = last;
		this.first = first;
		this.middle = middle;

	}
	// Getter and Setter methods for private variables
    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }

    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }

    public String getMiddle() {
        return middle;
    }

    public void setMiddle(String middle) {
        this.middle = middle;
    }



	// public void printName(int order)
	// {

	//    if(order == 0)
	//    {
	//       System.out.println(first + "  " + middle + "  " + last);

	//    }else if(order == 1)
	//        {

	//        System.out.println(last + " ," + middle + " " + first);

	//        }
	// 	else if(order == 2)
	// 		{

	// 		System.out.println(last + " ," + first + " " + middle);

	// 		}
	// }
	public void printName(int order) {
        String formattedName = formatName(order);
        System.out.println(formattedName);
    }

    private String formatName(int order) {
        if (order == 0) {
            return first + " " + middle + " " + last;
        } else if (order == 1) {
            return last + ", " + middle + " " + first;
        } else {
            return last + ", " + first + " " + middle;
        }
    }


}
