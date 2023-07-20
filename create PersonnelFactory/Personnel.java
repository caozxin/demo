import java.util.*;

public class Personnel {
    private ArrayList<Person> personList;

    public Personnel() {
        personList = new ArrayList<Person>();
    }

    public void addPersonnel(Person p) {
        personList.add(p);
    }
    public ArrayList<Person> getPersonList() {
        return personList;
    }




}