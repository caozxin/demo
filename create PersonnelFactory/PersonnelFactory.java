public class PersonnelFactory {

    public static Person createPersonnel(String personnelType, String last, String first, String middle, int id, double salary) {
        switch (personnelType.toLowerCase()) {
            case "employee":
                return new Employee(last, first, middle, id, salary);
            case "executive":
                return new Executive(last, first, middle, id, salary);
            case "security":
                return new Security(last, first, middle, id, salary);
            case "volunteer":
                return new Volunteer(last, first, middle, id,salary);
            default:
                throw new IllegalArgumentException("Invalid personnel type: " + personnelType);
        }
    }
}
