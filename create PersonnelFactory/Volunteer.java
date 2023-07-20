public class Volunteer extends Person{
	private int empID;

	public Volunteer(String last, String first, String middle, int id, double sal) {
		super(last, first, middle);
		empID = id;

	}

	public int getID()
	{
		return empID;
	}

    public void setID(int empID) {
        this.empID = empID;
    }


}
