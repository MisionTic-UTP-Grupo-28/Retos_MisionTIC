public class App {
    public static void main(String[] args) throws Exception {
        Dispositivo dispositivos2[] = new Dispositivo[7];
        dispositivos2[0] = new Tablet(150.0, 1);
        dispositivos2[1] = new Portatil(500.0, 2, 'E', 500);
        dispositivos2[2] = new Dispositivo();
        dispositivos2[3] = new Portatil(250.0, 4);
        dispositivos2[4] = new Tablet(400.0, 3, 'A', 4);
        dispositivos2[5] = new Dispositivo(50.0, 3);
        PrecioTotal solucion2 = new PrecioTotal(dispositivos2);
        solucion2.mostrarTotales();
    }
}
