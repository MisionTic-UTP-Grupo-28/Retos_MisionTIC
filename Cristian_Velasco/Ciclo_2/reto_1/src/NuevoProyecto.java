public class NuevoProyecto {

    // Attributes
    private double monto = 0;
    private double interes = 0;
    private int periodo = 0;

    // Methods

    public String compararInversion(int pPeriodo, double pMonto, double pInteres) {
        monto = pMonto;
        periodo = pPeriodo;
        interes = pInteres;

        double interesSimple = calcularInteresSimple();
        double interesCompuesto = calcularInteresCompuesto();
        double comparacion = interesCompuesto - interesSimple;

        return interesSimple + "\n" + interesCompuesto + "\n" + comparacion;
    }

    public double calcularInteresSimple() {
        double interesSimple = this.monto * (this.interes / 100) * this.periodo;
        return Math.round(interesSimple);
    }

    public double calcularInteresCompuesto() {
        double interesCompuesto = this.monto * (Math.pow(1 + (this.interes / 100), this.periodo) - 1);
        return Math.round(interesCompuesto);
    }

}
