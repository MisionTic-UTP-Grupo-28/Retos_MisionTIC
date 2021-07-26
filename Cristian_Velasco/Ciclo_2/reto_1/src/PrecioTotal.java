public class PrecioTotal {
    // Attributes

    private Double totalDispositivos;
    private double totalPortatiles;
    private Double totalTablets;
    private Dispositivo[] listaDispositivos;

    // Construtors
    public PrecioTotal(Dispositivo[] pDispositivos) {
        super();
    }

    // Methods
    public void mostrarTotales() {
        System.out.println("Total acerca de precios de dispositivos " + totalDispositivos);
        System.out.println("Total acerca de precios de tabletas " + totalTablets);
        System.out.println("Total acerca de precios de computadores portátiles " + totalPortatiles);
    }
}
