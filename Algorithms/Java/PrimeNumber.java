class PrimeNumber {

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }

        if (number <= 3) {
            return true;
        }

        if (number % 2 == 0 || number % 3 == 0) {
            return false;
        }

        int i = 5;
        while (i * i <= number) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPrime(11)); // true
        System.out.println(isPrime(12)); // false
    }
}
