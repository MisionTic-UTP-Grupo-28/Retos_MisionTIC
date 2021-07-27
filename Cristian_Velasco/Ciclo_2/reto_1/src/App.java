public class App {
    public static void main(String[] args) {
        NuevoProyecto np = new NuevoProyecto();
        System.out.println(np.compararInversion(6, 10000000, 1.2));
        System.out.println(np.compararInversion());
        System.out.println(np.calcularInteresSimple());
        System.out.println(np.calcularInteresCompuesto());

    }
}
